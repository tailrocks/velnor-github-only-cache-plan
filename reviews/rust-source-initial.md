# Independent Rust review of architecture and task cards

Reviewed the draft ARCHITECTURE.md and TASKS.json with 67 cards on 2026-10-25. This is a review of the draft, not implementation or runtime qualification. The parent has accepted the stable external execution-state root, qualified-tool hydration correction, direct rustdoc observation, empty MBX replay store, and precise timestamp restoration findings. The parent also selected fixed rendered data-only image authority operations, replacing the previously considered helper-API release route.

## Task-specific findings and minimal corrections

| Cards | Finding | Minimal correction |
|---|---|---|
| T08/T09/T17/T26 | The draft places .velnor-cache under GITHUB_WORKSPACE. Current Velnor .gitignore does not ignore it, while image source admission rejects all untracked files. This changes Git semantics and fails existing source checks. | Keep execution at current GITHUB_WORKSPACE but place transport, state, tools and source homes under a deterministic owned runner.temp root outside source. Include actual layout in compatibility. Do not edit consumer .gitignore or .git metadata to hide cache files. |
| T08/T12/T13/T31/T32 | QualifiedCheck environment projection does not remove the unconditional fresh download/build path in check_tool_acquire.rs. It also hardcodes tool prefixes in private homes. | Add a bounded hydration slice over orchestrator/check_tool_acquire.rs, orchestrator/check_tool_layout.rs, and mise/qualified_acquisition.rs. Reuse verified archives/prefixes before acquisition, retain independent checksum/tree/executable probes, and bind check_execution.rs::compiler_prefix to the same stable prefix through T08/T31. |
| T14/T21/T25/T45 | RUSTC_WRAPPER delegates Rust compilation but does not intercept direct rustdoc. MBX also retains its separate rustdoc cache adapter despite a preexisting rustc wrapper. | Configure a stable owned RUSTDOC adapter; distinguish documentation compilation, finalization, probes and doctest/descendant work. Unknown descendant work blocks qualification. Replay with an empty ephemeral MBX store after all sessions end. |
| T09/T17/T21/T45 | Byte/mode round trips do not establish Cargo freshness. Path rustdoc and old-style build scripts use mtimes in fingerprints. tar 0.4.46 default metadata/unpack loses subsecond time and normalizes zero. | Record original seconds+nanos, restore authenticated original metadata after safe extraction, restore directory times after children, and read back exact values. Never normalize timestamps. Preserve .mbx-rustdoc-parts inside complete output roots. |
| T34 | Actual generator release build setup/output lookup is in schema2_generator_release_assets.rs, absent from the card. Its build_script copies target/release or target/<triple>/release after executing the supplied argv. | Replace schema2_generator_release_source.rs in the T34 file list with schema2_generator_release_assets.rs; bind output lookup to the context. Keep source qualification unchanged. Preserve argv from product_release_pins.rs, including --release and explicit Intel target. |
| T07/T21/T34 | Ordinary CI recipes alone do not enumerate supported production variants. | Explicitly derive the producer recipe union from actual product_release_pins/build_steps and Jackin preview/stable commands, including LTO/SDK/target differences. Prepare only existing credential-free producer products. |
| T35 | preseed.rs owns PRESEED_BUILD_OUTPUT, checks, manifest source and staging copies; it is absent from the card. | Allocate that file in a small path-binding slice; setting CARGO_TARGET_DIR alone leaves source copies broken. Current image producer's schema2_job_image_native.rs needs the same correction. |
| T36–T39 | Earlier API-helper route has a release prerequisite cycle: T39 needs the new independently released API, while release handoff T58 is downstream of T39. | Parent chose fixed rendered data-only operations instead. Remove new API/descriptor/release work and use the concrete replacement below. |
| T21/T22 | Successful sequential producer history does not prove the published frozen payload survives restoration or supports all claimed recipes. | Freeze payload before the round-trip; restore exact frozen bytes at identical paths, then replay with empty MBX and full observation. Publish unchanged frozen bytes; keep replay proof outside archive. |
| T44/T45/T46/T49 | The inspected draft has self-prerequisite edges. | Remove self-edges and rerun DAG validation; parent is fixing task registration/module wiring separately. |

No additional compiler engine is necessary. MBX 1.26 and 1.27 both preserve existing RUSTC_WRAPPER, and configured_rustdoc honors an existing RUSTDOC. Do not invent an MBX_RUSTDOC=0 option: no such setting was found in the inspected configuration.

### Existing qualified-tool evidence

check_tool_acquire.rs::acquire unconditionally calls fetch_archives, builds Cargo-installed source tools via qualified_source_command, freezes/rechecks each prefix and probes executables. fetch_extract always invokes qualified_fetch_command and removes both the downloaded file and verified archive afterwards. observe_executables, compiler_prefix and validate_installations derive private-home paths. mise/qualified_acquisition.rs owns QualifiedCheck::qualified_tool_home, qualified_source_command, qualified_link_command and qualified_fetch_command. Pure check_qualified_tools.rs is catalog resolution, not the hydration seam.

## Fixed source-free image authority choice

Current images/job/ubuntu-26.04/candidate/publish.py uses Python standard library plus gh api and gh attestation verify. It implements bounded HTTPS OCI distribution requests directly to ghcr.io (HEAD, POST, PUT, GET); it does not invoke docker push, oras or skopeo. Preserve its repository ID, exact workflow/main/current-source, CI, artifact/run/attempt, attestation, digest/size, registry origin and auth-stripped allowlisted blob redirect checks.

Current source dependencies are git rev-parse in _current_identity, candidate.py imports, _verify_source_inputs(record, root), and .velnor/runner.lock parsing. Replace those root reads with independently authenticated GitHub source data at the exact source SHA. Candidate-supplied hashes alone never authorize signing. Do not fetch executable Python modules from the candidate artifact.

Suggested replacement scopes (three production files each):

1. **T36:** new renderer-owned job_image_authority_record.py, job_image_authority_oci.py, job_image_authority_tar.py. Factor existing strict record/OCI/tar validation into data-only code; no build or source execution entry.
2. **T37:** new job_image_authority_identity.py, job_image_authority_registry.py, job_image_authority_publish.py. Preserve current authenticated GitHub checks and exact OCI publication/readback; authenticate source/lock data through gh API.
3. **T38:** new job_image_authority.rs composing one fixed implementation shared by attestation and publication, plus orchestrator/image_maintenance/source.rs and build_candidate.rs only if producer evidence actually needs alteration. The source-closure artifact already exists; do not add a schema merely to occupy a task.
4. **T39:** schema2_job_image_candidate.rs, schema2_job_image_native.rs, and retirement of images/job/ubuntu-26.04/candidate/publish.py. Wire fixed code through the existing parent module, remove authority checkout/source compilation/local script execution, retain source-side validation in the credential-free producer, migrate existing publication tests. Retain candidate.py only for its still-current source-side uses.

No new CLI API or application-helper release prerequisite remains. Existing runner python3 is already used, but this review did not discover a separately Mise-pinned Python version; do not invent one. Use the existing pinned source-free gh acquisition path and qualify the actual hosted Python runtime.

## Exact archive timestamp capability

Pinned tar 0.4.46 source is in composefs/tar-rs, tag 0.4.46. Builder::append_pax_extensions is supported and can store an exact decimal PAX mtime. Ordinary unpack does not restore its precision: entry.rs::get_mtime reads the integer header, maps zero to one and creates FileTime with zero nanoseconds; regular extraction uses that value. Header metadata capture records integer seconds. Directory unpack returns before applying mtime.

Use the approved crate for archive framing and authenticated original metadata in the manifest/PAX fields, then restore original seconds+nanos through std FileTimes/File::set_times on safely opened regular files/directories. Directories are restored after child extraction. Read back the result and reject an unrepresentable host precision. File::open on a symlink would follow the target; use an already-approved no-follow facility or reject the unsupported case. Apply archived source metadata only to matching restored objects; changed current files and current .git remain untouched. This is ordinary restoration of original metadata, never a freshness timestamp fabrication.

Sources:
- https://github.com/composefs/tar-rs/blob/0.4.46/src/pax.rs#L157
- https://github.com/composefs/tar-rs/blob/0.4.46/src/header.rs#L789-L803
- https://github.com/composefs/tar-rs/blob/0.4.46/src/entry.rs#L484-L508
- https://github.com/composefs/tar-rs/blob/0.4.46/src/entry.rs#L693-L700
- https://doc.rust-lang.org/std/fs/struct.FileTimes.html
- https://doc.rust-lang.org/std/fs/struct.File.html#method.set_times

## Final recommended validation order

1. Join all Cargo, MBX, rustdoc and native producer sessions.
2. Capture and freeze the complete authenticated payload and manifest, including real metadata. Record its digest outside itself.
3. Clear only positively owned target/build and ephemeral MBX roots. Keep current checkout/.git, source authority and tools intact.
4. Restore that exact frozen payload to identical paths, reconcile current sources, apply original authenticated metadata and verify the manifest before execution.
5. Start the replay with a genuinely empty MBX store; supported MBX_CACHE_DIR selects its owned location.
6. Replay the exact compiler-producing recipes, recording all extra tests/work. Require zero unchanged dependency compiler work, complete family-specific observation and no destructive cross-recipe state collision.
7. Publish the same frozen bytes. The replay-mutated filesystem is not silently repacked into a different candidate.
8. Bind the separate replay evidence to frozen digest, coverage, host, source/run/job/attempt and observed outcomes. Remote readback later verifies the same frozen digest.

This proof cannot rely on same-job MBX rustdoc hits. MBX document() restores its own cached output and invokes finalize(), while --test bypasses that adapter; both boundaries must be visible. All required generated doc parts inside designated output directories remain in the snapshot.

