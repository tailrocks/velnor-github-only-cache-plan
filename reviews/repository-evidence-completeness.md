# Independent evidence completeness review

Read-only review on 2026-10-25. This checks provenance and scope, not the replacement architecture.

## Original four requested Jackin executions remain historical evidence

The recovered `previous/velnor-cache-redesign/evidence/original-jackin.json` has 131 job entries, 125 executed logs and six skipped jobs across exactly the four original requested runs. Its source snapshot and as-of date are historical; its original proposed architecture is not adopted. No historical timing delta is presented as a current design improvement.

| Run | Event | Attempt | SHA | Jobs / executed | Result |
|---|---|---:|---|---|---|
| [40076991878](https://github.com/jackin-project/jackin/actions/runs/40076991878) | workflow_run | 1 | `c98f5f5fdd831e6075e38fde93b9713575406140` | 11 / 10 | cancelled |
| [40078359402](https://github.com/jackin-project/jackin/actions/runs/40078359402) | pull_request | 1 | `9971e26249c2a601912419c84aad99980f88d28b` | 40 / 39 | success |
| [40078628319](https://github.com/jackin-project/jackin/actions/runs/40078628319) | pull_request | 1 | `e42f3f33abcea63d4178a6f90b9feca2d7169fa3` | 40 / 36 | success |
| [40078851667](https://github.com/jackin-project/jackin/actions/runs/40078851667) | push | 1 | `e737f4b5eb7c1a0d15ba6595fc260407ad178452` | 40 / 40 | success |

Historical evidence limitations are preserved: Cargo diagnostics can replay, successful named-check child output may be suppressed, cache restored bytes are transfers rather than occupancy, and cancelled preview logs do not prove cancellation cause. Original Jackin has a `workflow_run` preview, so current normal CI must not be used to erase the actual product context.

## Current seven ChainArgos scope

All seven named repositories are now accessible. Current source still identifies generator 0.1.41, with independent current fetches; this updates the earlier four service 404 results. The three processor heads/run pairs overlap the recovered evidence, but were re-read rather than treated as inherited truth. The seven current source trees have no product workflow; that does not establish no historical product. Bitcoin gRPC has the actual retired 0.1.31 `Velnor Publish` run, with all jobs and logs captured. No new production workflow or OCI recipe is proposed merely because the current tree lacks one.

The current repository package contains complete run inventories for every named repo (25–41 available runs each), selected attempt-specific all-job and all-step records for 22 executions, 117 jobs and 2,727 steps, 82 relevant complete logs, 223 pinned source files with Git blob and local content hashes. The 35 uninspected log bodies are skipped seeds or final verdict/gate jobs; their full metadata/step summaries are retained. There is no first-page truncation in these selected run/job reads.

## Remaining facts that cannot be promoted to conclusions

- No live cache inventory, current configured storage ceiling, total repository occupancy, complete cache-version/ref count, or eviction history. Connector allowlist 400 is not a GitHub permission 403.
- All selected candidate pairs are source/tool-warm and persistent-MBX-cold. None is a post-redesign true warm proof, and PR versus push is not a controlled performance comparison.
- Native MBX summary counters exist; actual OS-level rustc/C/C++ process counts and complete native/compiler version identities do not.
- Source-cache restore bytes, local MBX export bytes and allocated filesystem bytes measure different quantities. No reported export implies an uploaded cache when the save is refused.
- Private-source fetch summaries do not prove repeated network transfers; secrets and tokens are not part of proposed cache identity or stored snapshots.
- Testcontainers image names/tags are present, but actual image digests, transfer bytes and image-cache occupation are unknown.
- Root-agent current Jackin/Velnor evidence must be cited at its own pinned heads. Historical four-run evidence is retained as requested context, not relabeled current.

## Review result

Evidence is sufficient to establish that current tools/sources are warm, compiled bundle publication fails all seven 384 MiB ceilings, parallel seed work does not warm same-run consumers, and current pruning has no aggregate hard-byte admission. It is sufficient to define preserved task/native/private-input/profile boundaries. It is insufficient to claim a complete Cargo snapshot will fit or achieve a specific speedup before measured validation. No source ownership blocker exists for the seven repositories; changes belong in upstream generation and its supported inputs, followed by regeneration.
