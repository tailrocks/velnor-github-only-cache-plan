import json
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
    }, sort_keys=True, indent=2) + '\n')
sys.exit(status)
