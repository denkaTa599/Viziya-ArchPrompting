"""Deterministic negative/mutation tests; no model or network access."""
from pathlib import Path
import copy
import json
import shutil
import tempfile
import unittest

from validate import ROOT, load_cases, metadata, score_trace, validate
from agent_smoke import observed_reads


class PackageValidation(unittest.TestCase):
    def test_valid_package(self):
        self.assertEqual(validate()['modules'], 7)

    def mutate(self, relative, transform):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / 'skill'
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(
                '.git', '__pycache__', 'agent-results'))
            path = root / relative
            if transform is None:
                path.unlink()
            else:
                path.write_bytes(transform(path.read_bytes()))
            with self.assertRaises((ValueError, KeyError, UnicodeError)):
                validate(root)

    def test_missing_module_fails(self):
        self.mutate('references/MATERIAL_REALISM.md', None)

    def test_invalid_utf8_fails(self):
        self.mutate('references/VISUAL_QA.md', lambda data: data + b'\xff')

    def test_corrupt_jpeg_fails(self):
        self.mutate('assets/viziya-archprompting-banner.jpg', lambda data: b'not a JPEG')

    def test_broken_relative_link_fails(self):
        self.mutate('README.md', lambda data: data + b'\n[missing](examples/missing.md)\n')

    def test_duplicate_route_fails(self):
        def duplicate(data):
            row = next(line for line in data.splitlines()
                       if line.startswith(b'| `references/ARCHITECTURAL_FIDELITY.md`'))
            return data + b'\n' + row + b'\n'
        self.mutate('SKILL.md', duplicate)

    def test_conflicting_fixture_fails(self):
        def conflict(data):
            cases = json.loads(data)
            cases[0]['forbidden'].append('IMAGE_PROMPTING.md')
            return json.dumps(cases).encode('utf-8')
        self.mutate('tests/routing_cases.json', conflict)

    def test_stale_directory_tree_fails(self):
        self.mutate('README.md', lambda data: data.replace(b'  CHANGELOG.md\n', b''))

    def test_duplicate_and_invalid_metadata_fail(self):
        for frontmatter in ('name: image-prompting\nname: duplicate\ndescription: test',
                            'name: image-prompting\ndescription: true',
                            'name: image-prompting\ndescription: invalid: YAML'):
            with self.subTest(frontmatter=frontmatter), self.assertRaises(ValueError):
                metadata('---\n' + frontmatter + '\n---\n')


class TraceScoring(unittest.TestCase):
    def setUp(self):
        self.case = next(c for c in load_cases() if c['id'] == 'text-only')
        self.response = {'model': 'GPT Image', 'asks_model': False,
                         'blocks': [{'label': 'Prompt', 'text': 'Replace only the title.'}],
                         'message': 'One complete prompt.'}
        self.opened = ['SKILL.md', 'references/IMAGE_PROMPTING.md']

    def test_correct_trace(self):
        self.assertEqual(score_trace(self.case, self.opened, self.response), [])

    def test_extra_and_missing_reads_fail(self):
        for opened in (['SKILL.md'], self.opened + ['references/VISUAL_QA.md']):
            self.assertTrue(score_trace(self.case, opened, self.response))

    def test_repeated_read_fails(self):
        self.assertIn('Repeated module reads', score_trace(
            self.case, self.opened + ['references/IMAGE_PROMPTING.md'], self.response))

    def test_wrong_model_question_and_contract_fail(self):
        response = copy.deepcopy(self.response)
        response.update(model='Nano Banana', asks_model=True, blocks=[])
        self.assertEqual(len(score_trace(self.case, self.opened, response)), 3)

    def test_inherited_context_needs_no_rereads(self):
        case = next(c for c in load_cases() if c['id'] == 'followup-inherited')
        self.assertEqual(score_trace(case, [], self.response), [])
        self.assertTrue(score_trace(case, self.opened, self.response))

    def test_nano_correction_requires_full_two_blocks(self):
        case = next(c for c in load_cases() if c['id'] == 'geometry-correction')
        opened = ['SKILL.md'] + ['references/' + m for m in case['required']]
        response = {'model': 'Nano Banana', 'asks_model': False, 'message': 'Correction.',
                    'blocks': [{'label': label, 'text': 'Complete correction instructions.'}
                               for label in ['System Instruction', 'Prompt']]}
        self.assertEqual(score_trace(case, opened, response), [])
        response['blocks'] = response['blocks'][1:]
        self.assertTrue(score_trace(case, opened, response))

    def test_only_completed_tool_outputs_count_as_reads(self):
        events = [
            {'type': 'item.completed', 'item': {'type': 'agent_message',
             'text': 'ARCHPROMPT_READ::references/VISUAL_QA.md'}},
            {'type': 'item.completed', 'item': {'type': 'command_execution',
             'command': 'python tests/agent_smoke.py read SKILL.md',
             'aggregated_output': 'ARCHPROMPT_READ::SKILL.md\n---\nname: image-prompting'}},
            {'type': 'turn.completed', 'usage': {'input_tokens': 100, 'output_tokens': 20}},
        ]
        opened, commands, usage = observed_reads(events)
        self.assertEqual(opened, ['SKILL.md'])
        self.assertEqual(len(commands), 1)
        self.assertEqual(usage['input_tokens'], 100)


if __name__ == '__main__':
    unittest.main()
