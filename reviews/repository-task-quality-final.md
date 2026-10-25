# Independent final task-quality review

**Verdict: the reviewed 81-card plan passes task-quality review. Runtime qualification remains pending.**

This is a completed review of the regenerated task files.
It supersedes the first-draft review and is separate from the criteria document.
No implementation, workflow dispatch, cache mutation, or compiler experiment was performed.

| Reviewed file | SHA-256 |
|---|---|
| TASKS.json | `1f521b23ea4c5bc4054dc3f52dd03b8c3e4bb02334f14e05f4f3d12631328683` |
| TASKS.md | `025cc9e81b9abeae0e140a73e1e89f3546fcd57f7b5099d1a693998c594822fa` |

Retained copies are in `task-review/TASKS.final.json` and `task-review/TASKS.final.md`.
Mechanical results are in `TASK_QUALITY_CHECKS.json`.
The first review remains in `task-review/TASK_QUALITY_REVIEW.initial.md`.
The current source baseline is Velnor `e851b39e3bedc664f8bd6470c629e7bac36c561c`.

## 1. Mechanical results

| Check | Result |
|---|---|
| Task identity | 81 cards and 81 unique IDs. |
| Dependency references | No missing dependencies or self-dependencies. |
| Acyclic graph | All 81 cards are acyclic. |
| Graph representations | The 207 explicit edges exactly match prerequisites. No duplicate edge exists. |
| Explicit writer ordering | No unordered collisions across permitted files, tests, or registration roots. |
| Current source paths | Every declared existing production path matches the current tree. Proposed production and collector-test files are marked new. |
| Module parents | Every explicit module parent is permitted. New implementation owners have immediate parents or their existing module root. |
| Repeated new files | None. Later writers identify prior file origins. |
| Production-file cap | No unexplained violation. T05 has a justified report-validator exception. T70 has a justified four-file mechanical exception. |
| Nextest guards | All 114 direct Nextest run commands contain `--no-tests fail`. |
| Discovery | All 58 future-prefix cards have listing commands and required discovery evidence. |
| Qualification | C01–C22 occur once in the four implementation assignments. Final expected discovery count is 22. |
| Migrations | One Jackin card and one per ChainArgos repository. Velnor dogfood uses its candidate gates. |

The writer result covers the explicit file lists.
T01's future regression, removal, and generated-output maps must be expanded before scheduling their consumers.
The plan requires forward writer edges and another cycle/conflict check at that boundary.
It does not assume that unknown paths cannot conflict.

## 2. Subagents and task size

Implementation, verification, and review run in subagents.
No model is prescribed.

T56 owns the named security review.
T57 owns the named architecture review.
Both run in subagents.
That work remains bounded by source owners and behavioral cases.

The 81-card count is not a defect by itself.
The added cards separate bootstrap, production recipes, fixed authority fragments, and bounded qualification subsets.
They do not add per-crate migration tasks or new products.

## 3. Closure of the original findings

| Finding | Current resolution |
|---|---|
| Q01: self-dependencies | Removed. Writer paths are deduplicated and the graph is acyclic. |
| Q02: uncompiled modules | T22 now owns `lib.rs` registration. Other new Rust modules name an allowed parent or own their module root. |
| Q03: existing test ownership | T01 emits an exact regression map. Behavior-changing cards consume its paths before editing. |
| Q04: missing discovery/regressions | Cards list tests, require named discoveries and nonzero execution, and run existing package regressions. |
| Q05: missing hosted candidate | T64 generates and verifies the candidate before T65–T67. It requires real controller release and owner activation evidence. |
| Q06: unresolved runtime macros | T58 owns `run-commands.json`. Labels are explicitly blocked until exact approved command arrays exist. |
| Q07: wrong crate for runtime tests | T53 keeps pure contract tests. T54 owns admission, intent, snapshot, and repair fixtures. |
| Q08: unbound removal map | T01 emits `removal-map.json`. T69 consumes its exact removal entry. |
| Q09: stale/post-verification generation | Candidate generation now builds the current CLI, compares two outputs, writes them, then runs full verification. Consumers use an approved immutable binary. |
| Q10: measurement blocks code | T21 separates local implementation from runtime-envelope qualification. Unknown bounds still block publication. |
| Q11: repeated new-file claims | Removed. Later edits have explicit file-origin records. |

No original finding remains open in the reviewed plan.

## 4. Real callers and registered tests

The review inspected the existing CLI.
T28 owns the actual `dispatch.rs` and `dispatch/operation.rs` route.
T29 owns `main.rs` and the compiler adapter entry.
Algorithms remain in the owning crates.
No generic shell-execution operation is introduced.

The six existing integration roots remain the test route:

- `velnor-actions-contract/tests/velnor_contract.rs`.
- `velnor-actions-rust/tests/velnor_rust.rs`.
- `velnor-actions-mise/tests/velnor_mise.rs`.
- `velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.
- `velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.
- `velnor-actions-cli/tests/velnor_cli.rs`.

The manifests use explicit registration.
The plan does not rely on automatic discovery of an unregistered sibling file.
Shared registration writers are ordered.

T58 creates the qualification module and separate auxiliary filter.
T59–T62 include cases through that module.
Their cumulative exact discovery counts are 6, 12, 17, and 22.
Expected final names are `gc1_qualification::c01` through `gc1_qualification::c22`.
Auxiliary tests stay outside that filter.

These test names are proposed.
The plan does not claim they already exist or have executed.
Source inspection does not substitute for observed test discovery.

The current public CLI supports `generate --output-dir`.
The two-directory parity check uses that real interface.
The candidate command set rebuilds current source before assigning its binary path.
This resolves the stale-binary risk after obsolete-code removal.

## 5. Shared interfaces and architecture

CONTRACTS.md is inherited by the cards.
Its records are proposed typed local records for the existing binary.
They do not define a service, backend, dependency, or external runner.

The task owners cover the critical paths:

- Actual CI, named-check, preview, stable, native, and helper recipes.
- Consumed tool/Cargo homes and exact command arguments.
- Three initial command families with isolated writable lanes.
- Stable Rust/rustdoc and approved native observation entries.
- Authenticated source projection in the actual workspace.
- Complete state freezing with real seconds and nanoseconds.
- Replay from frozen state with empty ephemeral MBX state.
- Publication of unchanged frozen bytes and exact readback.
- Complete accounting, provenance guards, active intent, and bounded repair.
- Effective-attempt ledgers for failed-job reruns.

The pre-extraction guard covers every service-selectable exact or longer primary-prefix entry.
An empty restore-key list does not eliminate primary-key prefix fallback.
Post-restore key equality remains necessary.
It does not make earlier untrusted extraction safe.

Paired source/tool generation digests record provenance.
They do not require old archives when current families cover the required immutable subsets.
Unrelated tool-union or source-generation changes cannot invalidate usable Cargo state.
Runner image revision is audit data unless relevant effective build inputs change.

## 6. Bootstrap and image authority

T43 owns a fixed read-only bootstrap in the existing acquisition renderer.
It preserves independent released-controller provenance and digest verification.
It cannot save before the verified controller applies normal admission.
It does not assume that the audited release already supports the proposed operations.

T64 requires a real approved normal controller release and activation before hosted qualification.
It cannot fabricate a pin or publish automatically.
T44 uses the bridge before building a current source-bound helper.
Changed helper compilation stays visible as application work.

T45–T48 use fixed data-only Python fragments and existing gh/OCI behavior for image authority.
They do not introduce a candidate-built validator or new helper API in privileged jobs.
The fragments use the existing Python standard library.
Existing product/source authentication remains required.

No task introduces external dependency storage, MBX modification, or dependency transfer through artifacts.

## 7. Runtime gates and final source

T65 covers C01–C06 and C17–C19.
T66 covers C07–C15 and C20.
T67 covers C16, C21, and C22.
All 22 cases have an owner.

Hosted command records require exact workflows, inputs, source pins, budgets, and approval states.
Undefined or unapproved records remain blocked.
Local fixture success cannot complete those live tasks.

T72 regenerates after obsolete-code removal.
It verifies final source and generated output.
It requires affected runtime cases again unless independent review establishes strict removal equivalence.
Retained evidence stays bound to the actual source SHA.

T73–T80 require an approved generator, actual repository gates, applicable products, capacity proof, and runtime authorization.
They do not create release products for the seven ChainArgos CI-only current contracts.
Historical bitcoin-gRPC publication remains historical evidence.

T81 may finish a report containing explicit blockers.
The overall cache goal cannot complete while required observation, capacity, or runtime gates remain blocked.

## 8. Conditions retained for implementation

1. Expand and validate T01's exact maps before dependent tasks write files.
2. Enforce real module registration and nonzero discovery.
3. Resolve the approved controller release and candidate activation.
4. Resolve concrete hosted commands and bounded authorization.
5. Measure inventories, stored bytes, and qualified outer envelopes.
6. Qualify compiler, native, and acquisition observation.
7. Run controlled cold/warm and failure cases.
8. Bind final evidence to final source and generated outputs.

These are explicit execution requirements.
They are not approvals granted by this planning review.
No live ten-GB fit or measured speedup is approved here.
No compiler count is inferred from Cargo progress lines.
Unknown observation remains unknown.

## 9. Final collector and report integration

Four added tasks close a real existing-caller gap.
T35 binds grouped ledgers through the actual final merge.
T36 carries validated observations through existing report artifacts.
T37 validates API-bound observation evidence and effective attempts.
T38 aggregates complete executed lifecycle work.

The inspected collector currently requires several actual counters to remain null.
Its job identity validation also requires one global attempt.
Those rules cannot accept the proposed measured observations and mixed-attempt retained jobs unchanged.
The added tasks own the actual affected source files.
They preserve historical unknowns instead of replacing them with unsupported numbers.

The existing collector already accepts artifact API JSON, artifact ID, and the final ZIP together.
It verifies the API-bound size/digest and final-report identity.
The new cards reuse those inputs without adding a CLI or tool.
CONTRACTS.md now defines the versioned observation index within final-report.json and its bounded JSON members.
Member digests, producer jobs, source, plans, and actual attempts remain bound to that verified artifact.
Loose extracted reports do not become authenticated observations.
No artifact carries cached source, tool, Cargo, or dependency archive payloads.

Effective Required results and total executed lifecycle work are separate aggregates.
Retained successful jobs count once.
Failed attempts and subsequent reruns remain visible.
Bootstrap, helper, preparation, and frozen replay work are included.
Native CPU time remains unknown unless measured; compiler wall time is not a substitute.

Both new Python test commands were parsed successfully as Python source.
Their deterministic required-name sets, nonempty discovered-set checks, printed names, and wasSuccessful checks are present.
No future test was executed during this review.
T37 declares the new shared test file.
T38 identifies T37 as its origin and depends on it.
The shared test writer is therefore ordered.

The final 81-card graph has 207 matching edges and no cycles or explicit writer conflicts.
The new context-contract fourth file is the existing report validator.
Its exception is explicit and limited to keeping definition, validation, and registration consistent.

## 10. Review basis

I read the regenerated cards and matched earlier findings to their stable task names.
I compared paths with the current source tree.
I inspected the CLI, module roots, test roots, and contradictory legacy assertions.
I checked graph closure, edge equality, writer order, models, caps, and test guards mechanically.
The script uses existing standard-library Python and is not a new Velnor linter.

Pinned sources:

- [CLI command tree](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-cli/src/args.rs).
- [Private CLI dispatch](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-cli/src/dispatch.rs).
- [CLI entry point](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-cli/src/main.rs).
- [Orchestrator module root](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-orchestrator/src/lib.rs).
- [Existing lane assertion](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-orchestrator/tests/impl_lane_isolation.rs).
- [Verification policy](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/docs/implemented/repo-verification.md).
