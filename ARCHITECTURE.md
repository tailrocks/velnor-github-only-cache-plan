# Velnor GitHub-only cache replacement

Planning date: 2026-10-25. Status: selected design; runtime qualification pending.

This document replaces the earlier external-service proposal. It retains useful audit evidence only.
No implementation, workflow dispatch, cache mutation, setting change, or release occurred during planning.

## 1. Selected design

Use one internal Velnor cache policy. Use the existing pinned GitHub cache actions as its only persistent transport.
Keep three Rust cache families: verified dependency sources, verified tools, and complete Cargo build state.
Apply the same accounting and publication rules to existing non-Rust families.
Combine compatible package checks in one job. Preserve each exact command and each selected unit result.
Keep the existing build/test, Clippy, and documentation lanes initially. Serialize writers within each lane.
Allow existing bounded lane concurrency only when the lanes have independent writable directories.
Do not create an archive for each crate or compiler action.

Persist complete Cargo target directories and separate Cargo build directories, when configured.
Pair them with a verified workspace input projection. Preserve actual metadata on unchanged restored input files.
Authenticate the current checkout inventory before restoring source files.
Stage the archived projection in an owned directory.
Move matching restored files or unchanged subtrees into their original checkout locations.
Preserve their genuine archived metadata, including original timestamp seconds and nanoseconds.
Keep current changed and new files.
Discard cached-only paths. Check file type, mode, content, and link target.
Execute at the actual `GITHUB_WORKSPACE`. Keep its current `.git` untouched.
Restore authenticated original metadata; never invent, normalize, backdate, or touch timestamps to make Cargo accept an output.
Never cache the current workspace checkout's `.git`, authentication configuration, or credentials.
Sanitized Cargo Git databases/checkouts remain part of the separately verified source family.
Qualify Git status, directory watchers, broad build-script inputs, and deleted files.
Block qualification if a recipe cannot retain its Git or file-input semantics.

Keep the selected Cargo or MBX command route.
Install the owned compiler observer at a stable path as `RUSTC_WRAPPER`.
The inspected pinned MBX versions 1.26.0 and 1.27.0 support an existing wrapper through `MBX_PREVIOUS_RUSTC_WRAPPER`.
It then transparently delegates Rust compilation through that wrapper instead of using its object cache.
Preserve compiler argv, effective environment, query behavior, exit status, and workspace-wrapper nesting.
This supported path avoids changing consumer-owned Mise wrapper configuration.
Cargo freshness is the sole persistent compiled-state reuse mechanism.
Set supported `MBX_TARGET_VIEWS=0` before commands that contribute a snapshot.
Configure a stable owned `RUSTDOC` adapter too. A previous Rust compiler wrapper does not disable MBX's separate rustdoc adapter.
Observe documentation compilation, finalization, probes, doctests, and their compiler descendants.
Do not persist an MBX object store, managed target-view link, or MBX export alongside Cargo state.
Do not invent a dependency-only MBX export or modify its private object format.

Only trusted default-branch execution can publish the new namespace.
Set PR, merge-queue, tag, preview, and ordinary release consumers to explicit `cache-mode: read`.
Set signing and publication jobs to `cache-mode: none` unless an independently verified tool-only bootstrap requires read.
Never restore Cargo state into an authority job.

## 2. Why this design

Current sources and logs show oversized exports, missing producer dependencies, disposable homes, and repeated tool identities.
The seed uses workspace commands. Consumers use package commands with distinct feature and command contexts.
A source-cache hit does not supply compiled outputs. A green save step does not establish publication.

The pinned MBX group exporter has no dependency-only selector.
Its prediction receipt includes this run's completed predictions, not all inherited predictions.
Its Cargo-state attachment and restoration can warn and continue.
Complete Cargo snapshots avoid a new opaque-object union mechanism.
Their actual compressed size and complete fresh-run reuse still require measurement.

The workspace input projection addresses unchanged path dependencies and build-script file inputs.
It is justified duplicated source content, not another copy of the registry source archive.
Measure its separate raw and stored contribution. Do not assume it is free.

## 3. Five separate identities

| Concept | Meaning | Evidence |
|---|---|---|
| Compatibility | Effective inputs under which restored state may be reused. | Host, toolchain, native inputs, path layout, lane identity. |
| Requested coverage | Exact recipes requested by the current trusted plan. | Package, argv, features, target, profile, environment, dependency identities. |
| Completed coverage | Recipes that completed and produced their required state. | Bound unit results and a complete local payload manifest. |
| Published generation | One immutable archive observed through remote readback. | Key, ref, version, stored bytes, archive digest, readback result. |
| Scope and trust | Jobs allowed to read or produce that generation. | GitHub event/ref rules, explicit cache mode, audited writer policy. |

A key hit proves none of the other four concepts by itself.
Before publishing new state, prove that the exact frozen candidate survives restoration and supports every claimed recipe:

1. Join all Cargo, MBX, rustdoc, and native producer sessions.
2. Freeze the complete payload and manifest, including authenticated original metadata. Record the archive digest outside the archive itself.
3. Clear only positively owned target/build directories and the ephemeral MBX store. Keep the current checkout, `.git`, source authority, and tools intact.
4. Restore those same frozen bytes at identical paths. Reconcile current source inputs, restore authenticated original metadata, and verify the complete manifest before execution.
5. Start with a genuinely empty ephemeral MBX store at the supported `MBX_CACHE_DIR` location.
6. Replay the exact compiler-producing recipes with complete observation. Count the additional work and repeated tests. Require zero unchanged dependency compiler work and reject destructive cross-recipe state collisions.
7. Publish the unchanged frozen bytes. Do not silently repack the replay-mutated filesystem into a different candidate.

The manifest describes the candidate's contents. Separate writer evidence binds replay outcomes to the frozen digest, coverage, host, source, run, job, and actual attempt.
That proof is not an archive member or a self-referential archive digest.
Remote readback must verify the same frozen digest.
Do not infer final completeness from earlier command success or same-job MBX rustdoc hits.
Keep ordinary check results visible. Do not silently omit a conflicting recipe.

## 4. Layout and keys

Use namespace `velnor-gc1`. Do not add a branch, run number, timestamp, or repository commit to every key.

`velnor-gc1-{family}-{group}-{compatibility}-{coverage}-r{repair}`

Use SHA-256 canonical digests for `group`, `compatibility`, and `coverage`.
Use existing canonical JSON and digest code. Do not add a new dependency.
Set `repair` to zero normally. Change it only through a reviewed repair record for an unusable immutable entry.
Do not create repair epochs automatically on every miss.

| Family | Payload | Compatibility | Coverage | Writer |
|---|---|---|---|---|
| `sources` | Registry index/cache/src, Git database/checkouts, approved immutable private assets. | Source format, registry/source policy, authorized audience, stable layout. | Resolved immutable source identities and checksums. | Trusted default branch. |
| `tools` | Verified pinned tools, required components, reusable origin archives or verification receipts supported by current tooling. | Host/architecture/ABI, installation layout, relevant runtime version. | Exact tool versions, components, targets, trusted archive digests. | Trusted default branch on that host. |
| `state` | Complete Cargo target/build lanes and verified workspace input projection. | Workspace identity, host, effective compiler/native environment, path layout and lane scheme. | Exact recipes and dependency input identities. | Trusted default branch on that host. |
| Existing non-Rust families | Their currently supported payloads. | Existing effective compatibility, reviewed during migration. | Existing exact request, with common completeness rules. | Same common policy. |

Transport uses one frozen `payload.tar.gz` per family/group.
Create it with already-approved `tar` and `flate2` Rust dependencies.
Use the existing owned archive validation facilities for extraction.
The approved `tar` 0.4.46 crate can emit PAX metadata, but its ordinary metadata capture and unpack path do not preserve subsecond mtimes; its unpack path also normalizes a zero mtime and does not restore directory mtime on the ordinary directory branch.
Record original seconds and nanoseconds explicitly, and restore authenticated original file and directory times through approved Rust standard-library facilities after safe extraction.
Restore directory metadata after children, read back the exact result, and fail qualification if the host cannot represent it.
Use an already-approved no-follow facility for applicable link handling, or reject an unsupported case; never follow an archived link while applying metadata.
Apply archived source metadata only to matching restored objects. Changed current files and current `.git` retain their current metadata.
An unchanged child file does not authorize restoration of its changed parent directory's old metadata. Restore a source directory's archived metadata only when that directory's authenticated input subtree is unchanged; otherwise preserve current directory semantics and qualify the resulting freshness behavior.
This is restoration of real archived metadata, not a timestamp normalization scheme.
See the pinned [PAX writer](https://github.com/composefs/tar-rs/blob/0.4.46/src/pax.rs#L157), [metadata capture](https://github.com/composefs/tar-rs/blob/0.4.46/src/header.rs#L789-L803), [unpack timestamp path](https://github.com/composefs/tar-rs/blob/0.4.46/src/entry.rs#L484-L508), and Rust's [FileTimes](https://doc.rust-lang.org/std/fs/struct.FileTimes.html) / [File::set_times](https://doc.rust-lang.org/std/fs/struct.File.html#method.set_times).
The pinned cache action adds its own outer archive. Charge both packaging work and peak local disk use.
Do not equate inner bytes with GitHub stored bytes.

Use fixed generated action paths. Keep their order stable.
Example action transport path: `${{ runner.temp }}/velnor-gc1/transport/state/payload.tar.gz`.
Resolve the corresponding `RUNNER_TEMP` path in owned runtime commands; do not assume a shell variable expands inside an action's `path` input.
Execution root: the current actual `GITHUB_WORKSPACE`.
State root: `${RUNNER_TEMP}/velnor-gc1/state/{group}` outside the source checkout.
Keep source, tool, and Cargo homes in adjacent owned runner directories.
Keep transport and state outside the source checkout.
Do not modify consumer ignore files or Git metadata to hide cache directories.
Bind the actual absolute runner roots to compatibility.
Use existing declared repository paths only for inputs that require those paths.
The actual absolute root and path scheme form part of compatibility.
Do not include run-specific temporary directory names in cached build paths.
Keep this runner-temporary layout; do not assume it makes the action archive portable across hosts or checkout depths.
The pinned action's cache version incorporates literal paths and compression, and its archived member paths are relative to the actual workspace.
A logical union of portable source objects can therefore require separate physical source-cache versions for approved host/path/compression layouts.
Count every such replica in the repository allowance and qualify each actual restore path; the initial design assumes no cross-host restore portability.
Include the exact layout/version distinction in the compatible group identity, retaining at most two generations per such active group.
Each sources entry remains a complete source-family payload, separate from the state payload; do not hide source replicas inside state archives.

Cargo controls its internal unit fingerprints. Preserve complete designated directories.
Do not delete guessed Cargo or MBX files to reduce size.
Keep credentials, runtime tokens, independent logs, transport staging, and distribution directories outside the designated payload roots.
Reject a payload root that contains secrets. Do not filter guessed temporary or log names from a complete output tree.
Do not remove required generated inputs, native objects, fingerprints, proc macros, or build-script outputs.
Keep `.mbx-rustdoc-parts` when it is inside a designated output directory; it is required documentation output, not a second persistent MBX object store.

### Existing homes and tool hydration

Keep the current isolated HOME, credential lifecycle, and cleanup behavior of named/private checks.
Project the owned context into those homes without modifying non-generator-owned `mise.toml` files.
Place reusable source archives and verified tool prefixes at stable owned paths outside the checkout; private configuration remains private and disposable.
Hydrate through the actual acquisition seam in `crates/velnor-actions-orchestrator/src/check_tool_acquire.rs::acquire` and `fetch_extract` before their current unconditional download/build paths.
Retain independent archive checksum, installed-tree, and executable probes; a cache receipt alone does not validate a prefix.
Bind `crates/velnor-actions-mise/src/qualified_acquisition.rs` (`qualified_tool_home`, `qualified_source_command`, `qualified_link_command`, and `qualified_fetch_command`) and `check_execution.rs::compiler_prefix` to the same qualified context.
The pure tool catalog is not an acquisition bypass. Unchanged private-home materialization must not silently redownload or rebuild a covered tool.
Collect child compiler, native, and acquisition evidence before disposable homes are removed, including successful named checks whose child output is currently captured by `check_runtime.rs::run_check`.
For ordinary Mise and Rust tool verification, change the actual existing verifier bodies: `crates/velnor-actions-workflow-renderer/src/cache_steps_tools_installs_verify.sh` and `crates/velnor-actions-orchestrator/src/rust_toolchain_script.rs::toolchain_script`.
They currently acquire immutable verification inputs even when installs were restored; reuse independently reverified cached archives before their origin-fetch branches.
`cache_steps_tools_restore.rs` owns the generated Mise verifier composition. `toolchain_env_fetch.rs` only defines credential and fetch-redirect filters; it is not the acquisition implementation.

### Controller bootstrap prerequisite

Before live qualification or activation, obtain a real independently approved normal generator release containing the new cache operations through the existing release handoff.
Record its exact supported-host binary URL, source commit, and SHA-256 in the existing reviewed release descriptor / Velnor bootstrap-lock mechanism.
This is an explicit owner-approved release prerequisite, not an automatic release or an assumed capability of an old helper binary.
The current inspected Velnor source uses preseed source bootstrap and has no `generator.lock`; do not claim that the new controller pin already exists.
The image authority path in section 10 remains fixed data-only code and does not depend on a new image-helper API.

Extend `crates/velnor-actions-workflow-renderer/src/closure.rs::provision_acquire_step` and `steps.rs::acquire_velnor_step` with one fixed renderer-owned read-only bridge from `cache_bootstrap.py`.
Keep the existing `HelperProvenance::ReleaseAsset` URL, commit, digest, and staged-binary contract.
Use only already-approved hosted Python/system hash capabilities and the pinned cache restore action; no compiler or source-built archive guard is needed to stage the controller.
Before the controller exists, the bridge may inspect the tools-family payload as data and select only the exact bounded standalone controller member into an owned temporary file.
Reject duplicate, linked, special, escaping, malformed, or oversized candidate members; verify the selected bytes against the independently committed release digest before execution.
Do not trust a payload-provided digest as that independent authority. Apply the same pre-restore provenance/ref-shadow guard and outer-archive trust restrictions as ordinary discovery.
On a miss, use the existing bounded download of the exact release asset and independent SHA-256 verification.
The bridge performs no general source/state extraction, cache save, admission bypass, or dependency-artifact handoff.
Once the verified controller is staged, it owns general safe extraction, source reconciliation, coverage, observation, and common publication admission.
Render the ordering so covered bootstrap/tool inputs are hydrated before any setup or verifier that would otherwise fetch them again; qualify the actual pinned action behavior.

Keep Velnor's source candidate as application work: the independently pinned controller restores its execution context before the exact source-candidate compilation and output checks.
Do not use the current `build-owned-archive-guard.sh` source-build bootstrap to unlock warm cache extraction; that path creates a fresh bootstrap target and compiles the guard.
Count the initial normal-release build, initial controller download, first cache preparation, and source-candidate work in their appropriate cold/bootstrap lifecycle totals.
An initial cold bootstrap does not establish the warm guarantee. A later fresh-runner bootstrap must prove no unchanged controller/guard compilation and no covered immutable origin acquisition before the group can qualify.

## 5. Coverage rules

Derive recipes from the current selected task manifest and existing Cargo metadata machinery.
Retain package scope, argv, feature selection, target, profile, warning policy, and effective environment.
Keep Nextest's `ci` test profile distinct from Cargo's compilation profile.
Do not substitute `--workspace` for a set of package commands.

Hash immutable dependency identities and relevant workspace dependency inputs for coverage.
A lockfile change changes requested coverage. It does not invalidate all compatible restored compiler outputs.
Top-level application source alone does not create a new dependency generation.
A package used as another selected unit's dependency retains that dependency role.
Do not exclude unchanged workspace libraries merely to pass the performance target.
Use existing declared input rules for build scripts and external files.
Derive workspace/path dependency source membership from existing Cargo metadata and declared build/native inputs, then hash actual input content, type, mode, and link target.
Reconcile the complete allowlisted tracked workspace projection against the current authenticated checkout inventory before executing code; do not guess a smaller projection from Cargo's private fingerprint files.
Include actual declared Git-derived values when a dependency uses them. Preserve current `.git` semantics rather than supplying a stale cached repository or adding every application commit to every key.
Unknown input closure blocks that recipe's cache qualification. Normal required CI must still execute it.

Source-bound helper binaries require their complete source, dependency, profile, target, and tool identities.
Changed helper source legitimately requires new application output.
Do not reuse an old helper merely because the dependency generation matches.

Use one current generation for each active family/group.
Keep a predecessor only while publishing and verifying its replacement.
Keep zero historical predecessors after successful replacement, unless an approved active recipe still requires that generation.
Treat concurrently supported variants as active coverage, not disposable history.
Define active variants in the generated plan from existing products, target/profile combinations, and supported host environments.
Keep the initial three command families. Give conflicting feature/profile/native variants separate deterministic lanes within their group.
Charge every such lane. Do not retain every historical tag or compiler version.
Keep at most two stored generations per family/group, including replacement overlap.
A pending cleanup consumes the predecessor slot. Do not publish a third generation.
An older release outside retained complete coverage has an explicit cold boundary.
Retain a compatible old generation when publication fails.

### Exact candidate discovery

List authorized cache entries through the existing GitHub API client.
Filter by repository, allowed ref, family, group, compatibility, and expected cache version.
Before restore, inspect every service-selectable entry of the expected cache version across visible scopes: exact-key entries and longer keys matching the primary-key prefix, including current-ref candidates that can shadow a default-branch entry.
The action cannot select a cache by REST cache ID or force an allowed ref. Its matched-key output does not identify the selected ref or cache ID.
Omitting `restore-keys` does not disable the cache service's primary-key prefix fallback.
The pinned v2 action extracts the outer archive before returning its matched key, so a later equality check cannot prevent an unsafe extraction.
Decline ambiguous or unavailable provenance and recover cold; an apparently valid inner manifest alone does not authorize an entry from a different producer scope.
Only independently authenticated report evidence binding the exact bytes can resolve byte identity; it does not make extraction of an untrusted outer archive safe.
Try the exact requested key first.
Then try at most one retained compatible predecessor key.
Choose the remaining candidate by the current active coverage intent, then creation time only as a tie-breaker.
Use the pinned restore action with the selected full key and no additional restore keys, after the complete pre-extraction provenance/prefix preflight succeeds.
Require the returned matched key to equal the selected full key and validate the actual manifest after every restore. Reject a prefix-only result as the requested generation even when its extraction was independently safe.
Treat useful incomplete coverage as PARTIAL. Preserve its valid inputs for controlled preparation.
Do not cross a compatibility or trust boundary to find a fallback.
When inventory is unavailable, do not claim default provenance from the computed exact key alone.
An exact-key attempt is allowed only when authorized provenance and absence of an unsafe exact-key or primary-prefix shadow can be established independently; otherwise recover cold without extraction.
Report the inventory failure. Do not claim complete generation discovery during that service failure.
An unusable exact key requires a reviewed repair revision. Do not loop on the same corrupt entry.
If another family misses, retain an already usable immutable state generation.
Never compare its historical application bytes with unrelated new application output or attempt to overwrite its key.

## 6. Execution topology

Initial groups follow existing workspaces and required hosted execution environments.
ChainArgos CI uses one group per repository workspace.
Velnor retains separate root and nested-runner workspace groups.
Jackin retains its ordinary Linux workspace group and its actual native producer environment.
Keep distinct effective native/SDK/compiler variants separate within bounded groups.
Preserve actual preview and release profiles. Jackin preview and release currently use different LTO settings.
Do not create release groups for repositories without current release products.

A combined job runs each exact selected unit. It writes one result for each unit.
The three command lanes may share verified sources and tools. They never share conflicting writable target state.
The job exports one state archive for the workspace group, not one archive per lane or crate.

### Production recipe and output ownership

Build the active recipe union from both existing CI selection and actual supported production producers.
Ordinary CI recipes alone do not establish release or preview coverage.
Preserve native host, SDK, target, profile, LTO, feature, environment, and package distinctions; sequential command combination must not merge their feature semantics.
The current integration points include:

| Existing owner | Required integration |
|---|---|
| `crates/velnor-actions-orchestrator/src/product_release_pins.rs::mbx_build_argv` | Preserve the exact `build --release --locked --package velnor-actions-cli --bin velnor-actions` recipe and explicit target argument for Intel cross compilation. Retain the declared Mise/MBX command route. |
| `crates/velnor-actions-workflow-renderer/src/schema2_generator_release_assets.rs::build_steps` / `build_script` | Bind both build setup and executable lookup/copy to the owned context. Existing `target/release` and `target/<triple>/release` lookups must follow the effective output root. Setting `CARGO_TARGET_DIR` alone is insufficient. |
| `crates/velnor-actions-workflow-renderer/src/preseed.rs` | Bind `PRESEED_BUILD_OUTPUT`, checks, manifest inputs, and staging copies to the same output context. Preserve each source-bound helper's actual input identity. |
| `crates/velnor-actions-workflow-renderer/src/schema2_job_image_native.rs` | Bind the credential-free producer's helper output lookup, currently under `target/release`, to that context. Authority jobs do not build or consume a candidate executable. |
| `crates/velnor-actions-orchestrator/src/preview_producer.rs::execute_preview_task` and current native/stable producer paths | Preserve current prepared-check homes, source/ref/version/commit-count environment, resource limits, and actual preview/stable profile differences. Keep intentional clean-install qualification distinct and count it. |

Prepare only products and environments that currently exist. Source eligibility, signing, and publication remain separate from compiler preparation.

### Trusted default branch

1. Plan the exact work and required generations.
2. Restore and validate a candidate in a read-only combined job.
3. Run selected units there when coverage is complete.
4. Emit `needs_prepare` before consumer compilation when coverage is missing or partial.
5. Start the conditional writer after that reader completes.
6. Acquire the repository writer concurrency slot.
7. Recheck inventory, active coverage intent, and candidate availability.
8. Run the group's exact required recipes.
9. Publish only complete admitted state.
10. Run remote readback before requesting predecessor cleanup.

The writer is also the consumer for this branch. Do not rebuild the same checks in another fan-out.
If another writer completed the cache while this writer queued, restore the now-complete generation and still execute this run's selected units; another run's checks do not satisfy this run's ledger.
The warm path does not start a preparation runner or publish an unchanged generation.
The cold path can pay a second restore after the handoff. Report that cost.
Bootstrap writers and cleanup jobs use the same concurrency group.
Emit static per-group reader, writer, and conditional cleanup jobs.
Do not use `matrix` values in job-level `if` expressions.
Do not collect unit ledgers through colliding matrix outputs.
Use separate explicit cache capabilities for reader and writer reusable calls.
Apply concurrency only to the mutation-owning job. Avoid nested acquisition of the same group.
The writer revalidates the trusted plan. Reader outputs never become arbitrary commands.
Required uses outcome-aware `always()` logic and the existing report transport.
It requires exactly one complete unit ledger from the reader or writer.
A `needs_prepare` result is not successful completion of any unit.
If the selected writer hard-fails or is cancelled, the already completed reader cannot run retroactively. Required fails the missing or failed selected units.
Optional cache-operation failures inside a still-running job may continue through controlled cold execution; they do not turn a hard job failure into successful recovery.
For failed-job reruns, resolve each job's effective attempt through authenticated GitHub job records.
Accept an earlier successful ledger only when GitHub retained that exact job without rerunning it.
Require current results for every rerun job. Never relabel an old ledger as newly executed.
Keep the original source, plan, job ID, and actual attempt on every accepted result.
Use `queue: max` and `cancel-in-progress: false` for writers.
Do not place a writer inside a workflow-level cancellation policy that cancels necessary preparation.
Concurrency is coordination, not a distributed lock, storage reservation, or guaranteed dispatch order.
Recheck current desired coverage before publication and deletion.
If default HEAD moved, recompute its relevant identity with existing pure planning code.
Do not execute tasks while checking that identity.
Permit publication when the compatibility and coverage remain active.
Skip publication or deletion when intent is stale or cannot be verified.
An application-only commit does not make identical desired dependency coverage stale.

### PR, merge queue, tag, preview, and release build

Restore an authorized default baseline. Validate coverage and effective inputs.
Run each selected unit in the same combined execution context.
Fetch or compile missing inputs locally when required. Report controlled cold recovery.
Do not save from these jobs. Do not pass their outputs into a default-branch cache.
Preview and release workflows wait for their existing authenticated source/CI eligibility boundaries.
Cache availability never replaces those boundaries.

### Initial baseline and new trusted dependency coverage

Prepare every currently supported CI and production recipe on the trusted default branch.
Run production preparation only when that group's coverage is missing.
Use existing credential-free native producer commands. Do not sign or publish products during preparation.
Include preparation time, compiler work, transfers, and disk use in the lifecycle totals.
Where the exact native command also builds application output, count that output honestly.
Do not invent a dependency-only recipe unsupported by the current tools.

## 7. PR-to-main boundary

Application-only changes reuse the trusted baseline when their dependency inputs remain compatible.
New PR dependency work cannot become a default-branch cache through a broad restore prefix.
This design also disables PR-local publication to protect the shared byte budget.
Therefore new dependencies can rebuild on PR reruns until trusted default preparation exists.
After merge, one trusted preparation is the minimum required exception.
It can reuse unchanged dependencies from the old compatible baseline.
Preview and stable builds then reuse the appropriate prepared variants.
Do not execute unreviewed PR code under default-branch cache-write authority to avoid that exception.

## 8. State machine

`DISCOVER -> RESTORE -> VALIDATE -> COMPLETE | PARTIAL | MISSING | UNAVAILABLE | CORRUPT`

`COMPLETE -> EXECUTE_CHECKS -> REPORT`

`PARTIAL/MISSING -> READ_ONLY_COLD | NEEDS_PREPARE`

`UNAVAILABLE/CORRUPT -> DISCARD_UNUSABLE_EXTRACTION -> READ_ONLY_COLD | NEEDS_PREPARE`

Keep a valid previously restored family when another family fails.
Discard only the unusable extracted state. Retry each failed transfer at most once.
If access still fails, continue through the event's cold path and report the cause.

`NEEDS_PREPARE -> QUEUED -> RECHECK -> EXECUTE_RECIPES -> COMPLETE_LOCAL`

`COMPLETE_LOCAL -> FREEZE -> RESTORE_FROZEN -> REPLAY -> PROVEN -> ADMIT -> SAVE_UNCHANGED -> READBACK -> PUBLISHED -> REPORT -> CLEANUP`

`ADMIT -> CAPACITY_BLOCKED` when inventory, envelope, disk, or headroom is insufficient.
`SAVE_UNCHANGED -> DENIED | OVERSIZED | INTERRUPTED | SERVICE_FAILURE` when evidence supports the distinction.
`READBACK -> CORRUPT | UNVERIFIED` when exact remote bytes cannot be validated.
Every unsuccessful publication retains the last usable predecessor.
Optional ordinary cache failures preserve the normal check result path while the job can still execute it; a hard-failed or cancelled selected writer leaves Required failed.
Every qualification cache failure remains a failed qualification result.

Restore the exact saved transport key into an empty local transport path for readback.
Delete only the local transport copy before this restore.
Compare the restored archive digest and manifest with the frozen candidate.
Use inventory to record the exact ref, cache version, ID, and stored bytes.
Send the verified replacement tuple and predecessor IDs through existing report/control metadata.
Run deletion in a separate checkout-free cleanup job with Actions write permission.
The writer releases its concurrency slot before that job begins. Cleanup reacquires the same repository-wide group and revalidates its own mutation intent.
Bootstrap, publication, and deletion are separately queued mutation phases, not a single cross-job transaction or a retained retirement lock.
Recheck replacement presence, ownership, ref, version, and active coverage before deletion.
Charge predecessors until the API confirms deletion. Do not assume cleanup runs immediately.
The standalone save action has no usable publication output.
Do not treat its successful step conclusion as proof of storage.

If a good predecessor A and a reproducibly unusable remote replacement B occupy both allowed slots, retain A and stop ordinary publication.
A reviewed repair record may authorize the existing checkout-free cleanup job to delete exact owned B after rechecking current repair intent and evidence of its unusability.
An outage or missing readback alone does not prove corruption.
Confirm B's deletion before admitting B-r1 under a new mutation phase and a fresh capacity check. Do not create a third generation while both slots remain occupied.

Do not use scheduled timestamp generations as refresh.
A later normal trusted execution can restore and reuse the existing generation.
Do not assume lookup-only updates retention.
Eviction, expiry, deletion, corruption, and service failure can always require cold recovery.

## 9. Capacity policy

The configured repository allowance stays at 10 GB. Velnor uses a conservative ceiling of 10,000,000,000 bytes.
Use GitHub inventory `size_in_bytes` for final accounting.
Inventory every ref, namespace, cache version, and family. Preserve unrelated entries.
Include tools, sources, state, image namespaces if inventory shows them, old generations, PR entries, and migration overlap.
The inspected Velnor and ChainArgos workflows do not establish a direct BuildKit `gha` producer; do not invent an active image-cache family.
Report normal artifacts and release outputs separately. Do not use them as dependency storage.

Start with a provisional 8,000,000,000-byte operating ceiling.
Reserve at least 2,000,000,000 bytes for uncertainty and external pressure.
Increase the reserve when measured foreign writes, in-flight archives, or estimation error require it.
Do not raise the ten-billion-byte ceiling.
The provisional threshold is a conservative policy, not a measured fit.

Admission requires `inventory + pending_owned + candidate_upper_bound + foreign_inflight <= operating_ceiling`.
Inventory already includes old baselines and migration entries. Do not count them twice.
Measure the frozen inner archive and exact pinned-action outer packaging in preflight.
Require a qualified repack allowance for the installed tar/compressor behavior.
An unknown bound, unknown inventory, or unsupported runner blocks publication.
An existing non-Rust producer that cannot expose a justified pre-upload bound remains unqualified under the common admission policy.
Normal checks continue cold. Capacity qualification fails visibly.
Reconcile actual stored bytes after save before pruning.

Writers serialize across the repository. Uncooperative writers can still change usage outside this coordination.
No GitHub cache API provides an atomic repository-wide byte reservation or eviction pin.
Block qualification when uncontrolled in-flight exposure cannot be bounded.

Prune only reviewed, explicitly owned IDs. Prefer entries already superseded by verified current coverage.
Use measured saved compiler seconds per stored byte when two optional retained candidates compete.
Do not remove required active coverage to claim a fit.
Do not automatically delete the last usable baseline to make space for replacement.
Do not routinely rebuild unchanged dependencies just to compact an opaque target tree.

If the complete working set fails, report the exact capacity conflict.
First remove proven duplicate tool identities and obsolete owned generations.
Then test supported lane consolidation without changing command semantics.
Any profile or product change requires a separate explicit review and remains outside automatic migration.
If these permitted changes cannot fit, the requested full guarantee is infeasible under this ceiling.

## 10. Security and authority

Cache hashes prove integrity, not producer trust.
Audit all default-scope writers before accepting their namespace as trusted.
Set explicit cache modes at workflow and reusable-workflow call boundaries.
Set explicit least-privilege `GITHUB_TOKEN` permissions too.
Cache mode does not restrict REST deletion or other GitHub token authority.
Readers and compiling writers receive only contents read and Actions read where required.
Only checkout-free cleanup receives Actions write for approved cache deletion.
Keep release, OIDC, and repository-write credentials outside compiler jobs.
Do not execute cached compiler state with signing, publication, or broad repository credentials.
Keep private-fetch token mint, use, revoke, and environment scrubbing in their current boundaries.
Never store credentials or private data in a cache readable by unauthorized fork workflows.
Review derived compiler output for private data exposure too.
Repository/ref visibility cannot implement a new private-source authorization boundary.

The pinned action extracts its outer archive before Velnor can validate the inner payload.
Its `path` input does not sandbox archive members.
Thus trusted writer control remains necessary even with inner archive validation.
Reject traversal, external links, device files, and escaping paths during inner extraction and projection.
Never trust a PR manifest to grant writes, skip checks, or change Required expectations.

Remove source compilation from image attestation and publication.
Move source-derived evidence creation into the credential-free producer.
Render one fixed owned data-only validation/publication implementation, shared by image attestation and publication, following the current source-free SDK job pattern.
Use only the already-used Python standard-library runtime, the existing pinned source-free `gh` acquisition, and the current bounded HTTPS OCI publication operations.
Do not add a Velnor helper CLI API, independent helper release prerequisite, new executable tool, or new protocol.
The authority job has no application checkout, Cargo build, local application action/script, candidate-built executable, or candidate-supplied executable module.
Qualify the actual hosted `python3` runtime already used by the current job; no separately Mise-pinned Python version was established by this audit.

Factor the fixed code from the validated behavior in `images/job/ubuntu-26.04/candidate/publish.py` and its data validators.
Preserve repository identity, exact source/workflow/ref, current-main and CI eligibility, artifact/run/actual-attempt, attestation, OCI digest/size, registry-origin, upload, and readback checks.
The existing publisher uses `gh api`, `gh attestation verify`, and bounded OCI HTTPS `HEAD`, `POST`, `PUT`, and `GET` requests to `ghcr.io`; it does not require a newly introduced Docker/ORAS/Skopeo publication tool.
Preserve the allowlisted blob-download redirect behavior and omit registry authorization on redirected downloads.
Replace `_current_identity` Git reads, `_verify_source_inputs` checkout reads, `candidate.py` imports, and `.velnor/runner.lock` reads with fixed validation of independently authenticated GitHub source/blob/lock data at the exact source SHA.
Candidate-provided hashes alone do not authorize signing or publication.
Keep source-closure evidence generation and source-side validation in `crates/velnor-actions-orchestrator/src/image_maintenance/source.rs::check_job_source` and the credential-free candidate producer; reuse its existing evidence instead of inventing a schema or executing candidate code under authority.
Wire the fixed renderer into `schema2_job_image_candidate.rs` and `schema2_job_image_native.rs`, removing their authority-side checkout/source compilation/local publication script route.
Preserve existing source-free product attesters and publishers.

## 11. Measurements and acceptance

A qualified warm run has a readable, complete, compatible, authorized generation for a nonempty expected dependency workload.
Count actual eligible dependency compiler executions. Require zero.
Count origin downloads for covered immutable objects. Require zero.
Count cache-transfer bytes separately. Fresh runners still receive cached bytes.
Keep application compilation and intentional clean-install qualification separate and visible.

The owned observer records real Rust compiler executions with recipe and package identity.
It delegates supported compiler queries without classifying them as compilation.
The owned `RUSTDOC` adapter separately records documentation compilation, MBX document/finalize calls, probes, and doctest execution.
Doctest compilation can occur inside rustdoc or its descendants; `RUSTC_WRAPPER` events alone do not establish that boundary's coverage.
Qualify supported descendant observation and attribution, or mark that recipe's observation incomplete rather than claiming zero.
Do not invent an `MBX_RUSTDOC=0` option. Preserve the pinned adapter's supported command behavior, including its finalization and doctest fallback paths.
Use the empty ephemeral MBX store during frozen-candidate replay so same-job documentation cache hits cannot conceal missing persisted Cargo state.
Use stable approved CC/CXX adapters for native calls that honor those interfaces.
Record uncovered absolute native calls and unobserved build-script network access as unknown.
For historical MBX reports, sum `compiler.miss`, `compiler.unconsulted`, `compiler.bypass`, and `compiler.verification` invocations.
Do not count top-level hits, misses, bypasses, or Cargo diagnostics as physical compiler work.
MBX version-five reports alone cannot attribute every invocation to its package.
Current collectors do not observe all native processes or origin bytes.
Implement and qualify owned observation inside Velnor using existing dependencies.
Do not claim global observation from wrapper counters alone.
Unknown observation coverage is unknown, not zero.

Carry versioned owned child observations through the actual merge and report path (`merge.rs`, `merge_checks.rs`, `merge_request.rs`, `retrieve_reports.rs`, `task_report.rs`, and the rendered Required gate) into the existing final-report artifact. This artifact contains evidence only, never dependency-cache payloads.
The existing measurement command already accepts `--artifact-json`, `--artifact-id`, and `--final-artifact`; the last input is the actual ZIP. Keep that CLI unchanged.
Extend `measure_support.py` and `report_events.py` to verify the artifact's authenticated API identity, exact ZIP size/digest, strict unique allowed members, member digest bindings, and source/run/job/actual-attempt identities before admitting observations.
Then integrate them in `report_builder.py::build_report` and `report_counters.py::build_actual_counters`; merely emitting new Rust reports does not replace those collectors' current hard-null behavior.
Permit measured values only with complete bound evidence, retain null plus reason otherwise, and never promote loose extracted reports or legacy progress text into measured compiler/origin work.
Count every actual job, attempt, and process once, including bootstrap, helpers, preparation, replay, and failed attempts. Keep that lifecycle work separate from the effective retained-job ledger used by Required and from historical MBX log summaries. Compiler wall time is not native CPU time.

Measure complete pipeline wall time, runner time, setup, preparation, transfer, raw payload, stored bytes, and peak disk.
Set speed and regression thresholds from approved cold/warm baselines.
No speedup or ten-GB fit has yet been measured for this replacement.

## 12. Planning completion and remaining gates

Completed: current source audit, selected whole-pipeline evidence, pinned engine/action review, and architecture selection.
Pending: actual inventories/settings, controlled baselines, new archive measurements, native observation, runtime lifecycle qualification.
The connector rejects cache inventory endpoints with an allowlist HTTP 400.
This is not a repository permission denial or evidence of zero cache usage.
All nine repository sources are currently accessible.

The implementation plan must retain these pending gates. It must not mark them as completed work.
Bind hosted evidence to the actual qualified candidate SHA, generated workflow bytes, and effective job attempts.
Do not relabel earlier evidence after obsolete-code removal changes the final candidate.
Require an independently reviewed equivalence statement for strictly unreachable removal, or rerun affected bounded cases before final activation, including Velnor's own final generated paths.

Current Velnor source basis: [`e851b39e3bedc664f8bd6470c629e7bac36c561c`](https://github.com/tailrocks/velnor-new/tree/e851b39e3bedc664f8bd6470c629e7bac36c561c).
The source and interface findings above are planning inputs; they do not establish successful restoration, complete observation, or measured capacity on hosted runners.
