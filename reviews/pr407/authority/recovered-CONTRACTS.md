# Shared implementation contracts

Status: proposed interfaces. No replacement implementation or live qualification is claimed.

This file fixes the shared records used by the existing Velnor binary.
It does not define a service, backend, plugin interface, or external runner.
Use ARCHITECTURE.md for behavior, CACHE_BUDGET.md for limits, and ACCEPTANCE.md for qualification.
Task names below are stable ownership labels. Numeric task IDs may change during review.

## 1. Encoding and ownership rules

Use the existing strict JSON reader, canonical serializer, and SHA-256 implementation.
Use schema version `1` for these new records.
Do not reuse an older MBX receipt's schema number or meaning.
Reject duplicate keys, unknown fields, unknown variants, invalid paths, and unsupported versions.
An invalid cache record causes visible cold recovery. It never skips required checks.

Use Rust structs and closed enums. Do not pass untyped JSON maps between owners.
Apply `deny_unknown_fields` to serialized structs.
Use integers for counts, bytes, seconds, and nanoseconds. Do not use floating-point identity inputs.
Use the current owned SHA-256 digest representation consistently.
Render key components from the digest's hexadecimal body.
Do not introduce another hash representation or another hashing dependency.

Sort object keys through the existing canonical serializer.
Sort set-valued arrays by their declared identity. Reject duplicates.
Preserve ordered arrays such as argv, recipe execution order, and action path order.
Exclude a record's own digest field when computing that digest.
Keep run coordinates and measurement times outside dependency identity preimages.

Every record uses an existing request/report size limit.
Do not place a full file index or compiler ledger in GitHub job outputs.
Pass bounded record paths, digests, and dispositions through the current output mechanism.
Use existing report transport for evidence. Never transfer dependency payloads through it.

| Owner | Shared responsibility |
|---|---|
| `velnor-actions-contract/src/workflow/cache_identity.rs` and `cache_policy.rs` | New pure identity, coverage, policy, and outcome types from the identity task. |
| `velnor-actions-contract/src/workflow/cache_context.rs` and existing `report.rs` | New execution context and report bindings from the context task. |
| Existing `velnor-actions-rust/src/closure.rs`, `identity.rs`, `identity_closure.rs`, and `tasks.rs` | Cargo dependency roles, recipe inputs, and exact command selection. |
| Existing orchestrator source, check, cache-key, and crate-job owners | Compose the records and validate actual execution context. |
| Planned orchestrator snapshot, inventory, admission, publication, and cleanup modules | Implement the corresponding lifecycle operations through their task-declared parents. |
| Existing Mise command and acquisition owners | Execute approved child commands and collect observations. |
| Existing renderer cache, preseed, task-wrapper, and workflow owners | Emit typed fixed steps. Do not derive Cargo policy or execute processes. |
| Existing CLI `dispatch.rs`, `dispatch/operation.rs`, and `main.rs` | Reach the typed operations and compiler adapter entries. Do not implement their algorithms. |
| Existing orchestrator `merge.rs`, `merge_checks.rs`, `merge_request.rs`, `retrieve_reports.rs`, and `task_report.rs` | Bind effective group results and observations through the actual final-report path. |
| Existing `scripts/hosted_phase_measurement/measure_support.py`, `report_events.py`, `report_counters.py`, and `report_builder.py` | Admit authenticated report members and aggregate actual lifecycle work. Preserve the current collector CLI. |

The named new cache modules are already scoped by TASKS.json.
Register each through its task-declared compiled parent before that task completes.
Do not postpone compilation or public binding until the final integration review.

## 2. Common scalar and binding types

The following are nested values. They are not separate services or files.

| Rust value | Exact fields or values |
|---|---|
| `SchemaVersion` | The integer `1`. |
| `Digest` | `s256-` followed by exactly 64 lowercase hexadecimal characters, matching the existing cache digest spelling. |
| `RelativePath` | UTF-8 repository-relative or owned-root-relative path. Reject absolute paths, `..`, NUL, and ambiguous aliases. |
| `RealMtime` | `seconds: i64`, `nanoseconds: u32`. Require nanoseconds below 1,000,000,000. |
| `MeasuredU64` | `value: Option<u64>`, `unknown_reason: Option<ObservationGap>`. Exactly one is present. |
| `ObservationGap` | `code`, `detail`, `affected_recipe_ids`, `evidence_ref`. Codes are closed; detail cannot supply executable behavior. |
| `CacheFamily` | `sources`, `tools`, `state`, or an existing explicitly supported non-Rust family from `cache_family.rs`. |
| `CommandFamily` | Existing build/test, Clippy, documentation, named-check, helper, and native producer families. No inferred product. |
| `JobBinding` | `repository_id`, `repository`, `run_id`, `run_attempt`, `job_id`, `job_key`, `event`, `ref`, `workflow_sha`, `source_sha`, `plan_digest`. |
| `EntryTuple` | `repository_id`, `cache_id`, `ref`, `key`, `version`, `size_in_bytes`, `created_at`, `last_accessed_at`. |
| `GenerationId` | `family`, `group_digest`, `compatibility_digest`, `coverage_digest`, `repair_revision`. |

Use a measured zero only when the observation boundary is complete.
Use null and a reason when a value is unavailable.
Use an explicit applicability flag for a genuinely absent workload.
Do not encode unknown, not applicable, and zero as the same value.

Credentials and secret values never enter an identity, report, archive, or digest preimage.
Use immutable private-asset identities after authorized acquisition.
Do not hash a secret value as a substitute for excluding it.

### Rust and JSON field types

Use `String` newtypes for digests, existing semantic IDs, and validated paths.
Use `u64` for GitHub numeric IDs, counts, bytes, durations, and repair revisions.
GitHub run, job, repository, and cache IDs must be positive.
Use the existing Git-object type for source, tree, and workflow identities.
Use RFC 3339 UTC strings for report timestamps.
Only filesystem mtimes use `RealMtime`.
Use `Vec<T>` for the declared ordered arrays and validated sets.
Use `BTreeMap<String, String>` only for declared nonsecret environment values.
Use `bool` for explicit boolean fields.
Use `Option<T>` only where this specification permits absence.
An absent optional value serializes as JSON null, not an omitted field.

The common Rust shape is:

```rust
#[derive(Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
struct MeasuredU64 {
    value: Option<u64>,
    unknown_reason: Option<ObservationGap>,
}

#[derive(Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
struct RealMtime {
    seconds: i64,
    nanoseconds: u32,
}
```

Use existing derives and validation conventions.
The declarations above are proposed shapes, not code already present in the repository.
Each tagged record also carries literal `schema: 1`.
Validate cross-field invariants after strict deserialization.

## 3. Compatibility and requested coverage

**Type owner:** the identity and context contract modules.
**Derivation owner:** the Rust adapter and existing orchestrator planning owners.

### `CompatibilityV1`

Required fields:

- `schema`, `repository_id`, `workspace_id`, `family`.
- `host_os`, `host_arch`, `runner_image_identity`, `abi_identity`.
- `toolchain_identity`, `compiler_identity`, `native_environment_digest`.
- `target_environment_ids` for the currently supported target/SDK combinations.
- `path_layout_digest`, including actual stable absolute workspace and owned-home roots.
- `lane_scheme_digest`, `archive_format`, and `observer_interface_version`.
- `source_policy_digest` and `authorized_audience_digest` where that family needs them.

Record `runner_image_identity` for audit.
Exclude a blanket hosted-image revision from the compatibility digest.
Invalidate only when the image change alters an actual relevant compiler, linker, ABI, SDK, native input, or path requirement.
The native environment binds actual compiler, linker, library, and SDK identities.
An unknown required identity makes state compatibility unqualified.
It does not become a wildcard.
Source and tool families use only their relevant compatibility fields.
Document irrelevant fields through their closed family variant, rather than magic empty strings.

### `RecipeV1`

Required fields:

- `recipe_id`, `unit_id`, `workspace_id`, `package_id`, `command_family`, `lane_id`.
- `command_builder_id`, `argv`, `cwd_relative`, and `executable_identity`.
- `features`, `default_features`, `cargo_profile`, `nextest_profile`, and `targets`.
- `declared_nonsecret_environment` and `warning_policy_digest`.
- `dependency_input_digest`, `workspace_dependency_digest`, `native_input_digest`, `declared_external_input_digest`.
- `required_output_roles`, including configured target/build directories and required generated inputs.
- `source_bound_helper_digest`, present only for a source-bound helper recipe.

The existing command builder produces argv.
The record preserves it for identity and equality checks.
A received recipe cannot authorize arbitrary command execution.
The consumer resolves its ID against the locally authenticated plan and compares every semantic field.

Compute `recipe_id` from the canonical semantic recipe fields.
Exclude run coordinates and the application's full task identity.
Include a workspace library's source when another selected unit uses it as a dependency.
Include a helper's full source identity when the helper itself must be reused.
Keep Nextest's test profile separate from Cargo's compilation profile.

### `RequestedCoverageV1`

Required fields: `schema`, `generation`, `compatibility`, `ordered_recipe_ids`, `recipes`, `immutable_objects`, `active_variant_ids`, `dependency_inputs_digest`.

Each immutable object has `object_id`, `kind`, `approved_origin_id`, `immutable_locator`, `content_digest`, and `audience_digest`.
Kinds cover the existing source, tool, private asset, and verification inputs.
Do not use a mutable URL alone as immutable identity.

`coverage_digest` hashes the recipe semantics, dependency inputs, immutable object set, and active variants.
The execution order remains recorded separately when two equivalent sets share coverage.
`group_digest` identifies the bounded workspace/host grouping and supported lane scheme.
A lockfile change can change coverage without invalidating all compatible old output.
An application-only change does not create a new dependency generation.

## 4. Execution context and source binding

**Type owner:** `cache_context.rs` and existing report types.
**Runtime owners:** `check_prepare.rs`, `check_runtime.rs`, `source_prep.rs`, and Mise `check_execution.rs`.

### `ExecutionContextV1`

Required fields:

- `schema`, `job`, `generation`, `requested_coverage_digest`, `source_binding_digest`.
- `workspace_root`: the actual authenticated `GITHUB_WORKSPACE`.
- `owned_root`, `cargo_home`, `rustup_home`, `tool_root`, `transport_root`, `observation_root`.
- `lanes`: each has `lane_id`, `command_family`, `variant_digest`, `target_dir`, and optional separate `build_dir`.
- `compiler_adapters`: stable paths plus independently resolved real executable identities.
- `selected_driver`: the existing Cargo or MBX route.
- `mbx_target_views`: fixed false for contributing commands.
- `effective_cache_capability`, `trusted_default_writer`, and `private_audience_digest`.

All execution paths come from trusted layout code.
A cache manifest cannot supply an arbitrary absolute extraction destination.
Transport, reports, and state roots stay outside the checkout.
Do not add ignore files or alter Git metadata to hide them.
Keep private HOME teardown separate from shared owned homes.

### `SourceBindingV1`

Required fields: `schema`, `job`, `admitted_source_sha`, `admitted_tree_id`, `source_admission_digest`, `checkout_semantic_digest`, `declared_input_digest`, `git_semantics_digest`, `plan_digest`.

The source-admission digest refers to the existing authenticated source record.
Do not create a parallel release-eligibility authority.
The source binding records the source actually executed.
It does not relabel a producer's source SHA when default HEAD moves.

The checkout semantic index contains `path`, `kind`, `mode`, `content_digest`, and optional `link_target`.
Its digest excludes mtimes.
The archived projection index additionally records each entry's real `mtime`.
Hashing fresh-checkout mtimes into requested coverage would defeat the projection.

Before projection, authenticate current checkout content and Git state.
Restore matching archived files or unchanged subtrees into their actual checkout locations.
Preserve their real metadata through normal extraction and moves.
Keep changed and new current files. Discard cached-only paths.
Keep current `.git` untouched.
Reject escaping links, devices, credentials, and undeclared executable inputs.

Before execution and freezing, verify the final semantic source binding again.
Record source mutations caused by commands.
An unresolved mutation of a required input blocks snapshot qualification.
Do not fabricate timestamps to resolve it.

## 5. Observation and unit execution

**Observation owner:** Mise's existing command/acquisition boundary and the planned compiler adapters.
**Collection owner:** orchestrator `check_runtime.rs` and its declared observation module.
**Result owner:** existing unit reports and Required validation.

### `ObservationReportV1`

Required fields: `schema`, `job`, `execution_context_digest`, `recipe_id`, `observation_session_id`, `started_at`, `finished_at`, `compiler_events`, `acquisition_events`, `cache_transfer_events`, `gaps`, `summary`.

Compiler event fields:

- `event_id`, `recipe_id`, `package_id`, `dependency_role`, `lane_id`.
- `tool_kind`: rustc, clippy-driver, rustdoc, CC, CXX, or an explicitly observed existing native tool.
- `executable_identity`, `argv_digest`, `environment_digest`, `cwd`.
- `operation_kind`: compilation, compiler query, or observed noncompilation operation.
- `start_time`, optional `finish_time`, optional `exit_code`, optional `signal`, `interrupted`.
- `attribution_status` and `coverage_gap`, when attribution is incomplete.

Acquisition event fields: `event_id`, `recipe_id`, `object_id`, `origin_id`, `kind`, `attempt`, `received_bytes`, `verified_digest`, `outcome`, `duration_ms`.
Cache-transfer fields: `family`, optional `entry`, `direction`, `transferred_bytes`, `duration_ms`, `outcome`.

Summary fields use `MeasuredU64` for dependency compiler executions, application compiler executions, native compiler executions, origin acquisitions, origin bytes, cache bytes, and durations.
Separate query counts from compilation counts.
Separate failed and interrupted calls from successful calls.

MBX version-five totals are corroborating observations only.
They do not replace package attribution or native process closure.
Stable Rust wrappers do not prove direct rustdoc or absolute native calls were observed.
Record those gaps and block the affected zero-work claim.

### `UnitLedgerV1`

Required fields: `schema`, `job`, `group_digest`, `execution_branch`, `selected_unit_ids`, `ordered_results`, `observation_digest`, `source_binding_digest`.

`execution_branch` is reader or writer.
Each result has `unit_id`, `recipe_id`, `task_identity`, `argv_digest`, `effective_input_digest`, `outcome`, `exit_code`, `started_at`, `finished_at`, and `report_digest`.
Keep current full task identity in this execution record.
Do not insert it into every dependency cache key.

The ordered unit ledger must equal the authenticated selected command ledger.
Require one terminal result per selected unit.
Never treat `needs_prepare`, a cache hit, or a preparation receipt as a successful unit result.

### Effective attempts

Required builds an `EffectiveJobBinding` from authenticated GitHub job records.
Fields are `job_key`, `job_id`, `actual_attempt`, `source_sha`, `plan_digest`, `api_conclusion`, `retained_without_rerun`, and `ledger_digest`.
An earlier successful ledger is accepted only when GitHub retained that exact job without rerunning it.
A rerun job requires a result from its actual new job/attempt.
Do not overwrite an earlier record's attempt number.
Require exactly one complete reader-or-writer ledger for each effective group execution.

### Final report transport and collector binding

Extend the existing final-report JSON with a versioned `observations` object.
Do not create another artifact family or a dependency transport channel.
The outer artifact keeps its existing `velnor-final-r{run_id}-a{attempt}` name and `final-report.json` member.
Its current run/attempt/source binding remains unchanged.
An inner retained-job record may carry an earlier actual attempt only with authenticated retention evidence.

`FinalObservationEnvelopeV1` has these required fields:

- `schema`, `collector_job`, `source_binding_digest`, and `plan_digest`.
- `measurement_scope`: current attempt or the explicitly enumerated run lifecycle.
- `included_attempts`, `effective_jobs`, and `executed_job_bindings`.
- `observation_members`, `unit_ledger_bindings`, and `missing_observations`.

Each observation member binding contains `member_name`, `member_size_bytes`, `member_sha256`, `producer_job`, `observation_session_id`, and `unit_ledger_digest`.
Names are validated relative ZIP member paths generated by Velnor.
The digest covers the actual member bytes.
Each member contains one strict `ObservationReportV1` with the same producer binding.
The normal final-report artifact may contain these bounded JSON members and their index.
It must not contain source caches, tool installations, Cargo outputs, or frozen dependency archives.

The collector uses the existing `--artifact-json`, `--artifact-id`, and `--final-artifact` arguments together.
It verifies the artifact API's exact repository, run, name, source identity, size, and digest first.
Then it reads the final report and its indexed observation members.
Reject duplicate, missing, unindexed, escaping, oversized, or digest-mismatched observation members.
Join each member to authenticated job metadata and the accepted effective-job mapping.
An embedded producer claim cannot authenticate itself.
Keep loose `--task-report-dir` files in the existing legacy/unverified category.
Their hashes alone do not supply an API-bound artifact proof.

Replace the collector's blanket unknown-counter rule only for measurements with complete authenticated observation.
Uncovered historical fields remain null with a reason.
Unknown native process coverage stays unknown.
Compiler wall time does not establish native CPU time.
Keep legacy MBX summaries and Cargo progress diagnostics separate from owned process counts.

Deduplicate observations by repository, run, actual job ID, actual attempt, session, and event ID.
Maintain two distinct aggregates:

- Effective Required results contain exactly the retained-or-rerun jobs accepted for the current verdict.
- Executed lifecycle work contains every supplied authenticated execution, including failed attempts, bootstrap, helpers, preparation, and replay.

A retained successful job contributes its original work once.
A rerun contributes its new work in addition to earlier failed work.
Record missing attempt/job coverage explicitly.
Do not label a partial supplied lifecycle as a complete pipeline measurement.
Keep per-attempt wall time, total runner time, and campaign elapsed time distinct.

## 6. Snapshot manifest and frozen proof

**Owners:** the snapshot/archive tasks and the final-coverage replay task.
Use existing `tar`, `flate2`, and owned archive guards.

### `SnapshotManifestV1`

Required fields:

- `schema`, `generation`, `producer_job`, `source_binding_digest`.
- `claimed_completed_recipe_ids`, `requested_coverage_digest`, `compatibility_digest`.
- `paired_source_generation`, `paired_tool_generation`, and their archive digests when applicable.
- `lane_roots`, `projection_index_digest`, `state_index_digest`, `required_output_index_digest`.
- `archive_format`, `mtime_precision`, `excluded_path_policy_digest`.
- `raw_bytes_by_component` and `entry_count`.

The state index records every retained path's type, mode, size, content digest, link target, and real mtime.
Use the complete designated target/build roots.
Do not filter guessed Cargo internals or opaque compiler outputs.
The manifest itself is excluded from its own indexed-content digest.
The final archive digest covers the manifest and every payload byte.

Paired source/tool generation IDs and archive digests record producer provenance.
They are not hard requirements to restore those exact old family archives.
Validate that currently restored sources and tools cover the required immutable subset with the same relevant identities and paths.
An unrelated source-generation or tool-union update must not invalidate usable Cargo state.
Preserve real metadata on unchanged restored inputs through the normal family hydration rules.
Observe actual reuse during qualification instead of assuming identity equality proves freshness.

`claimed_completed_recipe_ids` is a candidate claim until frozen verification passes.
It does not grant publication or a Required result.

### `FrozenProofV1`

Required fields:

- `schema`, `producer_job`, `generation`, `manifest_digest`.
- `frozen_archive_digest`, `frozen_archive_bytes`, `frozen_at`.
- `paired_input_archive_bindings` and `restore_context_digest`.
- `restored_state_index_digest`, `restored_projection_index_digest`, `metadata_roundtrip_passed`.
- `ephemeral_mbx_initial_state`: empty or not applicable, with observed evidence.
- `replay_recipe_ids`, `replay_command_ledger_digest`, `replay_observation_digest`.
- `eligible_dependency_ids_digest`, `eligible_dependency_count`, `unchanged_dependency_compilations`.
- `covered_origin_acquisitions`, `observation_gaps`, `required_outputs_present`.
- `archive_digest_after_replay`, `completed_coverage_digest`, `qualification_outcome`.

The proof sequence is fixed:

1. Complete the planned producer recipe sequence.
2. Freeze one immutable archive from that final candidate state.
3. Record its byte count and SHA-256.
4. Remove only the owned execution state needed for the controlled replay.
5. Restore the frozen archive and its paired inputs to the actual deterministic paths.
6. Verify original seconds and nanoseconds against the recorded metadata.
7. Start replay with empty ephemeral MBX state and target views disabled.
8. Replay the exact compiler-producing recipes and required output checks.
9. Require nonempty eligible dependency coverage and zero unchanged dependency compilation.
10. Reject incomplete native or origin observation for the claimed guarantees.
11. Verify the archive digest remains unchanged.
12. Publish those same frozen bytes after admission.

Do not pack replay-mutated output as the candidate that was supposedly verified.
Do not update archive timestamps to make the test pass.
Use existing archive metadata support to retain nanoseconds.
If exact metadata cannot round-trip, leave this runtime unqualified.

The proof is report data outside the frozen archive.
It binds the immutable archive digest and the producer's authenticated job.
Its presence does not create a second dependency storage channel.
Its paired input bindings identify the actual source/tool payloads used for that replay.
Later consumers may satisfy the same required immutable subsets from newer compatible family generations.
Sources and tools use their existing integrity/coverage validators.
They do not need a compiler replay merely because they share publication policy.

## 7. Discovery and active intent

**Owners:** existing `cache_keys.rs` with its planned discovery and intent children.

### `DiscoveryV1`

Required fields: `schema`, `job`, `generation`, `expected_cache_version`, `allowed_refs`, `inventory_digest`, `inventory_complete`, `exact_candidate`, `predecessor_candidate`, `shadow_state`, `decision`, `reason`.

Each candidate has its complete `EntryTuple` and the expected generation identity.
Choose the exact requested key first.
Choose at most one retained compatible predecessor second.
Order a predecessor by active coverage intent, then creation time as a tie-breaker.
Do not use broad restore prefixes.

`shadow_state` is clear, conflicting-visible-ref, or unknown.
The pinned action cannot select a cache by ID or ref.
Its primary-key search can select longer prefix matches even without restore keys.
Its matched-key output alone cannot identify the stored tuple it restored.
Before extraction, inspect every service-selectable exact or longer primary-prefix entry across visible refs and the applicable version.
Include current-ref shadows and longer-key fallback candidates in that guard.
Do not extract when any selectable candidate has ambiguous or untrusted provenance.
Independent authenticated byte evidence can identify expected bytes.
It does not make untrusted outer extraction safe.

When inventory is unavailable, only the computed exact key may be considered.
Restore it only if existing independent provenance evidence still establishes safe scope.
Otherwise report unavailable and continue cold without extraction.
Do not manufacture a provenance guarantee from an embedded manifest.

After restore, require the actual matched key to equal the intended exact key.
Compare the manifest, compatibility, coverage, and archive identity too.
The post-restore equality check does not replace the pre-extraction provenance guard.
Distinguish complete, partial, missing, unavailable, and corrupt.
Retain a valid restored family when a different family fails.

### `ActiveIntentV1`

Required fields: `schema`, `repository_id`, `default_ref`, `observed_head_sha`, `configuration_digest`, `active_group_ids`, `active_coverage_ids`, `derived_at`, `derivation_evidence_digest`.

Recompute relevant intent after the writer obtains its queue slot.
Use existing pure planning and authenticated source data.
Do not execute repository tasks to determine current intent.
Repeat the check before publication and deletion.
An application-only HEAD change can leave the same coverage active.
Unknown or stale intent blocks mutation, not ordinary required checks.

## 8. Inventory and byte admission

**Owners:** inventory/admission modules registered by their existing orchestrator parent.

### `InventoryV1`

Required fields: `schema`, `repository_id`, `captured_at`, `entries`, `complete`, `pages_observed`, `unknown_reason`, `sum_stored_bytes`.
`entries` contains every ref, namespace, family, and cache version from all returned pages.
Require complete pagination before the sum can authorize a save.
Keep usage-summary data separate because it is not a complete exact inventory.

### `AdmissionV1`

Required fields:

- `schema`, `job`, `generation`, `active_intent_digest`, `inventory_digest`.
- `hard_ceiling_bytes`: exactly 10,000,000,000.
- `operating_ceiling_bytes`: initially 8,000,000,000 or a reviewed lower value.
- `inventory_bytes`, `pending_owned_bytes`, `foreign_inflight_bytes`.
- `candidate_inner_bytes`, `measured_outer_bytes`, `qualified_repack_allowance_bytes`.
- `outer_envelope_identity`, `candidate_upper_bound_bytes`.
- `occupied_generation_slots`, `maximum_generation_slots`: two for this family/group.
- `peak_local_disk_bound`, `available_local_disk`, `local_disk_reserve`.
- `decision`: admitted or blocked; `blocked_reasons`.

Use `MeasuredU64` for required values that can be unknown.
Use checked arithmetic.
Require inventory plus pending owned writes, candidate bound, and foreign exposure to fit the operating ceiling.
Keep the minimum two-billion-byte reserve below the hard ceiling.
Count old namespaces and migration overlap once.
Count an unverified remote candidate in bytes and generation slots.
Never credit an unconfirmed deletion.

The admission record is a point-in-time decision under the common queue.
It is not an atomic GitHub reservation.
Unknown foreign exposure or runtime envelope blocks publication qualification.
Code readiness may proceed with fixture-tested unknown states.

## 9. Publication and repair

**Owners:** publication/recovery modules and the thin renderer transport task.

### `PublicationV1`

Required fields: `schema`, `job`, `generation`, `frozen_archive_digest`, `manifest_digest`, `frozen_proof_digest`, `admission_digest`, `save_step_outcome`, `save_outcome`, `observed_entry`, `readback_outcome`, `readback_archive_digest`, `readback_manifest_digest`, `actual_stored_bytes`, `active_intent_digest`.

Use null for absent evidence, with an explicit outcome reason.
`save_outcome` distinguishes skipped-existing, denied, oversized, interrupted, service-failure, and attempted.
`readback_outcome` distinguishes verified, corrupt, unavailable, and not-attempted.
Only verified readback creates the published disposition.

Read back into an empty owned transport path.
Compare the restored digest with the frozen digest.
Match inventory ref, key, version, ID, and bytes.
Do not infer publication from the save step's conclusion.
Reconcile a stored-size bound violation before cleanup.

Keep an already usable immutable family unchanged when another family misses.
Do not compare its historical application output with a new application's output and call it corrupt.
Do not attempt to overwrite its immutable key.

### `RepairAuthorizationV1`

Required fields: `schema`, `repository_id`, `bad_entry`, `failure_evidence_digest`, `failure_class`, `retained_good_entry`, `retained_good_verification_digest`, `approved_repair_revision`, `approval_record_digest`.

The supported good-A/bad-B sequence is:

1. Keep usable generation A and charge both A and B.
2. Classify B as reproducibly corrupt using recorded validation evidence.
3. Obtain the reviewed exact-ID repair authorization.
4. Delete only B through the separate cleanup owner.
5. Confirm B's deletion before freeing its bytes or slot.
6. Prepare and admit the reviewed repair revision while retaining A.
7. Verify the replacement before retiring A.

A timeout or missing readback does not prove B is corrupt.
An unverified B continues to occupy its slot.
Do not publish a third generation around it.
Do not create a repair revision automatically for each run.

## 10. Cleanup request and result

**Owners:** existing cleanup/prune emitters and their planned cleanup-policy child.

### `CleanupV1`

Required fields: `schema`, `repository_id`, `requesting_job`, `mode`, `candidate_entry_ids`, `ownership_manifest_digest`, `active_intent_digest`, `replacement_publication`, `repair_authorization`, `decision`, `entry_results`.

`mode` is superseded-generation retirement or approved-corrupt-candidate repair.
Exactly the relevant authority record is present for that mode.
Each entry result has `entry`, `recheck_outcome`, `delete_outcome`, and `confirmed_absent`.

The checkout-free cleanup job owns Actions write authority.
It uses the same repository mutation queue as writers.
It rechecks ownership, active intent, replacement presence, ref, version, and coverage.
It never takes executable commands or a broad deletion prefix from a reader.
Retain entries when any required evidence is unavailable.
Only confirmed absence releases charged bytes and slots.

## 11. Bootstrap before the CLI is available

**Owners:** existing renderer `closure.rs` and `steps.rs`, with the task-declared fixed `cache_bootstrap.py`.
The existing `workflow_jobs_cache.rs`, `preseed.rs`, and `preseed_closure.rs` consume its verified handoff.

### `BootstrapDescriptorV1`

Required fields: `schema`, `generator_pin`, `descriptor_digest`, `repository_id`, `host_identity`, `fixed_action_pins`, `fixed_transport_paths`, `controller_release_pin`, `controller_archive_digest`, `controller_executable_digest`, `controller_descriptor_digest`, `tool_set`, `tool_coverage_digest`, `trusted_tool_verification_inputs`, `source_bound_helper_identity`, `effective_cache_capability`.

The generator emits this bounded descriptor with fixed data-only Python and action steps.
It identifies the independently approved released controller and the current tool set.
It cannot run arbitrary argv taken from a cache or PR request.
Use the already available Python and existing trusted tool-verification facilities.
Apply the same ref-shadow and outer-extraction trust guard before restoring tool content.
Verify the released controller against its independent descriptor before executing it.
The descriptor's expected digest cannot come from the unverified cache itself.

Bootstrap is read-only until that verification succeeds.
It may acquire a missing approved controller through the existing normal release acquisition path.
It may not save a cache, prune entries, or call a speculative controller API.
After verification, the controller may enter the normal trusted writer path.
That path still needs its queue, inventory, envelope, source, and capability checks.
Keep bootstrap origin acquisition and cache transfers visible.
There is no separate persistent bootstrap store or cache protocol.

The handoff records the descriptor digest, admitted controller pin, verified executable digest, actual path, and acquisition observations.
The verified controller resolves its closed cache operations locally.
The currently audited release does not gain those new operations merely because the plan names them.
A real approved normal controller release and activation must exist before hosted replacement qualification.
Keep that readiness gate pending until its immutable pin and acquisition evidence exist.

An ordinary application change does not invalidate unrelated dependency tools.
A source-bound helper change does invalidate that helper's reusable identity.
Image authority is excluded from this source-built helper path.

## 12. Internal operation boundary

Use one closed internal cache operation family in the existing binary.
Do not create a public network API or a custom cache-service client.

`CacheOperationRequestV1` has `schema`, `operation`, `context_record`, `context_digest`, `input_records`, and `output_record`.
`operation` is a closed enum for discovery, restore validation, freeze/proof validation, admission, publication readback validation, or cleanup.
Input/output paths must remain inside the approved request/report roots.
The CLI revalidates the current job, event, source binding, and effective capability.
It delegates to the existing owning crates.

Execution of actual selected recipes stays in the existing task/check/native command path.
Do not add a generic cache-run-shell operation.
The renderer supplies fixed operation tags and validated record paths.
The compiler entry uses the stable existing-binary adapter route.
Compiler arguments come from the actual invoking compiler path and validated context, not an untrusted cache record.

## 13. Final source and authority boundary

Before publishing state, bind the frozen proof to the source actually used by the producer.
Keep the current active-intent source distinct from that producer source.
Before accepting a unit result, bind it to its actual job and effective attempt.
Before a release product becomes eligible, apply the existing independent product/source admission rules.

Image validation and publication use fixed generated data-only Python, gh, and existing OCI operations.
The renderer owns those fixed snippets.
The producer supplies bounded data and authenticated GitHub coordinates through existing product evidence.
Authority jobs verify the actual source, run, product identity, and digest through their existing independent trust rules.
Do not execute repository scripts, candidate executables, cached Cargo state, or a new helper API there.
Dependency cache receipts never become release authority.

## 14. Required contract tests

Use the existing explicit Nextest roots.
Keep pure wire/identity validation in the contract crate.
Keep filesystem, admission, replay, and intent algorithms in orchestrator fixtures.
Keep process and compiler-adapter tests in the existing execution owner.

At minimum, test these cross-owner boundaries:

- Canonical identity is independent of map insertion order and run coordinates.
- Ordered argv and recipe differences remain significant.
- Application-only changes preserve dependency coverage; dependency-role changes do not.
- Unknown measurements cannot deserialize or validate as observed zero.
- Current-ref shadows and longer primary-prefix candidates cannot bypass the pre-extraction provenance guard.
- Frozen bytes retain original nanosecond metadata after restoration.
- Replay cannot replace the frozen archive with newly produced output.
- Empty eligible dependency coverage cannot pass frozen verification.
- Failed-job reruns preserve retained job attempts and reject stale rerun results.
- Good A survives bad B, its approved deletion, and replacement admission.
- Unknown inventory, stale intent, or unqualified outer bounds block mutation.
- Reader-provided records cannot select arbitrary commands, roots, or cache IDs for deletion.
- Bootstrap cannot grant itself writes or trust cached tool claims without verification.
- Image authority remains data-only and never consumes compiler state.

These are proposed validation requirements.
The implementation and live evidence must still establish each result.

## 15. Current source basis

The specification extends the existing owners below.
It does not claim that the proposed records already exist.

- [Canonical JSON owner](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-contract/src/canonical.rs).
- [Existing cache families and SHA-256 spelling](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-contract/src/workflow/cache_family.rs).
- [Existing private CLI operation boundary](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-cli/src/dispatch.rs).
- [Existing command execution owner](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-mise/src/command.rs).
- [Existing orchestrator module and API boundary](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-orchestrator/src/lib.rs).
- [Existing final-artifact verification and unknown-counter rules](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/scripts/hosted_phase_measurement/measure_support.py).
- [Existing collector report assembly](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/scripts/hosted_phase_measurement/report_builder.py).
