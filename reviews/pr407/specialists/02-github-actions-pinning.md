# Specialist report: 02-github-actions-pinning

Session: 01a17f04-1c27-7883-abd6-6b22fab7edad. Model: muse-spark-1.3. Read-only analysis, no writes.

---

Picking this apart from the Actions and provenance angle — tracing the lock, helper pins, and red verdict.

---

Found the hardcoded version check. Now tracing how CI downloads the helper and where the verdict gates.

---

Chain confirmed: downloaded binary re-validates the lock against its own baked-in consts. Now checking the release pipeline that produces both.

---

Verdict: **Choice B**. Choice A (skip the blessed check in the downloaded helper) is the wrong fix from an Actions/provenance standpoint. Details below.

## What I verified in the tree (read-only)

- `.velnor/generator.lock` pins `version = "0.1.55"`, `commit = "693f3aae…"`, plus per-target artifact URLs and sha256s under `releases/download/v0.1.55/`.
- Generated `.github/workflows/ci.yml` embeds that pin as immutable `VELNOR_ASSET_URL` / `VELNOR_ASSET_SHA256` (plus `VELNOR_RELEASE_COMMIT` in `required`) in plan, required, and every downstream job, with sha256-checked download-or-seed acquisition. The workflow layer already follows immutable-pin practice.
- The helper bakes the blessed pin in as compiled consts: `PUBLISHED_GENERATOR_VERSION/COMMIT/*_SHA256` in [crates/velnor-actions-mise/src/lock_verify.rs:14-22](/Users/donbeave/velnor-workspace/velnor-new/crates/velnor-actions-mise/src/lock_verify.rs), enforced by exact-equality in `verify_lock_against_published_release` (version, commit, per-target artifact+sha, mise bootstrap), reached via `validate_published_generator_lock` in [crates/velnor-actions-workflow-renderer/src/native_helper/published_lock.rs](/Users/donbeave/velnor-workspace/velnor-new/crates/velnor-actions-workflow-renderer/src/native_helper/published_lock.rs). The downloaded `velnor-actions-*` binary re-validates the tree's lock against its own consts in the plan path.
- Failure: lock bumped to 0.1.59 while the v0.1.59-tagged helper was built from a commit whose consts still said 0.1.55 → `version:0.1.59:0.1.55` mismatch → Plan red → Required verdict red. This is a **release-sequencing defect** (tag cut from a commit where consts ≠ release version), not a design flaw in the check.
- The repo already owns the correct release shape: [product-release-generator.yml](/Users/donbeave/velnor-workspace/velnor-new/.github/workflows/product-release-generator.yml) requires green CI at the exact main SHA, then build → qualify → attest (`Verify candidate provenance record`); `scripts/generator-release/source-qualification.sh` pins the exact source tree including `generator.lock`.

## Why B is standard practice

- GitHub Actions hardening guidance and SLSA-style provenance both say: pin the **tool** by immutable digest (already done via `VELNOR_ASSET_SHA256`), and validate **inputs** against a manifest that ships *with the qualified release*. The tool pin and the code/data pin are separate concepts that must advance together through qualification — never derive trust from ambient tree state at runtime.
- Choice A ("trust the tree-validated lock") collapses that separation: the executing binary would run whatever the lock claims, neutering the downgrade/mismatch guard that justifies the provenance record and the Required verdict. It trades a sequencing bug for a permanent supply-chain hole, and it contradicts the immutable-pin design already in the workflows.
- Choice B keeps the equality check (the guard is load-bearing) and fixes the actual bug: the helper's self-version and its blessed set diverged because the tag was cut from the wrong commit.

## Correct qualification / release / re-pin sequence

1. One atomic commit on main: bump `PUBLISHED_*` consts to the new version **and** regenerate `generator.lock` (new version/commit/shas) **and** regenerate workflows (new `VELNOR_ASSET_URL`/`SHA256`). Never land the lock bump without the const bump.
2. Qualify that exact commit: full CI green, including dogfood generate where the source-built helper (`cargo run --locked` in plan) validates the new lock against the new consts.
3. Tag `v0.1.59` on that exact qualified commit; the release workflow builds, qualifies, attests, and publishes from the tag — so the shipped helper embeds the version it releases.
4. Post-release CI downloads the new helper whose embedded consts equal the lock → green.

## Immediate unblock (pick one, no check-skipping)

- Either revert the lock bump to 0.1.55 to restore green, then redo the bump atomically per the sequence above; or re-cut the release (rebuild/re-tag, e.g. v0.1.60) from a commit with matching consts. The only safe "trust more than one version" variant is an explicit multi-version allowlist baked into a qualified release — never a runtime skip of the check.
