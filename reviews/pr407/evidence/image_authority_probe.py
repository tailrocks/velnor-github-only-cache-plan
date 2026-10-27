import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tarfile


REPO = Path('/workspace/scratch/226f2776372f/pr407-review')
OUT = Path('/workspace/scratch/226f2776372f/pr407-review-notes/image-authority-probe')
MODULES = REPO / 'crates/velnor-actions-workflow-renderer/src'
SOURCE = MODULES / 'job_image_authority.rs'
OLD = '1' * 40
CURRENT = '2' * 40


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':')).encode()


def tar(members):
    stream = io.BytesIO()
    with tarfile.open(fileobj=stream, mode='w', format=tarfile.USTAR_FORMAT) as archive:
        for name, data in members:
            info = tarfile.TarInfo(name)
            info.size = len(data)
            info.mode = 0o644
            info.mtime = 0
            archive.addfile(info, io.BytesIO(data))
    return stream.getvalue()


def make_fixture():
    layer = tar([('hello.txt', b'hello')])
    config = encoded({'architecture': 'amd64', 'os': 'linux',
                      'rootfs': {'type': 'layers', 'diff_ids': ['sha256:' + sha(layer)]}})
    manifest = encoded({
        'schemaVersion': 2,
        'mediaType': 'application/vnd.oci.image.manifest.v1+json',
        'config': {'mediaType': 'application/vnd.oci.image.config.v1+json',
                   'digest': 'sha256:' + sha(config), 'size': len(config)},
        'layers': [{'mediaType': 'application/vnd.oci.image.layer.v1.tar',
                    'digest': 'sha256:' + sha(layer), 'size': len(layer)}],
    })
    index = encoded({
        'schemaVersion': 2,
        'mediaType': 'application/vnd.oci.image.index.v1+json',
        'manifests': [{'mediaType': 'application/vnd.oci.image.manifest.v1+json',
                       'digest': 'sha256:' + sha(manifest), 'size': len(manifest),
                       'platform': {'architecture': 'amd64', 'os': 'linux'}}],
    })
    archive = tar([
        ('oci-layout', encoded({'imageLayoutVersion': '1.0.0'})),
        ('index.json', index),
        ('blobs/sha256/' + sha(manifest), manifest),
        ('blobs/sha256/' + sha(config), config),
        ('blobs/sha256/' + sha(layer), layer),
    ])
    inputs = [
        '.velnor/runner.lock', 'images/job/ubuntu-26.04/Dockerfile',
        'images/job/ubuntu-26.04/README.md', 'images/job/ubuntu-26.04/build-test.sh',
        'images/job/ubuntu-26.04/candidate/candidate.py',
    ]
    record = {
        'schema': 'velnor.job-image-candidate.v1',
        'source': {'commit': OLD, 'ref': 'refs/heads/main',
                   'inputs': {name: str(n) * 64 for n, name in enumerate(inputs)}},
        'workflow': {'repository': 'tailrocks/velnor-new', 'repository_id': 1390620900,
                     'event': 'workflow_dispatch',
                     'workflow_ref': 'tailrocks/velnor-new/.github/workflows/job-image-candidate.yml@refs/heads/main',
                     'authority_commit': OLD, 'run_id': 7, 'run_attempt': 2},
        'platform': 'linux/amd64',
        'build': {'builder': 'github.com/docker/buildx v0.25.0', 'platform': 'linux/amd64',
                  'arguments': [], 'exporter': 'oci', 'provenance': 'disabled',
                  'compression': 'gzip', 'force_compression': True},
        'archive': {'sha256': sha(archive), 'size_bytes': len(archive)},
        'oci': {'archive_index_digest': sha(index), 'archive_index_size_bytes': len(index),
                'platform_manifest_digest': 'sha256:' + sha(manifest),
                'platform_manifest_size_bytes': len(manifest),
                'image_configuration_digest': 'sha256:' + sha(config),
                'image_configuration_size_bytes': len(config),
                'layer_digests': ['sha256:' + sha(layer)]},
    }
    (OUT / 'candidate.oci.tar').write_bytes(archive)
    (OUT / 'candidate.json').write_bytes(encoded(record))
    return record


WRAPPER = '''import json
from pathlib import Path
import sys
import traceback

sys.dont_write_bytecode = True
program, modules, record, archive, result, audit_result = sys.argv[1:]
events = []
calibration = []

def blocked(event):
    return event.startswith('socket.') or event.startswith('subprocess.') or event in {
        'os.system', 'os.exec', 'os.posix_spawn', 'os.spawn', 'os.fork', 'os.forkpty'
    }

def tripwire(event, args):
    if blocked(event):
        events.append(event)
        raise RuntimeError('review_tripwire:' + event)

sys.addaudithook(tripwire)
for event in ['socket.connect', 'subprocess.Popen', 'os.system', 'os.exec']:
    try:
        sys.audit(event)
    except RuntimeError as error:
        if str(error) != 'review_tripwire:' + event:
            raise
        calibration.append(event)
    else:
        raise RuntimeError('tripwire calibration failed: ' + event)
events.clear()
sys.argv = [program, modules, record, archive, result]
status = 0
try:
    code = Path(program).read_bytes()
    exec(compile(code, program, 'exec'), {'__name__': '__main__', '__file__': program})
except BaseException:
    status = 1
    traceback.print_exc()
finally:
    Path(audit_result).write_text(json.dumps({
        'hook_active_before_program_compilation': True,
        'calibrated_blocked_events': calibration,
        'program_blocked_events': events,
        'blocked_event_policy': 'socket.*, subprocess.*, os.system, os.exec, os.posix_spawn, os.spawn, os.fork, os.forkpty',
        'program_exit_code': status,
    }, sort_keys=True, indent=2) + '\\n')
sys.exit(status)
'''


def main():
    OUT.mkdir(exist_ok=True)
    source_bytes = SOURCE.read_bytes()
    matches = list(re.finditer(rb'const EVIDENCE_PROGRAM: &str = r#"(.*?)"#;', source_bytes, re.S))
    if len(matches) != 1:
        raise RuntimeError('Expected one exact EVIDENCE_PROGRAM')
    program = matches[0].group(1)
    program_path = OUT / 'EVIDENCE_PROGRAM.py'
    program_path.write_bytes(program)
    wrapper = OUT / 'audit_wrapper.py'
    wrapper.write_text(WRAPPER)
    record = make_fixture()
    baseline_hashes = {name: sha((OUT / name).read_bytes())
                       for name in ['candidate.oci.tar', 'candidate.json']}
    results = []
    for case, source in [('matching-source', OLD), ('mismatched-source', CURRENT)]:
        result = OUT / (case + '.evidence.json')
        audit = OUT / (case + '.audit.json')
        result.unlink(missing_ok=True)
        audit.unlink(missing_ok=True)
        environment = {
            'PATH': os.environ.get('PATH', '/usr/bin:/bin'),
            'PYTHONDONTWRITEBYTECODE': '1',
            'VELNOR_IDENTITY_SOURCE': source,
            'VELNOR_WORKFLOW_REF': 'tailrocks/velnor-new/.github/workflows/job-image-candidate.yml@refs/heads/main',
            'VELNOR_RUN_ID': '7', 'VELNOR_RUN_ATTEMPT': '2', 'VELNOR_ARTIFACT_ID': '9',
        }
        command = [sys.executable, '-I', str(wrapper), str(program_path), str(MODULES),
                   str(OUT / 'candidate.json'), str(OUT / 'candidate.oci.tar'), str(result), str(audit)]
        completed = subprocess.run(command, cwd=OUT, env=environment, capture_output=True, timeout=30)
        (OUT / (case + '.stdout.txt')).write_bytes(completed.stdout)
        (OUT / (case + '.stderr.txt')).write_bytes(completed.stderr)
        evidence = json.loads(result.read_bytes()) if result.exists() else None
        audit_data = json.loads(audit.read_bytes()) if audit.exists() else None
        results.append({
            'case': case, 'command': command, 'exit_code': completed.returncode,
            'candidate_source': record['source']['commit'], 'environment_source': source,
            'evidence_source': evidence.get('source') if evidence else None,
            'evidence_status': evidence.get('status') if evidence else None,
            'evidence_ci': evidence.get('ci') if evidence else None,
            'evidence_digest_reference': evidence.get('digest_reference') if evidence else None,
            'candidate_source_matches_environment': record['source']['commit'] == source,
            'evidence_matches_environment': evidence is not None and evidence.get('source') == source,
            'audit': audit_data,
            'stdout': completed.stdout.decode(), 'stderr': completed.stderr.decode(),
        })
    unchanged = all(sha((OUT / name).read_bytes()) == digest for name, digest in baseline_hashes.items())
    summary = {
        'reviewed_revision': '586bdb2be3b1d203abbdd19a09bff8b188c20cc3',
        'python': sys.version,
        'extraction': {'path': str(SOURCE), 'source_file_sha256': sha(source_bytes),
                       'constant': 'EVIDENCE_PROGRAM', 'exact_program_sha256': sha(program),
                       'exact_program_bytes': len(program),
                       'source_first_line': source_bytes[:matches[0].start(1)].count(b'\n') + 1,
                       'source_last_line': source_bytes[:matches[0].end(1)].count(b'\n') + 1,
                       'program_bytes_match_literal': program_path.read_bytes() == program},
        'authority_module_hashes': {path.name: sha(path.read_bytes())
                                   for path in sorted(MODULES.glob('job_image_authority_*.py'))},
        'fixture_hashes': baseline_hashes,
        'fixture_construction_basis': 'gc1_t48_archive.rs:14-109; deterministic USTAR, one local hello.txt layer',
        'fixture_bytes_unchanged_between_cases': unchanged,
        'network_and_subprocess_boundary': 'Parent launches one Python child per case. Audit hooks block all socket and subprocess events inside the exact authority body.',
        'results': results,
        'rust_or_hosted_execution': False,
    }
    (OUT / 'summary.json').write_text(json.dumps(summary, sort_keys=True, indent=2) + '\n')
    print(json.dumps(summary, sort_keys=True, indent=2))
    if not unchanged or any(row['exit_code'] != 0 or row['evidence_status'] != 'PASS'
                            or row['audit']['program_blocked_events'] for row in results):
        raise SystemExit('Probe preconditions or expected observation failed; inspect summary.')


if __name__ == '__main__':
    main()
