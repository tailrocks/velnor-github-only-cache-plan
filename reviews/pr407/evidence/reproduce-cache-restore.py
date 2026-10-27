import io
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import yaml

repo = Path(sys.argv[1])
workflow = yaml.safe_load((repo / '.github/workflows/ci.yml').read_text())
command = next(step['run'] for step in workflow['jobs']['dependency-seed']['steps'] if step.get('name') == 'Recover state snapshot')
with tempfile.TemporaryDirectory(prefix='pr407-cache-restore-') as temporary:
    root = Path(temporary)
    owned = root / 'velnor-gc1'
    payload = owned / 'transport/state/payload.tar.gz'
    payload.parent.mkdir(parents=True)
    sentinel = owned / 'tools/sentinel'
    sentinel.parent.mkdir()
    sentinel.write_bytes(b'verified-tool-input\n')
    members = {'state/ordinary.o': b'expected-state\n', 'tools/sentinel': b'archive-overwrite\n'}
    with tarfile.open(payload, 'w:gz') as archive:
        for name, data in members.items():
            info = tarfile.TarInfo(name)
            info.size = len(data)
            info.mode = 0o644
            archive.addfile(info, io.BytesIO(data))
    result = subprocess.run(['/bin/bash', '--noprofile', '--norc', '-e', '-o', 'pipefail', '-c', command], env={'PATH': '/usr/bin:/bin', 'RUNNER_TEMP': str(root)}, capture_output=True, text=True, timeout=20)
    print('archive_members=' + repr(list(members)))
    print('exit_code=' + str(result.returncode))
    print('stdout=' + repr(result.stdout))
    print('stderr=' + repr(result.stderr))
    state = (owned / 'state/ordinary.o').read_bytes()
    print('normal_state=' + repr(state))
    if state != b'expected-state\n':
        sys.exit('Normal state restoration failed')
    after = sentinel.read_bytes()
    print('sibling_before=' + repr(b'verified-tool-input\n'))
    print('sibling_after=' + repr(after))
    if after != b'verified-tool-input\n':
        sys.exit('FAIL: state-family extraction changed the tools family')
    print('PASS: sibling ownership preserved')
