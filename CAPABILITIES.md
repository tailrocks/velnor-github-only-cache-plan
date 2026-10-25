# GitHub Actions cache capabilities and limits

Research date: **2026-10-25**. Scope: github.com and the existing pinned `actions/cache` **v6.1.0**, commit `55cc8345863c7cc4c66a329aec7e433d2d1c52a9`.

This is a source-verified platform contract and a live qualification checklist. No cache, workflow, repository setting, or release was changed during this review. All replacement-cache live tests remain pending. Use [ARCHITECTURE.md](ARCHITECTURE.md) for the selected policy and [ACCEPTANCE.md](ACCEPTANCE.md) for the required runtime cases.

## 1. Evidence dates and official sources

GitHub Docs pages below were opened on 2026-10-25. Their rendered pages do not supply a publication or revision date; the access date must not be described as their publication date. Changelog entries have the explicit publication dates shown. The pinned action's exact executable bundles, metadata, and wrappers were inspected, rather than assuming that the current main branch matches the deployed pin.

| ID | Official source | Source date |
|---|---|---|
| G1 | [Dependency caching reference](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching) | Accessed 2026-10-25 |
| G2 | [Read-only cache for untrusted triggers](https://github.blog/changelog/2026-06-26-read-only-actions-cache-for-untrusted-triggers/) | Published 2026-06-26 |
| G3 | [Explicit cache-mode control](https://github.blog/changelog/2026-09-10-control-github-actions-cache-access-with-cache-mode/) | Published 2026-09-10 |
| G4 | [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) | Accessed 2026-10-25 |
| G5 | [Cache REST API](https://docs.github.com/en/rest/actions/cache) | Accessed 2026-10-25; displayed API version 2026-03-10 |
| G6 | [Actions limits](https://docs.github.com/en/actions/reference/limits) | Accessed 2026-10-25 |
| G7 | [Workflow concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency) | Accessed 2026-10-25 |
| G8 | [Larger concurrency queues](https://github.blog/changelog/2026-05-07-github-actions-concurrency-groups-now-allow-larger-queues/) | Published 2026-05-07 |
| G9 | [Repository Actions and cache settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository) | Accessed 2026-10-25 |
| G10 | [Cache expansion and retention settings](https://github.blog/changelog/2025-11-20-github-actions-cache-size-can-now-exceed-10-gb-per-repository/) | Published 2025-11-20 |
| G11 | [REST rate limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) | Accessed 2026-10-25 |
| G12 | [Workflow events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows) | Accessed 2026-10-25 |
| G13 | [Rerunning workflows and jobs](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/re-run-workflows-and-jobs) | Accessed 2026-10-25 |
| G14 | [Reusable workflow configurations](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations) | Accessed 2026-10-25 |
| G15 | [Hosted runner specifications](https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job) | Accessed 2026-10-25 |
| G16 | [Dependency cache security concepts](https://docs.github.com/en/actions/concepts/workflows-and-actions/dependency-caching) | Accessed 2026-10-25 |
| G17 | [Hosted runner filesystem contract](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#file-systems) | Accessed 2026-10-25 |
| P1 | [Pinned action metadata and source](https://github.com/actions/cache/tree/55cc8345863c7cc4c66a329aec7e433d2d1c52a9) | Exact commit inspected 2026-10-25 |
| P2 | [Pinned restore executable](https://github.com/actions/cache/blob/55cc8345863c7cc4c66a329aec7e433d2d1c52a9/dist/restore-only/index.js) | Blob `2427fc716c959214d22297fbf24a33c040b968bb` |
| P3 | [Pinned save executable](https://github.com/actions/cache/blob/55cc8345863c7cc4c66a329aec7e433d2d1c52a9/dist/save-only/index.js) | Blob `b3a8aa37f9f7a608d7d5a63a8990b1fd4c043759` |

## 2. Scope, identity, and event authorization

The verified contract below is separate from Velnor's stricter policy. A documented capability does not establish that a target repository has passed its corresponding live test.

| Capability | Source-verified contract | Selected policy and pending test |
|---|---|---|
| Repository scope | Cache storage belongs to the repository. Eligible workflows within that repository can share entries. G1, G16. | No cross-repository cache pool. Include the calling repository when testing reusable workflows. C09 and C22. |
| Branch/default visibility | Runs can restore eligible current-branch and default-branch caches. PRs additionally have base-branch visibility. Sibling and child branch caches are not generally visible. G1. | Publish the broadly reusable baseline only on the trusted default branch. C07–C09. |
| PR merge scope | PR writes use `refs/pull/N/merge`; the base branch and other PRs cannot restore that PR entry. Such entries still consume repository quota. G1. | Explicit read-only PR jobs, including dependency-changing PRs. A cache namespace cannot enforce a one-entry quota on code holding a write-capable token. C07, C08, C22. |
| Tags | Different tag scopes do not read one another's tag caches. Sharing a commit does not turn a tag into the default branch. G1. | Read an eligible default baseline or recover cold. C09. |
| Merge queue | `merge_group` has its own event, SHA, and ref. G12. | Read-only consumer; qualify ordinary default visibility without inventing PR/base/queue sharing. C09. |
| Reusable calls | The `github` context belongs to the caller. Explicit caller cache capability limits constrain called workflows; incompatible overrequests fail validation. An omitted inferred mode must not be treated as an explicit permanent read cap. G1, G3, G4, G14. | Set explicit read at consumer workflow and call boundaries. Test caller-read/callee-write rejection and the omitted-mode case. C08–C09 and C14. |
| Default-scope event restriction | The June change makes low-trust triggers resolving to default scope read-only by default. Listed trusted triggers include `push`, `schedule`, `workflow_dispatch`, `repository_dispatch`, `delete`, `registry_package`, and `page_build`. It does not blanket-disable every PR or nondefault-scope write. G2. | Event names alone do not authorize Velnor publication. Require accepted default source, trusted planning, and explicit write. C07–C09. |
| Explicit cache mode | `read`, `write`, `write-only`, and `none` control cache capabilities; job settings override workflow settings. These are separate from `GITHUB_TOKEN` permissions. G3, G4. | Consumers read; trusted compilation writers write; cleanup none. Validate each mode against the existing action pin. C08, C14, C20. |
| Immutable identity | An existing entry cannot be updated in place. Identity includes repository/ref, key, and computed cache version. G1, P1–P3. | Canonical compatibility/coverage keys with reviewed repair revisions. Do not use automatic run/time generations. C03–C06, C15, C21. |
| Cache version | The pin hashes ordered literal paths, compression method, applicable Windows-only material, and a version salt. It is not just the key or Velnor schema. P2. | Fixed path ordering and qualified host/compressor identity. Test a path/order/compression change. C02, C06, C16. |
| Lookup selection | The service can search longer prefix matches for the primary key even when `restore-keys` is empty. The action exposes the returned matched key, not a selected cache ID, ref, or version. G1, P2. | Inspect every service-selectable candidate before restoration; reject any returned key unequal to the requested candidate. The shadow rule below remains necessary. C07–C09, C15. |

### Ref-shadow limitation

Filtering REST inventory to the default branch does **not** instruct the restore action to download that inventory ID. The action has no ref or cache-ID selector. A same-key/version entry or a longer primary-key prefix match in another service-visible ref can shadow the intended default entry. An empty `restore-keys` list does not impose strict server equality. A key match or producer-written manifest alone does not prove default provenance. This is an inference from G1 and P2's interface, not a claimed new API feature.

Before allowing restoration, examine every entry the service could select for that request and expected cache version: exact-key and longer primary-prefix candidates across all visible scopes. Establish authorized outer-archive provenance; otherwise decline restoration and use the permitted cold path. The pin downloads/extracts a differing matched key before returning it, so post-restore equality cannot protect against earlier outer extraction. Still reject any returned key unequal to the requested candidate. If inventory is unavailable, lookup may support optional recovery only where the execution context independently permits it; it cannot establish the missing ref/ID evidence. Qualify same-key and longer-prefix shadows with tiny controlled payloads. An inventory preflight is not atomic protection against an uncontrolled writer racing the restore; audited writer capabilities remain necessary.

### Portable source data and physical transport versions

Retain stable owned transport beneath `runner.temp` for the initial migration. The same logical portable source group may require separate physical entries for approved runner layouts or compression methods. The pin hashes the literal action path and compression; Linux and macOS have no separate OS salt, but their expanded `runner.temp` paths can still produce different versions. P2, P3.

In the exact pin, `resolvePaths` converts matched files to paths relative to `GITHUB_WORKSPACE`. Tar packing and extraction then use that workspace as their working root. Consequently a fixed absolute `/tmp/...` input would not guarantee an absolute archive member or portable extraction placement: it could merely equalize the version while retaining a workspace-relative placement dependency. GitHub does not promise static VM filesystem paths. P2, P3, G17.

Include source transport layout in the approved compatibility/group identity. Count every physical version and its replacement overlap; do not assume hidden cross-host deduplication. Keep at most two generations per active compatible group/version, with a bounded approved version set. C02 qualifies fresh-run restoration at each approved layout; C06 verifies correct version/placement isolation when layouts or compression change. Initial migration does not require cross-host sharing qualification. State and tools retain their host-specific compatibility requirements.

## 3. Exact pinned-action behavior

| Behavior | Observed in the pin | Consequence and test |
|---|---|---|
| Save outputs | Standalone save metadata has no outputs. Its internal cache ID is not exported through `setOutput`. P1, P3. | Never use step success as publication proof. C01, C14. |
| Nonfatal failures | The wrappers/toolkit catch many save and restore failures and warn or return an empty result. Validation errors can still fail. Denied saving may end with a successful step and no new entry. P1–P3. | Classify only what evidence establishes; preserve ordinary check results and fail qualification on absent publication. C11, C14, C15. |
| Restore outputs | `cache-hit` is the string `true` for exact restoration and `false` for fallback. An ordinary miss is generally unset; feature-unavailable has a special false path. The attempted primary key exists even on a miss. P1, P2. | Compare strings explicitly. Require a matched key and actual payload validation; the attempted key is not a receipt. C02, C14, C15. |
| Lookup-only | It returns after obtaining the matched download result and before downloading/extracting. The public contract does not establish whether this changes `last_accessed_at`. P2, G1. | Neither retention keepalive nor recency-neutral probe is promised. Compare inventory before/after lookup and real restore in a bounded dedicated test. C15. |
| v2 save sequence | The action packs the archive, obtains an entry reservation for key/version, uploads, and finalizes with stored size. P3. | The reservation is not a repository-wide byte reservation. No inventory/upload/delete transaction exists. C16, C22. |
| Size reporting | The action calculates its outer archive internally. No save output exposes the admission size. The legacy v1 individual-size guard is not proof of the v2 repository quota. P3. | Freeze and premeasure the existing packaging route; require a justified upper bound and reconcile inventory bytes afterward. C16, C21, C22. |
| Mode enforcement path | Neither inspected pinned executable contains the current `ACTIONS_CACHE_MODE` local prechecks. GitHub's scoped service-token contract remains applicable. P2, P3, G3. | Qualify backend denial with this exact pin; do not promise current-main log messages or local skip behavior. C14. |
| Outer extraction | The pin runs tar extraction with `-P` into the workspace. The action's `path` input is not a member-path sandbox or an extraction remapping facility. P2. | Trusted outer-writer control is required before inner validation. Never restore compiler state into a signing/publication authority job. C08, C15, C20. |

Verified publication requires a matching inventory tuple `(repository, ref, key, version, id, size_in_bytes)` and an actual exact readback after removing only the local transport copy. Compare the readback digest and manifest with the frozen candidate. An earlier existing entry must not be reported as a newly published candidate. A separate fresh-job restore qualifies cross-run use. Neither observation supplies a retention lease. C01, C02, C11, C14, and C15 exercise these distinctions.

## 4. Retention, settings, inventories, and limits

| Subject | Verified limit or behavior | Required interpretation |
|---|---|---|
| Retention and eviction | Default unused-entry retention is seven days; repository configuration can change retention. Size pressure evicts older accessed entries. GitHub can save before eviction. G1, G9, G10. | The included 10-GB setting is not an instantaneous no-overlap guarantee or pin on a baseline. Cold recovery remains necessary. |
| Paid expansion | GitHub permits storage expansion beyond the included allowance. G10. | Prohibited by this design; do not enable it or use it to claim fit. |
| Listing | Cache list has up to 100 entries per page and exposes ID, ref, key, version, `size_in_bytes`, creation and last-access times. G5. | Paginate all refs, namespaces, versions, and families. Do not infer current desired coverage from creation time. |
| Aggregate usage | Aggregate usage can lag by at least five minutes. G5. | Do not use it as a fresh atomic admission snapshot. Reconcile individual inventory and outstanding exposure. |
| Transfer/deletion quotas | Per repository: 200 uploads/minute, 1,500 downloads/minute, 400 cache-delete operations/minute. G6. | Bound transfer and delete retries; these are separate from general REST limits. |
| REST quota | `GITHUB_TOKEN` generally has 1,000 requests/hour/repository; applicable Enterprise Cloud resources have 15,000. Secondary limits include 100 concurrent requests and 900 REST points/minute; most GETs cost 1 point and most DELETEs 5. Other limits may apply. G11. | Honor rate/reset and Retry-After responses. The 400/minute cache delete limit is not an independently safe delete rate. |
| Configured quota and policy | GitHub's setting remains 10 GB. The selected Velnor accounting ceiling is the conservative **10,000,000,000 bytes**, with provisional operating ceiling **8,000,000,000 bytes**. | Decimal thresholds are policy choices, not a claim about GitHub's display units. No measured fit exists. |

Endpoint permissions below are the documented fine-grained permissions. A connector's endpoint allowlist is a different control.

| Endpoint after `/repos/OWNER/REPO` | Method | Repository permission |
|---|---|---|
| `actions/caches` | GET | Actions read |
| `actions/cache/usage` | GET | Actions read |
| `actions/cache/storage-limit` | GET | Actions read |
| `actions/cache/retention-limit` | GET | Administration read |
| `actions/cache/storage-limit` | PUT | Administration write |
| `actions/cache/retention-limit` | PUT | Administration write |
| `actions/caches/{id}` or key/ref deletion | DELETE | Actions write |

Readers and compiling writers use only necessary read permissions. Cache mode does not restrict REST deletion authority. A separate checkout-free cleanup job receives Actions write, validates exact owned IDs, reacquires the common queue, and rechecks replacement/intent before deleting. Do not delete by an unbounded key prefix. Charge predecessors until confirmed deletion. C11, C16, C21, C22.

**Observed access gap:** available connector inventory/usage requests returned HTTP **400, endpoint not allowed**. This is not a GitHub 403 permission denial and establishes no inventory or setting value. Actual nine-repository settings and current full inventories remain pending. The observed **1.714 GB** tools figure is a sum of **eight distinct historical tool keys**, not the size of one archive or a complete repository inventory. Image caches are counted **if present in actual inventory**; this plan does not invent an active image-cache producer.

## 5. Concurrency, reruns, and workflow execution

| Subject | Verified contract | Design consequence and qualification |
|---|---|---|
| Concurrency group | One active member per repository group. Group names are case-insensitive. Default behavior allows one pending member and replaces an older pending member. G7. | Use one consistently named repository mutation group for all owned writers and cleanup. C10–C11. |
| `queue: max` | Allows up to 100 queued members. It is incompatible with `cancel-in-progress: true`. Queue order follows waiting entry, not event dispatch; actual execution ordering is not an atomic sequencing promise. G7, G8. | Use `cancel-in-progress: false`; count saturation as a real failure. Do not launch 101 jobs merely to test the documented bound. C10. |
| Coordination limits | A group does not lock readers, reserve cache bytes, fence foreign writers, or make cleanup adjacent to its writer. G7 plus API interface. | Recheck inside each mutation job, retain delayed-cleanup charges, and block qualification when uncontrolled exposure is unbounded. C10, C11, C22. |
| Nested calls | Caller/callee share caller context; reusing the same group at nested acquisition boundaries can cancel or block intended work. G7, G14. | Acquire only at the mutation-owning job. Avoid workflow cancellation that kills required preparation. C10, C13. |
| Failed/specific reruns | Reruns preserve original SHA/ref and original actor privileges. Successful jobs may remain from an earlier attempt. Reruns are available for up to 30 days, with at most 50 reruns. G13, G14. | A consumer must restore/cold-recover without requiring a successful old producer to rerun. Preserve mixed-attempt provenance as described below. C12. |
| Skipped dependencies | A skipped/failed dependency can skip downstream jobs unless their conditions handle the outcome. Job-level `if` is evaluated before matrix expansion. G4. | Static reader/writer/cleanup jobs; outcome-aware `always()` Required; no `matrix` reference in job-level `if`. C13. |
| Matrix outputs | Duplicate output names from matrix jobs can overwrite each other, and matrix ordering is not guaranteed. G4. | Use noncolliding per-group ledgers. A cache outcome cannot satisfy a selected unit. C10, C13. |
| Resource ceilings | Matrix expansion maximum 256 jobs; hosted job execution maximum six hours. Standard advertised runner SSD is 14 GB, not guaranteed available free space. G6, G15. | Count all branches, retain measured timeout headroom, and measure extraction/build/inner/outer/readback disk peaks. C01, C02, C16. |
| Service failure | Optional cache errors may become misses or unsaved results, but hard job failures are still failures. P1–P3. | Running jobs continue checks cold where possible. A writer cancelled before units execute leaves explicit missing units and Required must fail. It cannot retroactively make the completed reader execute. C11, C13, C15. |

### Mixed-attempt Required evidence

Bind each ledger to its actual source, plan, run, job, and execution attempt. On a failed-jobs rerun, a successful unchanged job that GitHub retains from attempt 1 may provide its authenticated attempt-1 result. A job that actually reruns at attempt 2 needs its attempt-2 result. Do not relabel old evidence as new execution, and do not require successful retained jobs to rerun solely to satisfy a global `run_attempt` equality rule.

C12 must include two groups: A succeeds at attempt 1; B's writer fails; a failed-jobs rerun executes B and Required at attempt 2. Required accepts A's genuine retained result and B's genuine new result only after checking effective job outcomes. Also test retained/missing caches, skipped writers, duplicate ledgers, and an unauthorized cross-run receipt.

## 6. Capacity and trust conclusions

**Conditional feasibility:** existing GitHub caches can support bounded trusted default baselines and read-only consumers with cold recovery. They cannot supply an atomic repository byte allocator, an eviction pin, a mutable manifest transaction, or an unconditional always-warm guarantee. Inventory plus a successful step is insufficient publication evidence. These conclusions follow from G1, G5, G7 and the inspected action interfaces.

Admission must charge complete repository inventory, outstanding owned writes, a qualified candidate outer bound, bounded foreign in-flight pressure, all migration overlap, and delayed cleanup. The inner compressed archive is not GitHub's outer stored archive. Unknown inventory or an unjustified packaging bound disables publication and fails capacity qualification while ordinary checks remain usable. The provisional two-billion-byte reserve is not evidence that every possible foreign writer fits. C16, C21 and C22 must establish the actual accepted model.

**Security distinction:** hashes prove payload integrity; they do not identify a trustworthy producer. Audit all default-scope writers, keep cache write capability away from unreviewed PR code, and keep restored compiler state away from signing, OIDC, publication, and repository-write authority. Source-only PRs may consume an authorized baseline. New-dependency PRs can rebuild until trusted default preparation after merge; their compiler output is not promoted. Default preparation runs accepted source/configuration with existing tools and no new service. Cache ref visibility cannot create a private-source audience boundary. G1–G4, G16 and P2 support these restrictions; workload safety still needs the independent security review.

## 7. Live qualification checklist

All rows are **pending live evidence**. Local fixtures exercise policy logic and cannot replace GitHub service tests. Use small dedicated approved entries, existing hosted runners and existing tools; never force eviction by filling production storage.

| Check | Concrete observation | Acceptance case |
|---|---|---|
| Scope and shadow | Seed distinguishable tiny payloads in allowed default/current/PR/tag scopes; record inventory tuples and actual returned bytes; test a shadowed same key/version and a reusable call. | [C07–C09](ACCEPTANCE.md#c07-pr-rerun-merge-to-main-preview-and-stable-release) |
| Modes | Exercise exact reads and absent-key saves under read/write/write-only/none with the existing pin; verify explicit reusable-call cap rejection. | [C08](ACCEPTANCE.md#c08-fork-pr-with-restricted-permissions), [C14](ACCEPTANCE.md#c14-save-permission-denied-while-the-action-step-succeeds) |
| Immutability/version | Attempt distinct payloads under one identity; independently restore the winner. Change only path/order/compression and inspect version/miss behavior. | [C02](ACCEPTANCE.md#c02-identical-run-on-fresh-runners-with-empty-targets), [C06](ACCEPTANCE.md#c06-host-target-compiler-native-library-or-sdk-change) |
| Publication | Compare action status, exact inventory tuple, emptied-path readback digest, and a separate fresh-job restore. Include denial, interruption and corruption. | [C11](ACCEPTANCE.md#c11-cancellation-during-preparation-upload-or-cleanup), [C14](ACCEPTANCE.md#c14-save-permission-denied-while-the-action-step-succeeds), [C15](ACCEPTANCE.md#c15-eviction-expiry-deletion-corruption-and-restore-timeout) |
| Recency/retention | Compare bounded before/after `last_accessed_at` observations for lookup-only and full restore; observe natural expiry when available. Unobserved eviction/expiry remains pending. | [C15](ACCEPTANCE.md#c15-eviction-expiry-deletion-corruption-and-restore-timeout) |
| Queue/rerun/failure | Use a few bounded writers; record queue entry/start/outcomes; test cancellation and mixed-attempt Required; test optional cache outage separately from hard job failure. | [C10–C13](ACCEPTANCE.md#c10-simultaneous-runs-request-the-same-missing-generation) |
| Capacity and disk | Paginate all actual inventory; measure frozen inner, preflight outer, stored bytes, peak disk, overlap and delayed cleanup. Synthetic records exercise exact-fit/one-byte-over branches. | [C16](ACCEPTANCE.md#c16-publication-near-the-repository-budget), [C21](ACCEPTANCE.md#c21-migration-with-old-and-new-namespaces), [C22](ACCEPTANCE.md#c22-pressure-from-other-existing-cache-families) |
| Security and products | Qualify restricted forks, private inputs and derived outputs, credential-free native production preparation, and source-free authority jobs. | [C08](ACCEPTANCE.md#c08-fork-pr-with-restricted-permissions), [C20](ACCEPTANCE.md#c20-release-helpers-and-source-free-signing-or-publishing) |

No fit, speedup, universal cache hit, permanent retention, or complete native/origin observation is established by this document.
