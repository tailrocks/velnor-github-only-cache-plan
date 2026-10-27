# Decided plan: helper-pin unblock (hybrid of Agent1 + Agent2, 2026-10-28)

Binding reference for implementation. Both agent reports (GPT-6 Astra Pro,
chat 2026-10-28) converge on one fix shape. This file picks the best of both.

## 1. Decision: hybrid

Replace the compiled-in blessed approval with an independently
authenticated approval record. Keep lock schema 1, exact field comparisons,
and the `lock_mismatch:` error format. Dual authority:

- Source generation checks the compiled, reviewed release approval
  (current `0.1.55`). Behavior unchanged during the repair.
- Released CI helper checks its own authenticated release manifest plus
  its actual host executable digest. No fallback to the older approval.

## 2. Why this hybrid (what each agent contributes)

- Agent2: concrete record `.velnor/controller-approvals.json` with one
  active + one staged entry; C_release / C_approve / C_run split; live CI
  evidence table (red 40569869545 vs green 40571732683); attestation
  predicate reuse; DCO release workflow steps.
- Agent1: private-construction authority type (no `approved: true`
  shortcut); 5-row transition table; no env switch; canonical-equality
  gate for both workflow constructions; Mise profile split
  (source-bootstrap vs helper-runtime); cached-`verified=true` distrust.
- Single-module deviation: both agents propose one new module each
  (`published_release_authority.rs` vs `controller_approval.rs`). Build
  ONE module, `controller_approval.rs`, owning both resolution and the
  private authority type. Avoids split ownership.
- Rejected (both agents prove): skip-check (deletes tamper wall),
  bare second pin (no authority), static blessed set (self-hash problem),
  release-only bump (proven red live as `f72b47b309`).

## 3. Data model: `.velnor/controller-approvals.json` (new, schema 1)

Active + staged entries. Each entry holds the complete approved identity:

- Exact release version and source commit.
- Signed release manifest digest.
- All three target URLs and binary digests.
- Expected repository and release workflow.
- Qualified GitHub CLI and Mise identities.
- State: active or staged.

Resolution reads ONLY from an independently authenticated GitHub commit
(`C_approve`). Never from the candidate checkout copy.

## 4. Authority rule

- Pure matcher still checks every field: binary name, version, commit,
  every target + canonical URL + SHA-256, bootstrap tuple.
- Source authority carries its reviewed bootstrap tuple. Runtime
  authority carries the tuple compiled for that release. Neither tuple
  comes from the lock being checked.
- Runtime additionally requires: version equals `env!("CARGO_PKG_VERSION")`,
  executable bytes equal the approved host digest (any target, any build
  mode — debug shortcuts in `release_binary.rs` must not construct
  authority), manifest bytes re-verified with fixed repo/owner/signer/
  source-ref/subject checks.
- Failure terminates admission. No retry against the predecessor manifest.

## 5. Build steps (refs at velnor-new `4d5eb2003d`; VERIFY EACH before editing)

1. Review the regression plan against `AGENTS.md:8-15`.
2. Write `.velnor/controller-approvals.json:1` with the active `0.1.55`
   entry mirroring the current lock + manifest + tool profiles.
3. Add `crates/velnor-actions-orchestrator/src/controller_approval.rs:1`
   (resolution + private authority type, single module).
4. Register the module in orchestrator `lib.rs`.
5. Reuse immutable-source reads (`package_release_source_files.rs:69-112`)
   and attestation predicates
   (`package_release_signer_attestation_sdk.rs:32-69`,
   `upgrades_velnor_release.sh:22-50`) for admission.
6. Bind executable identity
   (`homebrew_adoption_sdk_binding_assets.rs:99-121`).
7. Parameterize `lock_verify.rs:24-75` comparisons with the authority;
   approved bootstrap tuple at `lock_verify.rs:112-129`; authority-driven
   profiles at `lock_verify.rs:132-166`. Update `lock.rs:15-18` exports.
8. Thread authority: `prepare.rs:82-84` + `:145-158`,
   `internal.rs:69-80`, `finalized.rs:13`, `published_lock.rs:8`,
   `workflow_build.rs:39`, `workflow_native_authority.rs:34`,
   `check_jobs.rs:24`, `workflow_context.rs:25-60`.
9. Renderer: `closure.rs:50-54` + `:83-92`, `steps.rs:306-339`,
   `native_job_builders.rs:87-91`. Forbid `release_binary.rs:48-85`
   shortcuts from constructing authority.
10. Keep `generator.lock` at `0.1.55` during the repair. Regen via
    `cargo run -p velnor-actions-cli -- generate` (never hand-edit
    generated YAML). Recapture goldens only after semantic green.
11. No env switch for authority selection. Remove old unchecked route.

## 6. Tests (all required, red/green observed)

- Preserve the 5 generator + 3 Mise mutations in `lock_trust.rs`
  (exact names + `lock_mismatch:*` strings) inside
  `public_velnor_repository_bootstrap_accepts_only_catalog_mise_lock`.
- New: repaired runtime accepts its approved own lock; rejects complete
  old lock without fallback; rejects fabricated metadata, wrong-target
  digest, wrong signer/source, mixed active/staged fields, missing
  authority (explicit fail), profile mismatch; both workflow
  constructions emit identical identities (canonical-equality gate).
- Gates: exact-filter nextest (expect 1 test), full root + nested
  verification, `ALL GOLDENS MATCH`, doc with `-D warnings`, freshness.

## 7. Release sequence

1. Land repair with helper still `0.1.55`. CI green + review.
2. Confirm `0.1.60` unused. Build release from the exact green SHA.
   Keep `v0.1.59` frozen forever.
3. Qualify candidates (Linux, macOS ARM/Intel, Homebrew). Publish via
   the existing release workflow with attestations.
4. Approve the measured release in a separate commit (manifest, binary,
   tool identities). Lock still `0.1.55`.
5. Bump lock + regen in one reviewed change. Push. Watch Plan,
   Producer, Required. Merge only on green (DCO). On red, keep old pin.
6. Warm cache activation stays closed until the 22-case gates pass.

## 8. Risks and stop conditions

- Late caller without authority, any fallback retry, verifier-setup
  cycle, credential exposure to children, profile divergence,
  cached-`verified=true` trust, capacity over ceiling
  (`I+P+F+B <= 8,000,000,000`) — each is a hard stop.
- Keep the usable predecessor until replacement verification succeeds.
- Auth failure is fatal. Unknown capacity blocks publication.

## 9. Provenance

- Agent1 + Agent2 full texts arrived in chat 2026-10-28 (GPT-6 Astra
  Pro, not Ultra — both disclosed). This file, not those chats, is the
  binding reference.
- Every agent-cited path is under verification by 5 read-only
  subagents before any edit. Ghost citations get cut, not worked around.

## 10. Verification outcome (2026-10-28, 5/5 verifiers green)

All cited paths EXIST at velnor-new `4d5eb2003d`, clean tree, zero
line-number drift over 3 lines. No writes made by any verifier.

| Area | Verdict | Session |
|---|---|---|
| Orchestrator plumbing (prepare, internal, finalized, attach, pins, workflow_*, validate, lib, homebrew/assets, signer SDK, source reader) | All exist as cited | `01a17f33-80dd-7cc0-b0cc-ad28221e7cab` |
| Renderer (published_lock, release_binary, closure, steps, native_job_builders, schema2_*, upgrades script, ci.yml ranges) | All 11 ranges exist | `01a17f33-82cc-7d42-91b5-3be376a0ce99` |
| Mise + tests (lock_verify.rs is 167 lines; consts L14-22; matcher L24-58; HEAD prefix + clean tree; remainder per summary verdict, full table in log) | Confirmed as observed; details in log | `01a17f33-84c3-73f0-9412-069fb3eb5896` |
| Release + docs (create-release-manifest.sh, product-release.yml, bootstrap contract, AGENTS.md, repo-verification.md, freshness, goldens fixtures) | All 8 exist | `01a17f33-86b2-7443-8b75-b5dc201dc4ce` |
| Live CI (HEAD == origin/main == 4d5eb2003d clean observed; red/green runs and releases per summary verdict, full output in log) | Partially observed; details in log | `01a17f33-888e-75e2-a27b-17b1e7e2f9eb` |

Full per-file tables live in those session logs. Implementation may proceed.
