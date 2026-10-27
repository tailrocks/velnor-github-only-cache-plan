# Specialist report: 05-flexible-solution-synth

Session: 01a17f04-210b-7492-8a9f-173667239966. Model: muse-spark-1.3. Read-only analysis, no writes.

---

Fixing the pin-without-weakening-lock puzzle — mapping the trust wall to pick your ship-first path.

---

I've charted the verification chain — now digging into the exact files that freeze the pin.

---

The wall is coming into focus — now tracing how the helper's embedded constants block the advance.

---

I've mapped the coupling that traps the pin — now weighing the escape routes to recommend one shippable fix.

---

Top finding: ship the bounded N/N+1 blessed-set hybrid first — not A, not full B.

Wall (confirmed in tree + `4d5eb2003d` message): any consts-carrying helper only admits its contemporary lock (`crates/velnor-actions-mise/src/lock_verify.rs:14` `PUBLISHED_GENERATOR_* = 0.1.55/...`), while the lock resolves downloads to `lock.version` (`subject_for_install_spec`/`coverage_for_subject` in `crates/velnor-actions-mise/src/mise_lockfile.rs:252,294`, `catalog_for_published_generator` at `lock_verify.rs:132` forcing `gh=2.103.2` over catalog `2.103.3`, `mise_binary_for_published_generator` at `lock_verify.rs:143` returning hard-coded `2026.10.19` vs `MISE_VERSION=2026.10.21`). Releases are immutable, so no triple past `0.1.55` goes green — observed live as `lock_mismatch:version:0.1.59:0.1.55`.

Why not A/B:

- A (skip blessed check for downloaded helper): deletes the only binding between lock and signed release. The 8 `lock_trust.rs:14-63` mutations (alt version/commit, 3 digest flips, mise URL/digest/version) would accept. Supply-chain hole, unshippable.
- B (independent helper pin): correct long-term direction but wrong first step — new lock schema section, release-workflow + goldens churn, two-release migration, still doesn't solve generator-version advance itself.

Recommend exactly one: bounded allowlist of ≤2 published generators (N proven-steady + N+1 candidate) as data, same exact-match semantics per member.

File-level sketch (single focused diff, caller signatures unchanged):

- `crates/velnor-actions-mise/src/lock_verify.rs`: replace scalar `PUBLISHED_GENERATOR_{VERSION,COMMIT,...}` + `PUBLISHED_GENERATOR_GH_VERSION` + hard-coded mise triple in `mise_binary_for_published_generator` with `struct PublishedGenerator { version, commit, linux/arm64/x64 sha, gh_version, mise version/sha-per-target/bytes }` and `const PUBLISHED_GENERATORS: &[PublishedGenerator] = &[GEN_0_1_55, GEN_NEXT]`. Rewrite `verify_lock_against_published_release` to accept iff the lock exactly matches one member (reuse existing `verify_lock_against_manifest` + parameterized mise-bootstrap check per member; reject zero or ambiguous matches). Rewrite `catalog_for_published_generator` / `mise_binary_for_published_generator` to first resolve the matching member, then apply that member's `gh`/`mise` identity — no global const fallback. Add `debug_assert!/test` that `len() <= 2`.
- No changes needed at call sites (`crates/velnor-actions-orchestrator/src/workflow_build.rs:helper_catalog`, `lock_audit_prepare.rs:published_helper_catalog`, `crates/velnor-actions-workflow-renderer/src/native_authority/plan.rs:helper_catalog`, `src/setup.rs:for_published_generator`, `src/native_helper/published_lock.rs:validate_published_generator_lock`) — they flow through the two functions.
- Roll procedure: PR adds N+1 entry alongside the candidate `generator.lock`; qualify + release; follow-up PR drops N. Never widen to a semver range (would admit unreviewed versions); self-describing helper (schema 3, helper reports its own versions under existing `helper_sha256` gate in `crates/velnor-runner/.../host`) is the follow-up, not the unblock.

Test plan preserving discrimination power:

- Extend `crates/velnor-actions-orchestrator/tests/.../lock_trust.rs:assert_lock_trust_rejections` to run all 8 existing mutations against each blessed member fixture (each must still fail with its exact `lock_mismatch:*` string, including `mise_bootstrap_artifact/sha256` and stale-version arms).
- Add positives: `0.1.55` lock accepted, N+1 candidate lock accepted; negatives: unblessed `0.1.54`/unknown-next still `lock_mismatch:version`, cross-member chimera (N version + N+1 commit/sha) rejected as `commit`/`target_diverged`.
- Gates: `cargo fmt`, `clippy 0 warnings`, `nextest` mise/orchestrator/renderer suites + runner `4/4`, goldens match, `check-freshness` PASS — same bar as the restore commit.
