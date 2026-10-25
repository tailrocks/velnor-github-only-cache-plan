# Complete implementation task plan

Status: planned. No implementation or runtime qualification is claimed.

Each card inherits the following rules. They are part of every task.

* Use ARCHITECTURE.md and CONTRACTS.md as the fixed shared-interface inputs.
* Use the exact permitted files or the named T01 ownership map.
* Register new tests in the existing explicit test root.
* Keep unknown measurements distinct from zero.
* Preserve all selected commands, units, products, and authority boundaries.
* Do not add third-party dependencies, tools, actions, engines, or storage backends.
* Do not deploy, merge, change settings, or publish products.
* Obtain independent review before integration.
* Run the full existing root and nested-workspace gates before an integration commit.
* Continue independent ready tasks when another task is blocked.

Implementation, verification, and review run in subagents.
Use a separate subagent for review.
Run the named architecture and security reviews in subagents.

## Exact command sets

`VERIFY_ROOT_AND_RUNNER` expands to these commands, in order.
Use an owned target directory. Do not alter an existing MBX target symlink.

```bash
export CARGO_TARGET_DIR="$PWD/.velnor-owned-verification-target"
cargo fmt --all -- --check
cargo clippy --locked --workspace --all-targets -- -D warnings
cargo nextest run --locked --workspace --no-tests fail
export VELNOR_ACTIONS_BIN="$CARGO_TARGET_DIR/debug/velnor-actions"
alint validate-config
alint check --fail-on-warning
cargo deny check
bash scripts/check-freshness.sh
cargo fmt --manifest-path crates/velnor-runner/Cargo.toml --all -- --check
cargo clippy --manifest-path crates/velnor-runner/Cargo.toml --locked --all-targets -- -D warnings
cargo nextest run --manifest-path crates/velnor-runner/Cargo.toml --locked --no-tests fail
cargo deny --manifest-path crates/velnor-runner/Cargo.toml check
```

Hosted command sets are defined in ACCEPTANCE.md.
They remain blocked until exact workflow inputs, authorization, and run budgets are recorded.
Do not replace them with arbitrary dispatches.

`GENERATE_CANDIDATE` and `GENERATE_VERIFIED_CONSUMER` expand to these exact commands.
Bind `VELNOR_ACTIONS_BIN` to the reviewed candidate or approved immutable consumer pin.
Reject debug-only release-manifest stand-ins before activation.
Both preview trees must match. Generate before running the full verification gates.

For `GENERATE_CANDIDATE`, first build the current source through these commands.
Do not reuse a binary from an earlier source revision.

```bash
export CARGO_TARGET_DIR="$PWD/.velnor-owned-verification-target"
cargo build --locked -p velnor-actions-cli --bin velnor-actions
export VELNOR_ACTIONS_BIN="$CARGO_TARGET_DIR/debug/velnor-actions"
```

For `GENERATE_VERIFIED_CONSUMER`, use the independently verified approved release binary.
Do not build a controller from the consumer repository.
Then use the following generation commands for either command set.

```bash
test -x "$VELNOR_ACTIONS_BIN"
VELNOR_GENERATE_A="$(mktemp -d "${TMPDIR:-/tmp}/velnor-gc1-a.XXXXXX")"
VELNOR_GENERATE_B="$(mktemp -d "${TMPDIR:-/tmp}/velnor-gc1-b.XXXXXX")"
"$VELNOR_ACTIONS_BIN" generate --output-dir "$VELNOR_GENERATE_A"
"$VELNOR_ACTIONS_BIN" generate --output-dir "$VELNOR_GENERATE_B"
git diff --no-index --exit-code "$VELNOR_GENERATE_A/.github" "$VELNOR_GENERATE_B/.github"
"$VELNOR_ACTIONS_BIN" generate
```

Hosted labels below are blocked command contracts, not shell commands.
The qualification harness owns `docs/proposed/cache-github-only/run-commands.json`.
It records exact commands, source pins, workflow IDs, inputs, case IDs, budgets, and approval states.
Each hosted card consumes that file. Do not execute a label literally.
The final candidate must retain evidence for its actual source SHA.
Only reviewed strict-removal equivalence can preserve earlier evidence without rerunning affected cases.

`JACKIN_EXISTING_GATES` is the exact current gate list frozen by T01 from Jackin instructions and task manifests.
`QUALIFY_REPOSITORY_MATRIX` uses that repository's frozen exact recipes and applicable ACCEPTANCE.md cases.
`FINAL_CONSTRAINT_REVIEW` applies CONSTRAINT_REVIEW.md to code, generated output, actual storage, and all evidence.

## Cards


### T01 — Freeze source and caller ownership

**Objective:** Freeze source and caller ownership.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** None.

**Permitted files:** `docs/proposed/cache-github-only/source-map.json`; `docs/proposed/cache-github-only/caller-map.md`; `docs/proposed/cache-github-only/output-map.json`; `docs/proposed/cache-github-only/regression-map.json`; `docs/proposed/cache-github-only/removal-map.json`.

**Steps:**

1. Read all applicable repository instructions.

2. Refresh the nine source revisions and generator headers.

3. Map every cache caller and explicit test root.

4. Enumerate generator-owned outputs for each consumer.

5. Assign existing regression files to their behavior-changing task.

6. Assign mechanical removals to one ordered task.

7. Record exact generator and repository gate commands.


**Exclude:** Do not edit implementation or generated outputs. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
git rev-parse HEAD
git status --short
rg -n "cache|preseed|prepare_check|source_steps" crates/velnor-actions-*
alint validate-config
alint check --fail-on-warning
```

**Expected result and completion:** The map contains every current caller, output owner, command family, and source revision. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Record access-dependent paths as unknown. Do not invent their contents. Do not replace unknown measurements with zero.


### T02 — Record inventories and baseline gaps

**Objective:** Record inventories and baseline gaps.

**Repository and source:** `tailrocks/velnor-new`. A1: Use each exact repository name in EVIDENCE.md. Use the existing approved gh installation.

**Prerequisites:** T01.

**Permitted files:** `docs/proposed/cache-github-only/baseline.json`; `docs/proposed/cache-github-only/cache-inventory.json`; `docs/proposed/cache-github-only/run-budget.json`.

**Steps:**

1. Read complete cache inventories for each authorized repository.

2. Read storage and retention settings without changing them.

3. Import complete selected-run measurements.

4. List approved experiments needed for missing measurements.


**Exclude:** Do not dispatch runs, delete caches, or infer stored bytes from raw exports. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
gh api --paginate "repos/$VELNOR_REPOSITORY/actions/caches?per_page=100"
gh api "repos/$VELNOR_REPOSITORY/actions/cache/usage"
gh api "repos/$VELNOR_REPOSITORY/actions/cache/storage-limit"
gh api "repos/$VELNOR_REPOSITORY/actions/cache/retention-limit"
```

**Expected result and completion:** Every field has a measured value or an explicit unknown state. Obtain review before integration.

**Evidence:** Save endpoint, date, authorization result, every inventory page, and all measured or unknown fields.

**Failure and blocks:** Block only live measurement gates when access fails. Core implementation can continue. Do not replace unknown measurements with zero.


### T03 — Replace obsolete cache and grouping policies

**Objective:** Replace obsolete cache and grouping policies.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T01.

**Permitted files:** `docs/hard-decisions.md`; `docs/proposed/cache-decisions.md`; `docs/proposed/cache-contract.md`; `docs/proposed/cache-families.md`; `docs/proposed/parallelism-and-selection-contract.md`; `docs/proposed/rust-quality-contract.md`.

**Existing regressions:** Use T01 key `regressions/policies`. Expand its exact files before scheduling.

**Steps:**

1. Replace one-crate-per-job and MBX-only storage rules.

2. Define group timeouts and unit-level Required results.

3. Adopt the fixed GitHub-only lifecycle and byte policy.

4. Retain credential and tool-integrity requirements.


**Exclude:** Do not weaken tests, release authority, or input completeness. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
alint validate-config
alint check --fail-on-warning
git diff --check
```

**Expected result and completion:** Normative policies agree with ARCHITECTURE.md and contain no obsolete mandatory cache path. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T04 — Define cache identity and coverage types

**Objective:** Define cache identity and coverage types.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T03.

**Permitted files:** `crates/velnor-actions-contract/src/workflow/cache_policy.rs`; `crates/velnor-actions-contract/src/workflow/cache_identity.rs`; `crates/velnor-actions-contract/src/workflow/mod.rs`.

**Existing regressions:** Use T01 key `regressions/identity_contract`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-contract/tests/gc1_t04.rs`; `crates/velnor-actions-contract/tests/velnor_contract.rs`.

**Required discovered tests:** `gc1_t04_preserves_contract`, `gc1_t04_rejects_invalid_state`.

**Steps:**

1. Define compatibility, requested coverage, and completed coverage separately.

2. Define immutable family, group, generation, and repair identities.

3. Reject run IDs and application commits as universal key inputs.

4. Add canonical serialization and invalid-input cases.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-contract -E 'test(gc1_t04_)' --message-format json
cargo nextest run --locked -p velnor-actions-contract -E 'test(gc1_t04_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-contract --no-tests fail
cargo clippy --locked -p velnor-actions-contract --all-targets -- -D warnings
```

**Expected result and completion:** Canonical identity tests reject incompatible fields and preserve compatible dependency reuse. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T05 — Define execution context and outcome types

**Objective:** Define execution context and outcome types.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T04.

**Permitted files:** `crates/velnor-actions-contract/src/workflow/cache_context.rs`; `crates/velnor-actions-contract/src/workflow/report.rs`; `crates/velnor-actions-contract/src/workflow/report_validate.rs`; `crates/velnor-actions-contract/src/workflow/mod.rs`.

**Existing regressions:** Use T01 key `regressions/context_contract`. Expand its exact files before scheduling.

**Scope exception:** The fourth file is the existing report validator. Update its typed bindings with the report definition and module registration.

**Tests and registration:** `crates/velnor-actions-contract/tests/gc1_t05.rs`; `crates/velnor-actions-contract/tests/velnor_contract.rs`.

**Required discovered tests:** `gc1_t05_preserves_contract`, `gc1_t05_rejects_invalid_state`.

**Steps:**

1. Define source, tool, target, build, and observer paths.

2. Define hit, partial, cold, denied, corrupt, and unavailable outcomes.

3. Define exactly-one-branch unit ledger bindings.

4. Bind each retained job result to its authentic effective attempt.

5. Keep unknown compiler and network counters nullable.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-contract -E 'test(gc1_t05_)' --message-format json
cargo nextest run --locked -p velnor-actions-contract -E 'test(gc1_t05_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-contract --no-tests fail
cargo clippy --locked -p velnor-actions-contract --all-targets -- -D warnings
```

**Expected result and completion:** Types cannot represent a cache hit as successful completion of an unexecuted unit. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T06 — Derive dependency coverage without application churn

**Objective:** Derive dependency coverage without application churn.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T04.

**Permitted files:** `crates/velnor-actions-rust/src/closure.rs`; `crates/velnor-actions-rust/src/identity.rs`; `crates/velnor-actions-rust/src/identity_closure.rs`.

**Existing regressions:** Use T01 key `regressions/coverage`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-rust/tests/gc1_t06.rs`; `crates/velnor-actions-rust/tests/velnor_rust.rs`.

**Required discovered tests:** `gc1_t06_preserves_contract`, `gc1_t06_rejects_invalid_state`.

**Steps:**

1. Reuse the existing resolved Cargo graph.

2. Separate dependency coverage from full task identity.

3. Include workspace dependencies and declared native inputs.

4. Keep application-only deltas outside dependency publication identity.


**Exclude:** Do not build a new Cargo resolver or exempt workspace dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-rust -E 'test(gc1_t06_)' --message-format json
cargo nextest run --locked -p velnor-actions-rust -E 'test(gc1_t06_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-rust --no-tests fail
cargo clippy --locked -p velnor-actions-rust --all-targets -- -D warnings
```

**Expected result and completion:** Application changes preserve dependency coverage; dependency, feature, and native changes update the correct identities. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T07 — Enumerate actual production and helper recipes

**Objective:** Enumerate actual production and helper recipes.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T05, T06.

**Permitted files:** `crates/velnor-actions-orchestrator/src/cache_recipes.rs`; `crates/velnor-actions-orchestrator/src/product_release_pins.rs`; `crates/velnor-actions-orchestrator/src/preview_producer.rs`.

**Existing regressions:** Use T01 key `regressions/production_recipes`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t07.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t07_preserves_contract`, `gc1_t07_rejects_invalid_state`.

**Steps:**

1. Register the new module through crates/velnor-actions-orchestrator/src/product_release_pins.rs.

2. Read existing CI and production command builders.

3. Enumerate exact native, preview, stable, and helper recipes.

4. Retain their profiles, targets, features, and source inputs.

5. Expose their union through the pure recipe catalog.


**Exclude:** Do not derive release coverage solely from crate CI tasks or invent dependency-only commands. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t07_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t07_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Coverage includes actual supported production commands without adding products or changing command semantics. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T08 — Plan compatible groups and exact unit sets

**Objective:** Plan compatible groups and exact unit sets.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T05, T06, T07.

**Permitted files:** `crates/velnor-actions-orchestrator/src/crate_jobs.rs`; `crates/velnor-actions-orchestrator/src/crate_jobs_build_jobs.rs`; `crates/velnor-actions-contract/src/workflow/crate_job.rs`.

**Existing regressions:** Use T01 key `regressions/group_plan`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t08.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t08_preserves_contract`, `gc1_t08_rejects_invalid_state`.

**Steps:**

1. Group units by workspace and effective hosted environment.

2. Retain exact package commands and semantic variants.

3. Define static reader and writer alternatives.

4. Derive grouped deadlines from measured command budgets.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t08_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t08_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** The new plan selects the same units and commands with bounded groups and no seed race. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T09 — Bind deterministic owned execution homes

**Objective:** Bind deterministic owned execution homes.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T05, T08.

**Permitted files:** `crates/velnor-actions-orchestrator/src/cache_execution_context.rs`; `crates/velnor-actions-orchestrator/src/check_prepare.rs`; `crates/velnor-actions-mise/src/check_execution.rs`.

**Existing regressions:** Use T01 key `regressions/homes`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t09.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t09_preserves_contract`, `gc1_t09_rejects_invalid_state`.

**Steps:**

1. Register the new module through crates/velnor-actions-orchestrator/src/check_prepare.rs.

2. Resolve stable approved source and tool homes.

3. Bind target and build paths for each lane.

4. Keep private HOME lifetime separate from shared state.

5. Prevent home teardown from deleting shared directories.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t09_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t09_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Child commands read the restored homes and preserve existing cwd, task bytes, and credential scrubbing. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T10 — Restore authenticated source objects and original metadata

**Objective:** Restore authenticated source objects and original metadata.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T06, T09.

**Permitted files:** `crates/velnor-actions-orchestrator/src/cache_source_projection.rs`; `crates/velnor-actions-orchestrator/src/source_prep.rs`; `crates/velnor-actions-orchestrator/src/source_cache.rs`.

**Existing regressions:** Use T01 key `regressions/projection`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t10.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t10_preserves_contract`, `gc1_t10_rejects_invalid_state`.

**Steps:**

1. Register the new module through crates/velnor-actions-orchestrator/src/source_prep.rs.

2. Authenticate current checkout files and declared inputs.

3. Validate staged paths and safe link targets.

4. Restore original seconds and nanoseconds during authenticated extraction.

5. Restore directory metadata after its children.

6. Move unchanged restored files or subtrees into place.

7. Keep changed files and current checkout Git metadata.


**Exclude:** Do not normalize timestamps or restore checkout Git metadata. Do not follow links during metadata restoration. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t10_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t10_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Path dependencies retain real archived metadata while changed source and Git semantics remain correct. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T11 — Hydrate one verified source family

**Objective:** Hydrate one verified source family.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T10.

**Permitted files:** `crates/velnor-actions-mise/src/cache_sources.rs`; `crates/velnor-actions-mise/src/cache_transport.rs`; `crates/velnor-actions-orchestrator/src/source_cache.rs`.

**Existing regressions:** Use T01 key `regressions/sources`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-mise/tests/gc1_t11.rs`; `crates/velnor-actions-mise/tests/velnor_mise.rs`.

**Required discovered tests:** `gc1_t11_preserves_contract`, `gc1_t11_rejects_invalid_state`.

**Steps:**

1. Restore registry and Git state into the consumed Cargo home.

2. Verify covered immutable source objects locally.

3. Fetch only missing approved objects.

4. Record source origin bytes separately from cache transfers.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-mise -E 'test(gc1_t11_)' --message-format json
cargo nextest run --locked -p velnor-actions-mise -E 'test(gc1_t11_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-mise --no-tests fail
cargo clippy --locked -p velnor-actions-mise --all-targets -- -D warnings
```

**Expected result and completion:** Warm immutable sources need no origin acquisition and cold missing sources remain fetchable. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T12 — Preserve private source authorization boundaries

**Objective:** Preserve private source authorization boundaries.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T09, T10, T11.

**Permitted files:** `crates/velnor-actions-orchestrator/src/private_wiring.rs`; `crates/velnor-actions-orchestrator/src/private_fetch_session.rs`; `crates/velnor-actions-workflow-renderer/src/private_source_steps.rs`.

**Existing regressions:** Use T01 key `regressions/private_sources`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t12.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t12_preserves_contract`, `gc1_t12_rejects_invalid_state`.

**Steps:**

1. Check cache-reader access before admitting private payloads.

2. Restore approved assets at their declared stable paths.

3. Retain token mint, fetch, revoke, and scrub ordering.

4. Reject cached credentials and unauthorized private output exposure.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t12_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t12_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Private inputs remain available only to authorized readers and no credential enters any payload. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T13 — Create one tool set for each host

**Objective:** Create one tool set for each host.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T04, T09.

**Permitted files:** `crates/velnor-actions-orchestrator/src/tool_cache_pins.rs`; `crates/velnor-actions-workflow-renderer/src/cache_steps_tools_restore.rs`; `crates/velnor-actions-workflow-renderer/src/cache_p08_tool_payload.rs`.

**Existing regressions:** Use T01 key `regressions/tools_union`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_t13.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_t13_preserves_contract`, `gc1_t13_rejects_invalid_state`.

**Steps:**

1. Union existing required pinned tools for each host.

2. Remove role-only Plan, seed, and crate tool identities.

3. Keep host, ABI, component, and native SDK distinctions.

4. Disable independent automatic saves outside common policy.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t13_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t13_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
cargo clippy --locked -p velnor-actions-workflow-renderer --all-targets -- -D warnings
```

**Expected result and completion:** Compatible jobs request one host tool set without losing any existing approved component. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T14 — Reuse verified immutable tool acquisition

**Objective:** Reuse verified immutable tool acquisition.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T13.

**Permitted files:** `crates/velnor-actions-workflow-renderer/src/cache_steps_tools_installs_verify.sh`; `crates/velnor-actions-orchestrator/src/rust_toolchain_script.rs`; `crates/velnor-actions-workflow-renderer/src/cache_steps_tools_restore.rs`.

**Existing regressions:** Use T01 key `regressions/tool_integrity`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_t14.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_t14_preserves_contract`, `gc1_t14_rejects_invalid_state`.

**Steps:**

1. Reuse supported verified local tool archives or receipts.

2. Retain independent trusted checksums and version probes.

3. Fetch only absent or invalid approved components.

4. Measure origin and verification work separately.


**Exclude:** Do not trust candidate-supplied checksums or add a new installer. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t14_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t14_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
cargo clippy --locked -p velnor-actions-workflow-renderer --all-targets -- -D warnings
```

**Expected result and completion:** Warm verification does not download an unchanged covered origin archive. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T15 — Hydrate qualified tools inside private checks

**Objective:** Hydrate qualified tools inside private checks.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T09, T12, T14.

**Permitted files:** `crates/velnor-actions-orchestrator/src/check_tool_acquire.rs`; `crates/velnor-actions-orchestrator/src/check_tool_layout.rs`; `crates/velnor-actions-mise/src/qualified_acquisition.rs`.

**Existing regressions:** Use T01 key `regressions/qualified_tools`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t15.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t15_preserves_contract`, `gc1_t15_rejects_invalid_state`.

**Steps:**

1. Restore qualified installed prefixes at deterministic owned paths.

2. Reuse verified archives without repeating origin acquisition.

3. Preserve complete tool proofs and source-build identities.

4. Keep private-home teardown away from shared prefixes.


**Exclude:** Do not change consumer Mise files or trust an unverified installed prefix. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t15_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t15_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Warm private checks reuse verified tools and stable sysroots without downloading or rebuilding them. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T16 — Render the shared tool and cache homes

**Objective:** Render the shared tool and cache homes.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T14, T15.

**Permitted files:** `crates/velnor-actions-workflow-renderer/src/toolchain_env_homes.rs`; `crates/velnor-actions-workflow-renderer/src/toolchain_env.rs`; `crates/velnor-actions-workflow-renderer/src/cache_p08_runtime_prelude.rs`.

**Existing regressions:** Use T01 key `regressions/render_homes`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_t16.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_t16_preserves_contract`, `gc1_t16_rejects_invalid_state`.

**Steps:**

1. Emit deterministic owned runner paths outside the source checkout.

2. Keep the actual checkout as the execution directory.

3. Pass source, tool, build, and observer paths through one context.

4. Remove conflicting disposable-home assignments from generated wrappers.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t16_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t16_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
cargo clippy --locked -p velnor-actions-workflow-renderer --all-targets -- -D warnings
```

**Expected result and completion:** Generated wrappers consume the same verified context without changing Git status. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T17 — Implement transparent Rust compiler observation

**Objective:** Implement transparent Rust compiler observation.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T05, T09, T11.

**Permitted files:** `crates/velnor-actions-mise/src/compiler_observer.rs`; `crates/velnor-actions-mise/src/command.rs`; `crates/velnor-actions-mise/src/lib.rs`.

**Existing regressions:** Use T01 key `regressions/rust_observer`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-mise/tests/gc1_t17.rs`; `crates/velnor-actions-mise/tests/velnor_mise.rs`.

**Required discovered tests:** `gc1_t17_preserves_contract`, `gc1_t17_rejects_invalid_state`.

**Steps:**

1. Record real rustc and rustdoc start and completion events.

2. Bind each event to its recipe and package.

3. Distinguish documentation compilation, finalization, probes, and doctest descendants.

4. Preserve arguments, wrappers, signals, and exit status.

5. Support existing MBX previous-wrapper and RUSTDOC delegation.


**Exclude:** Do not implement a compiler cache or modify MBX. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-mise -E 'test(gc1_t17_)' --message-format json
cargo nextest run --locked -p velnor-actions-mise -E 'test(gc1_t17_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-mise --no-tests fail
cargo clippy --locked -p velnor-actions-mise --all-targets -- -D warnings
```

**Expected result and completion:** Controlled fixtures distinguish application and dependency work without changing compiler behavior. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T18 — Observe supported native compiler boundaries

**Objective:** Observe supported native compiler boundaries.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T17.

**Permitted files:** `crates/velnor-actions-mise/src/native_compiler_observer.rs`; `crates/velnor-actions-mise/src/compiler_observer.rs`; `crates/velnor-actions-mise/src/lib.rs`.

**Existing regressions:** Use T01 key `regressions/native_observer`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-mise/tests/gc1_t18.rs`; `crates/velnor-actions-mise/tests/velnor_mise.rs`.

**Required discovered tests:** `gc1_t18_preserves_contract`, `gc1_t18_rejects_invalid_state`.

**Steps:**

1. Wrap approved CC and CXX executables at stable paths.

2. Preserve native flags and executable selection.

3. Classify unobserved absolute compiler calls as unknown.

4. Test nested native compiler failures and cancellations.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-mise -E 'test(gc1_t18_)' --message-format json
cargo nextest run --locked -p velnor-actions-mise -E 'test(gc1_t18_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-mise --no-tests fail
cargo clippy --locked -p velnor-actions-mise --all-targets -- -D warnings
```

**Expected result and completion:** Observed native work is counted accurately and unsupported observation cannot pass as zero. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T19 — Expose child compiler and acquisition evidence

**Objective:** Expose child compiler and acquisition evidence.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T09, T11, T15, T17, T18.

**Permitted files:** `crates/velnor-actions-orchestrator/src/compiler_observation.rs`; `crates/velnor-actions-orchestrator/src/check_runtime.rs`; `crates/velnor-actions-orchestrator/src/check_prepare.rs`.

**Existing regressions:** Use T01 key `regressions/observation_reports`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t19.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t19_preserves_contract`, `gc1_t19_rejects_invalid_state`.

**Steps:**

1. Register the new module through crates/velnor-actions-orchestrator/src/check_runtime.rs.

2. Create recipe-bound observation reports before execution.

3. Collect reports after successful and failed children.

4. Keep origin, cache-transfer, and compiler counters separate.

5. Retain reports before private-home cleanup.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t19_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t19_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Successful named checks no longer hide measured child work or missing observation. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T20 — Pack complete state and safe manifests

**Objective:** Pack complete state and safe manifests.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T05, T10, T19.

**Permitted files:** `crates/velnor-actions-orchestrator/src/cache_snapshot.rs`; `crates/velnor-actions-orchestrator/src/cache_archive.rs`; `crates/velnor-actions-orchestrator/src/lib.rs`.

**Existing regressions:** Use T01 key `regressions/snapshot`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t20.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t20_preserves_contract`, `gc1_t20_rejects_invalid_state`.

**Steps:**

1. Register the new module through crates/velnor-actions-orchestrator/src/lib.rs.

2. Pack complete target and separate build directories.

3. Include the authenticated workspace input projection.

4. Record original seconds, nanoseconds, modes, and safe link identities.

5. Use existing tar, flate2, and owned archive validation.

6. Keep required rustdoc parts and generated native state.

7. Exclude designated disposable roots outside complete output trees.


**Exclude:** Do not filter opaque Cargo state or required rustdoc parts. Do not persist the separate MBX object store. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t20_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t20_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Round trips preserve required state and reject unsafe or incomplete payloads. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T21 — Measure and qualify the outer archive envelope

**Objective:** Measure and qualify the outer archive envelope.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T20.

**Permitted files:** `crates/velnor-actions-orchestrator/src/cache_archive_envelope.rs`; `crates/velnor-actions-orchestrator/src/cache_archive.rs`; `crates/velnor-actions-orchestrator/src/cache_snapshot.rs`.

**Existing regressions:** Use T01 key `regressions/envelope`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t21.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t21_preserves_contract`, `gc1_t21_rejects_invalid_state`.

**Steps:**

1. Register the new module through crates/velnor-actions-orchestrator/src/cache_archive.rs.

2. Freeze one inner payload and record its exact bytes.

3. Implement preflight packaging through the existing pinned runtime tools.

4. Represent a measured envelope and an unknown envelope separately.

5. Test measured bounds with deterministic local fixtures.

6. Require hosted measurements before publication qualification.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t21_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t21_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Local implementation passes fixtures; publication requires a separately qualified runtime envelope. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** An unknown hosted envelope blocks publication qualification. It does not block unrelated implementation or ordinary CI. Do not replace unknown measurements with zero.


### T22 — Implement repository-wide byte admission

**Objective:** Implement repository-wide byte admission.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T04, T20, T21.

**Permitted files:** `crates/velnor-actions-orchestrator/src/cache_inventory.rs`; `crates/velnor-actions-orchestrator/src/cache_admission.rs`; `crates/velnor-actions-orchestrator/src/lib.rs`.

**Existing regressions:** Use T01 key `regressions/budget`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t22.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t22_preserves_contract`, `gc1_t22_rejects_invalid_state`.

**Steps:**

1. Register the new module through crates/velnor-actions-orchestrator/src/lib.rs.

2. Paginate every repository cache ref and version.

3. Use the fixed ten-billion-byte accounting ceiling.

4. Charge overlap, pending saves, other families, and reserved uncertainty.

5. Reject unknown inventory and insufficient publication headroom.

6. Charge corrupt replacements until exact deletion is confirmed.


**Exclude:** Do not raise settings, buy capacity, or delete unrelated entries. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t22_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t22_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Admission preserves required coverage and cannot credit unconfirmed deletion. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T23 — Bind all cache families to the common contract

**Objective:** Bind all cache families to the common contract.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T04, T05, T22.

**Permitted files:** `crates/velnor-actions-contract/src/workflow/cache_family.rs`; `crates/velnor-actions-contract/src/workflow/cache_family_steps.rs`; `crates/velnor-actions-orchestrator/src/stack_family_cache.rs`.

**Existing regressions:** Use T01 key `regressions/family_catalog`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-contract/tests/gc1_t23.rs`; `crates/velnor-actions-contract/tests/velnor_contract.rs`.

**Required discovered tests:** `gc1_t23_preserves_contract`, `gc1_t23_rejects_invalid_state`.

**Steps:**

1. Replace persisted MBX with the complete-state family.

2. Use one decimal byte constant and common admission outcome.

3. Retain supported source, tool, and non-Rust payload distinctions.

4. Inventory image namespaces only when present.

5. Remove independent family quota constants.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-contract -E 'test(gc1_t23_)' --message-format json
cargo nextest run --locked -p velnor-actions-contract -E 'test(gc1_t23_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-contract --no-tests fail
cargo clippy --locked -p velnor-actions-contract --all-targets -- -D warnings
```

**Expected result and completion:** All family callers use the new policy types and one accounting ceiling. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T24 — Select exact generations and validate active intent

**Objective:** Select exact generations and validate active intent.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T06, T22.

**Permitted files:** `crates/velnor-actions-orchestrator/src/cache_discovery.rs`; `crates/velnor-actions-orchestrator/src/cache_keys.rs`; `crates/velnor-actions-orchestrator/src/cache_intent.rs`.

**Existing regressions:** Use T01 key `regressions/discovery`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t24.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t24_preserves_contract`, `gc1_t24_rejects_invalid_state`.

**Steps:**

1. Register the new module through crates/velnor-actions-orchestrator/src/cache_keys.rs.

2. Try the exact authorized requested key first.

3. Check every service-selectable exact or primary-prefix entry for scope shadow.

4. Reject ambiguous trusted provenance before action extraction.

5. Select at most one compatible retained predecessor.

6. Require returned matched-key equality after restoration.

7. Validate completed coverage after restore.

8. Recheck current desired coverage when default HEAD changes.


**Exclude:** Do not infer current intent from creation time alone. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t24_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t24_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Discovery never crosses compatibility or trust boundaries and application-only HEAD changes do not retire valid coverage. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T25 — Validate final coverage before publication

**Objective:** Validate final coverage before publication.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T08, T19, T20, T24.

**Permitted files:** `crates/velnor-actions-orchestrator/src/cache_coverage_replay.rs`; `crates/velnor-actions-orchestrator/src/crate_jobs_obligations.rs`; `crates/velnor-actions-orchestrator/src/compiler_observation.rs`.

**Existing regressions:** Use T01 key `regressions/closure_replay`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t25.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t25_preserves_contract`, `gc1_t25_rejects_invalid_state`.

**Steps:**

1. Register the new module through crates/velnor-actions-orchestrator/src/crate_jobs_obligations.rs.

2. Join all producer processes before snapshot creation.

3. Freeze the complete candidate archive and its digest.

4. Clear only owned target, build, and ephemeral MBX directories.

5. Restore the same archive at identical paths.

6. Replay exact recipes with an empty MBX store.

7. Require zero unchanged dependency compiler executions during replay.

8. Bind the separate replay proof to the frozen digest.


**Exclude:** Do not publish replay-mutated state, invent dependency-only commands, or hide repeated tests. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t25_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t25_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** The manifest and separate digest-bound replay proof establish final coverage beyond command history. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T26 — Publish immutable generations and verify remote bytes

**Objective:** Publish immutable generations and verify remote bytes.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T21, T22, T24, T25.

**Permitted files:** `crates/velnor-actions-orchestrator/src/cache_publication.rs`; `crates/velnor-actions-orchestrator/src/cache_recovery.rs`; `crates/velnor-actions-orchestrator/src/lib.rs`.

**Existing regressions:** Use T01 key `regressions/publication`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t26.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t26_preserves_contract`, `gc1_t26_rejects_invalid_state`.

**Steps:**

1. Register the new module through crates/velnor-actions-orchestrator/src/lib.rs.

2. Save only missing complete admitted family generations.

3. Publish the exact frozen bytes that passed replay.

4. Retain already usable immutable families unchanged.

5. Restore the exact saved transport into an empty local path.

6. Report denied, oversized, interrupted, corrupt, and verified outcomes separately.


**Exclude:** Do not overwrite immutable keys or delete predecessors in compiler jobs. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t26_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t26_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Publication advances only after inventory reconciliation and actual digest-checked readback. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T27 — Delete only verified superseded owned entries

**Objective:** Delete only verified superseded owned entries.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T26.

**Permitted files:** `crates/velnor-actions-orchestrator/src/cache_cleanup_policy.rs`; `crates/velnor-actions-orchestrator/src/cache_cleanup_emit.rs`; `crates/velnor-actions-orchestrator/src/cache_prune_emit.rs`.

**Existing regressions:** Use T01 key `regressions/cleanup`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t27.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t27_preserves_contract`, `gc1_t27_rejects_invalid_state`.

**Steps:**

1. Register the new module through crates/velnor-actions-orchestrator/src/cache_cleanup_emit.rs.

2. Validate replacement tuples and proposed owned cache IDs.

3. Recheck current intent and replacement presence after queue entry.

4. Delete only superseded entries within reviewed ownership.

5. Permit reviewed exact-ID removal of a reproducibly unusable replacement.

6. Retain the usable predecessor during that repair.

7. Confirm deletion before admitting a repair generation.

8. Treat missing readback as unverified, not proof of corruption.


**Exclude:** Do not delete by an unbounded prefix or treat cleanup as an atomic transaction. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t27_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t27_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Cleanup preserves active coverage, foreign entries, and the last usable generation. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T28 — Expose existing-binary cache and observer operations

**Objective:** Expose existing-binary cache and observer operations.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T17, T26, T27.

**Permitted files:** `crates/velnor-actions-cli/src/dispatch/cache.rs`; `crates/velnor-actions-cli/src/dispatch/operation.rs`; `crates/velnor-actions-cli/src/dispatch.rs`.

**Existing regressions:** Use T01 key `regressions/cli_binding`. Expand its exact files before scheduling.

**Scope exception:** A separate observer entry task owns argv-zero dispatch; this task must not expand into main.rs.

**Tests and registration:** `crates/velnor-actions-cli/tests/gc1_t28.rs`; `crates/velnor-actions-cli/tests/velnor_cli.rs`.

**Required discovered tests:** `gc1_t28_preserves_contract`, `gc1_t28_rejects_invalid_state`.

**Steps:**

1. Register the new module through crates/velnor-actions-cli/src/dispatch.rs.

2. Add typed private cache operation dispatch.

3. Bind exact request files to authorized context.

4. Delegate algorithms to their existing owning crates.

5. Reject malformed operations and arbitrary command injection.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-cli -E 'test(gc1_t28_)' --message-format json
cargo nextest run --locked -p velnor-actions-cli -E 'test(gc1_t28_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-cli --no-tests fail
cargo clippy --locked -p velnor-actions-cli --all-targets -- -D warnings
```

**Expected result and completion:** The real CLI reaches each cache lifecycle operation through a validated request. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T29 — Bind compiler adapter entry and environment

**Objective:** Bind compiler adapter entry and environment.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T17, T18, T28.

**Permitted files:** `crates/velnor-actions-cli/src/main.rs`; `crates/velnor-actions-cli/src/dispatch/compiler.rs`; `crates/velnor-actions-workflow-renderer/src/task_wrapper_declared.rs`.

**Existing regressions:** Use T01 key `regressions/observer_entry`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-cli/tests/gc1_t29.rs`; `crates/velnor-actions-cli/tests/velnor_cli.rs`.

**Required discovered tests:** `gc1_t29_preserves_contract`, `gc1_t29_rejects_invalid_state`.

**Steps:**

1. Register the new module through crates/velnor-actions-cli/src/main.rs.

2. Expose approved rustc, rustdoc, CC, and CXX observer entries through the existing binary.

3. Resolve the real compiler from the validated context.

4. Set stable wrapper paths in generated task environments.

5. Preserve Clippy and preexisting wrapper nesting.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-cli -E 'test(gc1_t29_)' --message-format json
cargo nextest run --locked -p velnor-actions-cli -E 'test(gc1_t29_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-cli --no-tests fail
cargo clippy --locked -p velnor-actions-cli --all-targets -- -D warnings
```

**Expected result and completion:** Real generated commands invoke the observer without a new external tool or driver override. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T30 — Render thin source tool and state transport

**Objective:** Render thin source tool and state transport.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T16, T20, T23, T28.

**Permitted files:** `crates/velnor-actions-workflow-renderer/src/cache_steps.rs`; `crates/velnor-actions-workflow-renderer/src/cache_steps_mbx_bundle.rs`; `crates/velnor-actions-workflow-renderer/src/cache_steps_mbx_gate.rs`.

**Existing regressions:** Use T01 key `regressions/transport_render`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_t30.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_t30_preserves_contract`, `gc1_t30_rejects_invalid_state`.

**Steps:**

1. Replace MBX bundle steps with common snapshot operations.

2. Use fixed literal cache paths and exact selected keys.

3. Do not treat inventory filtering as action ref selection.

4. Emit pinned restore and save actions only.

5. Pass policy decisions through typed outputs.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t30_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t30_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
cargo clippy --locked -p velnor-actions-workflow-renderer --all-targets -- -D warnings
```

**Expected result and completion:** Rendered YAML delegates identity, coverage, and admission to Velnor code. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T31 — Render event permissions and writer queues

**Objective:** Render event permissions and writer queues.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T08, T27, T30.

**Permitted files:** `crates/velnor-actions-contract/src/workflow/ir.rs`; `crates/velnor-actions-orchestrator/src/workflow_policy.rs`; `crates/velnor-actions-workflow-renderer/src/dispatch_cache_boundary.rs`.

**Existing regressions:** Use T01 key `regressions/authority_render`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_t31.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_t31_preserves_contract`, `gc1_t31_rejects_invalid_state`.

**Steps:**

1. Set explicit read modes for untrusted and release consumers.

2. Grant cache writes only to trusted default writers.

3. Give Actions write only to checkout-free cleanup jobs.

4. Render queue:max without nested locks or cancellation of required preparation.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t31_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t31_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
cargo clippy --locked -p velnor-actions-workflow-renderer --all-targets -- -D warnings
```

**Expected result and completion:** Generated event paths enforce cache and GitHub token capabilities independently. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T32 — Integrate static reader writer and cleanup jobs

**Objective:** Integrate static reader writer and cleanup jobs.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T08, T24, T27, T31.

**Permitted files:** `crates/velnor-actions-orchestrator/src/crate_jobs.rs`; `crates/velnor-actions-orchestrator/src/crate_jobs_build_jobs.rs`; `crates/velnor-actions-orchestrator/src/crate_jobs_stage.rs`.

**Existing regressions:** Use T01 key `regressions/combined_jobs`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t32.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t32_preserves_contract`, `gc1_t32_rejects_invalid_state`.

**Steps:**

1. Emit static per-group reader and conditional writer jobs.

2. Decide the execution branch before consumer compilation.

3. Recheck state after the writer receives its queue slot.

4. Keep optional cache failures recoverable inside a running job.

5. Report hard writer failure without inventing reader recovery.

6. Count all branches against platform limits.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t32_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t32_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Warm groups run once without preparation; cold trusted groups execute once in the writer. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T33 — Integrate exact commands into isolated group lanes

**Objective:** Integrate exact commands into isolated group lanes.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T09, T25, T29, T32.

**Permitted files:** `crates/velnor-actions-orchestrator/src/crate_jobs_steps.rs`; `crates/velnor-actions-orchestrator/src/crate_jobs_obligations.rs`; `crates/velnor-actions-rust/src/tasks.rs`.

**Existing regressions:** Use T01 key `regressions/lanes`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t33.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t33_preserves_contract`, `gc1_t33_rejects_invalid_state`.

**Steps:**

1. Keep the existing build/test, Clippy, and documentation lanes.

2. Serialize exact package commands within each writable lane.

3. Preserve every feature, profile, target, and warning flag.

4. Continue independent selected checks after a unit failure.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t33_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t33_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Each selected unit retains its command semantics and produces its own result. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T34 — Integrate unit-level Required validation

**Objective:** Integrate unit-level Required validation.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T05, T33.

**Permitted files:** `crates/velnor-actions-orchestrator/src/required_dispositions.rs`; `crates/velnor-actions-orchestrator/src/required_evidence.rs`; `crates/velnor-actions-workflow-renderer/src/required_gate.rs`.

**Existing regressions:** Use T01 key `regressions/required`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t34.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t34_preserves_contract`, `gc1_t34_rejects_invalid_state`.

**Steps:**

1. Bind reports to source, plan, job, run, and effective attempt.

2. Authenticate retained successful jobs from earlier attempts.

3. Require new ledgers for jobs that GitHub reruns.

4. Require exactly one reader or writer ledger.

5. Reject missing, duplicate, skipped, failed, and unplanned units.

6. Fail Required after hard writer failure leaves missing units.

7. Use outcome-aware aggregation when writer jobs skip.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t34_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t34_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Cache outcomes cannot hide a missing check or make Required skip. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T35 — Bind grouped ledgers through the actual final merge

**Objective:** Bind grouped ledgers through the actual final merge.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T19, T34.

**Permitted files:** `crates/velnor-actions-orchestrator/src/merge.rs`; `crates/velnor-actions-orchestrator/src/merge_checks.rs`; `crates/velnor-actions-orchestrator/src/merge_request.rs`.

**Existing regressions:** Use T01 key `regressions/required_bridge`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t35.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t35_preserves_contract`, `gc1_t35_rejects_invalid_state`.

**Steps:**

1. Extend the actual merge request with typed group ledgers.

2. Validate each effective job against authenticated execution records.

3. Preserve original run, job, and attempt identities.

4. Join selected-unit results without rewriting old report identities.

5. Carry validated observation records into the final report payload.


**Exclude:** Do not weaken exact-set Required checks or accept an older result without retained-job proof. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t35_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t35_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** The real merge entrypoint preserves every selected result and exposes source-bound observation evidence. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T36 — Carry observation evidence through existing report artifacts

**Objective:** Carry observation evidence through existing report artifacts.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T34, T35.

**Permitted files:** `crates/velnor-actions-orchestrator/src/retrieve_reports.rs`; `crates/velnor-actions-orchestrator/src/task_report.rs`; `crates/velnor-actions-workflow-renderer/src/required_gate.rs`.

**Existing regressions:** Use T01 key `regressions/report_transport`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t36.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t36_preserves_contract`, `gc1_t36_rejects_invalid_state`.

**Steps:**

1. Collect typed observations with each normal unit report.

2. Retain exact artifact and member digest bindings.

3. Include validated observation members in the existing final report artifact.

4. Preserve actual job attempts and producer source identity.

5. Keep dependency payloads out of every report artifact.


**Exclude:** Do not treat loose extracted files or producer claims as authenticated artifact evidence. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t36_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t36_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** The existing final artifact transports complete bound observations without carrying any cache payload. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T37 — Validate owned measurement evidence and effective attempts

**Objective:** Validate owned measurement evidence and effective attempts.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T05, T36.

**Permitted files:** `scripts/hosted_phase_measurement/measure_support.py`; `scripts/hosted_phase_measurement/report_events.py`; `scripts/hosted_phase_measurement/tests/test_gc1_observation.py`.

**Existing regressions:** Use T01 key `regressions/measurement_binding`. Expand its exact files before scheduling.

**Tests and registration:** `scripts/hosted_phase_measurement/tests/test_gc1_observation.py`.

**Steps:**

1. Validate owned reports through the existing final-artifact ZIP inputs.

2. Verify its API-bound size and digest before reading members.

3. Bind each member to source, run, job, and actual attempt.

4. Permit measured counters only with complete bound observation.

5. Keep unknown counters and unverified loose reports explicitly unknown.


**Exclude:** Do not change the collector CLI or infer CPU time from compiler wall time. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
python3 - <<'PY'
import unittest

suite = unittest.TestLoader().discover('scripts/hosted_phase_measurement/tests', pattern='test_*.py')
def names(node):
    for item in node:
        if isinstance(item, unittest.TestSuite):
            yield from names(item)
        else:
            yield item.id()
found = set(names(suite))
print('\n'.join(sorted(found)))
required = set(['test_gc1_observation.Gc1ObservationTests.test_rejects_unbound_zero', 'test_gc1_observation.Gc1ObservationTests.test_accepts_bound_observation'])
if not found or not required <= found:
    raise SystemExit('Missing required measurement tests')
result = unittest.TextTestRunner(verbosity=2).run(suite)
if not result.wasSuccessful():
    raise SystemExit(1)
PY
```

**Expected result and completion:** Verified measurements are accepted; unbound zeros and forged effective attempts are rejected. Obtain review before integration.

**Evidence:** Save the discovered test IDs, nonzero test count, ZIP/digest fixtures, and independent review verdict.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T38 — Integrate complete lifecycle counters into the existing collector

**Objective:** Integrate complete lifecycle counters into the existing collector.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T37.

**Permitted files:** `scripts/hosted_phase_measurement/report_counters.py`; `scripts/hosted_phase_measurement/report_builder.py`; `scripts/hosted_phase_measurement/tests/test_gc1_observation.py`.

**Existing regressions:** Use T01 key `regressions/measurement_aggregation`. Expand its exact files before scheduling.

**Tests and registration:** `scripts/hosted_phase_measurement/tests/test_gc1_observation.py`.

**Steps:**

1. Consume the verified owned observations in build_report.

2. Count each real job, attempt, and process once.

3. Include bootstrap, helpers, preparation, replay, and failed attempts.

4. Separate effective Required results from total executed lifecycle work.

5. Keep origin bytes, cache bytes, and historical MBX summaries separate.


**Exclude:** Do not double-count retained jobs or promote legacy Cargo progress lines into compiler counts. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
python3 - <<'PY'
import unittest

suite = unittest.TestLoader().discover('scripts/hosted_phase_measurement/tests', pattern='test_*.py')
def names(node):
    for item in node:
        if isinstance(item, unittest.TestSuite):
            yield from names(item)
        else:
            yield item.id()
found = set(names(suite))
print('\n'.join(sorted(found)))
required = set(['test_gc1_observation.Gc1ObservationTests.test_join_uses_effective_attempt', 'test_gc1_observation.Gc1ObservationTests.test_pipeline_includes_helpers_and_replay'])
if not found or not required <= found:
    raise SystemExit('Missing required measurement tests')
result = unittest.TextTestRunner(verbosity=2).run(suite)
if not result.wasSuccessful():
    raise SystemExit(1)
PY
```

**Expected result and completion:** The existing collector reports all actual work without converting missing observations into zero. Obtain review before integration.

**Evidence:** Save discovered test IDs, complete pipeline fixtures, measured/unknown field comparisons, and independent review verdict.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T39 — Integrate named checks with restored context

**Objective:** Integrate named checks with restored context.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T09, T15, T19, T34, T36.

**Permitted files:** `crates/velnor-actions-orchestrator/src/check_prepare.rs`; `crates/velnor-actions-mise/src/check_execution.rs`; `crates/velnor-actions-orchestrator/src/check_runtime.rs`.

**Existing regressions:** Use T01 key `regressions/named_checks`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t39.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t39_preserves_contract`, `gc1_t39_rejects_invalid_state`.

**Steps:**

1. Pass the typed group context into prepare_check.

2. Project approved restored homes into QualifiedCheck.

3. Preserve declared task bytes, cwd, and private HOME isolation.

4. Collect child reports before cleanup.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t39_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t39_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Named checks consume verified cached state and still execute their declared tasks. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T40 — Integrate preview native producers

**Objective:** Integrate preview native producers.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T07, T30, T39.

**Permitted files:** `crates/velnor-actions-orchestrator/src/preview_producer.rs`; `crates/velnor-actions-orchestrator/src/preview_production_execution.rs`; `crates/velnor-actions-orchestrator/src/native_mise_tasks.rs`.

**Existing regressions:** Use T01 key `regressions/preview`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t40.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t40_preserves_contract`, `gc1_t40_rejects_invalid_state`.

**Steps:**

1. Pass the same context through execute_preview_task.

2. Keep authenticated source and native tool identities.

3. Restore the correct production variant before execution.

4. Report cache and origin work from all native children.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t40_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t40_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Preview uses the shared lifecycle without changing products, LTO, targets, or source admission. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T41 — Integrate stable and native build callers

**Objective:** Integrate stable and native build callers.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T40.

**Permitted files:** `crates/velnor-actions-orchestrator/src/native_check_runtime/execute.rs`; `crates/velnor-actions-orchestrator/src/native_check_runtime/install.rs`; `crates/velnor-actions-workflow-renderer/src/native_check_execution.rs`.

**Existing regressions:** Use T01 key `regressions/native_release`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t41.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t41_preserves_contract`, `gc1_t41_rejects_invalid_state`.

**Steps:**

1. Use the same verified context for compiler-producing native commands.

2. Retain existing host, SDK, linker, and release profiles.

3. Separate source-free consumption from compilation.

4. Preserve intentional clean-install qualification.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t41_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t41_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Stable and native paths report real reuse while retaining every current release requirement. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T42 — Bind product release build groups

**Objective:** Bind product release build groups.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T31, T41.

**Permitted files:** `crates/velnor-actions-workflow-renderer/src/schema2_generator_release_jobs.rs`; `crates/velnor-actions-workflow-renderer/src/schema2_generator_release_workflow_steps.rs`; `crates/velnor-actions-workflow-renderer/src/schema2_generator_release_assets.rs`.

**Existing regressions:** Use T01 key `regressions/release_render`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_t42.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_t42_preserves_contract`, `gc1_t42_rejects_invalid_state`.

**Steps:**

1. Attach the shared context to actual release build jobs.

2. Bind compiler output copies to the selected target paths.

3. Keep exact release and target command arguments.

4. Prepare supported production variants on trusted default coverage growth.

5. Keep signers and publishers free of Cargo-state restoration.

6. Retain product eligibility and clean qualification jobs.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t42_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t42_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
cargo clippy --locked -p velnor-actions-workflow-renderer --all-targets -- -D warnings
```

**Expected result and completion:** Current products use the shared cache policy without adding products to CI-only repositories. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T43 — Restore the pinned controller before cache operations

**Objective:** Restore the pinned controller before cache operations.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T14, T30, T42.

**Permitted files:** `crates/velnor-actions-workflow-renderer/src/closure.rs`; `crates/velnor-actions-workflow-renderer/src/steps.rs`; `crates/velnor-actions-workflow-renderer/src/cache_bootstrap.py`.

**Existing regressions:** Use T01 key `regressions/bootstrap`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_t43.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_t43_preserves_contract`, `gc1_t43_rejects_invalid_state`.

**Steps:**

1. Include one fixed read-only bridge in the existing acquisition renderer.

2. Preserve HelperProvenance::ReleaseAsset and its independent digest contract.

3. Use the independently approved normal generator release descriptor.

4. Apply the same exact-entry and primary-prefix provenance checks.

5. Select only the expected standalone binary from restored tools.

6. Reject links, duplicate members, oversized data, and digest mismatch.

7. Verify its independent digest before execution.

8. Use existing approved acquisition on a cold miss.

9. Permit no save before the verified controller applies common admission.


**Exclude:** Do not execute cached unverified code or compile archive guard to unlock restoration. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t43_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t43_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
cargo clippy --locked -p velnor-actions-workflow-renderer --all-targets -- -D warnings
```

**Expected result and completion:** Acquire Velnor avoids a warm origin download and reaches verified cache operations without source compilation. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Block warm activation until a real approved controller release supports the cache operations. Count initial bootstrap work explicitly. Do not replace unknown measurements with zero.


### T44 — Integrate Plan and source-bound helper reuse

**Objective:** Integrate Plan and source-bound helper reuse.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T14, T29, T30, T43.

**Permitted files:** `crates/velnor-actions-orchestrator/src/workflow_jobs_cache.rs`; `crates/velnor-actions-workflow-renderer/src/preseed.rs`; `crates/velnor-actions-workflow-renderer/src/preseed_closure.rs`.

**Existing regressions:** Use T01 key `regressions/helpers`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_t44.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_t44_preserves_contract`, `gc1_t44_rejects_invalid_state`.

**Steps:**

1. Run the verified controller before building the current source candidate.

2. Restore verified pinned tools and state before helper execution.

3. Key source-bound helpers by their actual build inputs.

4. Bind PRESEED_BUILD_OUTPUT and staging copies to the context.

5. Keep changed source-candidate compilation classified as application work.

6. Remove repeated helper compilation from compatible ordinary paths.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t44_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t44_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
cargo clippy --locked -p velnor-actions-workflow-renderer --all-targets -- -D warnings
```

**Expected result and completion:** Bootstrap has no circular cache dependency and unchanged covered helpers do not rebuild. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T45 — Factor fixed image record and archive validation

**Objective:** Factor fixed image record and archive validation.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T05, T44.

**Permitted files:** `crates/velnor-actions-workflow-renderer/src/job_image_authority_record.py`; `crates/velnor-actions-workflow-renderer/src/job_image_authority_oci.py`; `crates/velnor-actions-workflow-renderer/src/job_image_authority_tar.py`.

**Existing regressions:** Use T01 key `regressions/image_validation`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_t45.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_t45_preserves_contract`, `gc1_t45_rejects_invalid_state`.

**Steps:**

1. Port existing candidate.py data validation algorithms into fixed renderer inputs.

2. Keep strict record, OCI descriptor, and safe tar checks.

3. Use only the existing Python standard library.

4. Reject candidate imports, executables, and authority fields.


**Exclude:** Do not change image products or add a new validator release dependency. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t45_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t45_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
cargo clippy --locked -p velnor-actions-workflow-renderer --all-targets -- -D warnings
```

**Expected result and completion:** Fixed validators preserve current product checks without executing candidate source. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T46 — Factor fixed image identity and publication logic

**Objective:** Factor fixed image identity and publication logic.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T45.

**Permitted files:** `crates/velnor-actions-workflow-renderer/src/job_image_authority_identity.py`; `crates/velnor-actions-workflow-renderer/src/job_image_authority_registry.py`; `crates/velnor-actions-workflow-renderer/src/job_image_authority_publish.py`.

**Existing regressions:** Use T01 key `regressions/image_publication`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_t46.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_t46_preserves_contract`, `gc1_t46_rejects_invalid_state`.

**Steps:**

1. Port existing publish.py authorization and OCI operations.

2. Read source identities through authenticated exact-SHA GitHub data.

3. Retain current CI, artifact, attempt, and attestation checks.

4. Preserve approved redirect handling and credential stripping.

5. Use existing gh and Python capabilities.


**Exclude:** Do not upload products, add a registry cache, or introduce a new OCI client. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t46_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t46_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
cargo clippy --locked -p velnor-actions-workflow-renderer --all-targets -- -D warnings
```

**Expected result and completion:** The fixed data-only code preserves current publication authorization and byte verification. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T47 — Compose one source-free image authority body

**Objective:** Compose one source-free image authority body.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T46.

**Permitted files:** `crates/velnor-actions-workflow-renderer/src/job_image_authority.rs`; `crates/velnor-actions-workflow-renderer/src/schema2_job_image_candidate.rs`; `crates/velnor-actions-orchestrator/src/image_maintenance/source.rs`.

**Existing regressions:** Use T01 key `regressions/image_body`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_t47.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_t47_preserves_contract`, `gc1_t47_rejects_invalid_state`.

**Steps:**

1. Register the new module through crates/velnor-actions-workflow-renderer/src/schema2_job_image_candidate.rs.

2. Compose the fixed validated fragments through include_str.

3. Declare the module in the existing renderer parent.

4. Reuse existing producer source evidence where sufficient.

5. Add only missing authenticated data fields to source evidence.

6. Use one body for attestation and publication modes.


**Exclude:** Do not change credential-free image build semantics or introduce new authority claims. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t47_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t47_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
cargo clippy --locked -p velnor-actions-workflow-renderer --all-targets -- -D warnings
```

**Expected result and completion:** Both authority modes consume one fixed implementation without a candidate helper or new CLI. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T48 — Remove source execution from image authority jobs

**Objective:** Remove source execution from image authority jobs.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T14, T44, T47.

**Permitted files:** `crates/velnor-actions-workflow-renderer/src/schema2_job_image_candidate.rs`; `crates/velnor-actions-workflow-renderer/src/schema2_job_image_native.rs`; `crates/velnor-actions-workflow-renderer/src/job_image_authority.rs`.

**Existing regressions:** Use T01 key `regressions/image_render`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_t48.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_t48_preserves_contract`, `gc1_t48_rejects_invalid_state`.

**Steps:**

1. Replace authority checkout and source builds with the fixed data-only body.

2. Remove authority calls to repository publish.py.

3. Bind credential-free producer output copies to the shared context.

4. Keep compiler cache access disabled in authority jobs.

5. Preserve existing image production and publication boundaries.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t48_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t48_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
cargo clippy --locked -p velnor-actions-workflow-renderer --all-targets -- -D warnings
```

**Expected result and completion:** Image attestation and publication contain no checkout-dependent compilation or candidate code execution. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Block this path if existing capabilities cannot preserve every product trust check. Do not invent a helper release. Do not replace unknown measurements with zero.


### T49 — Apply common admission to existing cache families

**Objective:** Apply common admission to existing cache families.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T22, T23, T30, T41.

**Permitted files:** `crates/velnor-actions-orchestrator/src/stack_family_cache.rs`; `crates/velnor-actions-orchestrator/src/tofu_cache.rs`; `crates/velnor-actions-workflow-renderer/src/cache_steps_family.rs`.

**Existing regressions:** Use T01 key `regressions/other_families`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t49.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t49_preserves_contract`, `gc1_t49_rejects_invalid_state`.

**Steps:**

1. Route existing supported families through common admission and reporting.

2. Preserve their current supported payload and hydration semantics.

3. Count image namespaces only when inventory proves their presence.

4. Count all foreign entries in total usage.

5. Reject publication without a justified pre-upload bound.

6. Disable independent family saves that bypass the repository policy.


**Exclude:** Do not add a new backend or cache absent consumer products. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t49_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t49_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Every supported writer uses one budget policy while unrelated entries remain untouched. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T50 — Replace unbounded qualification cache writers

**Objective:** Replace unbounded qualification cache writers.

**Repository and source:** `tailrocks/velnor-new`. A0. T01 must confirm these renderer paths before edits; use its exact owner map if a module moved.

**Prerequisites:** T31, T48, T49.

**Permitted files:** `crates/velnor-actions-workflow-renderer/src/matrix_qualification.rs`; `crates/velnor-actions-workflow-renderer/src/schema2_mbx_qualification.rs`; `crates/velnor-actions-contract/src/workflow/qualification_cache_lineage.rs`.

**Existing regressions:** Use T01 key `regressions/qualification_writers`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_t50.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_t50_preserves_contract`, `gc1_t50_rejects_invalid_state`.

**Steps:**

1. Replace run-specific qualification cache generations with bounded owned slots.

2. Use the shared snapshot lifecycle and real observation contract.

3. Remove dependency-cache artifact transfer assumptions.

4. Keep hosted-only cache qualification within the approved budget.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t50_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t50_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
cargo clippy --locked -p velnor-actions-workflow-renderer --all-targets -- -D warnings
```

**Expected result and completion:** Qualification cannot evade repository admission or rely on persistent self-hosted state. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T51 — Replace obsolete consumer cache settings

**Objective:** Replace obsolete consumer cache settings.

**Repository and source:** `tailrocks/velnor-new`. A0. The exact current config definition is established by T01 before this task starts.

**Prerequisites:** T03, T31, T49.

**Permitted files:** `crates/velnor-actions-orchestrator/src/config.rs`; `crates/velnor-actions-orchestrator/src/config_workflow.rs`; `crates/velnor-actions-contract/src/config/workflow.rs`.

**Existing regressions:** Use T01 key `regressions/config`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t51.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t51_preserves_contract`, `gc1_t51_rejects_invalid_state`.

**Steps:**

1. Define the single GitHub-only policy configuration.

2. Reject obsolete PR-write and MBX-persistence options.

3. Allow only lower operating ceilings and reviewed repair revisions.

4. Preserve unrelated execution and product configuration.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t51_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t51_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** Configuration cannot request paid overflow, legacy caching, or a larger accounting ceiling. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T52 — Complete cross-crate caller bindings

**Objective:** Complete cross-crate caller bindings.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T26, T34, T38, T42, T44, T48, T50, T51.

**Permitted files:** `crates/velnor-actions-orchestrator/src/lib.rs`; `crates/velnor-actions-contract/src/workflow_reexports.rs`; `crates/velnor-actions-workflow-renderer/src/lib.rs`.

**Existing regressions:** Use T01 key `regressions/binding`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t52.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t52_preserves_contract`, `gc1_t52_rejects_invalid_state`.

**Steps:**

1. Export only the new owned interfaces required by real callers.

2. Remove obsolete persisted-cache exports from public surfaces.

3. Check every T01 caller against the new lifecycle.

4. Record any missing caller as incomplete integration.


**Exclude:** Do not hide behavior changes inside mechanical binding edits. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t52_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t52_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** No implemented cache module remains unused and every supported caller has a recorded new path. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T53 — Complete pure cache contract regression fixtures

**Objective:** Complete pure cache contract regression fixtures.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T22, T23, T24, T52.

**Permitted files:** `crates/velnor-actions-contract/tests/gc1_contract_cases.rs`; `crates/velnor-actions-contract/tests/velnor_contract.rs`.

**Tests and registration:** `crates/velnor-actions-contract/tests/gc1_contract_cases.rs`; `crates/velnor-actions-contract/tests/velnor_contract.rs`.

**Required discovered tests:** `gc1_contract_preserves_contract`, `gc1_contract_rejects_invalid_state`.

**Steps:**

1. Add lock, feature, path, profile, toolchain, and native identity cases.

2. Reject malformed coverage, context, and publication records.

3. Keep unknown counters distinct from zero.

4. Register every test in the existing explicit root.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-contract -E 'test(gc1_contract_)' --message-format json
cargo nextest run --locked -p velnor-actions-contract -E 'test(gc1_contract_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-contract --no-tests fail
```

**Expected result and completion:** All contract cases execute and fail when their stated invariant is violated. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T54 — Complete snapshot and observer regression fixtures

**Objective:** Complete snapshot and observer regression fixtures.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T10, T19, T52.

**Permitted files:** `crates/velnor-actions-orchestrator/tests/gc1_runtime_cases.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_runtime_cases.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_runtime_preserves_contract`, `gc1_runtime_rejects_invalid_state`.

**Steps:**

1. Test fresh checkouts with unchanged workspace dependencies.

2. Test original nanoseconds, directory watchers, deleted files, and Git state.

3. Test separate build directories and private-home teardown.

4. Test rustdoc attribution, compiler escape, and missing observations.

5. Test frozen snapshot replay with empty MBX state.

6. Test all-family admission, stale intent, and bounded repair.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_runtime_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_runtime_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
```

**Expected result and completion:** Correctness fixtures reject false warm results and unsafe source restoration. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T55 — Complete event and failure workflow fixtures

**Objective:** Complete event and failure workflow fixtures.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T31, T34, T50, T52.

**Permitted files:** `crates/velnor-actions-workflow-renderer/tests/gc1_workflow_cases.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_workflow_cases.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_workflow_preserves_contract`, `gc1_workflow_rejects_invalid_state`.

**Steps:**

1. Test PR, fork, main, merge-queue, tag, preview, and release modes.

2. Test skipped producers and hard writer failures.

3. Test mixed-attempt ledgers after failed-job reruns.

4. Test exact and primary-prefix current-ref shadow against default scope.

5. Test denied saves, corrupt replacement repair, and cleanup lag.

6. Test static branching, noncolliding ledgers, and platform limits.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_workflow_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_workflow_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
```

**Expected result and completion:** Every selected unit remains required under each generated failure path. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T56 — Review cache and authority boundaries

**Objective:** Review cache and authority boundaries.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T12, T48, T54, T55.

**Permitted files:** `docs/reviews/cache-github-only-security.md`.

**Steps:**

1. Review source projection and outer archive trust.

2. Review fork visibility and private derived output.

3. Review writer, cleanup, signer, and publisher permissions.

4. Block integration on any unresolved authority finding.


**Exclude:** Do not implement fixes inside the review task. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_runtime_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_workflow_)' --no-tests fail
git diff --check
```

**Expected result and completion:** An independent security verdict covers every cache reader and writer. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T57 — Review integrated architecture and task coverage

**Objective:** Review integrated architecture and task coverage.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T01, T53, T54, T55, T56.

**Permitted files:** `docs/reviews/cache-github-only-architecture.md`; `docs/proposed/cache-github-only/caller-map.md`.

**Steps:**

1. Check all real callers against the fixed contract.

2. Review actual command and product equivalence.

3. Review budget assumptions and unsupported observation.

4. Require explicit decisions for every remaining conflict.


**Exclude:** Do not declare a measured fit or speedup before live evidence. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo fmt --all -- --check
cargo clippy --locked --workspace --all-targets -- -D warnings
cargo nextest run --locked --workspace --no-tests fail
```

**Expected result and completion:** The implementation is complete enough for controlled runtime qualification without invented policies. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T58 — Define the bounded qualification harness and run commands

**Objective:** Define the bounded qualification harness and run commands.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T54, T57.

**Permitted files:** `crates/velnor-actions-orchestrator/tests/gc1_qualification_cases.rs`; `crates/velnor-actions-orchestrator/tests/gc1_qualification_support.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`; `docs/implemented/cache-github-only-qualification.md`; `docs/proposed/cache-github-only/run-commands.json`.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_qualification_cases.rs`; `crates/velnor-actions-orchestrator/tests/gc1_qualification_support.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_aux::rejects_empty_workload`, `gc1_aux::rejects_unapproved_fault`.

**Steps:**

1. Register the gc1_qualification module in the explicit test root.

2. Create shared case assertions and local fixture support.

3. Test the harness under the separate gc1_aux prefix.

4. Require nonempty dependency work and complete observation.

5. Write exact workflow IDs, inputs, source pins, and command arrays.

6. Bind case IDs, run budgets, fault limits, and approval states.

7. Reject production cache IDs in destructive fixture operations.


**Exclude:** Do not start hosted fault runs through a unit test by default. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_aux)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_aux)' --no-tests fail
```

**Expected result and completion:** The harness defaults to local fixtures and supplies concrete approval-bound hosted command records. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T59 — Implement input and cold-to-warm qualification cases

**Objective:** Implement input and cold-to-warm qualification cases.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T58.

**Permitted files:** `crates/velnor-actions-orchestrator/tests/gc1_qualification_inputs.rs`; `crates/velnor-actions-orchestrator/tests/gc1_qualification_cases.rs`.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_qualification_inputs.rs`; `crates/velnor-actions-orchestrator/tests/gc1_qualification_cases.rs`.

**Exact discovered case set:** `gc1_qualification::c01`, `gc1_qualification::c02`, `gc1_qualification::c03`, `gc1_qualification::c04`, `gc1_qualification::c05`, `gc1_qualification::c06`. Expected count: 6.

**Steps:**

1. Implement cold and fresh-runner replay cases.

2. Implement application-only and single-dependency changes.

3. Implement feature, profile, host, compiler, and native changes.

4. Check real compiler attribution and immutable origin coverage.

5. Include the cases in the existing gc1_qualification module.

6. Record every expected case name in the discovered test list.


**Exclude:** Do not run hosted faults by default or replace real compiler evidence with Cargo progress messages. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_qualification::)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_qualification::)' --no-tests fail
```

**Expected result and completion:** The assigned local qualification scenarios execute through real owned interfaces and reject false success. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T60 — Implement event and cancellation qualification cases

**Objective:** Implement event and cancellation qualification cases.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T59.

**Permitted files:** `crates/velnor-actions-orchestrator/tests/gc1_qualification_lifecycle.rs`; `crates/velnor-actions-orchestrator/tests/gc1_qualification_cases.rs`.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_qualification_lifecycle.rs`; `crates/velnor-actions-orchestrator/tests/gc1_qualification_cases.rs`.

**Exact discovered case set:** `gc1_qualification::c01`, `gc1_qualification::c02`, `gc1_qualification::c03`, `gc1_qualification::c04`, `gc1_qualification::c05`, `gc1_qualification::c06`, `gc1_qualification::c07`, `gc1_qualification::c08`, `gc1_qualification::c09`, `gc1_qualification::c10`, `gc1_qualification::c11`, `gc1_qualification::c12`. Expected count: 12.

**Steps:**

1. Implement PR, main, preview, release, fork, queue, and tag cases.

2. Implement competing producers and three cancellation phases.

3. Implement mixed-attempt failed-job reruns.

4. Check ref shadow and exact selected-unit results.

5. Include the cases in the existing gc1_qualification module.

6. Record every expected case name in the discovered test list.


**Exclude:** Do not run hosted faults by default or replace real compiler evidence with Cargo progress messages. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_qualification::)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_qualification::)' --no-tests fail
```

**Expected result and completion:** The assigned local qualification scenarios execute through real owned interfaces and reject false success. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T61 — Implement publication and recovery qualification cases

**Objective:** Implement publication and recovery qualification cases.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T60.

**Permitted files:** `crates/velnor-actions-orchestrator/tests/gc1_qualification_failure.rs`; `crates/velnor-actions-orchestrator/tests/gc1_qualification_cases.rs`.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_qualification_failure.rs`; `crates/velnor-actions-orchestrator/tests/gc1_qualification_cases.rs`.

**Exact discovered case set:** `gc1_qualification::c01`, `gc1_qualification::c02`, `gc1_qualification::c03`, `gc1_qualification::c04`, `gc1_qualification::c05`, `gc1_qualification::c06`, `gc1_qualification::c07`, `gc1_qualification::c08`, `gc1_qualification::c09`, `gc1_qualification::c10`, `gc1_qualification::c11`, `gc1_qualification::c12`, `gc1_qualification::c13`, `gc1_qualification::c14`, `gc1_qualification::c15`, `gc1_qualification::c16`, `gc1_qualification::c17`. Expected count: 17.

**Steps:**

1. Implement skipped and hard-failed producer cases.

2. Implement successful-step save denial and damaged cache cases.

3. Implement budget overlap and good-predecessor bad-replacement repair.

4. Implement coverage growth under unchanged compatibility.

5. Include the cases in the existing gc1_qualification module.

6. Record every expected case name in the discovered test list.


**Exclude:** Do not run hosted faults by default or replace real compiler evidence with Cargo progress messages. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_qualification::)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_qualification::)' --no-tests fail
```

**Expected result and completion:** The assigned local qualification scenarios execute through real owned interfaces and reject false success. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T62 — Implement private-home release and pressure qualification cases

**Objective:** Implement private-home release and pressure qualification cases.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T61.

**Permitted files:** `crates/velnor-actions-orchestrator/tests/gc1_qualification_paths.rs`; `crates/velnor-actions-orchestrator/tests/gc1_qualification_cases.rs`.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_qualification_paths.rs`; `crates/velnor-actions-orchestrator/tests/gc1_qualification_cases.rs`.

**Exact discovered case set:** `gc1_qualification::c01`, `gc1_qualification::c02`, `gc1_qualification::c03`, `gc1_qualification::c04`, `gc1_qualification::c05`, `gc1_qualification::c06`, `gc1_qualification::c07`, `gc1_qualification::c08`, `gc1_qualification::c09`, `gc1_qualification::c10`, `gc1_qualification::c11`, `gc1_qualification::c12`, `gc1_qualification::c13`, `gc1_qualification::c14`, `gc1_qualification::c15`, `gc1_qualification::c16`, `gc1_qualification::c17`, `gc1_qualification::c18`, `gc1_qualification::c19`, `gc1_qualification::c20`, `gc1_qualification::c21`, `gc1_qualification::c22`. Expected count: 22.

**Steps:**

1. Implement private-home named and native command cases.

2. Implement every actual test, Clippy, and documentation family.

3. Implement helper reuse and source-free authority cases.

4. Implement migration overlap and other-family pressure cases.

5. Include the cases in the existing gc1_qualification module.

6. Record every expected case name in the discovered test list.


**Exclude:** Do not run hosted faults by default or replace real compiler evidence with Cargo progress messages. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_qualification::)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_qualification::)' --no-tests fail
```

**Expected result and completion:** The assigned local qualification scenarios execute through real owned interfaces and reject false success. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T63 — Run full verification before candidate integration

**Objective:** Run full verification before candidate integration.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T62.

**Permitted files:** `docs/reviews/cache-github-only-local-verification.json`.

**Steps:**

1. Run the full root verification sequence.

2. Run the separate nested-runner verification sequence.

3. Verify existing pin freshness through the required script.

4. Leave generation parity to the next candidate task.

5. Record the exact source and successful review set.


**Exclude:** Do not replace full verification with focused tests. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
VERIFY_ROOT_AND_RUNNER
```

**Expected result and completion:** All required existing gates pass before an integration commit is permitted. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T64 — Prepare the reviewed generator candidate and activation handoff

**Objective:** Prepare the reviewed generator candidate and activation handoff.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T63.

**Permitted files:** `docs/reviews/cache-github-only-candidate.json`; `.velnor/config.toml`.

**Mapped scope:** Use T01 key `tailrocks/velnor-new/generated_outputs`.

**Scope exception:** Regenerate only Velnor outputs enumerated by T01. Never hand-edit them.

**Steps:**

1. Regenerate the candidate Velnor outputs with the verified binary.

2. Run full verification after candidate regeneration.

3. Prepare the exact normal-release and activation request.

4. Require a real controller release with the new cache operations.

5. Record its independent binary digest and descriptor.

6. Record owner approval for exact candidate activation and hosted qualification.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
GENERATE_CANDIDATE
VERIFY_ROOT_AND_RUNNER
git diff --check
```

**Expected result and completion:** A reviewable candidate exists; activation does not use a fabricated release or helper pin. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Record candidate source, generator binary digest, workflow SHA, generation parity, and owner activation decision.

**Failure and blocks:** Wait for explicit owner activation of the reviewed candidate. Do not merge, publish, or dispatch automatically. Do not replace unknown measurements with zero.


### T65 — Qualify cold warm and dependency-change behavior

**Objective:** Qualify cold warm and dependency-change behavior.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T02, T64.

**Permitted files:** `docs/reviews/cache-github-only-hosted-warm.json`.

**Runtime command owner:** T58 supplies `docs/proposed/cache-github-only/run-commands.json`. Use exact approved command arrays for this repository and case set. Unknown or unapproved commands remain blocked.

**Steps:**

1. Use the approved campaign and existing hosted runner classes.

2. Execute cases 1 through 6, 17, 18, and 19.

3. Measure compiler, origin, transfer, wall, runner, and disk work.

4. Reject incomplete observation or an empty expected workload.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
QUALIFY_CASES_01_06_17_18_19
```

**Expected result and completion:** Each supported warm recipe meets exact zero-work assertions and measured performance thresholds. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Remain blocked until hosted execution and its run budget are authorized. Do not report planned runs as executed. Do not replace unknown measurements with zero.


### T66 — Qualify event authority and recovery behavior

**Objective:** Qualify event authority and recovery behavior.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T65.

**Permitted files:** `docs/reviews/cache-github-only-hosted-lifecycle.json`.

**Runtime command owner:** T58 supplies `docs/proposed/cache-github-only/run-commands.json`. Use exact approved command arrays for this repository and case set. Unknown or unapproved commands remain blocked.

**Steps:**

1. Execute approved cases 7 through 15 and 20.

2. Retain every run attempt and selected unit result.

3. Count any duplicate work across the full lifecycle.

4. Verify source-free authority jobs and restricted fork behavior.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
QUALIFY_CASES_07_15_20
```

**Expected result and completion:** Lifecycle results match GitHub visibility and preserve checks through each failure. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Use dedicated owned test entries. Actual default-branch and release-path activation needs explicit owner authorization. Do not replace unknown measurements with zero.


### T67 — Qualify capacity migration and competing families

**Objective:** Qualify capacity migration and competing families.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T02, T27, T65.

**Permitted files:** `docs/reviews/cache-github-only-hosted-capacity.json`; `docs/proposed/cache-github-only/cache-budget.json`.

**Runtime command owner:** T58 supplies `docs/proposed/cache-github-only/run-commands.json`. Use exact approved command arrays for this repository and case set. Unknown or unapproved commands remain blocked.

**Steps:**

1. Execute approved cases 16, 21, and 22.

2. Measure inner, outer, stored, overlap, and peak disk bytes.

3. Verify publication bounds and delayed cleanup accounting.

4. Reject any repository whose full working set cannot fit.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
QUALIFY_CASES_16_21_22
```

**Expected result and completion:** Each accepted group fits its complete repository model without overflow or required-coverage deletion. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Report the exact capacity conflict when a fit fails. Do not substitute external storage or paid capacity. Do not replace unknown measurements with zero.


### T68 — Remove obsolete dependency seed implementation

**Objective:** Remove obsolete dependency seed implementation.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T58, T66, T67.

**Permitted files:** `crates/velnor-actions-orchestrator/src/dependency_seed.rs`; `crates/velnor-actions-contract/src/workflow/dependency_seed.rs`; `crates/velnor-actions-orchestrator/src/workflow_jobs.rs`.

**Existing regressions:** Use T01 key `regressions/remove_seed`. Expand its exact files before scheduling.

**Tests and registration:** `crates/velnor-actions-orchestrator/tests/gc1_t68.rs`; `crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs`.

**Required discovered tests:** `gc1_t68_preserves_contract`, `gc1_t68_rejects_invalid_state`.

**Steps:**

1. Remove the redundant workspace seed path.

2. Remove obsolete seed scheduling and success assumptions.

3. Retain any still-required non-cache planning behavior.

4. Update affected regression fixtures through their registered roots.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-orchestrator -E 'test(gc1_t68_)' --message-format json
cargo nextest run --locked -p velnor-actions-orchestrator -E 'test(gc1_t68_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-orchestrator --no-tests fail
cargo clippy --locked -p velnor-actions-orchestrator --all-targets -- -D warnings
```

**Expected result and completion:** No obsolete seed can compile hidden dependency work or bypass Required. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T69 — Remove persisted MBX cache policies and rendering

**Objective:** Remove persisted MBX cache policies and rendering.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T55, T68.

**Permitted files:** `crates/velnor-actions-contract/src/workflow/cache_family_mbx.rs`; `crates/velnor-actions-workflow-renderer/src/cache_steps_mbx_scripts.rs`; `crates/velnor-actions-workflow-renderer/src/cache_steps_mbx_command.rs`.

**Mapped scope:** Use T01 key `removals/remove_mbx_store`.

**Existing regressions:** Use T01 key `regressions/remove_mbx_store`. Expand its exact files before scheduling.

**Scope exception:** Mechanical reference removals use the exact T01 removal map. Split any behavioral change into a new reviewed task.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_t69.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_t69_preserves_contract`, `gc1_t69_rejects_invalid_state`.

**Steps:**

1. Remove persistent MBX import and export generation.

2. Remove raw 384-MiB publication gates.

3. Keep only supported ephemeral driver behavior still required.

4. Remove unreachable public references through the T01 removal map.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t69_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t69_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
cargo clippy --locked -p velnor-actions-workflow-renderer --all-targets -- -D warnings
```

**Expected result and completion:** No obsolete persisted MBX path remains executable. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T70 — Remove old family elections and pruning policies

**Objective:** Remove old family elections and pruning policies.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T69.

**Permitted files:** `crates/velnor-actions-workflow-renderer/src/cache_elect.rs`; `crates/velnor-actions-workflow-renderer/src/cache_save_budget.rs`; `crates/velnor-actions-workflow-renderer/src/cache_prune.rs`; `crates/velnor-actions-mise/src/cache_trust.rs`.

**Existing regressions:** Use T01 key `regressions/remove_old_budget`. Expand its exact files before scheduling.

**Scope exception:** The fourth file removes the existing Mise save/quota bypass. Keep this mechanical policy removal in the same ordered slice.

**Tests and registration:** `crates/velnor-actions-workflow-renderer/tests/gc1_t70.rs`; `crates/velnor-actions-workflow-renderer/tests/velnor_workflow_renderer.rs`.

**Required discovered tests:** `gc1_t70_preserves_contract`, `gc1_t70_rejects_invalid_state`.

**Steps:**

1. Remove conflicting per-family save elections and byte gates.

2. Replace count-only current-ref pruning with common operations.

3. Remove run-specific permanent generation rules.

4. Verify all remaining writers use shared admission.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
cargo nextest list --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t70_)' --message-format json
cargo nextest run --locked -p velnor-actions-workflow-renderer -E 'test(gc1_t70_)' --no-tests fail
cargo nextest run --locked -p velnor-actions-workflow-renderer --no-tests fail
cargo clippy --locked -p velnor-actions-workflow-renderer --all-targets -- -D warnings
```

**Expected result and completion:** There is one cache accounting and lifecycle policy with no compatibility mode. Obtain review before integration. The required discovered tests execute. Existing registered regressions remain valid.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Save the discovered test names and executed nonzero count. Include every required name.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T71 — Publish the qualified cache contract and operations guide

**Objective:** Publish the qualified cache contract and operations guide.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T03, T70.

**Permitted files:** `docs/proposed/cache-contract.md`; `docs/proposed/cache-families.md`; `docs/implemented/cache-github-only-operations.md`.

**Steps:**

1. Record measured groups, thresholds, and actual supported cases.

2. Document recovery, repair revisions, and private-source boundaries.

3. Document explicit PR-to-main and older-release exceptions.

4. Remove claims superseded by qualified behavior.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
alint validate-config
alint check --fail-on-warning
git diff --check
```

**Expected result and completion:** Documentation separates guarantees, operational policy, and known limitations. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.


### T72 — Finalize the qualified generator and immutable consumer pin

**Objective:** Finalize the qualified generator and immutable consumer pin.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T64, T71.

**Permitted files:** `docs/reviews/cache-github-only-final-candidate.json`; `.velnor/config.toml`.

**Mapped scope:** Use T01 key `tailrocks/velnor-new/generated_outputs`.

**Scope exception:** Regenerate only outputs enumerated by T01. Do not hand-edit generated files.

**Runtime command owner:** T58 supplies `docs/proposed/cache-github-only/run-commands.json`. Use exact approved command arrays for this repository and case set. Unknown or unapproved commands remain blocked.

**Steps:**

1. Regenerate Velnor outputs after obsolete-code removal.

2. Run the full required verification sequence.

3. Review evidence continuity against the final source SHA.

4. Rerun affected approved hosted cases unless removal equivalence is proved.

5. Include final Velnor generated paths in that proof.

6. Prepare the final normal-release handoff for owner approval.

7. Record the approved immutable generator pin before consumer activation.


**Exclude:** Do not change unrelated behavior or dependencies. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
GENERATE_CANDIDATE
VERIFY_ROOT_AND_RUNNER
QUALIFY_AFFECTED_FINAL_CASES
git diff --check
```

**Expected result and completion:** The final candidate has complete verification and a real approved activation pin. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict. Record candidate source, generator binary digest, workflow SHA, generation parity, and owner activation decision. Bind final runtime evidence to the final SHA, or attach reviewed strict-removal equivalence for each retained result.

**Failure and blocks:** Stage the complete change for approval. Do not invent a release, merge, or publish automatically. Do not replace unknown measurements with zero.


### T73 — Migrate jackin-project/jackin

**Objective:** Migrate jackin-project/jackin.

**Repository and source:** `jackin-project/jackin`. Recheck audited source faa2ab6c12e3de45a76ab6b98df0c64dac7aac6e. Keep Linux checks, named checks, six native products, distinct preview/release LTO, and tap helpers.

**Prerequisites:** T66, T67, T72.

**Permitted files:** `.velnor/config.toml`.

**Mapped scope:** Use T01 key `jackin-project/jackin/generated_outputs`.

**Scope exception:** Generated output count can exceed three files. T01 enumerates the exact allowlist; regenerate only.

**Runtime command owner:** T58 supplies `docs/proposed/cache-github-only/run-commands.json`. Use exact approved command arrays for this repository and case set. Unknown or unapproved commands remain blocked.

**Steps:**

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.


**Exclude:** Do not edit Cargo or Mise semantics, add products, or delete unrelated caches. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
GENERATE_VERIFIED_CONSUMER
git diff --check
JACKIN_EXISTING_GATES
QUALIFY_REPOSITORY_MATRIX
```

**Expected result and completion:** The repository passes its real command matrix and complete capacity model with no hand-edited generated output. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Block activation when the approved pin, run authorization, native observation, or capacity proof is missing. Do not replace unknown measurements with zero.


### T74 — Migrate ChainArgos/blockchain-explorer

**Objective:** Migrate ChainArgos/blockchain-explorer.

**Repository and source:** `ChainArgos/blockchain-explorer`. Recheck audited source 4b9fc98f29705541d74e181dcc52c717c21e6075. Keep one Rust crate, GraphQL/protobuf generation, migrations, and private SQL assets.

**Prerequisites:** T66, T67, T72.

**Permitted files:** `.velnor/config.toml`.

**Mapped scope:** Use T01 key `ChainArgos/blockchain-explorer/generated_outputs`.

**Scope exception:** Generated output count can exceed three files. T01 enumerates the exact allowlist; regenerate only.

**Runtime command owner:** T58 supplies `docs/proposed/cache-github-only/run-commands.json`. Use exact approved command arrays for this repository and case set. Unknown or unapproved commands remain blocked.

**Steps:**

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.


**Exclude:** Do not edit Cargo or Mise semantics, add products, or delete unrelated caches. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
GENERATE_VERIFIED_CONSUMER
git diff --check
hk check --all
sh scripts/check-rust-toolchain-mirror.sh
QUALIFY_REPOSITORY_MATRIX
```

**Expected result and completion:** The repository passes its real command matrix and complete capacity model with no hand-edited generated output. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Block activation when the approved pin, run authorization, native observation, or capacity proof is missing. Do not replace unknown measurements with zero.


### T75 — Migrate ChainArgos/bitcoin-grpc-server

**Objective:** Migrate ChainArgos/bitcoin-grpc-server.

**Repository and source:** `ChainArgos/bitcoin-grpc-server`. Recheck audited source cd0a5bfb92538c230d1762b0ab7fafb52282fc33. Keep two Rust crates and the actual dev debug profile. Do not recreate retired publication.

**Prerequisites:** T66, T67, T72.

**Permitted files:** `.velnor/config.toml`.

**Mapped scope:** Use T01 key `ChainArgos/bitcoin-grpc-server/generated_outputs`.

**Scope exception:** Generated output count can exceed three files. T01 enumerates the exact allowlist; regenerate only.

**Runtime command owner:** T58 supplies `docs/proposed/cache-github-only/run-commands.json`. Use exact approved command arrays for this repository and case set. Unknown or unapproved commands remain blocked.

**Steps:**

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.


**Exclude:** Do not edit Cargo or Mise semantics, add products, or delete unrelated caches. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
GENERATE_VERIFIED_CONSUMER
git diff --check
hk check --all
sh scripts/check-rust-toolchain-mirror.sh
QUALIFY_REPOSITORY_MATRIX
```

**Expected result and completion:** The repository passes its real command matrix and complete capacity model with no hand-edited generated output. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Block activation when the approved pin, run authorization, native observation, or capacity proof is missing. Do not replace unknown measurements with zero.


### T76 — Migrate ChainArgos/eth-grpc-server

**Objective:** Migrate ChainArgos/eth-grpc-server.

**Repository and source:** `ChainArgos/eth-grpc-server`. Recheck audited source 4b97aa1a0cf8c15f7a2ab75435c7c6da270b2ea6. Keep two Rust crates, protobuf generation, private migration inputs, and ETH SQL.

**Prerequisites:** T66, T67, T72.

**Permitted files:** `.velnor/config.toml`.

**Mapped scope:** Use T01 key `ChainArgos/eth-grpc-server/generated_outputs`.

**Scope exception:** Generated output count can exceed three files. T01 enumerates the exact allowlist; regenerate only.

**Runtime command owner:** T58 supplies `docs/proposed/cache-github-only/run-commands.json`. Use exact approved command arrays for this repository and case set. Unknown or unapproved commands remain blocked.

**Steps:**

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.


**Exclude:** Do not edit Cargo or Mise semantics, add products, or delete unrelated caches. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
GENERATE_VERIFIED_CONSUMER
git diff --check
hk check --all
sh scripts/check-rust-toolchain-mirror.sh
QUALIFY_REPOSITORY_MATRIX
```

**Expected result and completion:** The repository passes its real command matrix and complete capacity model with no hand-edited generated output. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Block activation when the approved pin, run authorization, native observation, or capacity proof is missing. Do not replace unknown measurements with zero.


### T77 — Migrate ChainArgos/tron-grpc-server

**Objective:** Migrate ChainArgos/tron-grpc-server.

**Repository and source:** `ChainArgos/tron-grpc-server`. Recheck audited source 9143caa0321469ca6627a9feb638e20da714dcb5. Keep two Rust crates, protobuf generation, private migration inputs, and TRON SQL.

**Prerequisites:** T66, T67, T72.

**Permitted files:** `.velnor/config.toml`.

**Mapped scope:** Use T01 key `ChainArgos/tron-grpc-server/generated_outputs`.

**Scope exception:** Generated output count can exceed three files. T01 enumerates the exact allowlist; regenerate only.

**Runtime command owner:** T58 supplies `docs/proposed/cache-github-only/run-commands.json`. Use exact approved command arrays for this repository and case set. Unknown or unapproved commands remain blocked.

**Steps:**

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.


**Exclude:** Do not edit Cargo or Mise semantics, add products, or delete unrelated caches. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
GENERATE_VERIFIED_CONSUMER
git diff --check
hk check --all
sh scripts/check-rust-toolchain-mirror.sh
QUALIFY_REPOSITORY_MATRIX
```

**Expected result and completion:** The repository passes its real command matrix and complete capacity model with no hand-edited generated output. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Block activation when the approved pin, run authorization, native observation, or capacity proof is missing. Do not replace unknown measurements with zero.


### T78 — Migrate ChainArgos/bitcoin-processor-rust

**Objective:** Migrate ChainArgos/bitcoin-processor-rust.

**Repository and source:** `ChainArgos/bitcoin-processor-rust`. Recheck audited source d9115d1d42c881b23e6a5dd2f0dcd2dab5f3babd. Keep four Rust crates, approved private assets, native libraries, and integration services.

**Prerequisites:** T66, T67, T72.

**Permitted files:** `.velnor/config.toml`.

**Mapped scope:** Use T01 key `ChainArgos/bitcoin-processor-rust/generated_outputs`.

**Scope exception:** Generated output count can exceed three files. T01 enumerates the exact allowlist; regenerate only.

**Runtime command owner:** T58 supplies `docs/proposed/cache-github-only/run-commands.json`. Use exact approved command arrays for this repository and case set. Unknown or unapproved commands remain blocked.

**Steps:**

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.


**Exclude:** Do not edit Cargo or Mise semantics, add products, or delete unrelated caches. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
GENERATE_VERIFIED_CONSUMER
git diff --check
hk check --all
sh scripts/check-rust-toolchain-mirror.sh
QUALIFY_REPOSITORY_MATRIX
```

**Expected result and completion:** The repository passes its real command matrix and complete capacity model with no hand-edited generated output. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Block activation when the approved pin, run authorization, native observation, or capacity proof is missing. Do not replace unknown measurements with zero.


### T79 — Migrate ChainArgos/eth-processor-rust

**Objective:** Migrate ChainArgos/eth-processor-rust.

**Repository and source:** `ChainArgos/eth-processor-rust`. Recheck audited source c08aa7d5232e43466fcfd4fa6929ef7dec7bb76c. Keep four Rust crates, test-helpers, Redis, zstd, and private assets.

**Prerequisites:** T66, T67, T72.

**Permitted files:** `.velnor/config.toml`.

**Mapped scope:** Use T01 key `ChainArgos/eth-processor-rust/generated_outputs`.

**Scope exception:** Generated output count can exceed three files. T01 enumerates the exact allowlist; regenerate only.

**Runtime command owner:** T58 supplies `docs/proposed/cache-github-only/run-commands.json`. Use exact approved command arrays for this repository and case set. Unknown or unapproved commands remain blocked.

**Steps:**

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.


**Exclude:** Do not edit Cargo or Mise semantics, add products, or delete unrelated caches. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
GENERATE_VERIFIED_CONSUMER
git diff --check
hk check --all
sh scripts/check-rust-toolchain-mirror.sh
QUALIFY_REPOSITORY_MATRIX
```

**Expected result and completion:** The repository passes its real command matrix and complete capacity model with no hand-edited generated output. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Block activation when the approved pin, run authorization, native observation, or capacity proof is missing. Do not replace unknown measurements with zero.


### T80 — Migrate ChainArgos/tron-processor-rust

**Objective:** Migrate ChainArgos/tron-processor-rust.

**Repository and source:** `ChainArgos/tron-processor-rust`. Recheck audited source 0e2a1050b34284530047a49d9a65fff333cecaed. Keep four Rust crates, test-helpers, Redis, zstd, and private assets.

**Prerequisites:** T66, T67, T72.

**Permitted files:** `.velnor/config.toml`.

**Mapped scope:** Use T01 key `ChainArgos/tron-processor-rust/generated_outputs`.

**Scope exception:** Generated output count can exceed three files. T01 enumerates the exact allowlist; regenerate only.

**Runtime command owner:** T58 supplies `docs/proposed/cache-github-only/run-commands.json`. Use exact approved command arrays for this repository and case set. Unknown or unapproved commands remain blocked.

**Steps:**

1. Refresh the exact source and approved generator pin.

2. Regenerate only the T01 owned outputs.

3. Assert equal output from two independent generations.

4. Run existing repository gates and the applicable qualification cases.

5. Record actual occupancy and the complete selected-unit ledger.


**Exclude:** Do not edit Cargo or Mise semantics, add products, or delete unrelated caches. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
GENERATE_VERIFIED_CONSUMER
git diff --check
hk check --all
sh scripts/check-rust-toolchain-mirror.sh
QUALIFY_REPOSITORY_MATRIX
```

**Expected result and completion:** The repository passes its real command matrix and complete capacity model with no hand-edited generated output. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Block activation when the approved pin, run authorization, native observation, or capacity proof is missing. Do not replace unknown measurements with zero.


### T81 — Close fleet qualification and obsolete namespace retirement

**Objective:** Close fleet qualification and obsolete namespace retirement.

**Repository and source:** `tailrocks/velnor-new`. A0: Recheck Velnor e851b39e3bedc664f8bd6470c629e7bac36c561c and the T01 ownership map.

**Prerequisites:** T71, T72, T73, T74, T75, T76, T77, T78, T79, T80.

**Permitted files:** `docs/reviews/cache-github-only-fleet.json`; `docs/implemented/cache-github-only-operations.md`.

**Steps:**

1. Verify the nine repository evidence sets and approved activation states.

2. Retire only proven obsolete owned namespaces after replacement qualification.

3. Run the final root and nested-workspace gates.

4. Report unsatisfied cases without declaring universal cache hits.


**Exclude:** Do not change repository settings or claim completion while a required capacity or observation gate remains blocked. Do not deploy, merge, change settings, or publish products.


**Verification:**

```bash
VERIFY_ROOT_AND_RUNNER
FINAL_CONSTRAINT_REVIEW
```

**Expected result and completion:** Every supported path has accepted evidence or an explicit blocker; no obsolete writer or external-storage requirement remains. Obtain review before integration.

**Evidence:** Record the scoped diff, registered test names, command results, and independent review verdict.

**Failure and blocks:** Stop this task when a required interface or capability is missing. Continue independent ready tasks. Do not replace unknown measurements with zero.

