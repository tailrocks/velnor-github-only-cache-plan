# Compact task reference



This is a compact index of full executable cards in TASKS.md. TASKS.json supplies all inherited fields and commands.



## T01 — Freeze source and caller ownership

Requires: none. Worker: GPT-6-Luna low. Reviewer: medium.

Files: D/source-map.json; D/caller-map.md; D/output-map.json; D/regression-map.json; D/removal-map.json.

1. Read all applicable repository instructions.

2. Refresh the nine source revisions and generator headers.

3. Map every cache caller and explicit test root.

4. Enumerate generator-owned outputs for each consumer.

5. Assign existing regression files to their behavior-changing task.

6. Assign mechanical removals to one ordered task.

7. Record exact generator and repository gate commands.

Pass: The map contains every current caller, output owner, command family, and source revision.

Exclude: Do not edit implementation or generated outputs.

Block: Record access-dependent paths as unknown. Do not invent their contents.



## T02 — Record inventories and baseline gaps

Requires: T01. Worker: GPT-6-Luna low. Reviewer: medium.

Files: D/baseline.json; D/cache-inventory.json; D/run-budget.json.

1. Read complete cache inventories for each authorized repository.

2. Read storage and retention settings without changing them.

3. Import complete selected-run measurements.

4. List approved experiments needed for missing measurements.

Pass: Every field has a measured value or an explicit unknown state.

Exclude: Do not dispatch runs, delete caches, or infer stored bytes from raw exports.

Block: Block only live measurement gates when access fails. Core implementation can continue.



## T03 — Replace obsolete cache and grouping policies

Requires: T01. Worker: GPT-6-Luna low. Reviewer: medium.

Files: docs/hard-decisions.md; docs/proposed/cache-decisions.md; docs/proposed/cache-contract.md; docs/proposed/cache-families.md; docs/proposed/parallelism-and-selection-contract.md; docs/proposed/rust-quality-contract.md.

1. Replace one-crate-per-job and MBX-only storage rules.

2. Define group timeouts and unit-level Required results.

3. Adopt the fixed GitHub-only lifecycle and byte policy.

4. Retain credential and tool-integrity requirements.

Pass: Normative policies agree with ARCHITECTURE.md and contain no obsolete mandatory cache path.

Exclude: Do not weaken tests, release authority, or input completeness.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T04 — Define cache identity and coverage types

Requires: T03. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: C/workflow/cache_policy.rs; C/workflow/cache_identity.rs; C/workflow/mod.rs.

1. Define compatibility, requested coverage, and completed coverage separately.

2. Define immutable family, group, generation, and repair identities.

3. Reject run IDs and application commits as universal key inputs.

4. Add canonical serialization and invalid-input cases.

Pass: Canonical identity tests reject incompatible fields and preserve compatible dependency reuse.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T05 — Define execution context and outcome types

Requires: T04. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: C/workflow/cache_context.rs; C/workflow/report.rs; C/workflow/report_validate.rs; C/workflow/mod.rs.

1. Define source, tool, target, build, and observer paths.

2. Define hit, partial, cold, denied, corrupt, and unavailable outcomes.

3. Define exactly-one-branch unit ledger bindings.

4. Bind each retained job result to its authentic effective attempt.

5. Keep unknown compiler and network counters nullable.

Pass: Types cannot represent a cache hit as successful completion of an unexecuted unit.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T06 — Derive dependency coverage without application churn

Requires: T04. Worker: GPT-6-Luna high. Reviewer: medium.

Files: R/closure.rs; R/identity.rs; R/identity_closure.rs.

1. Reuse the existing resolved Cargo graph.

2. Separate dependency coverage from full task identity.

3. Include workspace dependencies and declared native inputs.

4. Keep application-only deltas outside dependency publication identity.

Pass: Application changes preserve dependency coverage; dependency, feature, and native changes update the correct identities.

Exclude: Do not build a new Cargo resolver or exempt workspace dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T07 — Enumerate actual production and helper recipes

Requires: T05, T06. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/cache_recipes.rs; O/product_release_pins.rs; O/preview_producer.rs.

1. Register the new module through crates/velnor-actions-orchestrator/src/product_release_pins.rs.

2. Read existing CI and production command builders.

3. Enumerate exact native, preview, stable, and helper recipes.

4. Retain their profiles, targets, features, and source inputs.

5. Expose their union through the pure recipe catalog.

Pass: Coverage includes actual supported production commands without adding products or changing command semantics.

Exclude: Do not derive release coverage solely from crate CI tasks or invent dependency-only commands.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T08 — Plan compatible groups and exact unit sets

Requires: T05, T06, T07. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/crate_jobs.rs; O/crate_jobs_build_jobs.rs; C/workflow/crate_job.rs.

1. Group units by workspace and effective hosted environment.

2. Retain exact package commands and semantic variants.

3. Define static reader and writer alternatives.

4. Derive grouped deadlines from measured command budgets.

Pass: The new plan selects the same units and commands with bounded groups and no seed race.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T09 — Bind deterministic owned execution homes

Requires: T05, T08. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/cache_execution_context.rs; O/check_prepare.rs; M/check_execution.rs.

1. Register the new module through crates/velnor-actions-orchestrator/src/check_prepare.rs.

2. Resolve stable approved source and tool homes.

3. Bind target and build paths for each lane.

4. Keep private HOME lifetime separate from shared state.

5. Prevent home teardown from deleting shared directories.

Pass: Child commands read the restored homes and preserve existing cwd, task bytes, and credential scrubbing.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T10 — Restore authenticated source objects and original metadata

Requires: T06, T09. Worker: GPT-6-Luna high. Reviewer: medium.

Files: O/cache_source_projection.rs; O/source_prep.rs; O/source_cache.rs.

1. Register the new module through crates/velnor-actions-orchestrator/src/source_prep.rs.

2. Authenticate current checkout files and declared inputs.

3. Validate staged paths and safe link targets.

4. Restore original seconds and nanoseconds during authenticated extraction.

5. Restore directory metadata after its children.

6. Move unchanged restored files or subtrees into place.

7. Keep changed files and current checkout Git metadata.

Pass: Path dependencies retain real archived metadata while changed source and Git semantics remain correct.

Exclude: Do not normalize timestamps or restore checkout Git metadata. Do not follow links during metadata restoration.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T11 — Hydrate one verified source family

Requires: T10. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: M/cache_sources.rs; M/cache_transport.rs; O/source_cache.rs.

1. Restore registry and Git state into the consumed Cargo home.

2. Verify covered immutable source objects locally.

3. Fetch only missing approved objects.

4. Record source origin bytes separately from cache transfers.

Pass: Warm immutable sources need no origin acquisition and cold missing sources remain fetchable.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T12 — Preserve private source authorization boundaries

Requires: T09, T10, T11. Worker: GPT-6-Luna high. Reviewer: medium.

Files: O/private_wiring.rs; O/private_fetch_session.rs; W/private_source_steps.rs.

1. Check cache-reader access before admitting private payloads.

2. Restore approved assets at their declared stable paths.

3. Retain token mint, fetch, revoke, and scrub ordering.

4. Reject cached credentials and unauthorized private output exposure.

Pass: Private inputs remain available only to authorized readers and no credential enters any payload.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T13 — Create one tool set for each host

Requires: T04, T09. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/tool_cache_pins.rs; W/cache_steps_tools_restore.rs; W/cache_p08_tool_payload.rs.

1. Union existing required pinned tools for each host.

2. Remove role-only Plan, seed, and crate tool identities.

3. Keep host, ABI, component, and native SDK distinctions.

4. Disable independent automatic saves outside common policy.

Pass: Compatible jobs request one host tool set without losing any existing approved component.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T14 — Reuse verified immutable tool acquisition

Requires: T13. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: W/cache_steps_tools_installs_verify.sh; O/rust_toolchain_script.rs; W/cache_steps_tools_restore.rs.

1. Reuse supported verified local tool archives or receipts.

2. Retain independent trusted checksums and version probes.

3. Fetch only absent or invalid approved components.

4. Measure origin and verification work separately.

Pass: Warm verification does not download an unchanged covered origin archive.

Exclude: Do not trust candidate-supplied checksums or add a new installer.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T15 — Hydrate qualified tools inside private checks

Requires: T09, T12, T14. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/check_tool_acquire.rs; O/check_tool_layout.rs; M/qualified_acquisition.rs.

1. Restore qualified installed prefixes at deterministic owned paths.

2. Reuse verified archives without repeating origin acquisition.

3. Preserve complete tool proofs and source-build identities.

4. Keep private-home teardown away from shared prefixes.

Pass: Warm private checks reuse verified tools and stable sysroots without downloading or rebuilding them.

Exclude: Do not change consumer Mise files or trust an unverified installed prefix.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T16 — Render the shared tool and cache homes

Requires: T14, T15. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: W/toolchain_env_homes.rs; W/toolchain_env.rs; W/cache_p08_runtime_prelude.rs.

1. Emit deterministic owned runner paths outside the source checkout.

2. Keep the actual checkout as the execution directory.

3. Pass source, tool, build, and observer paths through one context.

4. Remove conflicting disposable-home assignments from generated wrappers.

Pass: Generated wrappers consume the same verified context without changing Git status.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T17 — Implement transparent Rust compiler observation

Requires: T05, T09, T11. Worker: GPT-6-Luna high. Reviewer: medium.

Files: M/compiler_observer.rs; M/command.rs; M/lib.rs.

1. Record real rustc and rustdoc start and completion events.

2. Bind each event to its recipe and package.

3. Distinguish documentation compilation, finalization, probes, and doctest descendants.

4. Preserve arguments, wrappers, signals, and exit status.

5. Support existing MBX previous-wrapper and RUSTDOC delegation.

Pass: Controlled fixtures distinguish application and dependency work without changing compiler behavior.

Exclude: Do not implement a compiler cache or modify MBX.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T18 — Observe supported native compiler boundaries

Requires: T17. Worker: GPT-6-Luna high. Reviewer: medium.

Files: M/native_compiler_observer.rs; M/compiler_observer.rs; M/lib.rs.

1. Wrap approved CC and CXX executables at stable paths.

2. Preserve native flags and executable selection.

3. Classify unobserved absolute compiler calls as unknown.

4. Test nested native compiler failures and cancellations.

Pass: Observed native work is counted accurately and unsupported observation cannot pass as zero.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T19 — Expose child compiler and acquisition evidence

Requires: T09, T11, T15, T17, T18. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/compiler_observation.rs; O/check_runtime.rs; O/check_prepare.rs.

1. Register the new module through crates/velnor-actions-orchestrator/src/check_runtime.rs.

2. Create recipe-bound observation reports before execution.

3. Collect reports after successful and failed children.

4. Keep origin, cache-transfer, and compiler counters separate.

5. Retain reports before private-home cleanup.

Pass: Successful named checks no longer hide measured child work or missing observation.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T20 — Pack complete state and safe manifests

Requires: T05, T10, T19. Worker: GPT-6-Luna high. Reviewer: medium.

Files: O/cache_snapshot.rs; O/cache_archive.rs; O/lib.rs.

1. Register the new module through crates/velnor-actions-orchestrator/src/lib.rs.

2. Pack complete target and separate build directories.

3. Include the authenticated workspace input projection.

4. Record original seconds, nanoseconds, modes, and safe link identities.

5. Use existing tar, flate2, and owned archive validation.

6. Keep required rustdoc parts and generated native state.

7. Exclude designated disposable roots outside complete output trees.

Pass: Round trips preserve required state and reject unsafe or incomplete payloads.

Exclude: Do not filter opaque Cargo state or required rustdoc parts. Do not persist the separate MBX object store.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T21 — Measure and qualify the outer archive envelope

Requires: T20. Worker: GPT-6-Luna high. Reviewer: medium.

Files: O/cache_archive_envelope.rs; O/cache_archive.rs; O/cache_snapshot.rs.

1. Register the new module through crates/velnor-actions-orchestrator/src/cache_archive.rs.

2. Freeze one inner payload and record its exact bytes.

3. Implement preflight packaging through the existing pinned runtime tools.

4. Represent a measured envelope and an unknown envelope separately.

5. Test measured bounds with deterministic local fixtures.

6. Require hosted measurements before publication qualification.

Pass: Local implementation passes fixtures; publication requires a separately qualified runtime envelope.

Exclude: Do not change unrelated behavior or dependencies.

Block: An unknown hosted envelope blocks publication qualification. It does not block unrelated implementation or ordinary CI.



## T22 — Implement repository-wide byte admission

Requires: T04, T20, T21. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/cache_inventory.rs; O/cache_admission.rs; O/lib.rs.

1. Register the new module through crates/velnor-actions-orchestrator/src/lib.rs.

2. Paginate every repository cache ref and version.

3. Use the fixed ten-billion-byte accounting ceiling.

4. Charge overlap, pending saves, other families, and reserved uncertainty.

5. Reject unknown inventory and insufficient publication headroom.

6. Charge corrupt replacements until exact deletion is confirmed.

Pass: Admission preserves required coverage and cannot credit unconfirmed deletion.

Exclude: Do not raise settings, buy capacity, or delete unrelated entries.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T23 — Bind all cache families to the common contract

Requires: T04, T05, T22. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: C/workflow/cache_family.rs; C/workflow/cache_family_steps.rs; O/stack_family_cache.rs.

1. Replace persisted MBX with the complete-state family.

2. Use one decimal byte constant and common admission outcome.

3. Retain supported source, tool, and non-Rust payload distinctions.

4. Inventory image namespaces only when present.

5. Remove independent family quota constants.

Pass: All family callers use the new policy types and one accounting ceiling.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T24 — Select exact generations and validate active intent

Requires: T06, T22. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/cache_discovery.rs; O/cache_keys.rs; O/cache_intent.rs.

1. Register the new module through crates/velnor-actions-orchestrator/src/cache_keys.rs.

2. Try the exact authorized requested key first.

3. Check every service-selectable exact or primary-prefix entry for scope shadow.

4. Reject ambiguous trusted provenance before action extraction.

5. Select at most one compatible retained predecessor.

6. Require returned matched-key equality after restoration.

7. Validate completed coverage after restore.

8. Recheck current desired coverage when default HEAD changes.

Pass: Discovery never crosses compatibility or trust boundaries and application-only HEAD changes do not retire valid coverage.

Exclude: Do not infer current intent from creation time alone.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T25 — Validate final coverage before publication

Requires: T08, T19, T20, T24. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/cache_coverage_replay.rs; O/crate_jobs_obligations.rs; O/compiler_observation.rs.

1. Register the new module through crates/velnor-actions-orchestrator/src/crate_jobs_obligations.rs.

2. Join all producer processes before snapshot creation.

3. Freeze the complete candidate archive and its digest.

4. Clear only owned target, build, and ephemeral MBX directories.

5. Restore the same archive at identical paths.

6. Replay exact recipes with an empty MBX store.

7. Require zero unchanged dependency compiler executions during replay.

8. Bind the separate replay proof to the frozen digest.

Pass: The manifest and separate digest-bound replay proof establish final coverage beyond command history.

Exclude: Do not publish replay-mutated state, invent dependency-only commands, or hide repeated tests.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T26 — Publish immutable generations and verify remote bytes

Requires: T21, T22, T24, T25. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/cache_publication.rs; O/cache_recovery.rs; O/lib.rs.

1. Register the new module through crates/velnor-actions-orchestrator/src/lib.rs.

2. Save only missing complete admitted family generations.

3. Publish the exact frozen bytes that passed replay.

4. Retain already usable immutable families unchanged.

5. Restore the exact saved transport into an empty local path.

6. Report denied, oversized, interrupted, corrupt, and verified outcomes separately.

Pass: Publication advances only after inventory reconciliation and actual digest-checked readback.

Exclude: Do not overwrite immutable keys or delete predecessors in compiler jobs.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T27 — Delete only verified superseded owned entries

Requires: T26. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/cache_cleanup_policy.rs; O/cache_cleanup_emit.rs; O/cache_prune_emit.rs.

1. Register the new module through crates/velnor-actions-orchestrator/src/cache_cleanup_emit.rs.

2. Validate replacement tuples and proposed owned cache IDs.

3. Recheck current intent and replacement presence after queue entry.

4. Delete only superseded entries within reviewed ownership.

5. Permit reviewed exact-ID removal of a reproducibly unusable replacement.

6. Retain the usable predecessor during that repair.

7. Confirm deletion before admitting a repair generation.

8. Treat missing readback as unverified, not proof of corruption.

Pass: Cleanup preserves active coverage, foreign entries, and the last usable generation.

Exclude: Do not delete by an unbounded prefix or treat cleanup as an atomic transaction.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T28 — Expose existing-binary cache and observer operations

Requires: T17, T26, T27. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: L/dispatch/cache.rs; L/dispatch/operation.rs; L/dispatch.rs.

1. Register the new module through crates/velnor-actions-cli/src/dispatch.rs.

2. Add typed private cache operation dispatch.

3. Bind exact request files to authorized context.

4. Delegate algorithms to their existing owning crates.

5. Reject malformed operations and arbitrary command injection.

Pass: The real CLI reaches each cache lifecycle operation through a validated request.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T29 — Bind compiler adapter entry and environment

Requires: T17, T18, T28. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: L/main.rs; L/dispatch/compiler.rs; W/task_wrapper_declared.rs.

1. Register the new module through crates/velnor-actions-cli/src/main.rs.

2. Expose approved rustc, rustdoc, CC, and CXX observer entries through the existing binary.

3. Resolve the real compiler from the validated context.

4. Set stable wrapper paths in generated task environments.

5. Preserve Clippy and preexisting wrapper nesting.

Pass: Real generated commands invoke the observer without a new external tool or driver override.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T30 — Render thin source tool and state transport

Requires: T16, T20, T23, T28. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: W/cache_steps.rs; W/cache_steps_mbx_bundle.rs; W/cache_steps_mbx_gate.rs.

1. Replace MBX bundle steps with common snapshot operations.

2. Use fixed literal cache paths and exact selected keys.

3. Do not treat inventory filtering as action ref selection.

4. Emit pinned restore and save actions only.

5. Pass policy decisions through typed outputs.

Pass: Rendered YAML delegates identity, coverage, and admission to Velnor code.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T31 — Render event permissions and writer queues

Requires: T08, T27, T30. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: C/workflow/ir.rs; O/workflow_policy.rs; W/dispatch_cache_boundary.rs.

1. Set explicit read modes for untrusted and release consumers.

2. Grant cache writes only to trusted default writers.

3. Give Actions write only to checkout-free cleanup jobs.

4. Render queue:max without nested locks or cancellation of required preparation.

Pass: Generated event paths enforce cache and GitHub token capabilities independently.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T32 — Integrate static reader writer and cleanup jobs

Requires: T08, T24, T27, T31. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/crate_jobs.rs; O/crate_jobs_build_jobs.rs; O/crate_jobs_stage.rs.

1. Emit static per-group reader and conditional writer jobs.

2. Decide the execution branch before consumer compilation.

3. Recheck state after the writer receives its queue slot.

4. Keep optional cache failures recoverable inside a running job.

5. Report hard writer failure without inventing reader recovery.

6. Count all branches against platform limits.

Pass: Warm groups run once without preparation; cold trusted groups execute once in the writer.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T33 — Integrate exact commands into isolated group lanes

Requires: T09, T25, T29, T32. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/crate_jobs_steps.rs; O/crate_jobs_obligations.rs; R/tasks.rs.

1. Keep the existing build/test, Clippy, and documentation lanes.

2. Serialize exact package commands within each writable lane.

3. Preserve every feature, profile, target, and warning flag.

4. Continue independent selected checks after a unit failure.

Pass: Each selected unit retains its command semantics and produces its own result.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T34 — Integrate unit-level Required validation

Requires: T05, T33. Worker: GPT-6-Luna high. Reviewer: medium.

Files: O/required_dispositions.rs; O/required_evidence.rs; W/required_gate.rs.

1. Bind reports to source, plan, job, run, and effective attempt.

2. Authenticate retained successful jobs from earlier attempts.

3. Require new ledgers for jobs that GitHub reruns.

4. Require exactly one reader or writer ledger.

5. Reject missing, duplicate, skipped, failed, and unplanned units.

6. Fail Required after hard writer failure leaves missing units.

7. Use outcome-aware aggregation when writer jobs skip.

Pass: Cache outcomes cannot hide a missing check or make Required skip.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T35 — Bind grouped ledgers through the actual final merge

Requires: T19, T34. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/merge.rs; O/merge_checks.rs; O/merge_request.rs.

1. Extend the actual merge request with typed group ledgers.

2. Validate each effective job against authenticated execution records.

3. Preserve original run, job, and attempt identities.

4. Join selected-unit results without rewriting old report identities.

5. Carry validated observation records into the final report payload.

Pass: The real merge entrypoint preserves every selected result and exposes source-bound observation evidence.

Exclude: Do not weaken exact-set Required checks or accept an older result without retained-job proof.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T36 — Carry observation evidence through existing report artifacts

Requires: T34, T35. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/retrieve_reports.rs; O/task_report.rs; W/required_gate.rs.

1. Collect typed observations with each normal unit report.

2. Retain exact artifact and member digest bindings.

3. Include validated observation members in the existing final report artifact.

4. Preserve actual job attempts and producer source identity.

5. Keep dependency payloads out of every report artifact.

Pass: The existing final artifact transports complete bound observations without carrying any cache payload.

Exclude: Do not treat loose extracted files or producer claims as authenticated artifact evidence.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T37 — Validate owned measurement evidence and effective attempts

Requires: T05, T36. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: scripts/hosted_phase_measurement/measure_support.py; scripts/hosted_phase_measurement/report_events.py; scripts/hosted_phase_measurement/tests/test_gc1_observation.py.

1. Validate owned reports through the existing final-artifact ZIP inputs.

2. Verify its API-bound size and digest before reading members.

3. Bind each member to source, run, job, and actual attempt.

4. Permit measured counters only with complete bound observation.

5. Keep unknown counters and unverified loose reports explicitly unknown.

Pass: Verified measurements are accepted; unbound zeros and forged effective attempts are rejected.

Exclude: Do not change the collector CLI or infer CPU time from compiler wall time.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T38 — Integrate complete lifecycle counters into the existing collector

Requires: T37. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: scripts/hosted_phase_measurement/report_counters.py; scripts/hosted_phase_measurement/report_builder.py; scripts/hosted_phase_measurement/tests/test_gc1_observation.py.

1. Consume the verified owned observations in build_report.

2. Count each real job, attempt, and process once.

3. Include bootstrap, helpers, preparation, replay, and failed attempts.

4. Separate effective Required results from total executed lifecycle work.

5. Keep origin bytes, cache bytes, and historical MBX summaries separate.

Pass: The existing collector reports all actual work without converting missing observations into zero.

Exclude: Do not double-count retained jobs or promote legacy Cargo progress lines into compiler counts.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T39 — Integrate named checks with restored context

Requires: T09, T15, T19, T34, T36. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/check_prepare.rs; M/check_execution.rs; O/check_runtime.rs.

1. Pass the typed group context into prepare_check.

2. Project approved restored homes into QualifiedCheck.

3. Preserve declared task bytes, cwd, and private HOME isolation.

4. Collect child reports before cleanup.

Pass: Named checks consume verified cached state and still execute their declared tasks.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T40 — Integrate preview native producers

Requires: T07, T30, T39. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/preview_producer.rs; O/preview_production_execution.rs; O/native_mise_tasks.rs.

1. Pass the same context through execute_preview_task.

2. Keep authenticated source and native tool identities.

3. Restore the correct production variant before execution.

4. Report cache and origin work from all native children.

Pass: Preview uses the shared lifecycle without changing products, LTO, targets, or source admission.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T41 — Integrate stable and native build callers

Requires: T40. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/native_check_runtime/execute.rs; O/native_check_runtime/install.rs; W/native_check_execution.rs.

1. Use the same verified context for compiler-producing native commands.

2. Retain existing host, SDK, linker, and release profiles.

3. Separate source-free consumption from compilation.

4. Preserve intentional clean-install qualification.

Pass: Stable and native paths report real reuse while retaining every current release requirement.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T42 — Bind product release build groups

Requires: T31, T41. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: W/schema2_generator_release_jobs.rs; W/schema2_generator_release_workflow_steps.rs; W/schema2_generator_release_assets.rs.

1. Attach the shared context to actual release build jobs.

2. Bind compiler output copies to the selected target paths.

3. Keep exact release and target command arguments.

4. Prepare supported production variants on trusted default coverage growth.

5. Keep signers and publishers free of Cargo-state restoration.

6. Retain product eligibility and clean qualification jobs.

Pass: Current products use the shared cache policy without adding products to CI-only repositories.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T43 — Restore the pinned controller before cache operations

Requires: T14, T30, T42. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: W/closure.rs; W/steps.rs; W/cache_bootstrap.py.

1. Include one fixed read-only bridge in the existing acquisition renderer.

2. Preserve HelperProvenance::ReleaseAsset and its independent digest contract.

3. Use the independently approved normal generator release descriptor.

4. Apply the same exact-entry and primary-prefix provenance checks.

5. Select only the expected standalone binary from restored tools.

6. Reject links, duplicate members, oversized data, and digest mismatch.

7. Verify its independent digest before execution.

8. Use existing approved acquisition on a cold miss.

9. Permit no save before the verified controller applies common admission.

Pass: Acquire Velnor avoids a warm origin download and reaches verified cache operations without source compilation.

Exclude: Do not execute cached unverified code or compile archive guard to unlock restoration.

Block: Block warm activation until a real approved controller release supports the cache operations. Count initial bootstrap work explicitly.



## T44 — Integrate Plan and source-bound helper reuse

Requires: T14, T29, T30, T43. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/workflow_jobs_cache.rs; W/preseed.rs; W/preseed_closure.rs.

1. Run the verified controller before building the current source candidate.

2. Restore verified pinned tools and state before helper execution.

3. Key source-bound helpers by their actual build inputs.

4. Bind PRESEED_BUILD_OUTPUT and staging copies to the context.

5. Keep changed source-candidate compilation classified as application work.

6. Remove repeated helper compilation from compatible ordinary paths.

Pass: Bootstrap has no circular cache dependency and unchanged covered helpers do not rebuild.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T45 — Factor fixed image record and archive validation

Requires: T05, T44. Worker: GPT-6-Luna high. Reviewer: medium.

Files: W/job_image_authority_record.py; W/job_image_authority_oci.py; W/job_image_authority_tar.py.

1. Port existing candidate.py data validation algorithms into fixed renderer inputs.

2. Keep strict record, OCI descriptor, and safe tar checks.

3. Use only the existing Python standard library.

4. Reject candidate imports, executables, and authority fields.

Pass: Fixed validators preserve current product checks without executing candidate source.

Exclude: Do not change image products or add a new validator release dependency.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T46 — Factor fixed image identity and publication logic

Requires: T45. Worker: GPT-6-Luna high. Reviewer: medium.

Files: W/job_image_authority_identity.py; W/job_image_authority_registry.py; W/job_image_authority_publish.py.

1. Port existing publish.py authorization and OCI operations.

2. Read source identities through authenticated exact-SHA GitHub data.

3. Retain current CI, artifact, attempt, and attestation checks.

4. Preserve approved redirect handling and credential stripping.

5. Use existing gh and Python capabilities.

Pass: The fixed data-only code preserves current publication authorization and byte verification.

Exclude: Do not upload products, add a registry cache, or introduce a new OCI client.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T47 — Compose one source-free image authority body

Requires: T46. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: W/job_image_authority.rs; W/schema2_job_image_candidate.rs; O/image_maintenance/source.rs.

1. Register the new module through crates/velnor-actions-workflow-renderer/src/schema2_job_image_candidate.rs.

2. Compose the fixed validated fragments through include_str.

3. Declare the module in the existing renderer parent.

4. Reuse existing producer source evidence where sufficient.

5. Add only missing authenticated data fields to source evidence.

6. Use one body for attestation and publication modes.

Pass: Both authority modes consume one fixed implementation without a candidate helper or new CLI.

Exclude: Do not change credential-free image build semantics or introduce new authority claims.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T48 — Remove source execution from image authority jobs

Requires: T14, T44, T47. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: W/schema2_job_image_candidate.rs; W/schema2_job_image_native.rs; W/job_image_authority.rs.

1. Replace authority checkout and source builds with the fixed data-only body.

2. Remove authority calls to repository publish.py.

3. Bind credential-free producer output copies to the shared context.

4. Keep compiler cache access disabled in authority jobs.

5. Preserve existing image production and publication boundaries.

Pass: Image attestation and publication contain no checkout-dependent compilation or candidate code execution.

Exclude: Do not change unrelated behavior or dependencies.

Block: Block this path if existing capabilities cannot preserve every product trust check. Do not invent a helper release.



## T49 — Apply common admission to existing cache families

Requires: T22, T23, T30, T41. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/stack_family_cache.rs; O/tofu_cache.rs; W/cache_steps_family.rs.

1. Route existing supported families through common admission and reporting.

2. Preserve their current supported payload and hydration semantics.

3. Count image namespaces only when inventory proves their presence.

4. Count all foreign entries in total usage.

5. Reject publication without a justified pre-upload bound.

6. Disable independent family saves that bypass the repository policy.

Pass: Every supported writer uses one budget policy while unrelated entries remain untouched.

Exclude: Do not add a new backend or cache absent consumer products.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T50 — Replace unbounded qualification cache writers

Requires: T31, T48, T49. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: W/matrix_qualification.rs; W/schema2_mbx_qualification.rs; C/workflow/qualification_cache_lineage.rs.

1. Replace run-specific qualification cache generations with bounded owned slots.

2. Use the shared snapshot lifecycle and real observation contract.

3. Remove dependency-cache artifact transfer assumptions.

4. Keep hosted-only cache qualification within the approved budget.

Pass: Qualification cannot evade repository admission or rely on persistent self-hosted state.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T51 — Replace obsolete consumer cache settings

Requires: T03, T31, T49. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/config.rs; O/config_workflow.rs; C/config/workflow.rs.

1. Define the single GitHub-only policy configuration.

2. Reject obsolete PR-write and MBX-persistence options.

3. Allow only lower operating ceilings and reviewed repair revisions.

4. Preserve unrelated execution and product configuration.

Pass: Configuration cannot request paid overflow, legacy caching, or a larger accounting ceiling.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T52 — Complete cross-crate caller bindings

Requires: T26, T34, T38, T42, T44, T48, T50, T51. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: O/lib.rs; C/workflow_reexports.rs; W/lib.rs.

1. Export only the new owned interfaces required by real callers.

2. Remove obsolete persisted-cache exports from public surfaces.

3. Check every T01 caller against the new lifecycle.

4. Record any missing caller as incomplete integration.

Pass: No implemented cache module remains unused and every supported caller has a recorded new path.

Exclude: Do not hide behavior changes inside mechanical binding edits.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T53 — Complete pure cache contract regression fixtures

Requires: T22, T23, T24, T52. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: crates/velnor-actions-contract/tests/gc1_contract_cases.rs; crates/velnor-actions-contract/tests/velnor_contract.rs.

1. Add lock, feature, path, profile, toolchain, and native identity cases.

2. Reject malformed coverage, context, and publication records.

3. Keep unknown counters distinct from zero.

4. Register every test in the existing explicit root.

Pass: All contract cases execute and fail when their stated invariant is violated.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T54 — Complete snapshot and observer regression fixtures

Requires: T10, T19, T52. Worker: GPT-6-Luna high. Reviewer: medium.

Files: crates/velnor-actions-orchestrator/tests/gc1_runtime_cases.rs; crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs.

1. Test fresh checkouts with unchanged workspace dependencies.

2. Test original nanoseconds, directory watchers, deleted files, and Git state.

3. Test separate build directories and private-home teardown.

4. Test rustdoc attribution, compiler escape, and missing observations.

5. Test frozen snapshot replay with empty MBX state.

6. Test all-family admission, stale intent, and bounded repair.

Pass: Correctness fixtures reject false warm results and unsafe source restoration.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T55 — Complete event and failure workflow fixtures

Requires: T31, T34, T50, T52. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: crates/velnor-actions-workflow-renderer/tests/gc1_workflow_cases.rs; crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs.

1. Test PR, fork, main, merge-queue, tag, preview, and release modes.

2. Test skipped producers and hard writer failures.

3. Test mixed-attempt ledgers after failed-job reruns.

4. Test exact and primary-prefix current-ref shadow against default scope.

5. Test denied saves, corrupt replacement repair, and cleanup lag.

6. Test static branching, noncolliding ledgers, and platform limits.

Pass: Every selected unit remains required under each generated failure path.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T56 — Review cache and authority boundaries

Requires: T12, T48, T54, T55. Worker: GPT-6.1-Sol high. Reviewer: high.

Files: docs/reviews/cache-github-only-security.md.

1. Review source projection and outer archive trust.

2. Review fork visibility and private derived output.

3. Review writer, cleanup, signer, and publisher permissions.

4. Block integration on any unresolved authority finding.

Pass: An independent security verdict covers every cache reader and writer.

Exclude: Do not implement fixes inside the review task.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T57 — Review integrated architecture and task coverage

Requires: T01, T53, T54, T55, T56. Worker: GPT-6.1-Sol high. Reviewer: high.

Files: docs/reviews/cache-github-only-architecture.md; D/caller-map.md.

1. Check all real callers against the fixed contract.

2. Review actual command and product equivalence.

3. Review budget assumptions and unsupported observation.

4. Require explicit decisions for every remaining conflict.

Pass: The implementation is complete enough for controlled runtime qualification without invented policies.

Exclude: Do not declare a measured fit or speedup before live evidence.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T58 — Define the bounded qualification harness and run commands

Requires: T54, T57. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: crates/velnor-actions-orchestrator/tests/gc1_qualification_cases.rs; crates/velnor-actions-orchestrator/tests/gc1_qualification_support.rs; crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs; docs/implemented/cache-github-only-qualification.md; D/run-commands.json.

1. Register the gc1_qualification module in the explicit test root.

2. Create shared case assertions and local fixture support.

3. Test the harness under the separate gc1_aux prefix.

4. Require nonempty dependency work and complete observation.

5. Write exact workflow IDs, inputs, source pins, and command arrays.

6. Bind case IDs, run budgets, fault limits, and approval states.

7. Reject production cache IDs in destructive fixture operations.

Pass: The harness defaults to local fixtures and supplies concrete approval-bound hosted command records.

Exclude: Do not start hosted fault runs through a unit test by default.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T59 — Implement input and cold-to-warm qualification cases

Requires: T58. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: crates/velnor-actions-orchestrator/tests/gc1_qualification_inputs.rs; crates/velnor-actions-orchestrator/tests/gc1_qualification_cases.rs.

1. Implement cold and fresh-runner replay cases.

2. Implement application-only and single-dependency changes.

3. Implement feature, profile, host, compiler, and native changes.

4. Check real compiler attribution and immutable origin coverage.

5. Include the cases in the existing gc1_qualification module.

6. Record every expected case name in the discovered test list.

Pass: The assigned local qualification scenarios execute through real owned interfaces and reject false success.

Exclude: Do not run hosted faults by default or replace real compiler evidence with Cargo progress messages.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T60 — Implement event and cancellation qualification cases

Requires: T59. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: crates/velnor-actions-orchestrator/tests/gc1_qualification_lifecycle.rs; crates/velnor-actions-orchestrator/tests/gc1_qualification_cases.rs.

1. Implement PR, main, preview, release, fork, queue, and tag cases.

2. Implement competing producers and three cancellation phases.

3. Implement mixed-attempt failed-job reruns.

4. Check ref shadow and exact selected-unit results.

5. Include the cases in the existing gc1_qualification module.

6. Record every expected case name in the discovered test list.

Pass: The assigned local qualification scenarios execute through real owned interfaces and reject false success.

Exclude: Do not run hosted faults by default or replace real compiler evidence with Cargo progress messages.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T61 — Implement publication and recovery qualification cases

Requires: T60. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: crates/velnor-actions-orchestrator/tests/gc1_qualification_failure.rs; crates/velnor-actions-orchestrator/tests/gc1_qualification_cases.rs.

1. Implement skipped and hard-failed producer cases.

2. Implement successful-step save denial and damaged cache cases.

3. Implement budget overlap and good-predecessor bad-replacement repair.

4. Implement coverage growth under unchanged compatibility.

5. Include the cases in the existing gc1_qualification module.

6. Record every expected case name in the discovered test list.

Pass: The assigned local qualification scenarios execute through real owned interfaces and reject false success.

Exclude: Do not run hosted faults by default or replace real compiler evidence with Cargo progress messages.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T62 — Implement private-home release and pressure qualification cases

Requires: T61. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: crates/velnor-actions-orchestrator/tests/gc1_qualification_paths.rs; crates/velnor-actions-orchestrator/tests/gc1_qualification_cases.rs.

1. Implement private-home named and native command cases.

2. Implement every actual test, Clippy, and documentation family.

3. Implement helper reuse and source-free authority cases.

4. Implement migration overlap and other-family pressure cases.

5. Include the cases in the existing gc1_qualification module.

6. Record every expected case name in the discovered test list.

Pass: The assigned local qualification scenarios execute through real owned interfaces and reject false success.

Exclude: Do not run hosted faults by default or replace real compiler evidence with Cargo progress messages.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T63 — Run full verification before candidate integration

Requires: T62. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: docs/reviews/cache-github-only-local-verification.json.

1. Run the full root verification sequence.

2. Run the separate nested-runner verification sequence.

3. Verify existing pin freshness through the required script.

4. Leave generation parity to the next candidate task.

5. Record the exact source and successful review set.

Pass: All required existing gates pass before an integration commit is permitted.

Exclude: Do not replace full verification with focused tests.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T64 — Prepare the reviewed generator candidate and activation handoff

Requires: T63. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: docs/reviews/cache-github-only-candidate.json; .velnor/config.toml.

1. Regenerate the candidate Velnor outputs with the verified binary.

2. Run full verification after candidate regeneration.

3. Prepare the exact normal-release and activation request.

4. Require a real controller release with the new cache operations.

5. Record its independent binary digest and descriptor.

6. Record owner approval for exact candidate activation and hosted qualification.

Pass: A reviewable candidate exists; activation does not use a fabricated release or helper pin.

Exclude: Do not change unrelated behavior or dependencies.

Block: Wait for explicit owner activation of the reviewed candidate. Do not merge, publish, or dispatch automatically.



## T65 — Qualify cold warm and dependency-change behavior

Requires: T02, T64. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: docs/reviews/cache-github-only-hosted-warm.json.

1. Use the approved campaign and existing hosted runner classes.

2. Execute cases 1 through 6, 17, 18, and 19.

3. Measure compiler, origin, transfer, wall, runner, and disk work.

4. Reject incomplete observation or an empty expected workload.

Pass: Each supported warm recipe meets exact zero-work assertions and measured performance thresholds.

Exclude: Do not change unrelated behavior or dependencies.

Block: Remain blocked until hosted execution and its run budget are authorized. Do not report planned runs as executed.



## T66 — Qualify event authority and recovery behavior

Requires: T65. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: docs/reviews/cache-github-only-hosted-lifecycle.json.

1. Execute approved cases 7 through 15 and 20.

2. Retain every run attempt and selected unit result.

3. Count any duplicate work across the full lifecycle.

4. Verify source-free authority jobs and restricted fork behavior.

Pass: Lifecycle results match GitHub visibility and preserve checks through each failure.

Exclude: Do not change unrelated behavior or dependencies.

Block: Use dedicated owned test entries. Actual default-branch and release-path activation needs explicit owner authorization.



## T67 — Qualify capacity migration and competing families

Requires: T02, T27, T65. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: docs/reviews/cache-github-only-hosted-capacity.json; D/cache-budget.json.

1. Execute approved cases 16, 21, and 22.

2. Measure inner, outer, stored, overlap, and peak disk bytes.

3. Verify publication bounds and delayed cleanup accounting.

4. Reject any repository whose full working set cannot fit.

Pass: Each accepted group fits its complete repository model without overflow or required-coverage deletion.

Exclude: Do not change unrelated behavior or dependencies.

Block: Report the exact capacity conflict when a fit fails. Do not substitute external storage or paid capacity.



## T68 — Remove obsolete dependency seed implementation

Requires: T58, T66, T67. Worker: GPT-6-Luna low. Reviewer: medium.

Files: O/dependency_seed.rs; C/workflow/dependency_seed.rs; O/workflow_jobs.rs.

1. Remove the redundant workspace seed path.

2. Remove obsolete seed scheduling and success assumptions.

3. Retain any still-required non-cache planning behavior.

4. Update affected regression fixtures through their registered roots.

Pass: No obsolete seed can compile hidden dependency work or bypass Required.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T69 — Remove persisted MBX cache policies and rendering

Requires: T55, T68. Worker: GPT-6-Luna low. Reviewer: medium.

Files: C/workflow/cache_family_mbx.rs; W/cache_steps_mbx_scripts.rs; W/cache_steps_mbx_command.rs.

1. Remove persistent MBX import and export generation.

2. Remove raw 384-MiB publication gates.

3. Keep only supported ephemeral driver behavior still required.

4. Remove unreachable public references through the T01 removal map.

Pass: No obsolete persisted MBX path remains executable.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T70 — Remove old family elections and pruning policies

Requires: T69. Worker: GPT-6-Luna low. Reviewer: medium.

Files: W/cache_elect.rs; W/cache_save_budget.rs; W/cache_prune.rs; M/cache_trust.rs.

1. Remove conflicting per-family save elections and byte gates.

2. Replace count-only current-ref pruning with common operations.

3. Remove run-specific permanent generation rules.

4. Verify all remaining writers use shared admission.

Pass: There is one cache accounting and lifecycle policy with no compatibility mode.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T71 — Publish the qualified cache contract and operations guide

Requires: T03, T70. Worker: GPT-6-Luna low. Reviewer: medium.

Files: docs/proposed/cache-contract.md; docs/proposed/cache-families.md; docs/implemented/cache-github-only-operations.md.

1. Record measured groups, thresholds, and actual supported cases.

2. Document recovery, repair revisions, and private-source boundaries.

3. Document explicit PR-to-main and older-release exceptions.

4. Remove claims superseded by qualified behavior.

Pass: Documentation separates guarantees, operational policy, and known limitations.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.



## T72 — Finalize the qualified generator and immutable consumer pin

Requires: T64, T71. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: docs/reviews/cache-github-only-final-candidate.json; .velnor/config.toml.

1. Regenerate Velnor outputs after obsolete-code removal.

2. Run the full required verification sequence.

3. Review evidence continuity against the final source SHA.

4. Rerun affected approved hosted cases unless removal equivalence is proved.

5. Include final Velnor generated paths in that proof.

6. Prepare the final normal-release handoff for owner approval.

7. Record the approved immutable generator pin before consumer activation.

Pass: The final candidate has complete verification and a real approved activation pin.

Exclude: Do not change unrelated behavior or dependencies.

Block: Stage the complete change for approval. Do not invent a release, merge, or publish automatically.



## T73 — Migrate jackin-project/jackin

Requires: T66, T67, T72. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: .velnor/config.toml.

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.

Pass: The repository passes its real command matrix and complete capacity model with no hand-edited generated output.

Exclude: Do not edit Cargo or Mise semantics, add products, or delete unrelated caches.

Block: Block activation when the approved pin, run authorization, native observation, or capacity proof is missing.



## T74 — Migrate ChainArgos/blockchain-explorer

Requires: T66, T67, T72. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: .velnor/config.toml.

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.

Pass: The repository passes its real command matrix and complete capacity model with no hand-edited generated output.

Exclude: Do not edit Cargo or Mise semantics, add products, or delete unrelated caches.

Block: Block activation when the approved pin, run authorization, native observation, or capacity proof is missing.



## T75 — Migrate ChainArgos/bitcoin-grpc-server

Requires: T66, T67, T72. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: .velnor/config.toml.

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.

Pass: The repository passes its real command matrix and complete capacity model with no hand-edited generated output.

Exclude: Do not edit Cargo or Mise semantics, add products, or delete unrelated caches.

Block: Block activation when the approved pin, run authorization, native observation, or capacity proof is missing.



## T76 — Migrate ChainArgos/eth-grpc-server

Requires: T66, T67, T72. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: .velnor/config.toml.

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.

Pass: The repository passes its real command matrix and complete capacity model with no hand-edited generated output.

Exclude: Do not edit Cargo or Mise semantics, add products, or delete unrelated caches.

Block: Block activation when the approved pin, run authorization, native observation, or capacity proof is missing.



## T77 — Migrate ChainArgos/tron-grpc-server

Requires: T66, T67, T72. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: .velnor/config.toml.

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.

Pass: The repository passes its real command matrix and complete capacity model with no hand-edited generated output.

Exclude: Do not edit Cargo or Mise semantics, add products, or delete unrelated caches.

Block: Block activation when the approved pin, run authorization, native observation, or capacity proof is missing.



## T78 — Migrate ChainArgos/bitcoin-processor-rust

Requires: T66, T67, T72. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: .velnor/config.toml.

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.

Pass: The repository passes its real command matrix and complete capacity model with no hand-edited generated output.

Exclude: Do not edit Cargo or Mise semantics, add products, or delete unrelated caches.

Block: Block activation when the approved pin, run authorization, native observation, or capacity proof is missing.



## T79 — Migrate ChainArgos/eth-processor-rust

Requires: T66, T67, T72. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: .velnor/config.toml.

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.

Pass: The repository passes its real command matrix and complete capacity model with no hand-edited generated output.

Exclude: Do not edit Cargo or Mise semantics, add products, or delete unrelated caches.

Block: Block activation when the approved pin, run authorization, native observation, or capacity proof is missing.



## T80 — Migrate ChainArgos/tron-processor-rust

Requires: T66, T67, T72. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: .velnor/config.toml.

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.

Pass: The repository passes its real command matrix and complete capacity model with no hand-edited generated output.

Exclude: Do not edit Cargo or Mise semantics, add products, or delete unrelated caches.

Block: Block activation when the approved pin, run authorization, native observation, or capacity proof is missing.



## T81 — Close fleet qualification and obsolete namespace retirement

Requires: T71, T72, T73, T74, T75, T76, T77, T78, T79, T80. Worker: GPT-6-Luna medium. Reviewer: medium.

Files: docs/reviews/cache-github-only-fleet.json; docs/implemented/cache-github-only-operations.md.

1. Verify the nine repository evidence sets and approved activation states.

2. Retire only proven obsolete owned namespaces after replacement qualification.

3. Run the final root and nested-workspace gates.

4. Report unsatisfied cases without declaring universal cache hits.

Pass: Every supported path has accepted evidence or an explicit blocker; no obsolete writer or external-storage requirement remains.

Exclude: Do not change repository settings or claim completion while a required capacity or observation gate remains blocked.

Block: Stop this task when a required interface or capability is missing. Continue independent ready tasks.


