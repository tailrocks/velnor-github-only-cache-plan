# Acceptance contract

## 1. Status and scope

This file defines future acceptance. It does not report completed runtime qualification.

Use [ARCHITECTURE.md](ARCHITECTURE.md) for the fixed design.
Use [CACHE_BUDGET.md](CACHE_BUDGET.md) for admission and accounting.
Use [EVIDENCE.md](EVIDENCE.md) for current and historical observations.

All 22 cases below are required.
All replacement-cache runtime results are **pending**.
The current repository audit does not constitute a controlled cold/warm baseline.
No measured speedup or ten-GB fit is claimed.

Keep these statuses separate:

| Status | Meaning |
|---|---|
| Source verified | A pinned source establishes an existing command, boundary, or behavior. |
| Fixture passed | An implemented local test passed with its recorded inputs. |
| Hypothesis | The design predicts behavior that needs a runtime test. |
| Pending measurement | No qualifying measurement exists. |
| Pending authorization | A live action lacks the required approval record. |
| Unsatisfied | A required assertion failed or cannot be observed under the allowed tools. |
| Qualified | Every required assertion has complete, attributable evidence. |

A local fixture does not prove GitHub service behavior.
A successful workflow does not prove cache publication.
An unknown measurement is not zero.
An unavailable native observer makes the affected guarantee unsatisfied.

## 2. Fixed implementation boundaries

Use the existing pinned tools, dependencies, actions, and hosted runner classes.
Do not install a new observer, packet monitor, tracing tool, cache client, or test runner.
Do not modify MBX.
Do not persist MBX objects or managed target views.
Keep MBX transparent wrapper chaining where the configured command route uses MBX.

Use separate sources, tools, and complete Cargo-state archives.
Keep the initial build/test, Clippy, and documentation lanes.
Pair Cargo state with its authenticated workspace source projection.

Execute in the actual `GITHUB_WORKSPACE`.
Restore matching files and matching subtrees there through normal archive restoration.
Preserve their real archived metadata, including original timestamp precision and directory metadata.
Record and round-trip nanoseconds where the source filesystem supplies them.
Restore directory metadata after restoring its authenticated children.
Restore a subtree's archived directory metadata only when the current subtree is unchanged.
An unchanged file inside a changed directory does not authorize restoring that directory's old metadata.
The existing tar crate's default unpack behavior is not sufficient evidence of fractional timestamp or directory-time preservation.
Use existing approved extraction and filesystem capabilities to restore recorded original metadata.
If the allowed host or extraction route cannot preserve required metadata, block that recipe's qualification.
Keep changed checkout files, new files, deletions, and current Git metadata correct.
Do not cache `.git`.
Do not write fabricated, normalized, or backdated timestamps.
Do not use an alternate execution root to conceal path-sensitive failures.
Keep cache homes and transport under stable owned RUNNER_TEMP paths outside the checkout.
Do not change consumer ignore files to hide cache directories.

Run each exact selected package command in the combined job.
Keep its features, target, profile, environment, warnings, and result.
Do not substitute workspace commands for package commands.
Do not remove dependency roles from unchanged workspace libraries.
Do not reduce checks, products, optimization, LTO, or debug settings to pass.

Only trusted default-branch jobs may publish dependency caches.
Use one repository mutation queue.
PR, merge-group, tag, preview, and release consumers remain read-only.
Authority jobs must not execute restored compiler state.

## 3. Evidence record

Every case produces one structured record.
Each record must contain these fields:

- Case ID and case name.
- Source SHA, generator version, workflow SHA, and pinned tool/action identities.
- Repository, event, ref, run ID, run attempt, and every relevant job ID.
- Runner image, host architecture, target, compiler, SDK, and native library identities.
- Exact selected unit IDs and exact argv for every command.
- Compilation profile, Nextest profile, features, environment identities, and working directory.
- Dependency roles, immutable source identities, and declared build-script inputs.
- Requested coverage, completed coverage, compatibility, scope, and publication identity.
- Cache key, ref, version, ID, actual stored bytes, and payload digest.
- Actual compiler ledger, origin ledger, cache-transfer ledger, and observation gaps.
- Source projection before/after digests and metadata comparisons.
- Whole-pipeline measurements and per-phase measurements.
- Case assertions, their evidence references, and their individual statuses.
- Approval record, live fault allowance, namespace, and budget when applicable.

Use null for unavailable numbers.
Attach a reason to every unavailable required field.
Do not replace missing values with zero, an empty list, or an estimate.

Record all pipeline jobs.
Include skipped, failed, cancelled, preparing, signing, publishing, and cleanup jobs.
Bind every job and log to its run attempt.
Keep each job's actual effective attempt.
Accept a retained earlier successful job only when authenticated GitHub records show that it did not rerun.
Require new results for rerun jobs. Never relabel an old receipt as current execution.

The command ledger must distinguish selected units from process observations.
Each selected unit needs one final result.
A cache receipt cannot satisfy a test or check result.
A `needs_prepare` response does not complete a unit.
Require exactly one complete result ledger from the reader or conditional writer.

## 4. Nonempty workload and observation rules

### 4.1 Positive controls

Define the eligible dependency set before each case.
Use the current task plan and dependency roles.
The set must contain at least one eligible dependency compilation unit.

Run the same workload with empty owned target/build homes in the approved cold control.
Observe at least one real eligible dependency compiler execution.
For a native claim, require at least one real native compiler execution in its cold control.
A compiler version query cannot satisfy either control.

Define the covered immutable-origin set before the case.
Include the actual required packages, Git sources, private assets, tools, and verification inputs.
Use empty acquisition homes in the controlled acquisition baseline.
Record positive origin acquisition when that case claims to test acquisition avoidance.

A dependency-free sentinel can test cache transport.
It cannot qualify zero dependency compilation or avoided dependency downloads.

For a fault case, keep the same nonempty dependency workload.
A deliberate missing cache may cause legitimate cold work.
The fault case passes only its recovery assertions.
It does not become a warm performance result.

### 4.2 Compiler ledger

Use the stable Velnor-owned `RUSTC_WRAPPER`.
Use the stable owned `RUSTDOC` adapter for direct documentation work.
Keep its path and invocation semantics stable across the paired runs.
Use supported MBX previous-wrapper chaining when MBX remains selected.
Do not use changing wrapper paths as an accidental Cargo invalidation input.
Rust compiler wrapper delegation does not by itself disable MBX's separate rustdoc reuse.
Qualify the selected rustdoc route independently and start replay with an empty ephemeral MBX store.

Record an invocation before delegation.
Record its completion and exit status.
Bind it to the recipe, package, dependency role, target, profile, and lane.
Distinguish true compilation from version, capability, target, and sysroot queries.
For rustdoc, distinguish dependency documentation compilation, merge finalization, probes, and doctest descendants.
Record descendant Rust compiler work even when the top-level rustdoc process is not itself eligible dependency compilation.
Retain failed and interrupted compiler invocations.

Validate observer completeness with an installed-compiler positive control.
Validate exit-code propagation with a controlled failing invocation.
Validate package attribution with two packages and an unchanged workspace dependency.
Do not infer physical compiler work from Cargo `Compiling` lines.

Historical MBX version-five evidence may corroborate counts.
Its physical compiler outcome sum is:

`compiler.miss.invocations + compiler.unconsulted.invocations + compiler.bypass.invocations + compiler.verification.invocations`

The report does not provide the required complete package ledger.
Top-level MBX hits and misses are not physical compiler counts.
MBX object imports and same-job hits do not prove cross-run Cargo-state reuse.

### 4.3 Native and origin observation

Use approved CC/CXX adapters for native commands that honor those interfaces.
Record the actual executable, arguments, identity, package, and result.
Audit absolute compiler calls and build-system escape paths.
A wrapper cannot prove that unobserved child processes did not execute.
Mark uncovered native execution as unknown.

Record acquisitions at every existing owned fetch boundary.
Bind each immutable object to its origin, identity, request, received bytes, and verification.
Count verification archives that tools download again.
Record failed and retried origin acquisition separately from successful acquisition.

Audit build scripts, code generators, private fetches, and native build commands.
Silent HTTP requests outside the observed boundaries remain unknown.
Do not claim zero origin traffic from an empty Cargo download summary.
Do not introduce a proxy or external packet observer.

For a fully qualified warm result, both observation closures must be complete.
Unknown native calls or silent origin acquisition block the corresponding zero-work claim.
Ordinary CI must still execute its checks.

### 4.4 Cache transfers

Measure cache downloads and uploads separately.
Record transferred bytes, duration, archive unpacking, verification, and materialization.
Fresh runners may receive nonzero cached bytes.

Record inner archive bytes and GitHub's stored `size_in_bytes` separately.
Record sources, tools, source projection, and each Cargo lane separately before packing.
Do not equate a tool log's download size with repository cache inventory.

### 4.5 Frozen-archive replay

Final publication proof must exercise the archive that will actually be saved:

1. Join every Cargo, MBX, rustdoc, and native producer process before snapshotting.
2. Freeze the complete payload and its manifest. Record the archive digest outside that archive.
3. Clear only positively owned target/build and ephemeral MBX directories, after all relevant processes have stopped.
4. Restore those same frozen bytes at the identical qualified paths, with authenticated source projection and original file/directory metadata.
5. Replay the exact compiler-producing recipe sequence against the restored state and empty ephemeral MBX store, using both Rust and rustdoc observation plus the applicable native/acquisition observers.
6. Require complete observation and zero unchanged eligible dependency compiler work during replay. Record tests, application work, and every repeated command separately.
7. Bind the replay result to the frozen digest and publish those unchanged bytes only after admission. Keep replay evidence outside the archive through existing report transport.

Do not repack the replay-mutated tree and claim the earlier replay proved that different archive.
An earlier successful recipe whose state was overwritten cannot establish final coverage.
Unknown observation, metadata loss, missing output, or repeated eligible dependency compilation fails qualification.
Ordinary check outcomes remain visible independently.

## 5. Numerical acceptance

### 5.1 Correctness and warm-work thresholds

Let `E` be the predeclared nonempty eligible dependency set.
Let `C(E)` count actual compiler executions attributable to that set.
Let `N(E)` count actual eligible native compiler executions.
Let `D(O)` count origin acquisitions for the covered immutable-origin set.
Let `B(O)` count their received origin bytes.

A qualified warm result requires:

```text
|E| > 0
cold_control.C(E) > 0
warm.C(E) = 0
warm.N(E) = 0                 when native work is covered and fully observed
warm.D(O) = 0
warm.B(O) = 0
unknown_required_observations = 0
unexpected_missing_outputs = 0
unexpected_selected_unit_results = 0
```

For a native claim, also require `cold_control.N(E) > 0`.
For an origin-avoidance claim, require a positive acquisition control.
A zero compiler count with a skipped workload fails.

Let `P` be the ordered planned command ledger.
Let `X` be the observed executed-unit ledger.
Normalize only volatile execution coordinates.
Require exact equality of unit identity, argv, features, targets, profiles, and effective input identities.
Require `P = X`.
Keep intentional recipe ordering and repeated commands visible.
Require one accepted terminal result per planned unit.

For a dependency update, partition dependencies before execution.
Let `U` contain unchanged, compatible dependencies outside the changed dependency closure.
Require `|U| > 0` and `C(U) = 0`.
Report legitimate changed-closure compilation separately.
Do not describe that entire update run as zero compilation.

### 5.2 Capacity and disk

Use `H = 10,000,000,000` bytes as the conservative repository ceiling.
Start with `L = 8,000,000,000` bytes as the operating ceiling.
Keep `H - L >= 2,000,000,000` bytes.
Increase the reserve when measured uncertainty requires it.

Let `I` be complete actual inventory bytes.
Let `P` be pending owned writes absent from that inventory.
Let `A` be the qualified outer-archive upper bound.
Let `F` be bounded foreign in-flight exposure.

Require `I + P + A + F <= L <= H` before publication.
Do not count old baselines twice when they already appear in `I`.
Do not omit old namespaces, other refs, cache versions, or foreign families.

After publication, reconcile actual inventory bytes.
Require actual occupied bytes plus outstanding charges to remain within the accepted bound.
Charge predecessors until deletion is confirmed.
Keep the usable predecessor when replacement verification fails.
Count an unverified or corrupt remote candidate as occupied bytes and a generation slot until exact-ID deletion is confirmed.
Do not publish a third generation to bypass unresolved readback or delayed cleanup.

Measure extraction, snapshot, packing, action repacking, and readback disk peaks.
Require the peak plus measured operating reserve to fit available runner disk.
Do not accept a compressed archive fit as proof of local disk fit.

Unknown inventory, unknown packaging bounds, or unbounded writers block publication qualification.
A simulated near-limit fixture must not fill the live repository.
Use synthetic inventory records for limit branches.
Use small approved live entries only to qualify packing and API accounting.

### 5.3 Time and resource thresholds

Collect repeated comparable baseline observations before setting time claims.
Use the same source, selected commands, runner class, tool pins, and observation.
Separate queue delay from execution time.
Keep queue delay in the user-visible full-pipeline report.

Measure these values:

- Full pipeline wall time.
- Required-check critical-path time.
- Sum of all job runner durations.
- Tool setup and verification time.
- Origin acquisition time and bytes.
- Cache restore, save, readback, and materialization time.
- Conditional preparation time.
- Cleanup time and delay.
- Raw payload bytes, stored bytes, and peak local disk.

Use an approved sample count before measurement.
Require at least five complete matched observations for a comparative timing claim.
Retain every admitted observation.
Apply predefined invalid-run rules without selecting favorable runs.

For metric `m`, compute baseline median `b50(m)`.
Compute median absolute deviation `MAD(m)`.
Compute baseline 95th percentile `b95(m)`.
Record timer resolution `r(m)`.

Define the baseline variability allowance:

`A(m) = max(b95(m) - b50(m), 3 * MAD(m), r(m))`

Set the regression ceiling to `R(m) = b50(m) + A(m)`.
Freeze the baseline and ceilings before the candidate series.
Require the candidate median to remain at or below `R(m)`.
Report candidate 95th percentiles separately.
Require `candidate95(m) <= b95(m) + A(m)` for the tail comparison.
Report sample count and the limited precision of small-sample percentiles.

For a speedup claim, define `G = cold50 - warm50`.
Require `G > A(cold) + A(warm)`.
Report the measured values and spread.
Do not report a percentage until both series exist.
Do not accept a faster Rust job when the complete pipeline regresses beyond its ceiling.

Cold preparation is real lifecycle cost.
Report total cost for baseline preparation plus the approved number of warm consumers.
Do not hide preparation in a different workflow.
If the sample budget cannot support timing qualification, report timing as pending.

## 6. Approved execution mechanisms

### Local fixture mechanism: L

Add the 22 deterministic lifecycle fixtures to Velnor's existing Nextest integration harness.
Use `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs` for registration.
Use bounded sibling test modules for case implementations.
The proposed module name is `gc1_qualification`.
These new tests do not exist at the audited head.

Use existing test-support temporary directories and installed commands.
Model GitHub responses through the existing owned transport seams.
Do not send mutations to GitHub from a unit test.
Test compiler and native adapters with bounded local positive controls.

Use the Rust crate's existing integration root for Rust-specific observer and recipe tests.
Use the contract and renderer roots for their respective pure tests.
Do not place process execution inside a stack-neutral contract crate.
Do not add a new integration-test binary for each case.
The affected manifests use explicit test registration.

### Hosted mechanism: H

Extend the generator-owned qualification path.
Use the existing `.github/workflows/qualification.yml` ownership boundary.
Replace obsolete MBX object-roundtrip assumptions through the generator.
Do not hand-edit generated workflow output.
Do not copy the older MBX qualification protocol into the new implementation.

Use fresh jobs and separate runs for cross-run reuse.
Use the actual source-bound workload.
Use only GitHub dependency caches for dependency state transfer.
Existing report transport may carry measurements and receipts.
It must not carry dependency archives.

A live campaign needs a concrete approval record.
Record its repository, source/workflow SHA, exact cases, events, runner classes, and maximum runs.
Record its maximum concurrent jobs, stored-byte budget, and fault allowance.
Record the approving owner and the authorized cleanup IDs or ownership rule.
Do not infer dispatch, deletion, cancellation, or settings authority from this plan.

The preceding qualification-harness task produces the exact run-command manifest consumed by hosted tasks.
It resolves repository, candidate source/workflow SHA, case IDs, existing event mechanism, runner classes, run limits, namespace, collection commands, and permitted fault/cleanup operations to concrete commands and inputs.
Use the existing workflows, GitHub client, and collection scripts; the manifest is existing test-control data, not a new runner or protocol.
Macros or placeholders in a hosted task remain blocked command contracts until this output is populated and covered by the campaign's authorization.
Do not invent dispatch commands or execute an unapproved command merely because it appears in the plan.

Use a distinct qualification namespace with an approved campaign identifier.
Keep that namespace outside production identity rules.
Bound its total bytes before the first write.
Require `inventory + pending + qualification_bound + foreign_bound <= L`.
Do not reserve an arbitrary fraction of the repository without inventory evidence.

Trigger events through approved existing workflows.
Use real event scopes when qualifying service access.
A synthetic local event JSON proves policy logic only.
Do not invent release products to obtain a release test.

### Retained-evidence mechanism: R

Use existing read-only collection and validation scripts.
Their current paths are source verified:

- `scripts/hosted_phase_measurement/measure_hosted_run.py`
- `scripts/source_qualification_execution.py`
- `scripts/owned_mbx_observation.py`
- `scripts/test_source_qualification_execution.py`
- `scripts/test_owned_mbx_observation.py`
- `scripts/test_qualify_mbx_observation.py`

Extend these owned paths only within their current responsibilities.
The MBX script currently says native qualification is unavailable.
Its smoke result is not native reuse evidence.

A retained-log collector does not generate absent observations.
Historical records remain historical.
A connector allowlist rejection remains distinct from a GitHub permission denial.

## 7. The 22 required cases

Each case uses the full evidence record and numerical rules above.
Each dependency workload is nonempty.
Each warm assertion requires its paired positive cold control.
Local simulation and live qualification have separate results.

### C01. Complete cold run with no cache entries

**Inputs.** Use the full selected command set and empty owned sources, tools, and Cargo-state homes.
Prove no matching qualification entries exist.
Require nonempty dependency, tool, and source acquisition sets.

**Mechanism.** Run L for lifecycle branches.
Run H only in the approved empty qualification namespace.
Do not delete production entries to create this condition.

**Assertions.** Observe positive actual dependency compilation and positive covered origin acquisition.
Observe native compilation where the workload includes native dependencies.
Execute every planned unit.
Publish only complete, admitted generations.
Verify exact remote readback and actual stored bytes.
Record all preparation, transfer, packing, and pipeline costs.

**Basis/status.** Source defines the commands and publication boundaries.
Cold correctness and actual size are hypotheses.
Controlled measurement and live authorization remain pending.

### C02. Identical run on fresh runners with empty targets

**Inputs.** Reuse C01's exact source, commands, tools, environment, and published generation.
Start another fresh runner with empty local owned homes.
Keep the same nonempty eligible dependency set.

**Mechanism.** Run L for validation and placement.
Run H in a separate approved workflow run.

**Assertions.** Restore all required state into the actual homes.
Verify the source transport's literal action path, computed cache version, workspace-relative outer members, and actual restored placement for each approved runner layout.
Charge separate physical source replicas when layouts or compression produce different versions; cross-host sharing is not required for initial acceptance.
Require zero eligible dependency compiler work and zero covered origin acquisition.
Require complete native observation before asserting native zero.
Measure cache transfer independently.
Do not start preparation or save an unchanged generation.
Require exact command-ledger equality.

**Basis/status.** Current source-cache hits establish neither state reuse nor this result.
Cross-run reuse, native zero, origin zero, and timing remain pending.

### C03. Application-only change with unchanged dependency inputs

**Inputs.** Change only top-level application inputs.
Keep at least one unchanged eligible dependency, including an unchanged workspace dependency.
Record the actual changed path list.
Keep dependency coverage unchanged.

**Mechanism.** Run L with changed, unchanged, new, deleted, executable, and link projection fixtures.
Run H with an approved source pair.

**Assertions.** Preserve real metadata for identical restored files and subtrees.
Compare original and restored timestamp seconds/nanoseconds, directory metadata, file types, modes, and link targets.
Include a recorded zero-epoch timestamp and subsecond timestamps in bounded extraction fixtures, so normalization or precision loss cannot pass unnoticed.
Include unchanged files inside a changed parent, unchanged whole subtrees, deleted/new entries, broad directory watchers, and Git-derived build inputs.
Keep changed checkout contents and current Git metadata correct.
Do not restore `.git`.
Do not fabricate timestamps.
Require zero unchanged dependency compiler work and covered origin acquisition.
Report legitimate application compilation separately.
Require the same dependency generation without a commit-keyed replacement.

**Basis/status.** Projection correctness is a design hypothesis.
Fresh-checkout Cargo reuse requires measurement.
Path-sensitive or metadata-sensitive failures remain unsatisfied until resolved.

### C04. One dependency update with unrelated dependencies unchanged

**Inputs.** Change one resolved dependency.
Predeclare its affected closure.
Keep a nonempty unchanged compatible set outside that closure.

**Mechanism.** Run L for closure classification and coverage changes.
Run H using an approved real dependency update or bounded existing fixture.

**Assertions.** Change requested coverage.
Reuse compatible predecessor outputs.
Measure raw and stored snapshot growth across successive dependency updates, including inherited obsolete Cargo outputs.
Two archive generations do not bound the contents of either snapshot.
Require zero compiler work for the unchanged set.
Attribute legitimate changed-closure compilation and origin acquisition.
After trusted publication, require C02's zeros for the new complete generation.
Do not convert a source-cache hit into a compiled-state claim.

**Basis/status.** Existing Cargo metadata machinery supplies selection inputs.
Selective reuse and complete replacement size remain pending.

### C05. Feature or profile change without a lockfile change

**Inputs.** Keep the lockfile fixed.
Change an actual configured feature set or compilation profile.
Include at least one dependency whose effective compilation inputs change.

**Mechanism.** Run L over the exact variant recipes.
Run H only for existing supported variants.

**Assertions.** Detect the changed coverage or compatibility input.
Do not accept the old receipt as complete.
Keep Nextest's test profile distinct from Cargo's compilation profile.
Run the exact commands and legitimate missing work.
Require warm zeros after trusted preparation of the new variant.
Keep cache transfers and native variant observations separate.

**Basis/status.** Current manifests and commands establish available variants.
Cross-variant reuse and stored working-set size remain pending.

### C06. Host, target, compiler, native-library, or SDK change

**Inputs.** Vary each relevant compatibility dimension separately.
Use actual supported producer environments.
Each variant retains nonempty eligible dependency work.

**Mechanism.** Run L for every identity dimension.
Run H only on existing approved runner classes and supported installed toolchains.

**Assertions.** Reject incompatible state before use.
Include approved source transport-layout and compressor changes; verify action-version isolation and actual archive-member placement.
Keep compatible source objects reusable where permitted.
Record compiler, target, native library, and SDK identities.
Do not infer compatibility from a matching lockfile.
Require a positive cold control and later warm zeros for each admitted variant.
Unknown native identity blocks that variant's qualification.

**Basis/status.** Source establishes required variants.
Actual native binary identities and per-variant measurements remain pending where absent.

### C07. PR rerun, merge to main, preview, and stable release

**Inputs.** Test an application-only sequence and a dependency-changing sequence.
Use each repository's actual products.
Preserve preview and stable profile differences.
Keep nonempty unchanged dependency coverage in each sequence.

**Mechanism.** Run L for trust transitions.
Run H only through approved real events and existing product workflows.

**Assertions.** PR runs never publish.
Application-only reruns reuse the trusted baseline.
New PR dependencies may rebuild until trusted main preparation exists.
After merge, prepare missing coverage once under trusted authority.
Do not promote PR compiler output through a cache prefix.
Preview and stable builds consume their correct prepared variants.
Record all sequence costs and each event's compiler/origin/cache ledgers.

**Basis/status.** Current product workflows establish applicability.
The minimum trusted preparation exception is architectural.
End-to-end sequence measurements remain pending.

### C08. Fork PR with restricted permissions

**Inputs.** Use a real restricted fork context where supported.
Keep a nonempty public or otherwise authorized dependency workload.
Include private-source denial as a distinct branch when applicable.

**Mechanism.** Run L with restricted capabilities and unauthorized private assets.
Run H only with an approved fork fixture and no added secrets.

**Assertions.** Enforce explicit read-only cache access.
Keep origin credentials and private cache contents outside unauthorized exposure.
Do not mint unavailable credentials or weaken checks silently.
Run authorized work through controlled cold recovery when needed.
Record blocked private work honestly.
Require warm zeros only for complete authorized coverage.

**Basis/status.** Permission and private-fetch code is source verified.
Actual fork service scope and private-output exposure review remain pending.

### C09. Merge-queue and tag events where used

**Inputs.** Use configured merge-group events and actual tag product events.
Keep a nonempty dependency set for each applicable event.
Record unsupported event/product combinations explicitly.

**Mechanism.** Run L for generated modes and plan preservation.
Run H only through approved existing event mechanisms.

**Assertions.** Keep these consumers read-only.
Preserve selected checks and product profiles.
Resolve only an authorized cache scope.
Test distinguishable default-ref and current-ref payloads with the same key and cache version, plus longer primary-key prefix matches.
The restore action has no ref/cache-ID selector; filtering REST inventory does not force its selection.
Inspect every service-selectable expected-version entry across visible scopes before restoration, including longer prefix matches even with no restore-keys.
The pin extracts a differing matched key before returning it; post-restore checks alone cannot protect outer extraction.
Reject any returned matched key unequal to the requested candidate, and reject unauthorized or ambiguous candidates before download.
An inventory check does not fence a racing uncontrolled writer; retain the audited capability boundary.
Reject an ambiguous or unauthorized scope rather than trusting the matched key or a producer-written manifest alone.
When inventory is unavailable, report incomplete provenance and use the permitted cold path; never claim a verified default ID/ref.
Include an explicit caller-read/callee-write rejection and a reusable workflow hosted in another repository.
Do not assume PR, merge-group, branch, and tag refs share writes.
Require zeros when complete compatible coverage is readable.
Report legitimate cold recovery otherwise.

**Basis/status.** Current workflow declarations establish applicability.
A configured event without a selected historical run remains unmeasured.
No new release product is authorized.

### C10. Simultaneous runs request the same missing generation

**Inputs.** Give two or more bounded trusted requests the same missing coverage.
Keep each request's selected nonempty workload explicit.

**Mechanism.** Run L for queue transitions and rechecks.
Run H with the approved concurrency count and run budget.

**Assertions.** Use the common repository mutation group.
Use `queue: max` and `cancel-in-progress: false`.
Recheck coverage and inventory after queue entry.
Later writers reuse the first verified generation when available.
Do not repeat dependency preparation merely because the first reader missed.
Preserve one result per selected unit.
Count queued time, all transfers, and all runner durations.

**Basis/status.** Coordination semantics are source reviewed.
Concurrency is not an atomic byte reservation or guaranteed dispatch order.
Actual races and duplicate-work avoidance remain pending.

### C11. Cancellation during preparation, upload, or cleanup

**Inputs.** Use one usable predecessor and a nonempty replacement workload.
Inject each cancellation point separately.
Keep candidate and predecessor identities distinct.

**Mechanism.** Run L with deterministic interruption fixtures.
Use H cancellation only when the campaign explicitly authorizes it.

**Assertions.** Preserve the last usable predecessor.
Never mark partial preparation complete.
Do not infer publication from successful action setup.
Reconcile any completed remote entry before further admission.
Retain predecessor charges until confirmed deletion.
A cancelled cleanup must not invalidate the verified replacement.
Record incomplete compiler/origin observations as interrupted, not zero.

**Basis/status.** Recovery behavior is a design requirement.
Live interruption and eventual accounting remain pending.

### C12. Failed-job rerun after the producer previously succeeded

**Inputs.** Let group A succeed at attempt 1 and let group B's writer fail for a controlled reason.
Rerun failed jobs so B and Required execute at attempt 2 while GitHub retains A.
Also cover an applicable consumer whose successful producer is retained.
Keep the same nonempty workload.
Test both retained and unavailable cache conditions.

**Mechanism.** Run L for missing-needs and rerun semantics.
Run H with approved failed-job rerun authority.
Delete only an explicitly approved fixture entry when deletion is necessary.

**Assertions.** The rerun must not require a successful producer to run again.
Use readable coverage when available.
Recover cold when it is unavailable.
Execute all required rerun units and preserve their failures.
Record attempt-specific ledgers and cache transfers.
Accept A's authentic attempt-1 ledger only after authenticated job records establish that A was retained without rerunning.
Require B's attempt-2 ledger and reject an old B result substituted for its rerun.
Do not impose global current-run-attempt equality on a successful retained job or relabel old evidence as new execution.
Reject duplicate reader/writer ledgers, unauthorized cross-run receipts, and mismatched source or plan identity.

**Basis/status.** Required-result behavior is source inspectable.
Actual service rerun behavior remains pending.

### C13. Skipped producer and failed producer

**Inputs.** Test an intentionally skipped writer, an optional cache error in a running writer, and a hard writer failure/cancellation before all units finish.
Keep a nonempty required consumer workload.
Include both available and missing predecessor coverage.

**Mechanism.** Run L for each dependency-graph outcome.
Run H only with a bounded approved failure fixture.

**Assertions.** Outcome-aware Required logic must run.
A skipped writer cannot erase required checks.
A failed writer cannot manufacture completed coverage.
When the reader completed the units, its skipped writer is expected.
An optional cache failure in a running worker continues through permitted cold recovery and executes its units.
A hard failed/cancelled writer cannot make the already-finished reader execute retroactively.
Required must fail with explicit missing/failed units in that branch; an authorized rerun can recover.
Preserve source, compiler, transfer, and failure evidence.
Reject missing or duplicate unit ledgers.

**Basis/status.** Generated topology and Required handling are source tested.
Live outcomes remain pending.

### C14. Save permission denied while the action step succeeds

**Inputs.** Use a complete local candidate from nonempty dependency work.
Deny cache writing in a bounded fixture.
Use a distinct key absent before the test.

**Mechanism.** Run L with successful step status and absent remote entry.
Run H under explicit read-only cache mode with an approved tiny fixture.

**Assertions.** Treat step success as insufficient.
Require exact readback and matching inventory identity for publication.
Record repository, ref, key, version, ID, stored bytes, and the frozen payload digest.
Remove only the local transport copy before readback and compare the actual restored digest and manifest.
Classify absent publication without claiming an existing entry.
Keep the predecessor.
Preserve ordinary check success or failure independently.
Record candidate compiler work, origin work, and attempted transfer.

**Basis/status.** The pinned save action lacks a usable publication receipt.
The denial outcome must be observed live before platform qualification passes.

### C15. Eviction, expiry, deletion, corruption, and restore timeout

**Inputs.** Exercise all five faults.
Start with a nonempty covered workload and a known usable generation.
Distinguish missing, unavailable, and corrupt states.
Include usable predecessor A plus reproducibly invalid candidate B occupying the second generation slot.

**Mechanism.** Run all faults through L.
Use H only for approved owned-entry deletion or bounded restore faults.
Observe natural expiry or eviction when available.
Do not flood storage or change retention settings.

**Assertions.** Reject corrupt inner payloads before use.
Do not claim inner validation sandboxes the action's outer extraction.
Keep trusted-writer controls.
Run required checks with bounded cold recovery.
Never report a failed restore as a warm zero-work pass.
Record origin recovery, compiler work, transfer retries, and fault latency.
Verify that a missing/timeout readback retains B's charge and does not authorize treating B as corrupt.
For reproducible corruption only, use reviewed repair intent and the existing checkout-free cleanup authority to delete exact owned B, retaining A.
Recheck identity, ownership, current repair intent, and A's usability after queue entry; confirm B deletion before admitting B-r1.
If required evidence is unavailable, retain both charges and skip mutation.
Compare bounded lookup-only and full-restore `last_accessed_at` observations without assuming either keepalive or recency neutrality.

**Basis/status.** Failure modes are documented requirements.
Each live fault needs its own result.
Unobserved expiry or eviction remains pending.

### C16. Publication near the repository budget

**Inputs.** Use complete synthetic inventories around both byte ceilings.
Include a real nonempty candidate workload.
Test exact-fit, one-byte-over, unknown-size, and pending-write cases.
Include delayed cleanup, all-ref/version occupancy, two occupied generation slots, and the reviewed corrupt-candidate repair sequence.

**Mechanism.** Run L for all numerical admission boundaries.
Use H only for a small approved packing/readback calibration.
Do not fill the repository to provoke eviction.

**Assertions.** Apply the full admission inequality.
Count actual stored bytes and the qualified outer envelope.
Block uncertain or oversized publication.
Require the actual final stored size to remain inside the justified preflight envelope.
An observed maximum or fixed percentage is not a proof of the repack bound.
Keep required checks running and retain the predecessor.
Do not delete active coverage to manufacture space.
Do not credit planned deletion or admit a repair third generation before exact-ID deletion confirmation.
Report a capacity conflict when complete coverage cannot fit.

**Basis/status.** Ten-billion and eight-billion byte values are policy thresholds.
Actual inventory, packaging bounds, and fit remain pending.

### C17. Coverage growth under the same compatibility identity

**Inputs.** Add an actual recipe or dependency variant under unchanged compatibility.
Keep a nonempty unchanged prior dependency set.
Preserve both old and new required coverage.

**Mechanism.** Run L for requested/completed coverage and immutable-key handling.
Run H with an approved supported coverage expansion.

**Assertions.** Restore the compatible prior state.
Compile only legitimate missing closure work.
Require zero compiler work for unchanged covered dependencies.
Publish a new coverage generation after complete preparation.
Run frozen-archive replay before publication; repeated earlier command success is insufficient.
Do not overwrite the immutable old key.
Remove superseded coverage only after verified replacement.
Queue an older dependency plan behind a newer one and confirm it cannot retire the currently active generation.
Permit an application-only HEAD change when the pure current-intent check establishes unchanged active compatibility and coverage.
Skip publication/deletion when that current-intent check is unavailable or the coverage retired.
Require warm zeros for the enlarged generation.

**Basis/status.** Separate compatibility and coverage are design requirements.
Union completeness and larger stored size remain pending.

Measure accumulated raw/stored payload growth across repeated coverage/dependency changes.
Do not delete guessed fingerprints or introduce an unreported/full maintenance rebuild to compact the state.
If growth prevents admitted replacement, report an explicit capacity conflict instead of claiming the generation-count limit proves fit.

### C18. Named checks and native commands with private homes

**Inputs.** Select actual named checks, native build commands, and private assets.
Use their real CARGO_HOME, RUSTUP_HOME, tool homes, and environment.
Include a nonempty dependency workload in each relevant path.

**Mechanism.** Run L for home resolution and token boundaries.
Run H with existing approved private-fetch permissions only.

**Assertions.** Restore bytes into the exact homes child commands use.
Preserve native flags, SDK inputs, generated code, and source-bound helpers.
Keep credential mint/use/revoke and scrubbing boundaries.
Exclude credentials from payloads.
Require attributable compiler/native/origin ledgers.
Unobserved absolute native calls or private fetches block warm qualification.

**Basis/status.** Current manifests and private asset paths are source verified.
Native process closure and all private acquisition bytes remain pending.

### C19. Every actual test, Clippy, and documentation command family

**Inputs.** Enumerate every currently selected command family.
Include Nextest build/list, Nextest run, doctests, Clippy, and documentation where configured.
Keep exact features, targets, profiles, warning flags, and package scope.
Require nonempty dependency work for each compiled family.
For a documentation-zero claim, require a cold positive control with actual eligible dependency rustdoc compilation.

**Mechanism.** Run L for recipe selection and lane routing.
Run H on the exact current command set.

**Assertions.** Keep the three initial lanes.
Do not share conflicting writable state.
Restore complete target/build state for each lane.
Require one result per command and unchanged semantic inputs.
Measure rustc, clippy-driver, rustdoc, build scripts, and native work as applicable.
Require warm zeros only with complete family-specific observation.
The RUSTC_WRAPPER alone does not observe direct rustdoc execution.
Use the stable owned RUSTDOC adapter and existing command-execution boundary.
Distinguish rustdoc dependency compilation, merge finalization, probes, and doctest descendants.
Run the frozen-byte replay with an empty ephemeral MBX store; MBX's separate rustdoc cache cannot satisfy the warm proof.
Verify the published digest equals the pre-replay frozen digest, with replay evidence stored only as control/report metadata.
Mark unobserved descendant compiler work unknown.

**Basis/status.** The existing command inventory is source verified.
Cargo diagnostics alone cannot qualify these families.
Per-family reuse and observation remain pending.

### C20. Release helpers and source-free signing or publishing

**Inputs.** Use actual release helpers and actual native producer recipes.
Preserve preview/stable differences.
Keep a nonempty producer dependency set.
Use a source-changing helper case.

**Mechanism.** Run L for helper identity and authority separation.
Run H only for credential-free build qualification.
Signing or publication requires its own existing authorization.

**Assertions.** Rebuild a changed helper when its full identity changes.
Reuse unchanged eligible dependencies.
Do not execute cached Cargo state with signing, OIDC, or publication authority.
Remove source compilation from attestation/publication jobs.
Use fixed renderer-owned data-only Python/gh/OCI operations adapted from the existing `candidate.py` and `publish.py` algorithms.
Preserve their authenticated GitHub evidence, eligibility checks, and existing OCI product-upload behavior.
Do not execute candidate-controlled code or a repository script from the checkout in the authority job.
Do not require a new helper API, helper release, tool, action, protocol, or pin for this authority change.
Verify product eligibility with authenticated evidence.
Do not invent release products for CI-only repositories.

**Basis/status.** Existing product boundaries are source verified.
Authority-safe restructuring and product-specific warm evidence remain pending.

### C21. Migration with old and new namespaces

**Inputs.** Include current old-family entries and a new complete candidate.
Use each repository's actual active families.
Retain a nonempty dependency workload.

**Mechanism.** Run L with mixed inventories and old-key refusal.
Run H only after a reviewed generator-owned consumer migration.

**Assertions.** Charge old and new entries during overlap.
Do not import old target or MBX archives into trusted new state.
Do not prune unowned entries.
Verify the new generation before deleting explicitly owned superseded IDs.
Remove obsolete implementation and generated paths through their owners.
Keep normal required checks and all products unchanged.

**Basis/status.** Old namespace and generator ownership are source verified.
Actual overlap bytes and live cleanup remain pending.
Use one bounded migration task per consumer repository.

### C22. Pressure from other existing cache families

**Inputs.** Include actual sources, tools, Rust state, other active families, and image-cache entries only if actual inventory contains them.
Include all refs, versions, migration entries, and bounded foreign pending writes.
Keep a nonempty Rust dependency workload alongside the other families.

**Mechanism.** Run L with complete mixed-family inventories.
Run H with approved existing families and small bounded writes.
Do not introduce a new image cache or external backend for this test.

**Assertions.** Enforce the repository-wide ceiling.
Do not count only the Rust namespace.
Recheck inventory after queue entry.
Block publication when foreign exposure is unknown.
An existing or future direct writer without a justified pre-upload bound remains unqualified; do not invent an image-cache producer or backend.
Preserve required active coverage.
Report compiler seconds saved per stored byte only from measured data.
Record every family's transfers and its contribution to pressure.

**Basis/status.** Existing family owners are source verified.
Actual all-ref inventory and simultaneous pressure remain pending.

## 8. Executable future fixture contract

Implement one case descriptor per C01 through C22.
Use the existing serialized test-fixture conventions.
The descriptor is test data, not a new external runner protocol.

Each descriptor must declare:

```json
{
  "case_id": "C02",
  "source_status": "source_verified",
  "runtime_status": "pending_measurement",
  "mechanisms": ["local_fixture", "approved_hosted_run"],
  "input_recipe_ids": ["fixture-recipe"],
  "eligible_dependency_ids": ["fixture-dependency"],
  "expected_origin_object_ids": ["fixture-source"],
  "positive_control_required": true,
  "native_control_required": false,
  "expected_state_transition": ["restore", "validate", "complete", "execute", "report"],
  "required_assertions": [
    "exact_command_ledger",
    "zero_eligible_dependency_compilation",
    "zero_covered_origin_acquisition",
    "separate_cache_transfer",
    "complete_observation"
  ],
  "approval_record": null,
  "evidence_records": []
}
```

The example is a future shape.
It is not an executed case or an existing production schema.
Use real fixture identities when implementing it.

The local fixture validator must reject:

- Missing, duplicate, or unknown case IDs.
- Empty recipe or eligible dependency sets.
- A warm claim without a positive cold control.
- Native zero without native observation closure.
- Origin zero without acquisition observation closure.
- Required null measurements marked qualified.
- Action step success used as the publication receipt.
- A partial command ledger marked complete.
- A live mutation without the approved namespace and budget.
- A source-only or simulated result marked as live performance evidence.

Register the module in the existing orchestrator integration root.
Keep per-case fixtures bounded.
Split implementation files where repository size limits require it.
Assign one task as the registration-file writer.

Future exact fixture discovery command:

```bash
cargo nextest list --locked -p velnor-actions-orchestrator --test velnor_orchestrator --message-format json -E 'test(gc1_qualification::)'
```

Future exact fixture execution command:

```bash
cargo nextest run --locked -p velnor-actions-orchestrator --test velnor_orchestrator --no-tests fail -E 'test(gc1_qualification::)'
```

The executable function names below are the fixed expected set. Each is a real test in the existing registered integration binary, not just a descriptor or empty sentinel.

| Case | Required discovered test suffix | Required scenario |
|---|---|---|
| C01 | `gc1_qualification::c01` | Complete cold run and verified publication. |
| C02 | `gc1_qualification::c02` | Separate fresh-run warm restoration. |
| C03 | `gc1_qualification::c03` | Application-only change and original projection metadata. |
| C04 | `gc1_qualification::c04` | Changed dependency closure with unchanged dependencies. |
| C05 | `gc1_qualification::c05` | Feature/profile change without lockfile change. |
| C06 | `gc1_qualification::c06` | Host/target/compiler/native/SDK change. |
| C07 | `gc1_qualification::c07` | PR rerun, merge, preview, and stable sequence. |
| C08 | `gc1_qualification::c08` | Restricted fork and private-source audience. |
| C09 | `gc1_qualification::c09` | Merge/tag/reusable scope and exact/prefix ref shadows. |
| C10 | `gc1_qualification::c10` | Concurrent requests and queued recheck. |
| C11 | `gc1_qualification::c11` | Preparation/upload/cleanup cancellation. |
| C12 | `gc1_qualification::c12` | Retained successful jobs and mixed-attempt reruns. |
| C13 | `gc1_qualification::c13` | Skipped writer, optional cache error, hard job failure. |
| C14 | `gc1_qualification::c14` | Denied save with successful action conclusion. |
| C15 | `gc1_qualification::c15` | All five faults, recency observation, exact-ID corruption repair. |
| C16 | `gc1_qualification::c16` | Complete byte admission, disk, and two-slot repair boundaries. |
| C17 | `gc1_qualification::c17` | Coverage growth, immutable replacement, current-intent guard. |
| C18 | `gc1_qualification::c18` | Named/native commands, private homes, and verified tools. |
| C19 | `gc1_qualification::c19` | All command families and frozen replay with rustdoc observation. |
| C20 | `gc1_qualification::c20` | Real helpers and fixed data-only product authority. |
| C21 | `gc1_qualification::c21` | Charged migration overlap and authorized retirement. |
| C22 | `gc1_qualification::c22` | Complete repository pressure from actual families. |

Require exactly these 22 lifecycle tests in the filter, matching complete discovered names by the listed unique suffixes.
Register auxiliary harness/observer tests outside that filter under `gc1_aux`, with their own exact expected names and nonzero execution gate.
Compare discovered names with the checked-in expected name list.
A positive process exit with zero selected tests fails.
Missing, duplicate, unexpected, ignored, or skipped required case tests fail the qualification gate.
Put the discovery/count/set assertions into the existing harness's executable verification commands, not only its documentation.
Each named case exercises every stated subcase and validates nonempty assertions; a test that only loads a descriptor does not satisfy the contract.

These commands are future commands.
The module is absent at the audited head.
Do not run them now and call an empty selection successful.

## 9. Existing verification commands

Use the repository root.
Use the already installed pinned Rust and Nextest environment.
Record their versions before execution.
If a required installed tool is absent, record a blocked gate.
Do not install another tool to satisfy this plan.

The root Nextest gate is:

```bash
cargo nextest run --locked --workspace --no-tests fail
```

Use the full existing root verification gates before integration.
Add `--no-tests fail` to the existing Nextest command.
Keep doctest commands in their existing separate lane.

For a source-verified, currently registered example:

```bash
cargo nextest list --locked -p velnor-actions-contract --test velnor_contract --message-format json -- impl_remed_cache::cache_secret_env_never_enters_identity --exact
cargo nextest run --locked -p velnor-actions-contract --test velnor_contract --no-tests fail -- impl_remed_cache::cache_secret_env_never_enters_identity --exact
```

Require exactly one discovered test for that exact filter.
Its presence is source verified.
Its current execution is not claimed by this plan.

Run these existing Python tests with the existing installed Python:

```bash
python3 - <<'PY'
import unittest

groups = [
    ('scripts', 'test_owned_mbx_observation.py'),
    ('scripts', 'test_qualify_mbx_observation.py'),
    ('scripts', 'test_source_qualification_execution.py'),
    ('scripts/hosted_phase_measurement/tests', 'test_*.py'),
]
for start, pattern in groups:
    suite = unittest.TestLoader().discover(start, pattern=pattern)
    if suite.countTestCases() == 0:
        raise SystemExit(f'No tests discovered: {start}/{pattern}')
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)
PY
```

Require a nonzero test count from every command.
These tests validate existing owned evidence behavior.
They do not prove live native reuse or replacement-cache performance.

The current retained-evidence collector supports this exact interface:

```bash
python3 -m scripts.hosted_phase_measurement.measure_hosted_run \
  --repository "$QUAL_REPOSITORY" \
  --run-json "$QUAL_RUN_JSON" \
  --jobs-json "$QUAL_JOBS_JSON" \
  --logs-zip "$QUAL_LOGS_ZIP" \
  --workflow-json "$QUAL_WORKFLOW_JSON" \
  --workflow-file "$QUAL_WORKFLOW_FILE" \
  --out "$QUAL_OUTPUT_JSON"
```

Resolve these variables to retained, source-bound inputs before execution.
Use complete run-attempt job data.
Collect report artifacts only for their existing evidence role.
Never transfer dependency state through those artifacts.

## 10. Source basis and completion rule

The following pinned sources establish the existing harness and owned paths.
They do not establish the replacement's runtime results.

- [Velnor orchestrator test registration](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs).
- [Velnor Rust test registration](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-rust/tests/velnor_rust.rs).
- [Existing generated qualification workflow](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/.github/workflows/qualification.yml).
- [Existing MBX qualification assertions](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-orchestrator/tests/impl_schema2_mbx_qualification.rs).
- [Existing retained-run measurement interface](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/scripts/hosted_phase_measurement/measure_hosted_run.py).
- [Existing source execution admission](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/scripts/source_qualification_execution.py).
- [Existing MBX observation limits](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/scripts/owned_mbx_observation.py).
- [Root verification policy](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/docs/implemented/repo-verification.md).
- [Rust test policy](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/docs/proposed/rust-test-policy.md).

Use [EVIDENCE.md](EVIDENCE.md) for the actual nine-repository command and product inventory.
Keep earlier selected runs as historical evidence.
Do not use them as a controlled replacement baseline.

Completion requires a per-case ledger with all 22 results.
Every applicable repository product and command family must map to a qualified case.
A genuinely absent product is recorded as not applicable, with source evidence.
An inaccessible measurement remains pending.
An unobservable required guarantee remains unsatisfied.

Runtime evidence remains bound to its measured generator/source/workflow SHAs.
After obsolete-code removal or final regeneration, do not relabel earlier candidate evidence as final-candidate execution.
An independent review may carry an explicitly identified result forward only after proving that strictly unreachable removal leaves that case's generated workflow, recipe/identity inputs, archive format, observer, authority, and runtime paths equivalent.
Record that equivalence separately while preserving the original evidence SHA.
Any affected or uncertain case requires its bounded approved hosted rerun before final immutable-pin activation.
Apply this rule to Velnor's own final workflows as well as every consumer migration.

Implementation may continue while independent measurements are blocked.
Do not mark the full cache goal complete until required live evidence exists.
Do not declare universal zero misses.
Do not claim that a complete working set fits until inventory and publication measurements prove it.

