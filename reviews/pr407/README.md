# PR #407 review pack (GPT-6 review, FINDINGS F1-F8 + S1-S13)

Source: `PR407-review.zip` from the review chat, extracted 2026-10-28.
Upstream: PR tailrocks/velnor-new#407, branch `chore/apache-2-license`.
That PR is MERGED as `8fb076bfe4`. F1/F2 repairs verified live at HEAD.

## Contents

- [REVIEW.md](REVIEW.md) — full findings F1-F8, candidate scores, execution plan S1-S13.
- [SCOPE.json](SCOPE.json) — review scope.
- [SHA256SUMS](SHA256SUMS) — checksums of the original pack.
- [authority/](authority/) — recovered ARCHITECTURE.md, CONTRACTS.md, GOAL.txt
  (provisional copies; canonical docs are the top-level plan files).
- [patches/](patches/) — `private-expression-fix.patch` (F1),
  `cache-placement-proposed.patch` (F2).
- [evidence/](evidence/) — diagnostic probes and reproductions
  (cache-restore, image-authority, measurement probes, merge-tree).

## Excluded

- `evidence/full-branch.diff` (4 MB) — intentionally not stored.
  The branch is merged; recover any diff via
  `git diff 7d8d076872ff256c194e375c62f1c44cbf134d81 8fb076bfe4`
  in tailrocks/velnor-new. SHA256 of the original file is in SHA256SUMS.

## Follow-up: helper-pin wall (F8)

After the merge, advancing the helper pin past 0.1.55 went red live:
`lock_mismatch:version:0.1.59:0.1.55` (advance `f72b47b309`,
reverted by `4d5eb2003d`, main green again).
See [unblock-analysis.md](unblock-analysis.md) for the 5-specialist
verdicts (3x B, 1x A-then-B, 1x hybrid) and the decision record.
