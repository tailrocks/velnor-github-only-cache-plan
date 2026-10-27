# Specialist report: 01-rust-trust-mechanism

Session: 01a17f04-1a75-7392-8691-2b1c62196e8a. Model: muse-spark-1.3. Read-only analysis, no writes.

---

Verdict first: Choice A — then the evidence.

---

Wrong path — locating the real files.

---

Core chain mapped — checking tamper tests and version pins.

---

Verdict: **B — separate helper-version pin independent of the blessed generator lock.**

What I verified (read-only, velnor-new):

- [lock_verify.rs](velnor-new/crates/velnor-actions-mise/src/lock_verify.rs:14) hardcodes `PUBLISHED_GENERATOR_VERSION = "0.1.55"` plus commit and 3 per-target sha256 (lines 14–22). `verify_lock_against_published_release` (line 60) builds a manifest from those constants and `verify_lock_against_manifest` (line 24) rejects on `version`, `commit`, per-target `artifact/sha256`, and mise-bootstrap mismatch — this is the `lock_mismatch:version:0.1.59:0.1.55` source.
- Workspace [Cargo.toml](velnor-new/Cargo.toml) is already at `version = "0.1.60"` while [.velnor/generator.lock](velnor-new/.velnor/generator.lock) still pins `version = "0.1.55"` — blessed lags HEAD, confirming the chicken-and-egg: an immutable v0.1.59/v0.1.60 helper ships with a 0.1.55 brain and can never bless its own version.
- Producer path [native_authority.rs](velnor-new/crates/velnor-actions-workflow-renderer/src/native_authority.rs:89) requires `published_generator_lock`, calls `validate_published_generator_lock` (→ `verify_lock_against_published_release` per [published_lock.rs](velnor-new/crates/velnor-actions-workflow-renderer/src/native_helper/published_lock.rs:8)), then stages the binary as `staged-binary{lock.generator.version}` — one version string serves two masters (which helper runs vs. which generator is blessed).
- `pins.rs` ([orchestrator](velnor-new/crates/velnor-actions-orchestrator/src/pins.rs:1)) and `catalog_tool_pins` already establish the pattern: every consumed tool gets its own pin. Helper version deserves the same, not an exemption.
- Test impact: no dedicated lock-tamper mutation test exists in `velnor-actions-mise/tests` (`gc1_t11.rs:198` guards cache-object bytes, unrelated). But 6+ renderer fixtures hardcode `"0.1.55"` (`gc1_t48_pins.rs:60`, `gc1_t42.rs:136`, `gc1_t47_argv.rs:186`, `gc1_t50.rs:109`, `gc1_t53.rs:96`, `gc1_workflow_cases_preserve.rs:165`) — any fix touches all of them, and negative tests must be added, not removed.

3 reasons for B (Rust ownership / supply-chain view):

1. **No trust inversion.** In A the downloaded helper — the trust anchor that decides which bytes execute — takes its version expectation from the tree-provided lock, i.e. from the very input it is supposed to authenticate. A PR-controlled tree can then hand any lock to the helper and it complies. B keeps the invariant that each layer pins what it consumes: the helper asserts its own identity (`env!("CARGO_PKG_VERSION")` vs. lock's `[helper]` pin) and still verifies generator artifact shas.
2. **Breaks the immutable-release deadlock.** B needs no hardcoded future version: the helper self-pin is stamped at compile time via `env!("CARGO_PKG_VERSION")`, so v0.1.59's helper accepts a lock saying `helper = 0.1.59` while `generator` blessing stays 0.1.55 until a real rotation ceremony. A merely deletes the check and reintroduces it as tree-side validation that has the same staleness problem.
3. **Fits existing architecture.** The codebase already separates concerns — `verify_lock_against_manifest` (caller-supplied manifest, reusable) vs. `verify_lock_against_published_release` (hardcoded constants). B adds a second caller-supplied check of the same shape instead of punching a hole in the one tamper boundary.

Risks of B: `GeneratorLock` schema change (contract type + `lock_from_doc` in [lock.rs](velnor-new/crates/velnor-actions-mise/src/lock.rs:271) + SCHEMA bump; old locks without `[helper]` reject — needs compat path), fixture churn across the 6 files above, and the generator-blessing rotation ceremony still needs a design. Risk of rejected A: must weaken or delete mismatch guards, enabling silent upgrade/downgrade via a tree-edited lock with no binary-side detection.

Smallest flexible fix sketch (B, no behavior change to sha verification):

1. `velnor-actions-contract`: add `helper: HelperPin { version }` to `GeneratorLock`, bump `SCHEMA`.
2. `mise/src/lock.rs:lock_from_doc`: parse `[helper]` section.
3. `mise/src/lock_verify.rs`: new `verify_helper_pin(lock)` — `lock.helper.version == env!("CARGO_PKG_VERSION")`, else `mismatch("helper_version:…")`; keep `verify_lock_against_manifest` untouched for artifact shas.
4. `renderer/src/native_authority.rs:89-102`: call both — helper self-pin check plus existing published-release check scoped to generator artifacts only.
5. `.velnor/generator.lock`: add `[helper] version = "<current>"`; update the 6 fixtures to parameterize helper vs. generator versions, and add two negative tests (tampered helper pin rejected; tampered generator sha still rejected).
