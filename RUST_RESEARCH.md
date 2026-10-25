# Velnor Rust and shared-cache research — GitHub-only replacement

Observation date: 2026-10-25. This is an evidence and architecture note, not an implementation task plan. No repository source was edited and no workflow was dispatched.

## Fixed source and pins

The inspected main snapshot is `e851b39e3bedc664f8bd6470c629e7bac36c561c`. The generated workflow marker is Velnor Actions 0.1.53. GitHub reports pull permission, no push or admin permission. Current source is retained under `source/`; upstream MBX and Cargo source under `mbx/` and `cargo/`.

The checked-in policy pins Rust 1.99.1; Cargo's verified executable version is 1.99.1 (5f94df478 2026-08-27); MBX 1.27.0; nextest 0.9.149; Mise 2026.10.18; GitHub CLI 2.103.2. Approved actions/cache restore/save pin: `55cc8345863c7cc4c66a329aec7e433d2d1c52a9` (v6.1.0). MBX action pin: `47ce49b32025d93a7a2f4570815afaa2b7092240` (v1.7.2). No local cargo, mbx, or mise executable exists in this research environment, so this audit does not claim a local warm-build experiment. CI logs confirm the deployed pins.

Sources: [version policy](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/.velnor/version-policy.toml), [current config](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/.velnor/config.toml).

Read policies: root and .github AGENTS; hard-decisions; cache-decisions and cache-contract; pr-1 review/adoption/disposition; rust-quality-contract; repo-verification; version policy. The .github namespace is generated: future changes belong in generator sources/config followed by regeneration, never hand patches.

## Current whole-pipeline evidence

Every selected run has run_attempt=1. The attempt-specific job endpoint was used with per_page=100; returned totals fit on one page. Every job's full metadata and steps are retained, including skipped jobs. Logs were fetched for every non-skipped job. Full seed logs and compact excerpts with original line numbers for all other jobs are saved. The first-page-only convenience wrapper was not used to infer attempt completeness.

| Run | Event / source | Jobs | Available logs | Skipped |
|---|---|---:|---:|---:|
| [40184071097](https://github.com/tailrocks/velnor-new/actions/runs/40184071097) | main push, e851b39 | 28 | 28 | 0 |
| [40182223763](https://github.com/tailrocks/velnor-new/actions/runs/40182223763) | PR, 327170b | 28 | 26 | 2 |
| [40185476122](https://github.com/tailrocks/velnor-new/actions/runs/40185476122) | product release workflow_dispatch, e851b39 | 27 | 24 | 3 |
| [40184071131](https://github.com/tailrocks/velnor-new/actions/runs/40184071131) | job image candidate push, e851b39 | 3 | 2 | 1 |
| [40184071101](https://github.com/tailrocks/velnor-new/actions/runs/40184071101) | main cache prune, e851b39 | 1 | 1 | 0 |
| [40184071655](https://github.com/tailrocks/velnor-new/actions/runs/40184071655) | closed PR cleanup, 327170b | 1 | 1 | 0 |

Detailed evidence: `evidence/current-pipelines.json`, `run-*-attempt-1-jobs.json`, `seed-0.log`, `seed-1.log`, `job-121141018859.log`, `job-121141020232.log`. The run list also exposes a still-incomplete Qualification run 40170993374 and a last completed Qualification run 40100246921 at an older commit. They were not represented as current-main warm proof.

Both PR and main have eighteen ordinary Rust consumers. **All 36 miss the MBX bundle.** Cargo sources are warm: these two whole pipelines contain zero visible Cargo crate-download diagnostics. Main Plan first builds the helper before consumer execution; its first MBX summary reports 0 hits, 0 misses, 152 not looked up and 7 bypassed. Plan contains 116 Cargo compile diagnostics. These diagnostics are not a physical compiler count.

The fresh main root seed [job 121142951473](https://github.com/tailrocks/velnor-new/actions/runs/40184071097/job/121142951473) exports 366 actions and 2,260 objects, displayed as 4.0 GiB; nested runner seed [job 121142951460](https://github.com/tailrocks/velnor-new/actions/runs/40184071097/job/121142951460) exports 826 actions and 5,130 objects, displayed as 5.2 GiB. **Both are rejected by the 384 MiB directory-size gate before GitHub upload/compression.** Both jobs conclude success. The old report's 3.0–7.5 GiB figures are historical; these two current observations replace them for this snapshot. These displayed MBX sizes and `du -sk` admission are not GitHub stored/compressed sizes, so they cannot prove repository capacity exhaustion.

The selected product release has 2,934 visible crate-download records; 1,957 occur in four qualification jobs. Three native generator builds and velnor-host build have initial MBX summaries with zero hits. The release fails in qualify-homebrew-macos; later macOS attestation, manifest attestation and generator publication skip. Qualification deliberately exercises clean installation/build paths: preserving that qualification is part of the requirement, not an accidental cache miss to eliminate.

The image-candidate build AND attestation jobs each build the exact-source maintenance binary. Each has 105 download records and an MBX summary of 209 not looked up plus 12 bypasses, zero hits. This is a genuine hidden compiler caller in an authority-related path. Product-release attestation/publication jobs in this *current* sample have zero visible Cargo compile/download diagnostics; do not repeat the prior snapshot's helper-build claim as if those exact jobs still did it.

## Shared 10,000,000,000-byte allowance

The current source incorrectly interprets its ten-GB policy as ten GiB: `CACHE_QUOTA_BYTES = 10 * 1024 * 1024 * 1024` in [cache_family.rs](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-contract/src/workflow/cache_family.rs). Replacement must use exactly 10,000,000,000 bytes, including all cache families, superseded generations, PR refs, qualification caches and publication overlap.

The selected PR/main logs reveal eight distinct `mise-tools-v2-` keys whose reported compressed bytes sum to **1,714,034,217**. A distinct Cargo sources key is **74,337,765** bytes. Nine unique observed entries sum to **1,788,371,982** bytes. See `evidence/observed-cache-sizes.json`. This is a unique-key observation sample, not a complete live inventory, not proof that every entry remained resident simultaneously, and not remaining capacity. The tools sample alone exceeds the docs' nominal 1.5 GiB tools allowance.

The typed family catalog also includes OpenTofu providers, Bun packages, Playwright browsers, dbt packages, uv wheels and Ansible tarballs. Velnor's current production config declares Rust and one named maintenance check, not active Bun/dbt/Ansible/OpenTofu projects; their existence in the generator does not establish Velnor cache occupancy. The actual extra current writers include tools and qualification paths:

* qualification.yml writes `g4-space-${run_id}-${attempt}-${job}` cache entries for hosted and scale-set tests.
* Two qualification MBX jobs use the approved MBX action's objects mode with run/attempt/SHA-specific cache-generation; only the write job saves on dispatch.
* Current `cache_prune.rs::prune_script` lists only each typed family's trusted prefix on the current ref, groups by compatibility prefix, retains the spec count, and limits the CLI list to 1,000. It does not inventory the whole repository, account actual bytes, retire old compatibility prefixes, or cover mise-tools and qualification keys.
* Current PR cleanup removes entries for the closed PR merge ref, but ongoing PRs still contribute to repository occupancy.

The per-family budget test is a static reference-repository sum (four Bun roots, two Tofu roots, etc.), not runtime admission against this repository's total. Current prune and cleanup logs return success without a visible actual deletion line. No live inventory endpoint was available through this connector, so no eviction diagnosis or fitted budget is asserted.

## Supported MBX 1.27 capabilities and limits

The inspected tag's source and generated CLI docs expose exactly:

`mbx cache export [--group GROUP] [--format tar|directory] ARCHIVE`
`mbx cache import ARCHIVE`

There is no supported dependency-only filter, arbitrary blob-selection selector, prediction-only union CLI, or package-closure exporter. Group export includes the union of **finished, not-yet-exported build receipts** in that group; successful export retires those receipts. Export verifies the strict action/object closure. It carries prediction manifests plus Cargo workspace-state attachments; target outputs already in CAS are referenced rather than duplicated. Directory import moves objects into the store and removes the imported directory.

Sources: [CLI export](https://github.com/jdx/mr-boxington/blob/v1.27.0/docs/cli/cache/export.md), [CLI import](https://github.com/jdx/mr-boxington/blob/v1.27.0/docs/cli/cache/import.md), [export implementation](https://github.com/jdx/mr-boxington/blob/v1.27.0/crates/mbx-cache-store/src/lib.rs), [workspace state](https://github.com/jdx/mr-boxington/blob/v1.27.0/crates/mbx/src/workspace_state.rs).

Important complete-generation limitation: `CacheAgent::commit_task_actions` returns only predictions completed by this run, explicitly excluding inherited cumulative predictions. A build that Cargo finds fresh may not initialize an MBX session and thus may record no group receipt. A warm imported snapshot followed by new partial compilation is not automatically a cumulative prediction archive. Export captures the recorded target state, which can retain Cargo-fresh outputs, but do not claim it preserves the union of every inherited prediction. Never parse/edit opaque bundle internals to solve this. An all-fresh run should retain the previous complete cache entry, not synthesize a replacement.

Import restores Cargo workspace state only for a matching checkout (root match or unique manifest/lock signature match), and only into an empty/absent target. `cache_export` catches workspace-state capture failure, warns, and may successfully export only the actions; import similarly warns and may succeed without target-state restoration. Consequently CLI exit success alone is not evidence of complete restored target state or zero dependency compiler work.

[Agent commit source](https://github.com/jdx/mr-boxington/blob/v1.27.0/crates/mbx-cache-core/src/agent.rs), [action-run commit](https://github.com/jdx/mr-boxington/blob/v1.27.0/crates/mbx/src/session.rs), [CLI warning fallback](https://github.com/jdx/mr-boxington/blob/v1.27.0/crates/mbx/src/cli/cache.rs).

Current CI explicitly sets MBX_CC=0, MBX_BUILD_SCRIPT_EXECUTION=0 and MBX_SHARE_OUT_DIR=0. Therefore ordinary object-hit summaries cannot prove elimination of native build-script compiler subprocesses. The supported `MBX_STATS_REPORT` JSON is version 5 and includes actual MBX-adapter compiler invocation counts/durations by outcome, misses, unconsulted, bypass reasons, hits, materialization bytes/times and session time. It does not provide complete external process coverage or a full per-dependency ledger. Cargo stdout and cumulative MBX progress messages cannot substitute for physical process counts. Evidence must combine supported MBX reports with the existing repository-owned measurement facilities, and explicitly leave unobserved native child processes unproven.

[Report option](https://github.com/jdx/mr-boxington/blob/v1.27.0/docs/cli/configuration.md), [report schema and count semantics](https://github.com/jdx/mr-boxington/blob/v1.27.0/crates/mbx/src/session/stats.rs).

## Supported Cargo alternative and candidate recommendation

Pinned Cargo commit resolved to `5f94df4789f005f9a352888e8355ffc645b7ed0e`; source layout is now `src/compiler/`, not `src/cargo/core/compiler/`. Its fingerprint module explicitly excludes registry and git package source-file mtimes from ordinary dep-info checks. That supports unchanged dependency reuse in a new checkout without timestamp tricks. Path packages, external inputs and build-script `rerun-if-changed`/`rerun-if-env-changed` remain separate validity inputs. This is a source-level capability finding, not a completed warm qualification.

Cargo has both target-dir and build-dir. `CARGO_TARGET_DIR` / `--target-dir` choose final output; `CARGO_BUILD_BUILD_DIR` / build.build-dir can separately locate intermediate state. Both must be preserved when separated. Intermediate layout is internal: preserve complete designated directories, do not manufacture a dependency-only subset by deleting guessed .fingerprint/build/dep-info files.

Sources: [Cargo fingerprint semantics](https://github.com/rust-lang/cargo/blob/5f94df4789f005f9a352888e8355ffc645b7ed0e/src/compiler/fingerprint/mod.rs), [build-cache docs](https://github.com/rust-lang/cargo/blob/5f94df4789f005f9a352888e8355ffc645b7ed0e/doc/book/src/reference/build-cache.md).

The smallest candidate to qualify is **complete Cargo target/build snapshots per bounded compatible build group, with separate verified source and tool caches**. Group by repository, workspace root, platform/architecture, toolchain and recipe; do not duplicate one workspace snapshot per crate. Preserve exact per-package feature/profile/target selections initially. Replacing several `-p` invocations with `--workspace` can change feature unification and therefore semantics; fewer jobs does not require that substitution.

Commands that mutate one Cargo lane run sequentially. Independent clippy/doc lanes may remain where concurrent check execution is retained; do not run simultaneous Cargo writers in one directory. Native release and CI profiles are different recipes and may require separate retained units. All per-task obligations and reports survive grouping. A same-source unchanged-dependency warm run must still execute tests and checks; cache restoration is not a successful task result.

Unmodified MBX may remain an ephemeral in-job optimization if qualified, with `MBX_TARGET_VIEWS=0` when archiving real target directories; do not persist its object store too. Its docs explicitly require disabling managed target views when a CI action archives target, otherwise the action can archive only a symlink. Direct pinned Cargo is an existing compile route, not a new cache engine. Compare actual complete archive sizes and measured compilation/restore cost before final selection. This report does not claim that direct target is necessarily smaller than MBX's deduplicated export.

Trusted publication must create a complete snapshot only after every producer recipe designated by that group succeeds; tests may fail later without discarding successful compilation. A failing compile, cancellation, incomplete group or missing size evidence never advances the complete generation. If no new compile state was produced, keep the old generation. Cache failure may execute cold for correctness but must be visible as a failure of warm-cache acceptance, never counted as zero repeated compilation.

## Exact future integration surfaces

| Concern | Current source/functions |
|---|---|
| Configuration and compile route | .velnor/config.toml; contract config; orchestrator/config.rs; mise/wrappers.rs::parse_cargo_wrapper; rust/detect.rs and rust/tasks.rs/argv.rs |
| Grouping/planning | contract/workflow/crate_job.rs; orchestrator/crate_jobs.rs::build_crate_jobs_with_seed_timeout, render_job; crate_jobs_obligations.rs; crate_job_ids.rs; plan_dispositions.rs |
| Exact per-task lanes and reports | orchestrator/crate_jobs_steps.rs::obligation_steps, lane_target_dir; matrix_step.rs; rust/tasks.rs; workflow-renderer/task_wrapper*.rs |
| Remove ineffective duplicate seed producer | orchestrator/dependency_seed.rs::seed_jobs, seed_job, lane_steps; contract/workflow/dependency_seed.rs |
| Sources and private fetch | orchestrator/source_cache.rs::plan_sources_steps, restore_step_for_crate; source_prep.rs; private_wiring.rs::PrivateWiring::steps_for_roots; mise/command_private_fetch.rs |
| Cache key / save / prune | contract/workflow/cache_family.rs; workflow-renderer/cache_steps_mbx_bundle.rs::key_step, export_step; cache_save_budget.rs; cache_prune.rs; cache_cleanup.rs; orchestrator/cache_keys.rs |
| Tool homes | workflow-renderer/toolchain_env_homes.rs::with_toolchain_homes, checked_task_env; tool cache restore/reverification composites |
| Named/private homes | orchestrator/check_prepare.rs::prepare_check, materialize; mise/check_execution.rs::QualifiedCheck::owned_env; check_runtime.rs::run_check |
| Native preview/release builds | orchestrator/preview_producer.rs::execute_preview_task uses prepare_check; preview_production_execution.rs; native_mise_tasks.rs; product-release build/qualify composites |
| Helpers/control plane | workflow_jobs.rs and preseed*.rs; scripts/build-owned-archive-guard.sh; scripts/archive-guard-build-namespace.sh; job-image-candidate.yml Build exact-source native image maintenance |
| Required and authority | orchestrator/required_dispositions.rs::fold_planned_jobs, check_full_event_skips; required_evidence.rs; workflow-renderer required/report code; current product release eligibility + attestation/publication jobs |

Named checks currently allocate `velnor-check-<pid>-<counter>`, create empty cargo/data/cache/state/rustup homes, bind owned CARGO_HOME/MISE_CARGO_HOME and RUSTUP_HOME to those homes, and delete the home on drop. Merely fixing an outer restore does not reach them. A future group projection must explicitly materialize the verified allowed source/tool/build subsets into stable owned paths without importing credentials or allowing repository tasks to select arbitrary homes. Native preview calls the same preparation function.

Private credentials must retain current mint/fetch/revoke ordering and exact source allowlist. Signing/publication cannot acquire repository-code execution just to warm a cache. Existing deliberately clean qualification remains explicit; ordinary build contexts and qualification contexts require distinct accounting.

## Authorized policy migration and verification

The user has explicitly permitted replacing the one-crate-one-job architecture. Update its actual normative surfaces together: hard-decisions.md §1 (and affected whole-job skip implications §3), cache-decisions.md decisions 2/3/7, cache-contract.md §2 path/owner rules, cache-families.md, workflow/rust-quality/task contracts where they fix crate job identity, and generated golden evidence. This is not permission to weaken Required, trust isolation, exact command semantics or quality checks.

Before future commit/merge, repo-verification.md requires root cargo fmt, cargo clippy --locked --workspace --all-targets -- -D warnings, cargo nextest run --locked --workspace, alint validate-config/check, cargo deny, freshness; nested runner is a separate workspace with its own fmt/clippy/nextest/deny gates. Never cargo test. Read-only planning did not run those compilation gates.

Unresolved acceptance inputs: actual repository-wide compressed cache inventory, complete new candidate archive sizes including overlap, cold/warm physical dependency compiler counts, native child process coverage, private asset projection stability, all-profile release and CI coverage, and actual cache failure behavior in the deployed environment. No claimed 10-billion-byte fit or zero-recompile success follows from the available evidence.

