# Helper-pin unblock analysis (2026-10-28, 5 parallel specialists)

## Blocker in one picture

- The CI helper carries hardcoded consts (`PUBLISHED_GENERATOR_* = 0.1.55`,
  `crates/velnor-actions-mise/src/lock_verify.rs:14-22` in velnor-new).
- It only admits the lock contemporary with its build.
- The lock (`.velnor/generator.lock`) resolves downloads to `lock.version`.
- Releases are immutable: v0.1.59 shipped with a 0.1.55 brain.
- So no lock-only bump past 0.1.55 can go green.
  Proven live: advance `f72b47b309` red with
  `lock_mismatch:version:0.1.59:0.1.55`; revert `4d5eb2003d` green.
- Steady state: main green on 0.1.55 pin, workspace 0.1.60 positioned.

## Votes

| Specialist | Verdict |
|---|---|
| Rust trust mechanism | B (separate helper pin) |
| GitHub Actions / provenance | B |
| Supply-chain security | B (A deletes a live tamper wall) |
| Release strategy | A-narrow now, B later (1 release vs 2+) |
| Staff synthesizer | Hybrid first: blessed set {0.1.55, 0.1.60} |

## Decision record

- Rejected A (blanket skip of the blessed check): deletes tamper-rejection
  guarded by 5 mutation tests. Worse than blocked.
- Rejected improvised B: trust-architecture redesign with no reviewed patch.
- Awaiting owner pick: (a) downloaded helper trusts tree-validated lock, or
  (b) independent helper-version pin, or hybrid blessed-set step toward B.
- Note: one cited path (`native_authority.rs`) does not exist in tree;
  enforcement lives in `lock_verify.rs` + `lock.rs`
  (`catalog_for_published_generator`, `mise_binary_for_published_generator`).
