# FINDINGS

**Merge status: BLOCKED.**

The private-source expression guard is wrong. F1 gives the exact cause and proposed patch.

The review used three GPT-6 Astra ultra subagents.
The source head was 586bdb2be3b1d203abbdd19a09bff8b188c20cc3.
The main snapshot was 7d8d076872ff256c194e375c62f1c44cbf134d81.
The released controller source was 693f3aae14406fb7851ac70f0aee647a869b5063.

The original open worktree was unavailable.
I inspected the remote branch and a reconstructed merge.
I cannot certify the user's uncommitted resolutions.
Rust and Cargo were unavailable.
No Rust tests ran in this review.

The required authority is velnor-github-only-cache-plan/GOAL.md.
That exact file was unavailable.
The recovered ARCHITECTURE.md and CONTRACTS.md came from the earlier plan.
Their section citations remain provisional until the actual documents receive a source review.

Only F1 and F2 have checked patches.
Their applicability checks passed against the remote head and reconstructed merge.
Neither patch was applied to product files.
F3–F7 need complete integration repairs.
No safe, complete patch is supplied for those repairs.
F8 is assessment only, as requested.

Source paths below are repository-relative.
Line numbers refer to the reviewed head unless a row says main.
Probe results are local evidence.
They are not hosted qualification results.

## Candidate scores

Scores are review judgments.
Each score uses four criteria from zero to five.
The criteria are behavior, authority, production use, and verification feasibility.
Higher scores are better.
These scores do not prove implementation quality.

| Finding | Candidate | Scores | Total |
|---|---|---|---:|
| F1 | Exact owned key/value exceptions | 5/5/5/5 | 20 |
| F1 | A new typed environment model | 5/5/5/4 | 19 |
| F1 | Broad runner/env expression exceptions | 5/1/5/3 | 14 |
| F1 | Remove expression rejection | 5/0/5/3 | 13 |
| F1 | Remove homes or substitute literals | 1/3/5/2 | 11 |
| F2 | Compare explicit sibling roots | 5/5/5/5 | 20 |
| F2 | Skip the first array element | 5/4/5/3 | 17 |
| F2 | Remove overlap validation | 5/0/5/2 | 12 |
| F3 | Connect the complete owning controller | 5/5/5/5 | 20 |
| F3 | Add only a tar member filter | 2/2/5/3 | 12 |
| F3 | Change logs or trust helper tests | 0/0/0/1 | 1 |
| F4 | Connect authenticated ledgers and effective jobs | 5/5/5/5 | 20 |
| F4 | Remove only the empty-ledger return | 1/3/5/2 | 11 |
| F4 | Keep an empty-ledger exception | 0/0/5/1 | 6 |
| F5 | Complete the fixed data-only authority | 5/5/5/5 | 20 |
| F5 | Restore the source-compiling publisher | 5/0/5/4 | 14 |
| F5 | Add only one identity check | 1/2/3/2 | 8 |
| F6 | Connect final evidence and authenticated job identities | 5/5/5/5 | 20 |
| F6 | Substitute display names or remove attempt checks | 2/0/5/2 | 9 |
| F7 | Complete reader-first execution and conditional preparation | 5/5/5/5 | 20 |
| F7 | Run the reader on push with an unconditional writer | 2/1/5/3 | 11 |
| F7 | Add only !cancelled() | 2/1/5/2 | 10 |
| F7 | Add only always() | 2/0/5/2 | 9 |
| F7 | Remove the reader dependency | 2/1/5/1 | 9 |
| F7 | Upgrade only the controller | 0/5/0/1 | 6 |
| F8 | Separate code repair, qualification, release, and pin update | 5/5/5/5 | 20 |
| F8 | Ignore skipped jobs by suffix | 2/0/5/2 | 9 |
| F8 | Release the current code and update its pin | 0/5/0/2 | 7 |

The execution plan keeps only the highest-ranked design for each finding.
F8's selected repair remains outside this review.

## F1 [P1]

File: crates/velnor-actions-workflow-renderer/src/private_source_steps.rs

Lines: 83–95

Problem: The validator rejects Velnor's own toolchain-home expressions.
Every nonempty PrivateWiring block reaches this rejection.

Proof:

~~~rust
        }) || self
            .toolchain_env
            .values()
            .any(|value| value.contains("${{"))
        {
            return Err(bad("toolchain_env"));
        }
~~~

The producer creates these exact values:

~~~rust
pub const RUSTUP_HOME_EXPR: &str = "${{ runner.temp }}/velnor/rustup";
pub const CARGO_HOME_EXPR: &str = "${{ runner.temp }}/velnor/cargo";
~~~

Source: crates/velnor-actions-mise/src/runtime_paths.rs:8–9.

The complete caller chain is present:

| Boundary | Source |
|---|---|
| Build private wiring | crates/velnor-actions-orchestrator/src/workflow_build.rs:150 |
| Obtain task environment | crates/velnor-actions-orchestrator/src/private_wiring.rs:77 |
| Select runner homes | crates/velnor-actions-orchestrator/src/matrix_step.rs:98–100 |
| Retain both home keys | crates/velnor-actions-orchestrator/src/private_wiring.rs:26–36,78–81 |
| Pass the environment | crates/velnor-actions-orchestrator/src/private_wiring.rs:143–151 |
| Validate before token creation | crates/velnor-actions-workflow-renderer/src/private_source_steps.rs:112–113 |

One reported detail needs correction.
The first Rust reference is a shell reference.
It becomes a GitHub expression later.

~~~rust
*out.version_slot(*tool) = project_tool_shell_ref(*tool);
~~~

Source: crates/velnor-actions-mise/src/catalog_project.rs:74–79.
Lines 21 and 41–47 define the Rust references.
The later conversion is in crates/velnor-actions-workflow-renderer/src/project_tool_resolver_tree.rs:14–20.

The two home expressions cause the immediate error.
The selected patch also accepts the exact owned Rust expression.

Fix:

~~~diff
--- a/crates/velnor-actions-workflow-renderer/src/private_source_steps.rs
+++ b/crates/velnor-actions-workflow-renderer/src/private_source_steps.rs
@@ -87,12 +87,24 @@
                 || key.starts_with("VELNOR_")
         }) || self
             .toolchain_env
-            .values()
-            .any(|value| value.contains("${{"))
+            .iter()
+            .any(|(key, value)| value.contains("${{") && !is_toolchain_expression(key, value))
         {
             return Err(bad("toolchain_env"));
         }
         Ok(())
+    }
+}
+
+fn is_toolchain_expression(key: &str, value: &str) -> bool {
+    use velnor_actions_mise::runtime_paths::{CARGO_HOME_EXPR, RUSTUP_HOME_EXPR};
+    use velnor_actions_mise::{PinnedTool, project_tool_expression};
+
+    match key {
+        "MISE_RUSTUP_HOME" => value == RUSTUP_HOME_EXPR,
+        "MISE_CARGO_HOME" => value == CARGO_HOME_EXPR,
+        "RUSTUP_TOOLCHAIN" => value == project_tool_expression(PinnedTool::Rust),
+        _ => false,
     }
 }
 
--- a/crates/velnor-actions-orchestrator/tests/gc1_t12.rs
+++ b/crates/velnor-actions-orchestrator/tests/gc1_t12.rs
@@ -26,6 +26,8 @@
     PrivateSourcesSpec, private_source_steps,
 };
 
+mod toolchain_expressions;
+
 fn fail(message: &str) -> Box<dyn Error> {
     io::Error::other(message).into()
 }
@@ -279,6 +281,7 @@
     check_triple_ordering()?;
     check_mint_carries_no_credential()?;
     check_fetch_and_revoke_token_binding()?;
+    toolchain_expressions::check_generated_toolchain_expressions()?;
     check_allowlist_gates_payload()?;
     check_approved_assets_restore_at_stable_paths()?;
     Ok(())
@@ -378,6 +381,7 @@
 #[test]
 fn gc1_t12_rejects_invalid_state() -> Result<(), Box<dyn Error>> {
     check_rejects_unauthorized_payloads()?;
+    toolchain_expressions::check_rejects_unowned_toolchain_expressions()?;
     check_rejects_unapproved_or_tampered_assets()?;
     Ok(())
 }
--- /dev/null
+++ b/crates/velnor-actions-orchestrator/tests/gc1_t12/toolchain_expressions.rs
@@ -0,0 +1,68 @@
+// SPDX-FileCopyrightText: 2026 Alexey Zhokhov
+// SPDX-License-Identifier: Apache-2.0
+
+use std::error::Error;
+
+use velnor_actions_contract::{PRIVATE_FETCH_TOKEN_ENV, PRIVATE_TOKEN_OUTPUT_EXPR, StepKind};
+use velnor_actions_mise::{PinnedTool, ToolHomes, project_tool_expression, project_tool_shell_ref};
+
+use super::{fail, reject_parts, render, valid_parts};
+
+pub(super) fn check_generated_toolchain_expressions() -> Result<(), Box<dyn Error>> {
+    let homes = ToolHomes::runner_temp();
+    for toolchain in [
+        project_tool_shell_ref(PinnedTool::Rust),
+        project_tool_expression(PinnedTool::Rust),
+    ] {
+        let mut parts = valid_parts();
+        parts.toolchain.extend([
+            ("MISE_RUSTUP_HOME".to_owned(), homes.rustup_home().to_owned()),
+            ("MISE_CARGO_HOME".to_owned(), homes.cargo_home().to_owned()),
+            ("RUSTUP_TOOLCHAIN".to_owned(), toolchain),
+        ]);
+        let steps = render(&parts, &["cargo", "release-assets"])?;
+        let StepKind::Internal { env, .. } = &steps[1].kind else {
+            return Err(fail("generated private fetch step kind drifted"));
+        };
+        for (key, value) in &parts.toolchain {
+            if env.get(key) != Some(value) {
+                return Err(fail("generated private fetch toolchain changed"));
+            }
+        }
+        if env.get(PRIVATE_FETCH_TOKEN_ENV).map(String::as_str) != Some(PRIVATE_TOKEN_OUTPUT_EXPR)
+        {
+            return Err(fail("generated private fetch token binding changed"));
+        }
+    }
+    Ok(())
+}
+
+pub(super) fn check_rejects_unowned_toolchain_expressions() -> Result<(), Box<dyn Error>> {
+    for (key, value) in [
+        ("MISE_CARGO_HOME", "${{ runner.temp }}/velnor/rustup"),
+        ("MISE_RUSTUP_HOME", "${{ runner.temp }}/velnor/cargo"),
+        ("RUSTUP_HOME", "${{ runner.temp }}/velnor/rustup"),
+        ("CARGO_HOME", "${{ runner.temp }}/velnor/cargo"),
+        ("MISE_NO_CONFIG", "${{ env.VELNOR_TOOL_RUST }}"),
+        ("MISE_RUSTUP_HOME", "${{ runner.temp }}/velnor/rustup/extra"),
+        ("RUSTUP_TOOLCHAIN", "${{ env.VELNOR_TOOL_RUST }}-nightly"),
+        ("MISE_RUSTUP_HOME", "${{ secrets.FIXTURE_APP_PRIVATE_KEY }}"),
+        ("MISE_RUSTUP_HOME", "${{ secrets['FIXTURE_APP_PRIVATE_KEY'] }}"),
+        ("RUSTUP_TOOLCHAIN", "${{ github.token }}"),
+        ("RUSTUP_TOOLCHAIN", "${{ github['token'] }}"),
+        ("MISE_CARGO_HOME", "${{ steps.deps-token.outputs.token }}"),
+        (
+            "MISE_CARGO_HOME",
+            "${{ steps['deps-token']['outputs']['token'] }}",
+        ),
+        (
+            "MISE_CARGO_HOME",
+            "${{ runner.temp }}/velnor/cargo${{ secrets.KEY }}",
+        ),
+    ] {
+        let mut parts = valid_parts();
+        parts.toolchain.insert(key.to_owned(), value.to_owned());
+        reject_parts("unowned toolchain expression", &parts, &["cargo"])?;
+    }
+    Ok(())
+}
~~~

This patch includes the reviewed regression helpers.
It preserves the existing twelve tests.
It retains every credential-key rejection.
It rejects mixed, indexed, secret, token, suffix, and cross-key expressions.

Contract: ARCHITECTURE.md §10, lines 448–450.
CONTRACTS.md §2, lines 76–89, preserves secret exclusion.
CONTRACTS.md §4, lines 198–202, preserves trusted homes.

Verify:

~~~bash
CARGO_TARGET_DIR=/tmp/velnor-pr407-review-586bdb2-target cargo nextest run --locked -p velnor-actions-orchestrator --test workflow_configuration_public -E 'test(bun_assets_routing::) | test(bun_private_credentials::) | test(bun_private_credentials_boundaries::)' --no-tests fail
~~~

Expected after the fix: exit 0; 12 passed; 0 failed.
This result remains pending.

## Merge resolution review

The reconstructed merge has eleven conflicted paths.
The conflict list is in evidence/merge-tree.txt:2–34.
It does not contain the user's resolutions.

| Resolution | Assessment | Exact source |
|---|---|---|
| Retain both renderer test targets | Correct, if both blocks remain registered | Main and branch crates/velnor-actions-workflow-renderer/Cargo.toml:36–38 |
| Regenerate .github in place | Correct method; current bytes remain unverified | .github/AGENTS.md:4–6,12–16 |
| Recapture goldens | Conditional; equality does not prove behavior | scripts/capture-opentofu-goldens.sh:6–18,398–415 |
| Set bun_lane_plan to None | Correct for this empty-task fixture | crates/velnor-actions-workflow-renderer/tests/gc1_t41.rs:104–120; main crates/velnor-actions-workflow-renderer/src/render_context.rs:43–59 |

The conflicted manifest is the renderer manifest.
It is not the workspace Cargo.toml.
The merged renderer manifest needs both exact blocks:

~~~toml
[[test]]
name = "velnor_workflow_renderer"
path = "tests/velnor_workflow_renderer.rs"

[[test]]
name = "generator_release_prepare_public"
path = "tests/generator_release_prepare_public.rs"
~~~

The renderer disables automatic test discovery:

~~~toml
autotests = false
~~~

Source: crates/velnor-actions-workflow-renderer/Cargo.toml:10.
Deleting either block would remove an explicit test target.

The fixture has no workflow tasks:

~~~rust
        workflow_tasks: Vec::new(),
~~~

Source: crates/velnor-actions-workflow-renderer/tests/gc1_t41.rs:115.

Main adds this field:

~~~rust
    pub bun_lane_plan: Option<BunLanePlan>,
~~~

Source: main crates/velnor-actions-workflow-renderer/src/render_context.rs:55.

Therefore, bun_lane_plan: None preserves this fixture's meaning.

The eleven conflict paths need these treatments:

| Exact path | Required treatment |
|---|---|
| crates/velnor-actions-workflow-renderer/Cargo.toml | Retain both test blocks |
| .github/velnor/task-execution-manifest-v1.json | Regenerate from the corrected generator |
| docs/proposed/opentofu-goldens/MANIFEST.sha256 | Recapture after semantic checks |
| docs/proposed/opentofu-goldens/cases/dogfood/plan.txt | Recapture after semantic checks |
| docs/proposed/opentofu-goldens/cases/dogfood/preview/.github/velnor/task-execution-manifest-v1.json | Recapture after semantic checks |
| docs/proposed/opentofu-goldens/cases/dogfood/tree.sha256 | Recapture after semantic checks |
| docs/proposed/opentofu-goldens/cases/empty-suite/tree.sha256 | Recapture after semantic checks |
| docs/proposed/opentofu-goldens/cases/mbx-nextest/preview/.github/workflows/ci.yml | Recapture after semantic checks |
| docs/proposed/opentofu-goldens/cases/mbx-nextest/tree.sha256 | Recapture after semantic checks |
| docs/proposed/opentofu-goldens/cases/minimal-cargo/tree.sha256 | Recapture after semantic checks |
| docs/proposed/opentofu-goldens/cases/nested/tree.sha256 | Recapture after semantic checks |

The golden script covers Rust fixtures.
Its fixture list excludes these Bun credential cases.
Thus, ALL GOLDENS MATCH does not refute F1.
Source: scripts/capture-opentofu-goldens.sh:6–12,79,415.

## All twelve reported failures

The paths below start with crates/velnor-actions-orchestrator/tests/workflow_configuration_public/.
These test sources came from main 7d8d076872.
Their same contents occur in the reconstructed merge.

| File and lines | Exact test name | Root cause |
|---|---|---|
| bun_assets_routing.rs:20,124 | schema2_bun_both_routes_private_asset_handoffs_once | F1 stops preparation |
| bun_assets_routing.rs:25,124 | schema2_bun_scale_set_routes_private_asset_handoffs_once | F1 stops preparation |
| bun_private_credentials.rs:23,212 | private_asset_app_key_minting_stays_on_hosted_producer | F1 stops preparation |
| bun_private_credentials_boundaries.rs:23,31 | mixed_default_and_member_overrides_keep_private_producers_hosted | F1 stops preparation |
| bun_private_credentials_boundaries.rs:61,68–75 | explicit_local_private_asset_producer_override_is_rejected | F1 returns the wrong error |
| bun_private_credentials_boundaries.rs:80,82 | renderer_rejects_missing_member_asset_import | F1 prevents the mutation |
| bun_private_credentials_boundaries.rs:104,106 | renderer_rejects_member_without_its_asset_producer_dependency | F1 prevents the mutation |
| bun_private_credentials_boundaries.rs:124,126 | renderer_rejects_conditionally_skipped_member_asset_import | F1 prevents the mutation |
| bun_private_credentials_boundaries.rs:153,155 | renderer_rejects_conditionally_skipped_member_asset_prepare | F1 prevents the mutation |
| bun_private_credentials_boundaries.rs:174,176 | renderer_rejects_conditionally_skipped_member_asset_download | F1 prevents the mutation |
| bun_private_credentials_boundaries.rs:196,198 | renderer_rejects_registry_install_before_member_asset_handoff | F1 prevents the mutation |
| bun_private_credentials_boundaries.rs:234,236 | renderer_rejects_unrecognized_setup_before_member_asset_handoff | F1 prevents the mutation |

The local-producer test requires these exact reasons:

~~~rust
    assert!(error.contains("execution.overrides.bun-fixture-web--assets.profile"));
    assert!(error.contains("bun_private_assets_hosted_only"));
~~~

Source: main bun_private_credentials_boundaries.rs:74–75, under the path prefix above.

The other negative tests first require successful preparation:

~~~rust
    let mut prepared = prepare(repo.path())?;
~~~

Source: main bun_private_credentials_boundaries.rs:82,106,126,155,176,198,236.

The branch's earlier fixture uses a literal home:

~~~rust
("MISE_RUSTUP_HOME".to_owned(), "/owned/rustup".to_owned())
~~~

Source: crates/velnor-actions-orchestrator/tests/gc1_t12.rs:42–53.
That fixture missed the real producer values.

Keep all twelve assertions.
Do not replace their expected errors with the new construction error.
ARCHITECTURE.md §10, line 450, requires the existing credential boundaries.

## Credential and token review

The selected F1 patch preserves the following source behavior.
This is a source review, not a live token test.

| Boundary | Exact code | Source |
|---|---|---|
| Read-only token | ("permission-contents".to_owned(), "read".to_owned()) | crates/velnor-actions-workflow-renderer/src/private_source_steps.rs:133 |
| Literal repository list | ("repositories".to_owned(), spec.repositories.join(",")) | crates/velnor-actions-workflow-renderer/src/private_source_steps.rs:132 |
| Automatic revocation remains enabled | ("skip-token-revoke".to_owned(), "false".to_owned()) | crates/velnor-actions-workflow-renderer/src/private_source_steps.rs:134 |
| Fetch receives the owned token expression | PRIVATE_TOKEN_OUTPUT_EXPR.to_owned() | crates/velnor-actions-workflow-renderer/src/private_source_steps.rs:149–153 |
| Explicit revoke runs after a successful mint | "always() && steps.deps-token.outcome == 'success'" | crates/velnor-actions-workflow-renderer/src/private_source_steps.rs:22,170–176 |
| Exact token bindings remain required | if value != expected { | crates/velnor-actions-workflow-renderer/src/support_private_tokens.rs:63–89 |
| Fetch rechecks the allowlist | if expected != request.repositories { | crates/velnor-actions-orchestrator/src/private_fetch.rs:132–142 |
| Token files use private permissions | std::os::unix::fs::OpenOptionsExt::mode(&mut options, 0o600); | crates/velnor-actions-orchestrator/src/private_fetch_session.rs:128–146 |
| Child environments are cleared | command.env_clear(); | crates/velnor-actions-mise/src/command_env.rs:150–160; crates/velnor-actions-mise/src/command.rs:293–299 |
| Revoke requires a rejected token probe | 401 => return Ok(()), | crates/velnor-actions-orchestrator/src/private_revoke.rs:34–63 |
| Bun install disables lifecycle scripts | "--ignore-scripts" | crates/velnor-actions-orchestrator/src/bun_registry_install.rs:144–149 |

No new credential exception is needed.
The expression fix changes only three exact nonsecret key/value pairs.
Contract: ARCHITECTURE.md §10, lines 448–451.

## F2 [P1]

File: crates/velnor-actions-orchestrator/src/cache_execution_context.rs

Lines: 28–36,45–53,65–86

Problem: The overlap check compares the owner directory with its own children.
This branch runtime rejects every otherwise valid named check before execution.

Proof:

~~~rust
            self.owned_root.as_path(),
            self.transport_root.as_path(),
~~~

~~~rust
        transport_root: owned_root.join(TRANSPORT_DIR),
~~~

~~~rust
    for (index, first) in all.iter().enumerate() {
        for second in &all[index + 1..] {
            if first == second || first.starts_with(second) || second.starts_with(first) {
                return Err(internal("execution_roots_overlap"));
~~~

The first pair always has the parent/child relationship.
The caller returns this error before materialization.
Source: crates/velnor-actions-orchestrator/src/check_prepare.rs:120–137.

Fix:

~~~diff
--- a/crates/velnor-actions-orchestrator/src/cache_execution_context.rs
+++ b/crates/velnor-actions-orchestrator/src/cache_execution_context.rs
@@ -69,8 +69,16 @@
             return Err(internal("execution_root_inside_checkout"));
         }
     }
-    for (index, first) in all.iter().enumerate() {
-        for second in &all[index + 1..] {
+    let disjoint_roots = [
+        roots.transport_root.as_path(),
+        roots.source_root.as_path(),
+        roots.tool_root.as_path(),
+        roots.cargo_home.as_path(),
+        roots.rustup_home.as_path(),
+        roots.observation_root.as_path(),
+    ];
+    for (index, first) in disjoint_roots.iter().enumerate() {
+        for second in &disjoint_roots[index + 1..] {
             if first == second || first.starts_with(second) || second.starts_with(first) {
                 return Err(internal("execution_roots_overlap"));
             }
~~~

All roots remain subject to checkout exclusion.
Private HOME remains separate from all shared roots.
Only the sibling comparison changes.

Contract: CONTRACTS.md §4, lines 183–202.
ARCHITECTURE.md §4, lines 130–148, defines adjacent owned roots.

Verify:

~~~bash
git apply --check /workspace/scratch/226f2776372f/pr407-review-notes/cache-placement-proposed.patch
~~~

Observed result: exit 0; no output.
This verifies applicability only.
A public named-check regression remains required before acceptance.
No Rust behavior test ran here.

## F3 [P0]

File: crates/velnor-actions-workflow-renderer/src/cache_steps_mbx_bundle.rs

Lines: 133–145,154–182,254–262

Problem: The active restore bypasses the new provenance and extraction checks.
A state archive can overwrite the adjacent tools family.

Proof:

~~~rust
        "rm -rf \"$root\"".to_owned(),
        "mkdir -p \"$parent\"".to_owned(),
        "if tar -xzf \"$payload\" -C \"$parent\"; then if [ -d \"$root\" ] && [ ! -L \"$root\" ]; then printf '%s\\n' 'velnor: state snapshot recovered'; else printf '%s\\n' '::warning::cache_corrupt: state payload missed the state root; building cold'; rm -rf \"$root\"; rm -f \"$payload\"; fi; else printf '%s\\n' '::warning::cache_corrupt: state payload unreadable; building cold'; rm -rf \"$root\"; rm -f \"$payload\"; fi".to_owned(),
~~~

The generated command is in .github/workflows/ci.yml:330–332.
Its extraction parent is $RUNNER_TEMP/velnor-gc1.
The check only requires a nonsymlink state directory afterward.

I executed that exact generated command.
The archive contained state/ordinary.o and tools/sentinel.
The command overwrote tools/sentinel.
It printed state snapshot recovered.
It exited 0.

Evidence: evidence/cache-restore-reproduction.json:14–26.
The proof requires a selected malformed or malicious payload.
No real cache poisoning was demonstrated.
No real GitHub cache was changed.

The publication path has the same missing integration.
It prints published before the save action runs:

~~~rust
        "printf 'velnor: state snapshot published (%s bytes)\\n' \"$size\"".to_owned(),
~~~

Source: crates/velnor-actions-workflow-renderer/src/cache_steps_mbx_bundle.rs:262.

The new CLI publication operation only validates supplied admission data:

~~~rust
        AdmissionDecision::Admitted => ExitCode::SUCCESS,
~~~

Source: crates/velnor-actions-cli/src/dispatch/cache.rs:240–251.

The recover and cleanup operations also return success after local validation.
They do not perform their named remote operations.
Source: crates/velnor-actions-cli/src/dispatch/cache.rs:254–279.

Fix: BLOCKED. No complete, reviewed patch exists for this integration repair.

~~~text
none
~~~

The selected repair must replace the active shell path.
It must connect discovery, provenance, safe extraction, replay, admission, publication, and exact readback.
It must remove the old key/import/export route.
A successful validation-only CLI exit cannot serve as publication proof.

Contract: CONTRACTS.md §§6–9.
ARCHITECTURE.md §8 defines verified publication.
ARCHITECTURE.md §10, lines 455–459, requires safe extraction and trusted writers.

Verify:

~~~bash
python3 /workspace/scratch/226f2776372f/pr407-review-notes/reproduce-cache-restore.py /workspace/scratch/226f2776372f/pr407-review
~~~

Observed result: exit 1.
Exact final output:

~~~text
FAIL: state-family extraction changed the tools family
~~~

This command proves the current defect.
It is not an acceptance test for the missing controller integration.

## F4 [P1]

File: crates/velnor-actions-orchestrator/src/merge_checks/ledgers.rs

Lines: 18–20,47–64

Problem: Normal Required requests bypass group-ledger checks.
Submitted ledgers also lack authenticated effective-job bindings.

Proof:

~~~rust
    if request.group_ledgers.is_empty() {
        return;
    }
~~~

The request type supplies an empty default:

~~~rust
    #[serde(default)]
    pub(crate) group_ledgers: Vec<serde_json::Value>,
~~~

Source: crates/velnor-actions-orchestrator/src/merge.rs:59–60.

Normal request assembly omits this field.
Its JSON ends with:

~~~rust
        "check_proofs": check_proofs,
        "required_job_ids": inventory,
        "required_jobs": jobs,
        "assembly_errors": errors,
~~~

Source: crates/velnor-actions-orchestrator/src/merge_request.rs:70–84.

Even supplied ledgers compare their run identity with one another:

~~~rust
            None => run_identity = Some((ledger.job.run_id, ledger.job.run_attempt)),
            Some(identity) => {
                if identity != (ledger.job.run_id, ledger.job.run_attempt) {
~~~

Source: crates/velnor-actions-orchestrator/src/merge_checks/ledgers.rs:57–64.

This does not bind them to authenticated GitHub jobs.
It also cannot accept mixed effective attempts through this rule.

Fix: BLOCKED. No complete, reviewed patch exists for this integration repair.

~~~text
none
~~~

The selected repair must connect terminal ledger creation, artifact collection, and authenticated effective-job resolution.
Required must validate one complete selected reader-or-writer ledger.
The validator must reject missing, duplicate, foreign, stale, or incomplete evidence.
Earlier results need proof that GitHub retained their actual jobs.

Contract: CONTRACTS.md §5, lines 270–281.
The deciding rule is exact:

~~~text
Require exactly one complete reader-or-writer ledger for each effective group execution.
~~~

Verify:

~~~bash
rg -n 'UnitLedgerV1|EffectiveJobBindingV1|group_ledgers' crates/*/src
~~~

Expected on the reviewed head: definitions, exports, and the optional ledger consumer.
There is no production effective-job resolver.
Normal assembly has no group_ledgers field.
This is source evidence, not an executed Required-verdict test.
I did not demonstrate a false-green Required result.

## F5 [P0]

File: crates/velnor-actions-workflow-renderer/src/job_image_authority.rs

Lines: 106–157

Problem: The image publisher reports PASS without publishing or checking remote bytes.
It can relabel unchanged candidate bytes with another source SHA.

Proof:

~~~python
identity = {
    "source": os.environ["VELNOR_IDENTITY_SOURCE"],
    "workflow_ref": os.environ["VELNOR_WORKFLOW_REF"],
    "run_id": int(os.environ["VELNOR_RUN_ID"]),
    "run_attempt": int(os.environ["VELNOR_RUN_ATTEMPT"]),
    "artifact_id": int(os.environ["VELNOR_ARTIFACT_ID"]),
}
ci = {
    "run_id": int(os.environ["VELNOR_RUN_ID"]),
    "run_attempt": int(os.environ["VELNOR_RUN_ATTEMPT"]),
}
~~~

The evidence helper then emits:

~~~python
        "status": "PASS",
        "package": PACKAGE,
        "digest_reference": f"{PACKAGE}@{oci['platform_manifest_digest']}",
~~~

Source: crates/velnor-actions-workflow-renderer/src/job_image_authority_publish.py:147–151.

The production publish job calls this exact body:

~~~rust
        authority::materialize_step(),
        authority::assemble_evidence_step(&archive, &record, result, artifact_id),
        publication_evidence_upload_step("${{ runner.temp }}/job-image-publication.json"),
~~~

Source: crates/velnor-actions-workflow-renderer/src/schema2_job_image_candidate.rs:179–184.

The exact program passed both local probes:

| Candidate source | Environment source | Exit | Evidence source | Evidence status |
|---|---|---:|---|---|
| Forty 1 characters | Forty 1 characters | 0 | Forty 1 characters | PASS |
| Forty 1 characters | Forty 2 characters | 0 | Forty 2 characters | PASS |

The candidate and archive bytes were unchanged.
Calibrated network and subprocess guards recorded no attempted calls.
Evidence: evidence/image-authority-probe/summary.json:20–26,28–108.

The new attest path has a related gap.
It checks local archive agreement before signing.
It does not establish the complete source and workflow authority.
Sources: crates/velnor-actions-workflow-renderer/src/job_image_authority.rs:71–90; crates/velnor-actions-workflow-renderer/src/schema2_job_image_candidate.rs:139–144,161–167.

Fix: BLOCKED. No complete, reviewed patch exists for this authority repair.

~~~text
none
~~~

The selected repair must complete the fixed data-only authority.
It must preserve current-main, CI, source, artifact, attempt, attestation, upload, and readback checks.
It must not restore application compilation in authority jobs.

Contract: ARCHITECTURE.md §10, lines 461–477.
Line 470 requires the complete existing authority and publication checks.
CONTRACTS.md §13 requires authenticated source and product identities.

Verify:

~~~bash
python3 /workspace/scratch/226f2776372f/pr407-review-notes/image_authority_probe.py
~~~

Observed result: exit 0.
Both result records contain "evidence_status": "PASS".
The second record contains a mismatched candidate source.
Both program_blocked_events arrays are empty.
This result proves the defect.
It does not qualify a repaired publisher.

## F6 [P1]

File: scripts/hosted_phase_measurement/report_events.py

Lines: 23–29

Problem: The collector joins workflow job IDs against display names.
Its earlier validator also rejects retained jobs from earlier attempts.

Proof:

~~~python
        name = job.get("name")
        attempt = job.get("run_attempt")
~~~

~~~python
        key = (name, attempt)
~~~

The producer binds a workflow job ID:

~~~rust
        producer_job: entry.job_id.clone(),
~~~

Source: crates/velnor-actions-orchestrator/src/task_report/observation.rs:270–276.

The generated job ID and name differ:

~~~yaml
  rust-velnor-actions-actionlint-write:
    name: Rust / velnor-actions-actionlint (write)
~~~

Source: .github/workflows/ci.yml:802–803.

The earlier attempt check is exact:

~~~python
        if job.get("run_id") != run_id or job.get("run_attempt") != attempt or job.get("head_sha") != sha:
            fail(f"job {job.get('id')} belongs to a different run/attempt/source")
~~~

Source: scripts/hosted_phase_measurement/measure_support.py:201–202.
The public collector calls it before lifecycle joining.
Source: scripts/hosted_phase_measurement/report_builder.py:82,93.

The final artifact also omits separate observation members:

~~~yaml
          path: ${{ runner.temp }}/velnor/r${{ github.run_id }}-a${{ env.VELNOR_RUN_KEY_ATTEMPT }}/final-report.json
~~~

Source: .github/workflows/ci.yml:714.
The collector searches for observation members in that ZIP.
Source: scripts/hosted_phase_measurement/report_builder.py:69–76.

Fix: BLOCKED. No complete, reviewed patch exists for this evidence repair.

~~~text
none
~~~

The selected repair must connect the final observation envelope and authenticated effective-job identities.
It must preserve actual attempt numbers.
It must not convert missing measurements to zero.
It must not weaken artifact or source validation.

Contract: CONTRACTS.md §5, lines 274–310.
ARCHITECTURE.md §11 requires complete lifecycle measurement.

Verify:

~~~bash
python3 /workspace/scratch/226f2776372f/pr407-review-notes/measurement-probe/probe.py
~~~

Observed collector exits: control 0; display-name case 2; retained-attempt case 2; copied-display-name case 2.
The probes use synthetic API files.
They do not prove live GitHub retention authority.
Evidence: evidence/measurement-probe/results.json.

## F7 [P1]

File: crates/velnor-actions-orchestrator/src/crate_jobs_stage.rs

Lines: 97–99,149–184

Problem: Push events skip the reader that each writer requires.
GitHub then skips the writer before its controller starts.

Proof:

~~~rust
pub(crate) const TRUSTED_WRITER_EVENT_GATE: &str = "github.event_name == 'push'";

pub(crate) const UNTRUSTED_READER_EVENT_GATE: &str = "github.event_name != 'push'";
~~~

The writer always requires its reader:

~~~rust
    needs.insert(reader_id.to_owned());
~~~

Source: crates/velnor-actions-orchestrator/src/crate_jobs_stage.rs:183.

The generated reader condition is exact:

~~~yaml
    if: (!contains(needs.plan.outputs.not_affected_jobs, ',rust-velnor-actions-actionlint,')) && github.event_name != 'push'
~~~

Source: .github/workflows/ci.yml:748.

The generated writer has this dependency and condition:

~~~yaml
    needs:
      - plan
      - rust-velnor-actions-actionlint-read
    if: (!contains(needs.plan.outputs.not_affected_jobs, ',rust-velnor-actions-actionlint,')) && github.event_name == 'push'
~~~

Source: .github/workflows/ci.yml:807–810.

GitHub adds success() when a condition has no status function.
A skipped required job therefore prevents this writer from running.
This conclusion follows the documented rule.
No hosted scheduling test ran.

Official sources, checked on 2026-10-27:

- [Workflow syntax, jobs.needs](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idneeds).
- [Expressions, status check functions](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions#status-check-functions).

The runner source confirms the default:

~~~csharp
            return hasStatusFunction ? condition : $"{PipelineTemplateConstants.Success}() && ({condition})";
~~~

Source: actions/runner at 80ca6ea6c936dc9532d0d86625f862585e800f75.
File: src/Sdk/DTPipelines/Pipelines/ObjectTemplating/PipelineTemplateConverter.cs:721–734.

Fix: BLOCKED. No complete, reviewed patch exists for this lifecycle repair.

~~~text
none
~~~

The selected repair must run the trusted reader first.
Complete coverage must select the reader's unit execution.
Missing coverage must produce an explicit needs_prepare result.
Only that result may select trusted writer preparation.
Each path must provide the complete ledger required by F4.

Contract: ARCHITECTURE.md §6, lines 281–305.
The warm path must not start a preparation runner.
The cold path must retain all selected checks.

Verify:

~~~bash
python3 - <<'PY'
from pathlib import Path
import re
text = Path(".github/workflows/ci.yml").read_text()
blocks = dict(re.findall(r"^  ([a-z0-9-]+):\n(.*?)(?=^  [a-z0-9-]+:\n|\Z)", text, re.M | re.S))
writers = {key: value for key, value in blocks.items() if key.startswith("rust-") and key.endswith("-write")}
assert writers
for key, block in writers.items():
    reader = key[:-6] + "-read"
    reader_if = re.search(r"^    if: (.+)$", blocks[reader], re.M).group(1)
    writer_if = re.search(r"^    if: (.+)$", block, re.M).group(1)
    assert "github.event_name != 'push'" in reader_if
    assert "github.event_name == 'push'" in writer_if
    assert f"      - {reader}\n" in block
    assert not re.search(r"\b(?:always|cancelled|failure|success)\s*\(", writer_if)
print(f"{len(writers)} writers depend on push-skipped readers")
PY
~~~

Expected on the reviewed head: 18 writers depend on push-skipped readers.
This checks emitted structure.
It does not run GitHub's scheduler.


## F8 [P0]

File: crates/velnor-actions-orchestrator/src/required_dispositions.rs

Lines: 42–47,80–85

Problem: The current code still rejects the normal skipped writer through the unplanned-job rule.
A release-only change cannot remove this blocker.

Proof:

~~~rust
            None => fold_unplanned(job.conclusion, signals),
~~~

~~~rust
        JobConclusion::Skipped | JobConclusion::Neutral => signals.not_run = true,
~~~

The reviewed branch and main contain the same function.
Tag v0.1.55 contains the same behavior at lines 77–82.
The tag differs here only by the SPDX header.

The generated writer skips outside push:

~~~yaml
    if: (!contains(needs.plan.outputs.not_affected_jobs, ',rust-velnor-actions-actionlint,')) && github.event_name == 'push'
~~~

Source: .github/workflows/ci.yml:810.

Required still includes that writer.
Source: .github/workflows/ci.yml:634–635,693–707.

The needs parser preserves skipped results.
Source: crates/velnor-actions-orchestrator/src/needs_channel.rs:35–48,80–89.

The skipped writer sets not_run.
Without a higher-priority failure, the verdict becomes NotRun.
Either verdict fails the gate.
Sources: crates/velnor-actions-orchestrator/src/merge.rs:189–194,300–301; crates/velnor-actions-orchestrator/src/internal_request.rs:216–226; crates/velnor-actions-cli/src/dispatch.rs:351–354.

The reported versions are correct:

~~~toml
version = "0.1.57"
~~~

Source: Cargo.toml:34.

~~~toml
version = "0.1.55"
commit = "693f3aae14406fb7851ac70f0aee647a869b5063"
~~~

Source: .velnor/generator.lock:5–6.

Fix: none. This blocker is assessment only.

~~~text
none
~~~

It needs a separate code repair.
That repair then needs qualification and a controller release.
The generated pin must then reference that qualified release.
This review authorizes none of those external actions.

Contract: CONTRACTS.md §5, lines 270–281.
The selected branch must supply complete results.
A suffix-based skipped-job exception cannot establish that fact.

Verify:

~~~bash
git diff 7d8d076872ff256c194e375c62f1c44cbf134d81 586bdb2be3b1d203abbdd19a09bff8b188c20cc3 -- crates/velnor-actions-orchestrator/src/required_dispositions.rs
~~~

Observed result: exit 0; no output.
The branch has no repair in this file.
No Rust fold was executed in this review.

# EXECUTION PLAN

This plan permits only the two supplied patches.
It stops before integration while the other blockers remain.
It is not a complete repair plan for F3–F7.

Authority: velnor-github-only-cache-plan/GOAL.md.

Do not publish.
Do not deploy.
Do not merge to main.
Do not change repository settings.
Do not add dependencies.
Do not change MBX.
Do not change files outside Velnor ownership.
Do not add shims.
Do not merge with red CI.
Do not fix F8 in this work.

All commands run from the actual user worktree root.
The review checkout cannot substitute for that worktree.
Keep each gate result with its exact source revision.

## S1. Action: Verify the actual review inputs.

File: velnor-github-only-cache-plan/GOAL.md

Edit: none

Command:

~~~bash
python3 - <<'PY'
from pathlib import Path
import subprocess

def git(*args):
    return subprocess.check_output(["git", *args], text=True).strip()

assert git("branch", "--show-current") == "chore/apache-2-license"
assert git("rev-parse", "HEAD") == "586bdb2be3b1d203abbdd19a09bff8b188c20cc3"
assert git("rev-parse", "MERGE_HEAD") == "7d8d076872ff256c194e375c62f1c44cbf134d81"
for name in ("GOAL.md", "ARCHITECTURE.md", "CONTRACTS.md"):
    assert Path("velnor-github-only-cache-plan", name).is_file(), name
print("REVIEW INPUTS MATCH")
PY
~~~

Expected: REVIEW INPUTS MATCH

Read all three authority documents before S2.
Compare their deciding sections with this report.

Stop: Any source mismatch, missing merge, missing document, unreviewed authority, or unresolved contract difference.

## S2. Action: Verify the reported source resolutions.

File: crates/velnor-actions-workflow-renderer/Cargo.toml; crates/velnor-actions-workflow-renderer/tests/gc1_t41.rs

Edit: none

Command:

~~~bash
python3 - <<'PY'
from pathlib import Path
import tomllib
import subprocess
p = Path("crates/velnor-actions-workflow-renderer")
m = tomllib.loads((p / "Cargo.toml").read_text())
assert m["package"]["autotests"] is False
targets = {(t["name"], t["path"]) for t in m["test"]}
assert ("velnor_workflow_renderer", "tests/velnor_workflow_renderer.rs") in targets
assert ("generator_release_prepare_public", "tests/generator_release_prepare_public.rs") in targets
fixture = (p / "tests/gc1_t41.rs").read_text()
assert not any(line.startswith(("<<<<<<< ", "=======", ">>>>>>> ")) for line in fixture.splitlines())
subprocess.run(["git", "diff", "--check"], check=True)
subprocess.run(["git", "diff", "--cached", "--check"], check=True)
assert "bun_lane_plan: None," in fixture
assert "workflow_tasks: Vec::new()," in fixture
print("MERGE STRUCTURE PASS")
PY
~~~

Expected: MERGE STRUCTURE PASS

Stop: Any missing registration, changed fixture meaning, or conflict marker.

## S3. Action: Create the isolated verification target.

File: none

Edit: none

Command:

~~~bash
python3 - <<'PY_TARGET'
from pathlib import Path
import os
p = Path("/tmp/velnor-pr407-review-586bdb2-target")
assert not p.is_symlink()
p.mkdir(mode=0o700, exist_ok=True)
assert p.is_dir()
assert p.stat().st_uid == os.geteuid()
print(p)
PY_TARGET
~~~

Expected: /tmp/velnor-pr407-review-586bdb2-target

Stop: The path is a symlink, has another owner, or cannot be created.

## S4. Action: Record the twelve-test baseline.

File: crates/velnor-actions-orchestrator/tests/workflow_configuration_public.rs

Edit: none

Command:

~~~bash
CARGO_TARGET_DIR=/tmp/velnor-pr407-review-586bdb2-target cargo nextest run --locked -p velnor-actions-orchestrator --test workflow_configuration_public -E 'test(bun_assets_routing::) | test(bun_private_credentials::) | test(bun_private_credentials_boundaries::)' --no-tests fail
~~~

Expected: 12 selected tests fail through F1.

Stop: Zero selected tests, compilation failure, or a different failure cause.

## S5. Action: Add the reviewed expression regression helpers.

File: crates/velnor-actions-orchestrator/tests/gc1_t12.rs; crates/velnor-actions-orchestrator/tests/gc1_t12/toolchain_expressions.rs

Edit: none

Command:

~~~bash
git apply --include=crates/velnor-actions-orchestrator/tests/gc1_t12.rs --include=crates/velnor-actions-orchestrator/tests/gc1_t12/toolchain_expressions.rs /workspace/scratch/226f2776372f/pr407-review-notes/private-expression-fix.patch
~~~

Expected: Exit 0; no output.

Stop: Patch mismatch or an unexpected file change.

## S6. Action: Prove the new positive regression fails.

File: crates/velnor-actions-orchestrator/tests/gc1_t12.rs

Edit: none

Command:

~~~bash
CARGO_TARGET_DIR=/tmp/velnor-pr407-review-586bdb2-target cargo nextest run --locked -p velnor-actions-orchestrator --test velnor_orchestrator -E 'test(gc1_t12::)' --no-tests fail
~~~

Expected: 1 passed; 1 failed.
gc1_t12_preserves_contract fails with private_sources:toolchain_env.

Stop: Zero selected tests, compilation failure, or another failure reason.

## S7. Action: Apply the exact expression fix.

File: crates/velnor-actions-workflow-renderer/src/private_source_steps.rs

Edit: none

Command:

~~~bash
git apply --include=crates/velnor-actions-workflow-renderer/src/private_source_steps.rs /workspace/scratch/226f2776372f/pr407-review-notes/private-expression-fix.patch
~~~

Expected: Exit 0; no output.

Stop: Patch mismatch or a changed credential guard.

## S8. Action: Verify the twelve public cases.

File: crates/velnor-actions-orchestrator/tests/workflow_configuration_public.rs

Edit: none

Command:

~~~bash
CARGO_TARGET_DIR=/tmp/velnor-pr407-review-586bdb2-target cargo nextest run --locked -p velnor-actions-orchestrator --test workflow_configuration_public -E 'test(bun_assets_routing::) | test(bun_private_credentials::) | test(bun_private_credentials_boundaries::)' --no-tests fail
~~~

Expected: Exit 0; 12 passed; 0 failed.

Stop: Any failure or a selected-test count other than twelve.

## S9. Action: Verify the expression security cases.

File: crates/velnor-actions-orchestrator/tests/gc1_t12.rs

Edit: none

Command:

~~~bash
CARGO_TARGET_DIR=/tmp/velnor-pr407-review-586bdb2-target cargo nextest run --locked -p velnor-actions-orchestrator --test velnor_orchestrator -E 'test(gc1_t12::)' --no-tests fail
~~~

Expected: Exit 0; 2 passed; 0 failed.

Stop: Any failure or a selected-test count other than two.

## S10. Action: Require public named-check regression evidence.

File: crates/velnor-actions-orchestrator/src/check_runtime.rs; crates/velnor-actions-orchestrator/src/check_prepare.rs

Edit: none

Command: none

Expected: An independently reviewed public regression patch with observed failure through execute_check.
The positive case executes its selected child.
The negative case must reject a temporary directory inside checkout.
The positive case must verify private HOME cleanup.
Shared homes must remain.
This gate permits no product acceptance before the later green result.

Stop: This evidence is absent.
The current review has no compiled regression patch for this gate.

## S11. Action: Apply the exact placement fix.

File: crates/velnor-actions-orchestrator/src/cache_execution_context.rs

Edit: none

Command:

~~~bash
git apply /workspace/scratch/226f2776372f/pr407-review-notes/cache-placement-proposed.patch
~~~

Expected: Exit 0; no output.

Stop: Patch mismatch or removal of checkout/private-HOME checks.

## S12. Action: Verify the named-check repair.

File: crates/velnor-actions-orchestrator/tests/velnor_orchestrator.rs

Edit: none

Command:

~~~bash
CARGO_TARGET_DIR=/tmp/velnor-pr407-review-586bdb2-target cargo nextest run --locked -p velnor-actions-orchestrator --test velnor_orchestrator --no-tests fail
~~~

Expected: Exit 0; all registered tests pass.
The S10 regression must execute.

Stop: Any failure, absent regression, or missing independent green review.

## S13. Action: Block integration on the remaining findings.

File: none

Edit: none

Command:

~~~bash
printf '%s\n' 'BLOCKED: F3 F4 F5 F6 F7 need reviewed repairs; F8 needs a separate qualified controller.'
exit 1
~~~

Expected: Exit 1 with the exact BLOCKED line.

Stop: Always.
Do not regenerate after this stop.
Do not recapture goldens after this stop.
Do not release after this stop.
Do not merge after this stop.

## Required later verification

This section records gates.
It does not authorize work beyond S13.

The corrected branch must pass bash scripts/verify-local.sh.
That script covers the root and nested workspaces.
Source: docs/implemented/repo-verification.md:42–48.

Generated output must come from the corrected generator.
Do not edit generated YAML manually.
Source: .github/AGENTS.md:4–6,14–16.

Golden recapture must follow semantic verification.
Golden check must finish with ALL GOLDENS MATCH.
Source: scripts/capture-opentofu-goldens.sh:14–18,415.

Each new test needs an independent plan review.
Each retained test needs observed red/green evidence.
Source: AGENTS.md:9–16.

## Merge readiness verdict

PR 407 is not ready to merge.
F1 explains all twelve reported Bun failure paths.
F2 blocks valid named checks.
F3 and F5 have executed local failure proofs.
F4 leaves Required ledger enforcement disconnected.
F6 breaks the measurement join.
F7 prevents trusted push writers from starting.
F8 needs code before any release can help.
The actual open merge and Rust test results remain unverified.
Do not merge on red CI.

