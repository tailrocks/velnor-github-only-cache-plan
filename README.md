# Velnor Actions: GitHub-only cache replacement plan

Planning date: 2026-10-25.

This is a replacement plan, not an implemented system.
It supersedes the external-service design and retains useful audit evidence only.
No workflow was dispatched, cache mutated, setting changed, release published, or code deployed during planning.

## Decision

Use existing pinned GitHub cache actions for three Rust cache families: sources, tools, and complete Cargo state.
Combine compatible checks in bounded jobs, with exact unit results and isolated writable command lanes.
Use a trusted default-branch baseline and read-only PR/release consumers.
Validate restored coverage independently from cache-key matching.
Publish immutable frozen archives only after completeness replay, byte admission, and actual readback.
Keep deletion authority in a separate checkout-free job.

No external cache service, additional storage product, modified upstream engine, new third-party dependency, or new tool is required.
The included 10-GB repository allowance remains the hard boundary.
The plan uses a conservative decimal ten-billion-byte ceiling and a provisional eight-billion-byte operating ceiling.

## Important limits

- All nine repository sources and selected pipeline job sets were inspected.
- The index contains 39 selected executions and 504 job records.
- Actual full cache inventories and settings remain unavailable through the current connector route.
- Replacement archive size, peak disk, observation closure, warm work, and speed remain unmeasured.
- Every repository's complete capacity fit is pending.
- New dependencies first built in a PR still need trusted default preparation after merge.
- A real approved normal controller release is required before hosted replacement qualification.
- Existing image authority uses fixed generated data-only code; it needs no new image-helper API.

## Read and execute

1. Read EVIDENCE.md for verified observations and access gaps.
2. Read ARCHITECTURE.md and CONTRACTS.md for fixed engineering decisions.
3. Read CAPABILITIES.md for official GitHub behavior and the exact action pin.
4. Read CACHE_BUDGET.md for complete repository accounting.
5. Read WORKFLOWS.md for event paths and publication states.
6. Read ACCEPTANCE.md for all 22 qualification cases and performance gates.
7. Use GOAL.md as the copyable implementation prompt.
8. Use TASKS.json for scheduling and TASKS.md for complete task cards.
9. Use MIGRATION.md for generator and consumer activation order.
10. Apply CONSTRAINT_REVIEW.md before qualification closure.

## Files

| File | Purpose |
|---|---|
| GOAL.md | Complete copyable `/goal` prompt in simplified technical English. |
| ARCHITECTURE.md | Selected small architecture, identities, storage, lifecycle, security, and caller decisions. |
| CONTRACTS.md | Exact proposed shared records and one owner per interface. |
| TASKS.md | Every bounded task, source scope, steps, models, tests, evidence, and blocking conditions. |
| TASKS.json | Machine-readable task graph, command contracts, and model assignments. |
| CAPABILITIES.md | Cited current GitHub restrictions and exact pinned-action behavior. |
| CACHE_BUDGET.md | Accounting, archive/disk measurement, per-repository capacity models, and conflict handling. |
| CACHE_BUDGET.json | Machine-readable nine-repository model with explicit null measurements. |
| WORKFLOWS.md | Event-specific graphs and the publication/recovery state machine. |
| ACCEPTANCE.md | Cold/warm baselines, all 22 cases, actual-work metrics, and baseline-derived thresholds. |
| MIGRATION.md | Candidate, controller, retirement, regeneration, and fleet qualification order. |
| CONSTRAINT_REVIEW.md | Final hard-boundary review and explicit pending runtime gates. |
| EVIDENCE.md | Repository access, exact revisions, current findings, and all selected pipelines. |
| REPOSITORY_FINDINGS.md | Detailed ChainArgos commands, products, native inputs, and observed workflows. |
| RUST_RESEARCH.md | Rust, Cargo, MBX, tool-home, and source reuse research. |
| RUST_SECURITY_REVIEW.md | Independent archive, private-input, compiler, and authority review. |
| CAPACITY_REVIEW.md | Independent stored-byte, overlap, and runner-disk analysis. |
| PLAN_VALIDATION.json | Mechanical graph, task scope, model, test guard, and sentence-length checks. |
| evidence/ | Machine-readable source revisions, generator headers, pipelines, all jobs, and observed counters. |
| reviews/ | Independent review findings and final planning dispositions. |

## Execution subagents

Planning used separate repository, Rust, platform, capacity, security, and task-quality reviews.
No model is prescribed.

Run implementation, verification, and review in subagents.
Run review and the two named architecture and security gates in subagents.
The final task JSON is authoritative for exact counts and subagent assignments.

## Evidence status

`planning complete` means the architecture and bounded task contract are written and reviewed.
It does not mean implementation, capacity fit, hosted qualification, or fleet migration is complete.
Unknowns remain null or explicitly pending.
No measured speedup or universal zero-miss guarantee is claimed.

The goal and procedural task steps use ASD-STE100 style.
The sentence-length checks do not constitute independent STE certification.
