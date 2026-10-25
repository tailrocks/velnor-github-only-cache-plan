# Repository cache budget

Status: accounting policy selected; actual repository fits pending.

## 1. Units and limits

Keep GitHub's configured included allowance at 10 GB.
Use **10,000,000,000 bytes** as Velnor's conservative accounting ceiling, `Q`.
This decimal convention is an implementation policy. It does not assert GitHub's internal GB conversion.
Do not use the old `10 * 1024 * 1024 * 1024` policy constant.

Start with reserve `R = 2,000,000,000 bytes` and operating ceiling `O = Q - R`.
Thus the provisional operating ceiling is **8,000,000,000 bytes**.
Increase the reserve when measured uncertainty or uncontrolled activity requires it.
Do not increase `Q` or the configured GitHub allowance.
This provisional threshold is conservative policy, not evidence that any repository fits.

## 2. Non-overlapping accounting

| Symbol | Definition | Measurement |
|---|---|---|
| `I` | All currently listed repository cache bytes. | Sum unique cache IDs and `size_in_bytes` across every page/ref/version. |
| `P` | Known owned uploads or finalized entries not yet represented in `I`. | Admitted upper envelopes, without double counting listed IDs. |
| `F` | Bounded foreign in-flight exposure not represented in `I`. | Measured cooperating writer limits or an explicit conservative bound. |
| `B` | Upper envelope of this candidate's actual outer cache archive. | Qualified same-runtime packaging preflight plus repack allowance. |
| `R` | Reserve for measurement error, observation lag, and unmodeled variation. | At least two billion bytes; increase from measurements. |

Admit a save only when:

`I + P + F + B <= Q - R`

Inventory already includes old baselines, retained variants, PR entries, and migration namespaces.
Do not add those entries again as separate charges.
Do not subtract a proposed deletion before the API confirms it.
Do not count known pending bytes again inside the uncertainty reserve.

A steady repository must leave space for the largest next admitted replacement:

`steady_I + P + F + largest_replacement_B <= Q - R`

Also reserve space for predecessors waiting behind other jobs in the cleanup queue.
A writer lock does not make cleanup immediate.
If that lag cannot be bounded, publication qualification fails.

## 3. Archive measurement

Use one frozen inner `payload.tar.gz` per family/group.
Create it with the already-approved `tar 0.4.46` and `flate2 1.1.10` dependencies.
Record raw logical bytes, unique file bytes, inner archive bytes, and archive digest separately.
Capture authenticated original file and directory metadata, including timestamp precision, in the existing manifest/archive route.
Join all producer processes before freezing it.
Clear only owned target/build and ephemeral MBX directories; restore the frozen archive at identical paths, then replay exact recipes with Rust, RUSTDOC, and applicable native/origin observation.
Require zero unchanged eligible dependency compiler work and complete replay evidence bound to the frozen digest outside the payload.
Publish those unchanged frozen bytes; never replace them with a repack of replay-mutated state.

The pinned cache action creates another archive around that file.
Perform one preflight using its exact packaging arguments, fixed path, working directory, and existing runner tools.
Measure that preflight archive as `m`.
Delete the preflight copy before the official save.
Use `B = m + qualified_repack_allowance`.

The allowance must have a conservative documented basis for metadata, padding, and streaming compression behavior.
Paired observations support that basis. An observed maximum alone is not a guaranteed bound.
Do not invent a fixed one-percent allowance.
Do not apply a one-pass Zstandard bound to an unqualified streaming command.
Unknown tool identity or envelope blocks a save, not ordinary CI correctness.

After save, query the exact owned entry's stored bytes.
Perform actual exact readback into an empty transport path.
Compare the restored frozen archive digest and manifest.
Record the actual repository/ref/key/version/ID tuple; the action itself supplies no ref/ID selection or publication receipt.
An unauthorized or ambiguous ref shadow cannot establish trusted publication or baseline provenance.
The preflight must include every expected-version candidate the service could select, including longer prefix matches for the primary key with no restore-keys supplied.
The pin can extract a differing matched key before returning it; post-restore equality remains required but does not replace pre-extraction provenance control.
Inventory checks are not atomic fencing against uncontrolled writers.
Record any bound violation as a qualification failure before requesting predecessor cleanup.

## 4. Family ownership and retention

| Family | Owner | Steady retention | Replacement charge |
|---|---|---|---|
| Sources | Trusted default source preparation. | One complete generation per authorized source group. | Current plus candidate; include verified private assets where permitted. |
| Tools | Trusted default tool preparation on each existing host. | One complete tool union per host/ABI group. | Current plus candidate; no Plan/seed/crate copies. |
| Cargo state | Trusted default combined writer. | One complete generation per active workspace/host group. | Current plus candidate, with all target/build lanes and source projection. |
| Existing supported non-Rust families | Their current owners through the common policy. | One required complete generation per active compatibility group. | The same overlap and admission rules. |
| Foreign or unrelated entries | Their existing owners. | Count all entries; do not delete them. | Count bounded pending activity or block qualification. |
| Old Velnor namespace | Reviewed migration owner. | Retain until the replacement qualifies. | Count full old/new coexistence. |

Do not retain a historical predecessor after verified replacement and authorized cleanup.
An active platform, feature, native, target, or profile variant is required coverage, not disposable history.
Do not keep every historical tag or every retired compiler identity.
The plan records the current bounded active group list for each repository.
Keep at most two stored generations per active compatible family/group/version, including an unverified candidate awaiting resolution.
Enumerate the bounded approved physical version set in the current plan; additional inventory versions remain charged, not silently approved.

### Source replicas across approved runner layouts

Keep transport in stable owned `runner.temp` paths for initial migration.
Portable logical source data may occupy separate physical action-cache versions on different approved runner layouts or compression methods.
The pin hashes the literal action path and compression, so different expanded temp paths can create distinct versions even on Unix hosts.
It also converts matched source paths to paths relative to `GITHUB_WORKSPACE` before tar creation; extraction uses that workspace root.
A common absolute `/tmp/...` input therefore does not by itself guarantee common archive-member placement.
Do not introduce that cross-host path invariant for the initial migration.

Include source layout in the active compatibility/group identity and count every physical source copy, current generation, candidate, and delayed-cleanup overlap.
There is no assumed global deduplication between versions.
C02 tests fresh-run restore at each approved layout; C06 tests layout/compressor version changes and placement isolation.
Cross-host sharing is not an initial acceptance prerequisite. Keep state and tool compatibility host-specific.

### Growth inside a complete Cargo snapshot

The two-generation retention limit bounds archive generations, not the contents of one Cargo target/build tree.
Repeated dependency or recipe updates can leave obsolete outputs inside a complete inherited snapshot.
Measure both raw and stored growth across C04 dependency updates and C17 coverage changes, including successive updates rather than only the first replacement.
Use the resulting candidate bytes and overlap in admission; do not assume stable archive size because the number of keys is bounded.
Do not delete guessed Cargo fingerprints/outputs, hide a full rebuild as compaction, or schedule an automatic maintenance rebuild.
If complete payload growth exhausts permitted headroom, report the exact capacity conflict and retain required coverage under the existing failure policy.

If a candidate is reproducibly corrupt, cleanup can delete that exact owned candidate ID.
Retain the usable predecessor. Confirm deletion before admitting a reviewed repair generation.
The checkout-free cleanup job must reacquire the common queue and validate exact ownership/ref/version, reproducible invalidity, the retained predecessor, and currently approved repair intent.
Unavailable proof retains both charges and blocks the repair save; it does not authorize a third generation.
Do not classify a timeout or missing readback as proof of corruption.
Do not create a repair epoch for each run.

Normal predecessor retirement separately requires a verified replacement that remains active under the current accepted coverage plan.
If default HEAD changes, use the existing pure identity/planning path to recheck active coverage without executing tasks.
Application-only changes need not retire identical coverage. Stale or unavailable intent skips deletion.
Do not select the active generation by `created_at` alone or assume cleanup immediately follows its writer.

## 5. Current per-repository evidence

The observed-byte column sums distinct restored keys in the sampled runs.
It is not a live inventory and does not prove simultaneous residency.
The export column reports current local MBX output, not stored compressed occupancy.
All replacement-state sizes and complete fits remain pending.

| Repository | Observed distinct archive bytes | Current local rejected export | Initial required contexts | Full 10-GB fit |
|---|---:|---|---|---|
| jackin-project/jackin | 1,565,288,037 | 7.5 GiB | Linux CI; macOS named checks; actual Xcode native preview/stable variants. | Pending. |
| tailrocks/velnor-new | 1,788,371,982 | Root 4.0 GiB; runner 5.2 GiB | Root/nested CI; current Linux/macOS/cross release builds; actual helpers and clean qualification. | Pending. |
| ChainArgos/blockchain-explorer | 1,240,054,926 | 3.3 GiB | One Linux workspace; codegen/private assets/native inputs. | Pending. |
| ChainArgos/tron-grpc-server | 1,234,406,153 | 3.0 GiB | Two-package Linux workspace; protobuf/private SQL/native inputs. | Pending. |
| ChainArgos/eth-grpc-server | 1,234,711,274 | 3.1 GiB | Two-package Linux workspace; protobuf/private SQL/native inputs. | Pending. |
| ChainArgos/bitcoin-grpc-server | 1,256,630,728 | 953.8 MiB | Two-package Linux workspace; actual dev/debug profile. | Pending. |
| ChainArgos/tron-processor-rust | 1,237,576,104 | 3.1 GiB | Four-package Linux workspace; test-helpers/private/native variants. | Pending. |
| ChainArgos/eth-processor-rust | 1,237,412,710 | 3.3 GiB | Four-package Linux workspace; test-helpers/private/native variants. | Pending. |
| ChainArgos/bitcoin-processor-rust | 1,236,902,711 | 3.0 GiB | Four-package Linux workspace; private/native variants. | Pending. |

Velnor's observed tool subtotal is **1,714,034,217 bytes across eight keys**.
It is not one tool archive.
Each ChainArgos sample restores four distinct tool identities before consolidation.
Do not estimate new state size by adding these old raw exports to old compressed tool totals.

No active BuildKit GitHub-cache producer was found in the inspected current workflows.
Count image cache entries if inventory reveals them.
Do not invent an image-cache product or a Docker cache backend.
Current OCI image publication is a normal product output, not dependency storage.
Any existing or future direct producer that cannot expose a justified pre-upload bound remains unqualified.
Do not claim the one-file archive bound covers such a backend automatically.

## 6. Peak local disk and time

Measure free disk on each actual existing runner class.
Do not assume the advertised runner disk is all free.
Charge working source/tools, three initial Cargo lanes, separate build directories, staged projection, frozen inner archive, outer archive, and replay state.
Delete the preflight outer archive before action packaging.
Stop all Cargo/MBX/native sessions before clearing positively owned replay directories.
Keep current checkout, Git metadata, tool authority, and source authority intact.
Validate file/directory metadata and original nanosecond precision after extraction with the existing approved capabilities.
Preserve changed parent directories rather than resetting them to a cached subtree's timestamp.
Count any temporary staging needed for correct metadata restoration in peak disk.

Publication cost includes build, inner packing, preflight packing, final packing, upload, readback, verification, and cleanup.
Coverage replay adds real commands and may repeat tests. Count them.
Do not hide this cost in maintenance or another workflow.
For failed-job reruns, sum the actual attempted executions and transfers once each.
A successful job retained from an earlier attempt keeps its original cost; do not invent a new execution or hide the failed attempt's work.

## 7. Migration and capacity conflicts

First stop obsolete writers through reviewed generated configuration.
Inventory and classify old entries by exact owner, ref, version, and coverage.
Do not delete the only usable baseline merely to start migration.
Admit new candidates with old/new overlap and all unrelated occupancy charged.
Qualify actual restore and workloads before deleting superseded owned IDs.

If the complete model fails, record the exact deficient bytes and affected recipes.
First remove proven duplicate tool identities and already superseded owned entries.
Next qualify supported lane consolidation while preserving command semantics.
Keep genuinely conflicting variants separate.
Do not strip required state or compact it through unreported dependency rebuilding.
Any optimization/profile/product change needs a separate explicit policy review.
If no permitted change fits, report the requested guarantee as infeasible under the ceiling.

## 8. Separate costs

Normal test reports, provenance reports, logs, and actual release products can remain.
Record their storage, retention, transfer, and compute costs separately.
They do not extend the dependency-cache allowance.
Never put target directories, compiler archives, tool caches, or dependency sources into report artifacts.

## 9. Guarantee limit

GitHub provides no atomic repository-byte reservation, cache pin, or eviction protection.
The configured storage ceiling is an eviction policy, not a transaction covering old/new overlap.
Velnor can enforce conservative admission for cooperating owned writers.
Unknown writers, delayed observation, service behavior, and eviction remain explicit limits.
No repository is declared fitted until its complete model and runtime publication pass.
Live capacity commands come from the prior qualification-harness command manifest and require their recorded namespace/run/fault budget.
Do not run a near-limit fill experiment or an unapproved deletion to establish this model.
After final source changes, preserve original measurement SHAs and require case-specific reviewed equivalence or an affected-case rerun before carrying capacity evidence to the final candidate.
