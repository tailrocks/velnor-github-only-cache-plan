import hashlib
import os
import sys
sys.path.insert(0, sys.argv[1])
from pathlib import Path
import job_image_authority_oci as oci_module
import job_image_authority_publish as publish_module
import job_image_authority_record as record_module
record_path = Path(sys.argv[2])
archive_path = Path(sys.argv[3])
result_path = Path(sys.argv[4])
record = record_module.validate_record(record_module.load_record(record_path))
verified = oci_module.verify_oci_archive(archive_path)
raw = archive_path.read_bytes()
publish_module.check_record_binding(
    record,
    hashlib.sha256(raw).hexdigest(),
    len(raw),
    verified,
)
manifest = publish_module.read_manifest_bytes(
    archive_path,
    verified["platform_manifest_digest"],
    verified["platform_manifest_size_bytes"],
)
record_raw = record_path.read_bytes()
identity = {
    "source": os.environ["VELNOR_IDENTITY_SOURCE"],
    "workflow_ref": os.environ["VELNOR_WORKFLOW_REF"],
    "run_id": int(os.environ["VELNOR_RUN_ID"]),
    "run_attempt": int(os.environ["VELNOR_RUN_ATTEMPT"]),
    "artifact_id": int(os.environ["VELNOR_ARTIFACT_ID"]),
}
ci = {
    "run_id": int(os.environ["VELNOR_RUN_ID"]),
    "run_attempt": int(os.environ["VELNOR_RUN_ATTEMPT"]),
}
record_archive = {
    "sha256": hashlib.sha256(raw).hexdigest(),
    "size_bytes": len(raw),
}
evidence = publish_module.build_evidence(
    identity,
    ci,
    record_archive,
    verified,
    manifest,
    hashlib.sha256(record_raw).hexdigest(),
)
result_path.write_bytes(evidence)
print("fixed authority body assembled the publication evidence")
