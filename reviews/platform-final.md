# Final targeted platform review

Reviewed 2026-10-25. Scope: GitHub cache lifecycle, publication/cleanup authority, capacity accounting, source transport layout, service selection semantics, and the executable qualification contract. This is a planning review, not implementation or runtime acceptance.

## Disposition

**Ready for bounded implementation and controlled qualification; no remaining material platform-contract blocker in this reviewed snapshot.** Actual repository inventories/settings, packaging bounds, complete snapshot sizes, disk peaks, observation closure, and performance remain pending. The plan does not establish a ten-billion-byte fit or universal warm behavior.

The earlier six findings are incorporated: effective per-job rerun attempts; ref shadow; explicit failure after a hard terminated writer; inventory-if-present non-Rust/image families; exact-ID repair of a corrupt candidate occupying the second slot; and evidence continuity after final source changes.

## Additional findings resolved in this revision

### Primary-key prefix selection

The official reference permits primary-key prefix fallback even with no restore-keys. In the exact pinned v2 restore implementation, the action sends key/restoreKeys/version, downloads and extracts the selected archive, and only then returns its matched key. There is no strict-key pre-extraction guard in the pin.

The discovery and bootstrap task contracts now require preflight of every service-selectable exact or primary-prefix candidate in visible scopes, with unauthorized or ambiguous provenance rejected before action extraction. They also require returned matched-key equality. Inventory preflight is not an atomic fence; audited writer capabilities remain necessary. C09 includes exact and longer-prefix shadows.

Source: [official matching contract](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching), opened 2026-10-25; [pinned restore executable](https://github.com/actions/cache/blob/55cc8345863c7cc4c66a329aec7e433d2d1c52a9/dist/restore-only/index.js), inspected directly.

### Source transport replicas

Retaining owned runner.temp transport is the smaller initial policy. The pin hashes literal action paths and compression, so approved Linux/macOS layouts can create physical source versions even when the logical source payload is portable. Its save path resolver also converts matched files to paths relative to GITHUB_WORKSPACE; tar creation/extraction uses that workspace root. A fixed absolute /tmp input therefore would not alone establish portable archive-member placement. GitHub does not promise static VM filesystem paths.

CAPABILITIES.md and CACHE_BUDGET.md now put source layout in compatibility/group identity, charge every physical version and replacement overlap, and apply the two-generation limit per active compatible group/version. The approved version set is bounded by the plan. No hidden global deduplication or mandatory cross-host source sharing is assumed. C02/C06 cover approved placement and version isolation.

Sources: [pinned save executable](https://github.com/actions/cache/blob/55cc8345863c7cc4c66a329aec7e433d2d1c52a9/dist/save-only/index.js), functions getCacheVersion/resolvePaths/getTarArgs; [runner filesystem contract](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#file-systems), opened 2026-10-25.

### Snapshot growth and proof order

Two archive generations do not bound obsolete Cargo outputs accumulating within an inherited target/build snapshot. Budget and C04/C17 now require repeated-update raw/stored growth measurement, with no guessed fingerprint deletion, hidden full rebuild, or automatic maintenance rebuild. Exhausted headroom remains an explicit capacity conflict.

Acceptance now proves the frozen archive rather than only a live build tree: join producers, freeze bytes and manifest, clear only owned target/build/ephemeral-MBX locations, restore the same bytes at identical paths, replay with Rust/RUSTDOC and applicable native/origin observation, and publish those unchanged bytes. Replay evidence binds the frozen digest outside the payload. Original seconds/nanoseconds, zero-epoch cases, and directory metadata are qualified without restoring stale metadata to changed parent directories.

### Authority and live execution

Image authority uses fixed renderer-owned data-only Python/gh/OCI code adapted from existing candidate.py/publish.py algorithms; it introduces no new validator API or release prerequisite. The independently approved normal generator controller bootstrap remains a separate existing release-asset trust boundary.

Hosted task macros remain blocked command contracts until the preceding qualification harness supplies concrete commands, source/workflow pins, namespace, run/fault budgets and applicable approval records. This review authorizes no workflow dispatch or mutation.

### Final report and measurement integration

The final 81-card revision adds explicit ownership for the actual merge and collection path. `required_bridge` preserves authenticated effective-job results through the final merge; `report_transport` carries typed observation members through the existing final report artifact with artifact/member digest bindings; `measurement_binding` validates the existing API-bound final-report ZIP before accepting its members; `measurement_aggregation` exposes those validated counters through the existing report builder.

These are report/control observations, not dependency payloads. Cache archives, target/build contents, sources, and tool bytes remain excluded from artifacts. Existing final-artifact CLI inputs and the authenticated size/digest boundary are retained. Loose files or producer-declared zeros do not become measured evidence.

The collector contracts distinguish effective Required results from total lifecycle work: retained jobs count once, actual reruns and failed attempts remain visible, and helpers/bootstrap/preparation/replay cannot disappear from resource totals. Missing observation remains unknown. The new Python verification commands check required discovered test IDs before execution; the acceptance examples explicitly reject an empty discovered suite rather than relying on unittest's process exit alone.

## Mechanical verification of the current task snapshot

- 81 tasks and 207 prerequisite edges; the graph is acyclic.
- The four qualification cards partition C01–C22 exactly once.
- Their cumulative discovered-test expectations are 6, 12, 17, and 22.
- The final set is exactly gc1_qualification::c01 through gc1_qualification::c22, matching ACCEPTANCE.md.
- No direct task Nextest run lacks --no-tests fail.
- Acceptance also requires executable discovered-name/count comparison, rejects missing/ignored/skipped required cases, and keeps auxiliary harness tests outside the 22-case filter.
- Final candidate generation explicitly builds the actual controller binary first.

No source compilation, test execution, workflow dispatch, cache read/write/delete, or runtime measurement was performed by this review. Mechanical checks validate the plan's structure, not the future implementation.

## Reviewed file identities

Final narrow equivalence: the task snapshot below declares the new Python observation test in T37's `new_files` and records T37 as T38's origin for that shared test file. These inspected metadata corrections complete file ownership without changing execution, authorization, capacity, or evidence policy. The accompanying WORKFLOWS.md and CACHE_BUDGET.md revisions add spacing to `attempt 2` and the root/runner GiB labels; their meanings are unchanged. This carries the preceding targeted verdict from task hash `b43129014e4da2691e5cc8c5dec2b5894c887f3657487ed097c7b28bd2c0fc7d` to the final hash below without claiming new runtime execution.

| File | SHA-256 |
|---|---|
| TASKS.json | `1f521b23ea4c5bc4054dc3f52dd03b8c3e4bb02334f14e05f4f3d12631328683` |
| ARCHITECTURE.md | `662323f1d73f3fe17b9496df65c5a85e6d52246a4dcadb50480c3dbba63ad9e9` |
| CAPABILITIES.md | `1a87c6d1c492e1e57461181173cf9a7a877ba199edf3a816bcf5c06d78adf970` |
| ACCEPTANCE.md | `e4898079990041c3df327bc1cfa067b3a60f6c2221c4e6d37b9a32fb10ea0e46` |
| WORKFLOWS.md | `4f36c47dc3d280700f5570c41f431b1a25850248882fa0857f2723e2db86ffe6` |
| CACHE_BUDGET.md | `eec63fc255276b06a4d45bbef06cac2cb0e3e18fc652928e4ffc95874c7368c5` |

These identities supersede the earlier 67-, 71-, 76-, and 77-card review snapshots for this targeted platform verdict. A later file change retains its own review/evidence binding rather than silently inheriting this hash.
