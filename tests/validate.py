"""Dependency-free package/fixture validation, not an LLM or image benchmark."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MODULES = {
    'IMAGE_PROMPTING.md', 'ARCHITECTURAL_FIDELITY.md', 'MATERIAL_REALISM.md',
    'PHOTOGRAPHIC_REALISM.md', 'REFERENCE_DECONSTRUCTION.md',
    'VISUAL_QA.md', 'PROJECT_CONTINUITY.md',
}
OPERATIONS = {'create', 'edit', 'revise', 'analyze', 'correct', 'maintenance'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def project_files(root):
    return sorted(p for p in root.rglob('*') if p.is_file()
                  and not any(part in {'.git', '__pycache__', 'agent-results'}
                              for part in p.relative_to(root).parts)
                  and p.suffix != '.pyc')


def metadata(text):
    """Validate the package's intentionally flat, string-only YAML frontmatter."""
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    require(match is not None, 'Missing YAML frontmatter')
    result = {}
    for line in match[1].splitlines():
        key, separator, value = line.partition(':')
        require(separator and key in {'name', 'description'}, 'Unsupported metadata field')
        require(key not in result, f'Duplicate metadata: {key}')
        value = value.strip()
        if value.startswith('"'):
            value = json.loads(value)
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        else:
            require(not re.search(r':\s|\s#|^[|>\[\]{&*!]', value),
                    f'Quote YAML scalar: {key}')
            require(value.lower() not in {'true', 'false', 'null', '~'},
                    f'Metadata must be a string: {key}')
        require(isinstance(value, str) and value.strip(), f'Empty metadata: {key}')
        result[key] = value
    require(result.get('name') == 'image-prompting', 'Skill identity changed')
    require('description' in result, 'Missing description')
    return result


def load_cases(root=ROOT):
    cases = json.loads((root / 'tests/routing_cases.json').read_text(encoding='utf-8'))
    require(isinstance(cases, list) and len(cases) >= 18, 'Need at least 18 scenarios')
    ids, tasks = set(), set()
    fields = {'id', 'operation', 'task', 'required', 'forbidden', 'prior_model',
              'already_loaded', 'expected_model', 'expects_question', 'expected_blocks'}
    for case in cases:
        require(isinstance(case, dict) and set(case) == fields, 'Invalid fixture schema')
        require(isinstance(case['id'], str) and case['id'] not in ids, 'Duplicate case id')
        require(isinstance(case['task'], str) and case['task'].strip(), 'Empty task')
        require(case['task'] not in tasks, 'Duplicate task with potentially conflicting route')
        ids.add(case['id'])
        tasks.add(case['task'])
        require(case['operation'] in OPERATIONS, 'Invalid operation')
        for key in ('required', 'forbidden', 'already_loaded'):
            values = case[key]
            require(isinstance(values, list) and all(isinstance(v, str) for v in values),
                    f'Invalid module list: {key}')
            require(len(values) == len(set(values)) and set(values) <= MODULES,
                    f'Unknown/duplicate module: {key}')
        required, forbidden = set(case['required']), set(case['forbidden'])
        require(not required & forbidden and required | forbidden == MODULES,
                f'Incomplete/conflicting positive-negative expectations: {case["id"]}')
        require(set(case['already_loaded']) <= required, 'Cached module outside route')
        require((not required) == (case['operation'] == 'maintenance'),
                'Only maintenance omits core')
        require(not required or case['required'][0] == 'IMAGE_PROMPTING.md', 'Core first')
        require(case['expected_model'] in {None, 'Nano Banana', 'GPT Image'}, 'Invalid model')
        require(case['prior_model'] in {None, 'Nano Banana', 'GPT Image'}, 'Invalid prior model')
        require(isinstance(case['expects_question'], bool), 'Question flag must be boolean')
        if case['expects_question']:
            require(case['expected_model'] is None and case['prior_model'] is None,
                    'Do not confirm an established model')
        blocks = [] if case['expects_question'] or case['operation'] in {
            'maintenance', 'analyze'} else (
            ['System Instruction', 'Prompt'] if case['expected_model'] == 'Nano Banana'
            else ['Prompt'])
        require(case['expected_blocks'] == blocks, 'Fixture output contract mismatch')
    require({c['operation'] for c in cases} == OPERATIONS, 'Missing operation coverage')
    return cases


def score_trace(case, opened, response):
    """Score observed file-read events; never infer reads from the agent's claims."""
    expected = set(case['required']) - set(case['already_loaded'])
    actual = [p.removeprefix('references/') for p in opened if p != 'SKILL.md']
    issues = []
    if set(actual) != expected:
        issues.append(f'missing={sorted(expected - set(actual))}; extra={sorted(set(actual) - expected)}')
    if len(actual) != len(set(actual)):
        issues.append('Repeated module reads')
    if not case['already_loaded'] and case['required'] and 'SKILL.md' not in opened:
        issues.append('Router not read')
    if not case['already_loaded'] and actual and actual[0] != 'IMAGE_PROMPTING.md':
        issues.append('Core not read first')
    if response.get('model') != case['expected_model']:
        issues.append('Wrong model')
    if response.get('asks_model') != case['expects_question']:
        issues.append('Wrong model-question behavior')
    blocks = response.get('blocks', [])
    if not isinstance(blocks, list) or [b.get('label') for b in blocks] != case['expected_blocks']:
        issues.append('Wrong output blocks')
    elif any(not isinstance(b.get('text'), str) or not b['text'].strip() for b in blocks):
        issues.append('Empty output block')
    if not isinstance(response.get('message'), str) or not response['message'].strip():
        issues.append('Missing response/question')
    return issues


def documented_files(readme):
    block = re.search(r'```text\nViziya-ArchPrompting/\n(.*?)```', readme, re.S)
    require(block is not None, 'Missing complete directory tree')
    folders, files = [], set()
    for line in block[1].splitlines():
        if not line.strip():
            continue
        depth = (len(line) - len(line.lstrip(' '))) // 2 - 1
        name = line.strip()
        folders = folders[:depth]
        if name.endswith('/'):
            folders.append(name[:-1])
        else:
            files.add('/'.join(folders + [name]))
    return files


def validate(root=ROOT):
    files = project_files(root)
    texts = {}
    for path in files:
        relative = path.relative_to(root).as_posix()
        data = path.read_bytes()
        if path.suffix.lower() == '.jpg' and relative.startswith('assets/'):
            require(data.startswith(b'\xff\xd8\xff') and data.endswith(b'\xff\xd9'),
                    f'Invalid JPEG asset: {relative}')
            continue
        require(not data.startswith(b'\xef\xbb\xbf'), f'UTF-8 BOM: {relative}')
        texts[relative] = data.decode('utf-8', errors='strict')
    router, core = texts['SKILL.md'], texts['references/IMAGE_PROMPTING.md']
    metadata(router)
    require({p.name for p in (root / 'references').glob('*.md')} == MODULES,
            'Missing or unexpected reference module')
    paths = set(re.findall(r'references/[A-Z_]+\.md', router))
    require(paths == {'references/' + m for m in MODULES}, 'Incorrect router paths')
    rows = re.findall(r'^\| `references/([A-Z_]+\.md)` \| (.+?) \| (.+?) \|$', router, re.M)
    require(len(rows) == 6 and {r[0] for r in rows} == MODULES - {'IMAGE_PROMPTING.md'},
            'Duplicate/missing routing rows')
    require(len({(r[1], r[2]) for r in rows}) == 6, 'Conflicting duplicate route conditions')
    for word in ('Nano Banana', 'GPT Image', 'System Instruction', 'Prompt'):
        require(word in router and word in core, f'Missing output-contract token: {word}')
    require('without confirmation' in core and 'inherit the established model' in core,
            'Model selection regression')
    for relative, text in texts.items():
        if not relative.endswith('.md'):
            continue
        # Markdown links and code-form local document paths; external/installation paths are excluded.
        targets = re.findall(r'\[[^\]]*\]\(([^)]+)\)', text)
        targets += re.findall(r'`((?:\.\./|references/|tests/|examples/)?[A-Za-z_./-]+\.(?:md|py|json|yml))`', text)
        for target in targets:
            target = target.split('#', 1)[0]
            if not target or re.match(r'^[a-z]+:|^/|^~', target, re.I):
                continue
            resolved = (root / relative).parent / target
            require(resolved.resolve().is_relative_to(root.resolve()) and resolved.is_file(),
                    f'Broken/escaping relative path in {relative}: {target}')
    cases = load_cases(root)
    tree = documented_files(texts['README.md'])
    actual_files = {p.relative_to(root).as_posix() for p in files}
    require(tree == actual_files,
            f'README tree mismatch: missing={actual_files-tree}, stale={tree-actual_files}')
    examples = [text for name, text in texts.items() if name.startswith('examples/')]
    require(len(examples) == 6, 'Need six practical examples')
    for text in examples:
        for heading in ('## User request', '## Expected modules', '## Reference roles',
                        '## Output format', '## Locked characteristics', '## Representative output'):
            require(heading in text, f'Incomplete example: {heading}')
        require('Hypothetical' in text, 'Label hypothetical examples')
    workflow = texts['.github/workflows/validate.yml']
    require('on: [push, pull_request]' in workflow and 'contents: read' in workflow,
            'CI trigger/permissions regression')
    require('actions/checkout@v7' in workflow and 'actions/setup-python@v7' in workflow,
            'Unexpected action versions; review current supported upstream releases')
    require('python tests/validate.py' in workflow
            and 'python -m unittest discover -s tests -v' in workflow, 'CI omits checks')
    require('agent_smoke.py run' not in workflow, 'Live agent tests must stay opt-in')
    return {'files': len(files), 'modules': len(MODULES), 'fixtures': len(cases)}


if __name__ == '__main__':
    try:
        result = validate()
    except (ValueError, KeyError, UnicodeError, json.JSONDecodeError) as error:
        sys.exit(f'FAIL: {error}')
    print(f'PASS: static package validation {result}')
    print('Fixtures and deterministic checks do not establish live agent or image quality.')
