"""Opt-in real Codex CLI tests. Existing account usage applies; never runs in CI."""
from pathlib import Path
import argparse
import datetime
import json
import re
import shutil
import subprocess
import sys

from validate import MODULES, ROOT, load_cases, score_trace

MARKER = 'ARCHPROMPT_READ::'


def read_files(paths):
    # Instrument the actual read result, not a model's self-reported module list.
    allowed = {'SKILL.md'} | {'references/' + name for name in MODULES}
    for name in paths:
        if name not in allowed:
            raise ValueError(f'Not a skill instruction file: {name}')
        text = (ROOT / name).read_text(encoding='utf-8')
        print(MARKER + name)
        print(text)


def observed_reads(events):
    opened, commands, usage = [], [], None
    for event in events:
        if event.get('type') == 'turn.completed':
            usage = event.get('usage')
        if event.get('type') != 'item.completed':
            continue
        item = event.get('item', {})
        if item.get('type') == 'command_execution':
            commands.append(item.get('command', ''))
            opened.extend(re.findall(r'^' + MARKER + r'([^\r\n]+)',
                                     item.get('aggregated_output', ''), re.M))
    return opened, commands, usage


def run_case(case, output):
    cli = shutil.which('codex')
    if not cli:
        raise RuntimeError('Codex CLI not found; live testing unavailable')
    output.mkdir(parents=True, exist_ok=True)
    final = output / (case['id'] + '-response.json')
    reader = f'& "{sys.executable}" -X utf8 "{Path(__file__).resolve()}" read' if sys.platform == 'win32' else (
        f'"{sys.executable}" -X utf8 "{Path(__file__).resolve()}" read')
    prior = ''
    if case['prior_model']:
        prior += f'Previously selected model: {case["prior_model"]}.\n'
    if case['already_loaded']:
        prior += 'Seeded prior context: these complete current instructions were already read:\n'
        prior += '\n' + (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        for name in case['already_loaded']:
            prior += '\n' + (ROOT / 'references' / name).read_text(encoding='utf-8')
    prompt = f'''This is an authorized text-only routing experiment on the candidate image-prompting skill in {ROOT}.
Use this candidate rather than installed versions. Do not generate images, browse, edit files, inspect tests/fixtures, or invoke other skills. References in the task are hypothetical written briefs, not images you can claim to have inspected.
Read SKILL.md and only the required instruction files. ALL filesystem reads must use exactly this instrumented reader (one or more relative paths):
{reader} SKILL.md
Use the same command with references/FILENAME.md for selected modules. Run no other shell commands, wrappers, or direct reads. The reader's successful stdout records real reads. Do not read tests, examples, or expected answers.
{prior}
User task: {case['task']}
Return the actual response using the required JSON transport: model (canonical family or null), asks_model, message, and blocks (label/text). Put the complete model-specific output into blocks; for an essential model question or analysis-only response use an empty blocks array. Do not add routing self-reports. The JSON is only a test transport, not a new skill output contract.
'''
    command = [cli, '-a', 'never', 'exec', '--ignore-user-config', '--skip-git-repo-check',
               '--sandbox', 'read-only', '--json', '-C', str(ROOT),
               '--output-schema', str(ROOT / 'tests/agent_response.schema.json'),
               '-o', str(final), '-']
    # No model override, API keys or plugin services are configured by this harness.
    result = subprocess.run(command, input=prompt, capture_output=True,
                            text=True, encoding='utf-8', timeout=300)
    (output / (case['id'] + '-events.jsonl')).write_text(result.stdout, encoding='utf-8')
    (output / (case['id'] + '-stderr.txt')).write_text(result.stderr, encoding='utf-8')
    events = []
    for line in result.stdout.splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    opened, commands, usage = observed_reads(events)
    try:
        response = json.loads(final.read_text(encoding='utf-8')) if final.exists() else {}
    except json.JSONDecodeError:
        response = {}
    issues = score_trace(case, opened, response)
    if result.returncode:
        issues.append(f'Codex exit status {result.returncode}; inspect stderr')
    if any('agent_smoke.py' not in command or 'read' not in command for command in commands):
        issues.append('Off-protocol commands: read trace may be incomplete')
    blocked = not opened and 'blocked by policy' in result.stderr
    report = {'case': case['id'], 'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'opened': opened, 'expected_new_modules': sorted(set(case['required']) - set(case['already_loaded'])),
              'usage': usage, 'commands': commands, 'issues': issues,
              'passed': not issues, 'status': 'blocked' if blocked else ('passed' if not issues else 'failed'),
              'seeded_prior_context': bool(case['already_loaded']),
              'limitations': 'Instrumented text-only CLI session; no actual images inspected or generated. '
                             'Seeded follow-up context is not a resumed multi-turn dialogue.'}
    (output / (case['id'] + '-result.json')).write_text(
        json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report), flush=True)
    return report['status']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    read = sub.add_parser('read')
    read.add_argument('paths', nargs='+')
    run = sub.add_parser('run')
    run.add_argument('--case', action='append', required=True, help='Repeat for several case IDs')
    run.add_argument('--output', type=Path, required=True, help='Outside the tracked source directory')
    args = parser.parse_args()
    if args.action == 'read':
        read_files(args.paths)
        return
    output = args.output.resolve()
    if output.is_relative_to(ROOT):
        parser.error('Keep runtime evidence outside the source package')
    cases = {case['id']: case for case in load_cases()}
    if any(name not in cases for name in args.case):
        parser.error('Unknown case ID')
    statuses = []
    for name in args.case:
        status = run_case(cases[name], output)
        statuses.append(status)
        if status == 'blocked':
            print('Live file reads are blocked by environment policy; stopping without weakening it.')
            break
    sys.exit(0 if all(status == 'passed' for status in statuses) else 1)


if __name__ == '__main__':
    main()
