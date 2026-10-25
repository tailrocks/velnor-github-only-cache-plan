# Final Rust and source integration review

Reviewed: 2026-10-25. Scope: selected GitHub-only architecture and the 81-card implementation plan, including final merge/report transport and measurement integration. This is a planning disposition, not implementation approval or hosted runtime qualification.

## Disposition

The selected complete Cargo target/build snapshots, paired with an authenticated workspace source projection and separate source/tool families, form a coherent implementation candidate. The final plan addresses the material Rust integration defects identified during source review. No unresolved source-level contradiction remains in that selection, subject to the explicit controller-release prerequisite and live qualification gates below. This review does not establish that the complete working set fits the repository allowance or that every recipe can achieve zero unchanged dependency compiler work.

The source basis is Velnor [`e851b39e3bedc664f8bd6470c629e7bac36c561c`](https://github.com/tailrocks/velnor-new/tree/e851b39e3bedc664f8bd6470c629e7bac36c561c). Current source and caller evidence is recorded in [RESEARCH.md](../RUST_RESEARCH.md), the earlier security analysis in [SECURITY_REVIEW.md](rust-security.md), and the concrete correction history in [TASK_REVIEW.md](rust-source-initial.md). The final selected [ARCHITECTURE.md](../ARCHITECTURE.md) supersedes earlier alternatives in those research files, including the discarded image-helper API/release route.

| Reviewed artifact | SHA-256 at review |
|---|---|
| `deliverables/ARCHITECTURE.md` | `c3fac5e1bd3d2a703ed7db42e0b666e0e7ae1ad1f1dba9a72db5181124b71eec` |
| `deliverables/TASKS.json` — 81 cards | `1f521b23ea4c5bc4054dc3f52dd03b8c3e4bb02334f14e05f4f3d12631328683` |

Metadata-only equivalence: after the substantive `b43129014e4da2691e5cc8c5dec2b5894c887f3657487ed097c7b28bd2c0fc7d` review, T37 explicitly declares the new Python observation test file and T38 records T37 as that file's origin. This changes file-ownership metadata only; architecture, behavior, task scopes, and the reviewed test requirements are unchanged.

Later edits require a fresh disposition for the affected claims; these hashes are not transferable to changed bytes.

## Rust state and freshness

Execute at the actual current checkout. Place target/build directories, transport, verified tool prefixes, source archives, and reusable Cargo homes at deterministic owned runner paths outside it. Preserve the current checkout's Git metadata and private configuration boundaries. Sanitized Cargo Git databases and checkouts are permitted in the separate source family; the prohibition concerns current application-checkout Git metadata and credentials.

Reconcile every allowlisted tracked workspace input against the authenticated current inventory by content, type, mode, and link target. Only matching restored objects retain original archived metadata. Changed/current-only files remain current; cached-only paths are discarded. An unchanged child does not authorize restoration of its changed parent directory's old metadata. Git-derived dependency inputs retain their actual current semantics. Unknown filesystem, environment, Git, or native input closure blocks that recipe's cache qualification while normal CI still runs.

The approved tar crate does not make precision preservation automatic. Its PAX writer can record fractional time, but ordinary metadata capture/unpack uses integer mtimes, normalizes zero, and does not restore directory mtime through the ordinary directory branch. The implementation must record authenticated original seconds and nanoseconds, safely restore those original values, restore directory metadata after children, and verify actual host precision. It must never fabricate, normalize, or backdate timestamps for Cargo freshness. Unsupported link/metadata cases fail qualification. See the pinned [PAX writer](https://github.com/composefs/tar-rs/blob/0.4.46/src/pax.rs#L157), [header capture](https://github.com/composefs/tar-rs/blob/0.4.46/src/header.rs#L789-L803), [entry timestamp path](https://github.com/composefs/tar-rs/blob/0.4.46/src/entry.rs#L484-L508), and [Rust FileTimes](https://doc.rust-lang.org/std/fs/struct.FileTimes.html).

Full designated output trees retain generated native state and `.mbx-rustdoc-parts`. T20 now excludes designated disposable roots outside those trees; it does not authorize guessing which files inside Cargo output directories are expendable.

## Observation and completeness

The inspected MBX 1.26.0 and 1.27.0 support previous `RUSTC_WRAPPER` delegation and `MBX_TARGET_VIEWS=0`. Preserve the existing declared Cargo/MBX route without editing non-generator-owned Mise files. Persist no MBX object store, managed target views, or exports. A previous compiler wrapper does not disable MBX's separate rustdoc adapter.

Both owned Rust compiler and `RUSTDOC` observation are necessary. Distinguish compilation, probes, documentation finalization, doctest parents, and compiler descendants. Attribute actual work to the recipe/package; totals alone cannot prove zero dependency work when an application compiles. Unsupported descendant/native execution and unobserved build-script network traffic remain unknown and cannot pass as zero. Historical MBX version-five reports do not replace that attribution.

T25 now correctly requires a manifest **and separate digest-bound replay proof**. Join all producers, freeze complete bytes, clear only owned outputs and ephemeral MBX state, restore the same bytes at identical paths, then replay exact compiler-producing recipes with an empty MBX store and full observation. Publish the unchanged frozen bytes, not a repack of replay-mutated state. Count repeated tests and all extra compiler work. This prevents same-job MBX documentation hits from concealing missing persistent Cargo state.

## Existing caller integration

The corrected plan includes the actual integration seams:

| Area | Current source owner and required binding |
|---|---|
| Named/private checks | `check_prepare.rs`, `check_runtime.rs`, Mise `check_execution.rs`, and `qualified_acquisition.rs`: preserve disposable private HOME and declared task semantics while shared sources/tools/state use stable owned paths. Collect successful child evidence before cleanup. |
| Qualified tools | `check_tool_acquire.rs` and `qualified_acquisition.rs`: hydrate verified prefixes/archives before unconditional acquisition/build; preserve independent checks and probes. |
| Ordinary tool verification | `cache_steps_tools_installs_verify.sh`, `rust_toolchain_script.rs`, and `cache_steps_tools_restore.rs`: use verified cached archives before existing origin-fetch branches. `toolchain_env_fetch.rs` is a credential-filter file, not the acquisition owner. |
| Production coverage | `product_release_pins.rs`, `preview_producer.rs`, and actual native/stable producers: enumerate existing exact recipes, targets, LTO/profile/native environments and helper source identities. CI-only recipes are insufficient. |
| Output lookup | `schema2_generator_release_assets.rs`, `preseed.rs`, and credential-free `schema2_job_image_native.rs`: update executable lookup and staging as well as `CARGO_TARGET_DIR`. Preserve exact release arguments. |
| Required results | Accept exactly one bound selected-unit ledger across reader/writer branches. Authenticate retained earlier-attempt jobs separately from rerun jobs. A hard-failed selected writer cannot resurrect the completed reader. |

## Controller bootstrap: explicit prerequisite

The current Velnor source has no `generator.lock` and uses source preseed. There is no verified new controller pin with the proposed cache operations. Before live qualification/activation, the existing normal generator release handoff must produce a real independently approved controller asset and descriptor. The owner approves the exact release and activation; the plan does not automatically release a helper or assume an older binary implements new operations.

The bootstrap card's three-file boundary is appropriate: renderer `closure.rs::provision_acquire_step`, `steps.rs::acquire_velnor_step`, and new fixed `cache_bootstrap.py`. Preserve `HelperProvenance::ReleaseAsset` and its independently committed URL/source/digest contract. The bridge uses existing approved runtime capabilities, selects only the exact bounded standalone controller member from the tools payload, rejects unsafe/duplicate/linked members, and checks its independently expected SHA-256 before execution. It is read-only: no general state extraction and no save/admission bypass. A miss uses existing bounded exact-asset acquisition. The verified controller then owns general cache extraction and policy.

Keep the current source candidate as application work. The pinned controller restores its context before candidate compilation. Do not compile `build-owned-archive-guard.sh` to unlock warm restoration: that source bootstrap creates a fresh bootstrap target. Count initial normal-release work, controller download, first cache preparation, and candidate work in their correct lifecycle totals. Qualify the actual setup-action ordering so tools are hydrated before a setup/verifier that would otherwise redownload them.

## Fixed source-free image authority

The selected authority route is fixed renderer-owned data-only Python/`gh`/OCI code shared by attestation and publication, using the currently approved capabilities in `images/job/ubuntu-26.04/candidate/publish.py`. It preserves repository/workflow/source/CI/artifact/attempt/attestation and OCI byte checks, including allowed redirect handling and credential stripping. Independently authenticated exact-source GitHub data replaces local checkout reads. Candidate hashes alone do not confer authority.

Authority jobs perform no application checkout, source compilation, local application-script execution, candidate executable invocation, or candidate module import. Source evidence remains in the credential-free producer. No new image-helper CLI API, tool, protocol, or helper-release prerequisite is retained. This is separate from the ordinary controller bootstrap prerequisite above.

## Final merge and measurement integration

The final caller review identified that emitting owned Rust observations alone would leave the existing hosted collector reporting null. The 81-card plan now closes that integration path explicitly:

- **T35, required bridge:** `merge.rs`, `merge_checks.rs`, and `merge_request.rs` carry typed selected-unit ledgers and validated observations through the actual final merge while preserving original job/attempt identity.
- **T36, report transport:** `retrieve_reports.rs`, `task_report.rs`, and renderer `required_gate.rs` retain artifact/member provenance and include observations in the existing final-report artifact. This transports evidence, not dependency payloads.
- **T37, measurement binding:** `measure_support.py` and `report_events.py` validate versioned observations and actual effective attempts. The existing `validate_actual_counter_unknowns` rejects every numeric value for its listed counters, and `validate_identity` requires every job to match the top-level attempt; both need the explicit proof-aware change rather than silent removal of checks.
- **T38, measurement aggregation:** `report_counters.py::build_actual_counters` and `report_builder.py::build_report` ingest those verified records. They count each physical job/attempt/process once, keep lifecycle rerun/replay work separate from effective Required results, and retain separate origin/cache/MBX categories.

The existing `--artifact-json`, `--artifact-id`, and `--final-artifact` inputs already provide authenticated artifact metadata plus the actual final ZIP. `measure_support.py::validate_artifact` checks repository/run/source/name/attempt identity, exact archive size, and SHA-256 against the artifact API record before reading the payload. Extend that existing path to strict unique allowed observation members and explicit member-digest/source/run/job/actual-attempt bindings; no collector CLI change or new tool is necessary. Loose `task_report_dir` inputs currently lack parent ZIP digest verification and must not be promoted to authoritative measurement.

The report contract's existing validator is included in the explicitly bounded fourth-file exception for T05. The four new scopes and that validation wiring address the identified actual-caller gap without another cache architecture. Unknown observations remain null with reasons; compiler wall time does not establish native CPU time. Tests must cover unbound zeros, forged effective attempts, digest/member failures, retained-job deduplication, and complete helper/replay lifecycle work.

## Transport and lifecycle corrections

An exact primary key with no `restore-keys` is not an exact-only cache-service request. Preflight every service-selectable expected-version exact entry and longer primary-prefix entry across visible scopes. The pinned action extracts before reporting its matched key. Reject ambiguous/unsafe provenance before outer extraction, then require returned-key equality afterwards. There is no cache-ID/ref selector. A trusted-looking inner manifest cannot undo an unsafe outer extraction. See the platform's [CAPABILITIES.md](../CAPABILITIES.md) and [task review](platform-final.md).

The action's path/compression version and workspace-relative archived paths also prevent assuming cross-host portability. Count physical source-family replicas for distinct qualified host/path/compression layouts. Each compatible active group retains at most a current generation plus replacement overlap.

Mutation phases release and reacquire the same repository queue; they are not one cross-job transaction. When good A and reproducibly unusable B occupy both slots, reviewed cleanup may remove exact owned B while retaining A, confirm deletion, and only then admit a repaired generation. Missing readback during an outage is not corruption proof.

## Live gates still open

- Complete cache inventories and relevant settings remain unverified; the connector's allowlist HTTP 400 is not a permissions denial or zero usage.
- A real approved controller release and the hosted read-only bootstrap must be established before warm claims.
- Fresh-runner source/output metadata restoration, directory/Git semantics, complete production recipe replay, rustdoc/doctest/native attribution, and immutable origin coverage require live evidence.
- Full stored working-set size, action outer-envelope bounds, source replicas, migration overlap, competing families, peak disk, and cleanup lag must fit the unchanged 10,000,000,000-byte ceiling.
- Complete-pipeline wall/runner time and actual zero unchanged dependency compilation/origin download must be measured. No speedup or capacity fit is established here.
- Evidence must remain bound to the actual qualified final candidate SHA and generated bytes; later removals need reviewed equivalence or affected-case reruns.

No source implementation, workflow dispatch, cache mutation, settings change, or release occurred during this review.
