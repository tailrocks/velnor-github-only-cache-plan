# Specialist report: 04-release-strategy

Session: 01a17f04-1f6a-7801-9c34-4b223e1f9eb0. Model: muse-spark-1.3. Read-only analysis, no writes.

---

Fix the red advance with fewest releases — mapping the strategy now.

---

I've mapped the immutable-release deadlock — now designing the minimal safe path to 0.1.60.

---

Top finding: Choice A (narrow trust-tree skip) wins on both count and risk — 1 release (0.1.60) vs 2+ for B — provided it is a minimal, reviewed, flag/narrowly-scoped repair, not a permanent bypass; then do B later as hardening.

Current state (verified read-only):

- `main` green at `4d5eb2003d`: workspace `0.1.60` (`Cargo.toml:34`), helper pin `0.1.55` (`lock_verify.rs:14`, `.velnor/generator.lock` → `v0.1.55`/`693f3aae`).
- `f72b47b309` red: bumped consts + lock to `0.1.59` (`4bb72411`) while workspace went `0.1.60`. Revert message + live CI agree on cause: `lock_mismatch:version:0.1.59:0.1.55`.
- `v0.1.59` release immutable, and its helper still carries stale `0.1.55` `PUBLISHED_GENERATOR_*` consts, so no `(lock, consts, helper)` triple past `0.1.55` can go green.
- Root cause in [lock_verify.rs](/Users/donbeave/velnor-workspace/velnor-new/crates/velnor-actions-mise/src/lock_verify.rs:60): `verify_lock_against_published_release()` compares `lock.generator.version/commit/sha` against hardcoded `PUBLISHED_GENERATOR_*` baked at build time, while the lock always resolves downloads to `lock.version`. Consumers: `catalog_for_published_generator`, `mise_binary_for_published_generator`, and `validate_published_generator_lock` in [published_lock.rs](/Users/donbeave/velnor-workspace/velnor-new/crates/velnor-actions-workflow-renderer/src/native_helper/published_lock.rs:8). Fixture encoding the strict triple: [lock_trust.rs](/Users/donbeave/velnor-workspace/velnor-new/crates/velnor-actions-orchestrator/tests/homebrew_adoption_seed_public_assertions/lock_trust.rs:1).

A vs B:

- A — trust-tree skip (narrow): relax only the version-equality leg, keep `commit` + per-target `sha256` + `mise_bootstrap` checks. Fewer releases (just `0.1.60`), less immutable-release risk. Cost: temporarily weaker supply-chain guarantee.
- B — separate helper pin: decouple helper version from workspace, publish intermediate helper-only release(s) to rebuild a green triple, then workspace release. More releases (≥2), each immutable, and each can strand the next lock bump the same way. Higher risk.

End-to-end sequence (from green `4d5eb2003d`, no releases until step 6):

1. Code repair: minimal change in `lock_verify.rs` — explicitly admit workspace-leads-helper skew (e.g. accept `lock.version == workspace version` when `commit/sha` match the release-candidate manifest, or gate the version leg behind a reviewed flag/env). Keep digest/commit/mise legs strict; update `lock_trust.rs` fixture expectations.
2. Tests with red/green proof: first reproduce red (assert `f72b47b309` logic fails with `lock_mismatch:version:0.1.59:0.1.55`), then green with fix (`fmt`, `clippy 0 warnings`, `nextest 343/343 + runner 4/4`, `ALL GOLDENS MATCH`, `check-freshness`, `cargo doc` — the gates both commits claim).
3. Regen: `.github` tree + opentofu goldens from the fixed generator; confirm diff is version-substitution only.
4. Push candidate; get Required green.
5. Release `0.1.60` (single release; generator pipeline already templates `0.1.60` assets).
6. Re-pin: new commit bumping `generator.lock` + `PUBLISHED_GENERATOR_*` consts + `lock_trust.rs` fixtures to the real `0.1.60` digests/commit.
7. Verify: full gates green on the re-pin; trust-tree strict again.

Flexible middle path (recommended): phased A-now-behind-flag, B-later.

- Now: land A as a narrow, flagged skew-allowance to unblock `0.1.60` in one release.
- Later: implement B properly — single source of truth for helper version consumed by both `generator.lock` and `lock_verify.rs`, so lock/consts/helper advance atomically — then remove the flag and restore strict triple checking.
