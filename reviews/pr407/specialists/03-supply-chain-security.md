# Specialist report: 03-supply-chain-security

Session: 01a17f04-1dcf-7e12-9099-5b935ca22dba. Model: muse-spark-1.3. Read-only analysis, no writes.

---

Tamper boundary or redundant check — comparing the two options against the live guards.

---

Found the blessed-version pin and its verifiers — now tracing the download paths and tamper tests.

---

Mapped the mutation-test coverage — now examining the helper download paths for the final comparison.

---

Verdict: **B — independent helper pin. Choice A deletes a live tamper-rejection boundary; tree validation is not a substitute.**

Why:

- Blessed-version check is real enforcement, not dead code. `crates/velnor-actions-mise/src/lock_verify.rs:60` `verify_lock_against_published_release` pins version (`0.1.55`), commit, all three per-target artifact+sha256, and mise-bootstrap artifact+sha (`:112`-`:130`). It runs before every lock-coupled download: `native_authority.rs:93` `validate_published_generator_lock`, `native_authority/plan.rs:135` `catalog_for_published_generator` (helper tool catalog), `setup.rs:49` `mise_binary_for_published_generator`, plus orchestrator gates in `workflow_build.rs:313`, `lock_audit_prepare.rs:189`, `prepare.rs:157`.
- `lock_acquire_for_target` (`native_helper/acquire.rs:31`) does **no** verification itself — it copies URL+sha from the lock, and the download script (`:90`) checksums the bytes against the lock's own sha. A tampered lock (evil URL + evil sha) therefore self-consistently passes download. Only the blessed comparison catches the URL/sha swap.
- The mutation tests prove the boundary is live: `homebrew_adoption_seed_public_assertions/lock_trust.rs:14-63` asserts rejection of 5 core generator mutations (alternate version, alternate commit, 3 target-digest swaps → `lock_mismatch:version/commit/target_diverged`) plus 3 mise-bootstrap mutations. Deleting the check turns all of these into accepts.
- Tree validation (`tap_tree_validation`, `guard::validate_tree_path`) checks tree shape/paths, not release identity — it cannot detect a well-formed lock pointing at attacker bytes.

Minimal guard to preserve (Choice B):

- Keep `verify_lock_against_published_release` on all three lock-coupled paths (acquire, helper catalog, mise binary). Never call `lock_acquire_for_target` with an unverified lock.
- To unblock version advance, rotate atomically: `PUBLISHED_GENERATOR_VERSION/COMMIT/*_SHA256` + `PUBLISHED_GENERATOR_GH_VERSION` + bootstrap constants in `lock_verify.rs`, the `.velnor/generator.lock` contents, and the expected `lock_mismatch:*` values in `lock_trust.rs` — keep the check shape, change only the pinned values.
