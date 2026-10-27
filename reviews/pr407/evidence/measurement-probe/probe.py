import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import zipfile


ROOT = Path('/workspace/scratch/226f2776372f/pr407-review')
OUTPUT = Path(__file__).resolve().parent
REPOSITORY = 'fixture-owner/fixture-repo'
RUN_ID = 4242
HEAD_SHA = '0123456789abcdef0123456789abcdef01234567'
JOB_ID = 'rust-velnor-actions-actionlint-write'
DISPLAY_NAME = 'Rust / velnor-actions-actionlint (write)'
NUMERIC_JOB_ID = 101
ARTIFACT_ID = 777
MATRIX_KEY = 'm-aaaaaaaaaaaaaaaa'
TASK_ID = 'task-r4242-a1-m-aaaaaaaaaaaaaaaa-bbbbbbbbbbbbbbbb'
MEMBER = f'{MATRIX_KEY}/tasks/{TASK_ID}.observation.json'


def write_json(path, data):
    path.write_text(json.dumps(data, sort_keys=True, indent=2) + '\n')


def write_zip(path, members):
    with zipfile.ZipFile(path, 'w') as archive:
        for name, data in sorted(members.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 27, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED
            archive.writestr(info, json.dumps(data, sort_keys=True).encode())


def receipt(path):
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def run_case(name, api_name, run_attempt, producer_job, expected_exit, expected_error):
    directory = OUTPUT / name
    directory.mkdir(exist_ok=True)
    run_key = f'r{RUN_ID}-a{run_attempt}'
    run = {'id': RUN_ID, 'run_attempt': run_attempt, 'head_sha': HEAD_SHA}
    job = {
        'id': NUMERIC_JOB_ID, 'run_id': RUN_ID, 'run_attempt': 1,
        'head_sha': HEAD_SHA, 'name': api_name,
        'run_url': f'https://api.github.com/repos/{REPOSITORY}/actions/runs/{RUN_ID}',
        'html_url': f'https://github.com/{REPOSITORY}/actions/runs/{RUN_ID}/job/{NUMERIC_JOB_ID}',
        'status': 'completed', 'conclusion': 'success',
    }
    observation = {
        'schema': 1, 'task_report_id': TASK_ID,
        'artifact_id': f'velnor-crate-r{RUN_ID}-a1-{JOB_ID}',
        'member_name': MEMBER, 'member_size_bytes': 512,
        'member_digest': 'b3-' + 'ab' * 32,
        'producer_job': producer_job, 'producer_attempt': 1,
        'source_sha': HEAD_SHA, 'observation_session_id': 'review-fixture-session',
        'unit_ledger_digest': 'b3-' + 'cd' * 32,
    }
    write_json(directory / 'run.json', run)
    write_json(directory / 'jobs.json', {'total_count': 1, 'jobs': [job]})
    write_zip(directory / 'logs.zip', {})
    write_zip(directory / 'final.zip', {
        'final-report.json': {'run_key': run_key, 'report_id': f'final-{run_key}',
                              'status': 'passed', 'counts': {}},
        MEMBER: observation,
    })
    final_receipt = receipt(directory / 'final.zip')
    write_json(directory / 'artifact.json', {
        'total_count': 1,
        'artifacts': [{
            'id': ARTIFACT_ID, 'name': f'velnor-final-{run_key}',
            'url': f'https://api.github.com/repos/{REPOSITORY}/actions/artifacts/{ARTIFACT_ID}',
            'size_in_bytes': final_receipt['bytes'],
            'digest': 'sha256:' + final_receipt['sha256'],
            'workflow_run': {'id': RUN_ID, 'head_sha': HEAD_SHA},
        }],
    })
    output_path = directory / 'report.json'
    output_path.unlink(missing_ok=True)
    argv = [sys.executable, '-B', '-m', 'scripts.hosted_phase_measurement.measure_hosted_run',
            '--repository', REPOSITORY,
            '--run-json', str(directory / 'run.json'),
            '--jobs-json', str(directory / 'jobs.json'),
            '--logs-zip', str(directory / 'logs.zip'),
            '--artifact-json', str(directory / 'artifact.json'),
            '--artifact-id', str(ARTIFACT_ID),
            '--final-artifact', str(directory / 'final.zip'),
            '--out', str(output_path)]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    completed = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True, text=True, timeout=30)
    outcome = {
        'case': name, 'cwd': str(ROOT), 'argv': argv,
        'environment_override': {'PYTHONDONTWRITEBYTECODE': '1'},
        'exit_code': completed.returncode, 'stdout': completed.stdout, 'stderr': completed.stderr,
        'expected_exit': expected_exit, 'expected_error_substring': expected_error,
        'fixtures': [receipt(directory / item) for item in
                     ['run.json', 'jobs.json', 'logs.zip', 'artifact.json', 'final.zip']],
    }
    if output_path.exists():
        report = json.loads(output_path.read_text())
        outcome['report'] = receipt(output_path)
        outcome['observed_lifecycle'] = report['observed_lifecycle']
    write_json(directory / 'result.json', outcome)
    if completed.returncode != expected_exit or expected_error not in completed.stderr:
        raise RuntimeError(f'Unexpected result for {name}: {completed.returncode}: {completed.stderr}')
    if expected_exit == 0:
        lifecycle = outcome['observed_lifecycle']
        if lifecycle['join']['observation_count'] != 1:
            raise RuntimeError('Control did not join exactly one observation')
        if lifecycle['process_counts']['compiler_executions'] is not None:
            raise RuntimeError('Control invented compiler execution measurements')
        if lifecycle['byte_channels']['origin_acquisition_bytes'] is not None:
            raise RuntimeError('Control invented origin acquisition measurements')
    return outcome


def main():
    cases = [
        ('01_matching_control', JOB_ID, 1, JOB_ID, 0, ''),
        ('02_display_name', DISPLAY_NAME, 1, JOB_ID, 2, 'has no authenticated job record'),
        ('03_retained_attempt', JOB_ID, 2, JOB_ID, 2, 'belongs to a different run/attempt/source'),
        ('04_display_name_in_binding', DISPLAY_NAME, 1, DISPLAY_NAME, 2, 'bad producer_job'),
    ]
    results = [run_case(*case) for case in cases]
    source_files = [ROOT / 'scripts/hosted_phase_measurement' / name for name in
                    ['measure_hosted_run.py', 'report_builder.py', 'measure_support.py',
                     'report_events.py', 'report_counters.py']]
    write_json(OUTPUT / 'results.json', {
        'scope': 'Synthetic external fixtures; public CLI execution; no real API authentication or GitHub retention evidence.',
        'source_head': '586bdb2be3b1d203abbdd19a09bff8b188c20cc3',
        'sources': [receipt(path) for path in source_files],
        'probe': receipt(Path(__file__).resolve()), 'results': results,
    })
    (OUTPUT / 'commands.txt').write_text('\n\n'.join(
        'cwd=' + result['cwd'] + '\nPYTHONDONTWRITEBYTECODE=1 ' + shlex.join(result['argv'])
        for result in results) + '\n')
    for result in results:
        print(json.dumps({'case': result['case'], 'exit_code': result['exit_code'],
                          'stderr': result['stderr'],
                          'observation_count': result.get('observed_lifecycle', {}).get('join', {}).get('observation_count')}))


if __name__ == '__main__':
    main()
