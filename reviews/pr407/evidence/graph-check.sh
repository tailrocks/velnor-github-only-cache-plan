python3 - <<'PY'
from pathlib import Path
import re
text = Path(".github/workflows/ci.yml").read_text()
blocks = dict(re.findall(r"^  ([a-z0-9-]+):\n(.*?)(?=^  [a-z0-9-]+:\n|\Z)", text, re.M | re.S))
writers = {key: value for key, value in blocks.items() if key.startswith("rust-") and key.endswith("-write")}
assert writers
for key, block in writers.items():
    reader = key[:-6] + "-read"
    reader_if = re.search(r"^    if: (.+)$", blocks[reader], re.M).group(1)
    writer_if = re.search(r"^    if: (.+)$", block, re.M).group(1)
    assert "github.event_name != 'push'" in reader_if
    assert "github.event_name == 'push'" in writer_if
    assert f"      - {reader}\n" in block
    assert not re.search(r"\b(?:always|cancelled|failure|success)\s*\(", writer_if)
print(f"{len(writers)} writers depend on push-skipped readers")
PY
