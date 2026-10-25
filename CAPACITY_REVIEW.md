# Independent capacity review

Date: 2026-10-25. Reviewed candidate: GitHub dependency-cache storage only; verified sources, verified installed tools, complete Cargo target/build snapshots (including the agreed tracked-input source projection); MBX object/export storage excluded. No remote runs, upload, deletion or configuration change performed.

## Verdict

**Conditionally feasible; current fit is unproven.** The proposed reduction to three persistent families and no PR saves is a substantial capacity improvement, but three names do not imply three entries: every incompatible host, workspace/build lane, compiler/profile/feature set, path version and migration generation can multiply storage. One repository's allocation cannot be borrowed by another.

**Recommended single policy:** freeze each publishable family/group into one standard tar.gz payload with Velnor’s already-approved Rust tar0.4.46 and flate2=1.1.10 (rust_backend) dependencies; admit that immutable file using a qualified upper envelope for the official action's outer archive; serialize all owned cache writers and pruning in one repository group; count old+new until a real empty-path readback verifies the new archive; then schedule only observed superseded owned IDs for checkout-free cleanup. Decline publication whenever inventory, outer-envelope bound, disk or overlap budget is unknown. Consumers always remain correct cold.

Do not claim that this proves GitHub's instantaneous stored bytes can never exceed10,000,000,000. The repository limit is an eviction setting, inventory is not transactional, and the official action exposes neither a pre-upload callback nor an aggregate reservation. The design can enforce Velnor's conservative admission policy under explicit cooperation/runtime assumptions, not a universal physical-storage invariant.

## 1. Exact accounting quantities

Use integer bytes throughout. The Velnor policy ceiling is C=10,000,000,000. The provisional operating ceiling is O0=8,000,000,000, leaving at least2,000,000,000bytes of total reserve until actual measurements can tighten the threshold. This is a conservative provisional policy, not evidence that the candidate families fit or that2GB covers every replacement. The GitHub setting must separately be verified at10GB. The decimal policy ceiling is a deliberately conservative project choice, not a verified definition of GitHub's displayed GB.

For each repository:

- I = sum of every currently inventoried cache entry's size_in_bytes, across all pages/refs/versions/prefixes.
- P = subset of I consisting of retained current/previous owned entries. Do not add P again: it is already in I.
- F = subset of I from foreign, legacy or unmanaged entries, including old MBX exports/native-target snapshots/tools and PR entries.
- B = pre-upload upper bound for the actual NEW archive produced by actions/cache, including its outer tar/compression framing.
- R = conservatively charged bytes for known owned in-flight publication not yet present in inventory. Normal serialization makes R zero only after older writers were drained and inventory reconciled.
- H = measured/reserved allowance for API observation delay, unmanaged variation and size-model uncertainty. It is not an atomic reservation, and cannot bound a malicious/uncooperative writer.

Admission condition, with H at least2,000,000,000 and increased when measured uncertainty/external/in-flight exposure requires it:

    I + R + B <= min(8,000,000,000, C - H)

The previous generation remains in I until readback succeeds and its deletion is confirmed. Never subtract a planned deletion or assume the service will choose a harmless victim. If inventory fails, is incomplete, or migration/in-flight ownership is unresolved, skip the save.

For a steady operating occupancy T that always leaves room for the largest permitted next candidate Bmax:

    T <= min(8,000,000,000, C - H) - Bmax

Bmax must cover the replacement that can actually occur, not the median archive. If a source+tool+target compatibility change requires several new entries, publish and verify one at a time, re-inventory after each; the required overlap is the largest sequential stage, plus any old generations that cannot yet be removed. If all new components must coexist before any predecessor can be removed, reserve their sum instead.

## 2. Current evidence does not establish fit

The available connector rejected target cache inventory/usage endpoints with400 “endpoint not allowed.” This gives no current byte totals or settings evidence. It is not a403 permission finding.

Root’s corrected evidence is approximately **1.714GB total across eight distinct observed Velnor tools keys**, not a single tool archive. This is a partial observed sum; it is not complete repository cache usage and does not establish the size of any one replacement candidate. Exact per-key API size_in_bytes, refs, versions, observation times and completeness remain required for admission. No multiplication of1.714GB as a per-archive figure is valid.

The same exact tools identity may be shared across compatible jobs in one repository, but should not be duplicated merely because each workspace has a different state snapshot. Equally, host/architecture/toolset/install-path incompatibility must not be hidden to obtain apparent savings.

Registry/git/private source bytes need their own measurements. Shared content can be deduplicated only where the existing source adapter safely supplies the same verified source archive. Private sources must stay in their allowed repository/trust context. “Dependency-only cache” does not mean small: complete Cargo target/build state includes all relevant native fingerprints, build-script outputs, incremental units, generated files and the tracked-source projection required for reuse.

## 3. Pre-upload choices

### A. Direct directory save plus raw-size or compressed-size estimate

This is the fewest code changes, but not the selected policy.

du output is filesystem usage or apparent file size, not a tar size or compressed stored size. Sparse files, hardlinks, symlinks, long names, POSIX extended headers, record padding and directory entries change the relation. A compile process still modifying the directory invalidates any measurement. A manually generated compressed archive is not the exact archive later generated by the action.

A conservative bound based on a completely enumerated, frozen raw tree can be derived for a qualified archiver/compressor, but doing so over arbitrary trees is more complicated than bounding a wrapper containing one regular file. It is also liable to reject useful compressed snapshots when apparent target size is much greater than stored size.

### B. Prepack once and call the official action on the archive file

**Selected.** Use ordinary tar.gz through the existing approved Rust tar/flate2 dependencies and owned-archive guard; this is not MBX export object storage or a new remote protocol. Root verified these existing dependencies in Cargo.toml. No new inner-packing tar/zstd executable requirement is introduced. A fixed short transport filename avoids outer member-name variability. Put the compatibility/source manifest inside the payload so the action's sole input is one regular file. The path must be stable between save and restore because it affects the GitHub cache version.

Freeze after the last required producer command, complete the inner archive, compute its exact file size and digest, then admit it. No producer may mutate that file after measurement. This directly measures the actual payload and avoids walking a changing Cargo tree inside the action. Consumers first restore the payload and then use the existing validated extraction/restore boundary.

**The inner file size is still not GitHub's stored size.** The official action creates a second tar archive containing it and compresses that outer archive. The API later reports the outer stored size. Recompression may save a little or expand; do not claim equal sizes or zero overhead.

### C. Measure an “exact” outer tar in advance, then invoke actions/cache

Do not describe this as exact upload measurement. The action will create another archive. POSIX timestamps/metadata, environment, archiver/compressor version and scheduling can differ. Even when practical results match, the two files are not the same object handed to the uploader. Supplying a prepared outer tar to actions/cache simply creates another wrapping layer.

Running a preflight wrapper measurement is useful for qualification and calibration. It cannot replace a proven upper bound with an equality claim.

## 4. Concrete outer-envelope measurement protocol

This is an unresolved enablement gate, not a numeric bound invented by this review.

For each immutable inner payload, apply this one protocol; do not use competing estimated-size modes.

1. Finish and close the inner tar.gz using existing Rust libraries. Record exact payload length p, its digest, logical uncompressed member size/count, fixed short relative transport filename and manifest identity. No build/writer process can modify this file afterward.
2. Record the actual runner image, OS/architecture, action SHA, detected tar implementation/version, compressor implementation/version and relevant environment. Match the approved packaging environment exactly. Unknown environment disables save. The inner encoder does not depend on these executables; they are already required by the official action's outer packaging.
3. In a disposable directory on the same filesystem, generate one preflight outer archive using the actual tar/compressor selected by the pinned action and the same arguments, working directory, fixed single-member manifest, path spelling and approved environment. For the Linux GNU-tar/zstd path inspected, the action uses POSIX tar with a files-from manifest, workspace-relative member and zstdmt. Do not change compression levels or disable compression for the measurement.
4. Measure that completed preflight outer file's actual bytes m. Delete the preflight copy before invoking actions/cache so it does not add a third concurrent archive. This is an exact measurement of the preflight file, not a claim that the action later uploads that identical file.
5. Calculate B=m+delta, where delta is the preapproved maximum repack difference for that exact environment/fixed member shape. The allowance must document how outer metadata/padding and compressor streaming behavior are bounded, with paired preflight-versus-action observations to validate the model. A sample maximum alone is an empirical estimate, not a mathematical upper bound. If no defensible allowance exists, mark the envelope unqualified and skip publication.
6. Re-read complete inventory immediately before action save while still holding the repository writer group. Evaluate I+R+B against the current operating ceiling. A missing page, unresolved older writer, unknown setting, or insufficient disk/overlap causes optional save to be skipped.
7. After upload, compare the exact API size_in_bytes with B and the preflight m, perform empty-path readback/hash/manifest verification, and only then prune predecessors. An underbound is a qualification failure and disables future publication under that environment; it never licenses deleting the predecessor or retroactively calling admission correct.

For notation:

    B = m + delta(runtime, action pin, fixed member shape)

Qualification includes representative real source/tool/state payloads and incompressible already-compressed inputs at the largest proposed envelope, repeated packaging with the allowed metadata variations, and comparison of action upload logs to API integer byte sizes. These observations verify that the model applies; they do not replace its conservative basis. No installed library/tool/action is added. The optional preflight pays a second outer-compression pass but avoids a bespoke transport.

The fixed wrapper must account for its file header, any POSIX extended metadata,512-byte file padding, terminal blocks, record padding, compressor framing, worst-case expansion and relevant multithread/streaming behavior. Only the supported action environment is qualified. This review does not supply a numeric delta because actual runner tool versions and paired archive measurements are absent. **Until those exist, publication is disabled and qualification remains blocked; ordinary CI remains cold-correct.**

**Do not substitute p, p+1%, or p+1MiB and call it rigorous.** These may be reasonable engineering allowances after measurement, but they are not proven bounds as stated.

The official Zstandard manual labels ZSTD_compressBound as a worst-case **single-pass** bound. The upstream implementation explicitly warns that streaming flush/block overhead can exceed it. The pinned action invokes the CLI through tar using zstdmt (or platform alternatives), so applying the one-pass formula to that stream without proving the relevant CLI behavior is invalid. No new library call or tool should be added to bypass this distinction.

A valid rollout has two honest choices. The recommended strict Velnor policy keeps saves disabled for an unqualified envelope. If the project instead chooses a measured engineering margin, describe admission as best-effort and retain the10GB GitHub eviction setting; do not promote that to a hard pre-upload proof. This review recommends the former.

Important scope: the action version is pinned, but hosted runner image tools can change. The qualification key must include or explicitly recognize the archiver/compressor environment that underlies U. Unknown environment means optional publication skipped, not failure of required CI.

## 5. Runner disk and time

Repository quota and runner disk are different resources. Standard GitHub-hosted runners advertise14GB SSD, which is not a promise that14GB is free when a job begins.

Let:

- E = all live extracted families and workspace/build output.
- p = inner compressed archive.
- U = outer candidate archive bound.
- Q = any retained local predecessor/archive or validation extraction.
- D = other job/runner temporary files plus a free-space reserve.

Conservative packaging peak:

    E + p + U + Q + D

On platforms whose action pipeline first emits an uncompressed outer tar, add that intermediate tar too. The pinned Windows BSD-tar workaround has such a separate stage. Do not reuse the Linux disk model unmodified.

Stream the inner tar into the existing flate2 gzip encoder rather than materializing an extra uncompressed whole-tree tar. Pack/upload/readback one family at a time; remove disposable local archive copies promptly; never delete live source/target state merely to pretend a disk measurement fits. During restore, account for downloaded outer archive + restored inner archive + extracted state; the official action removes its temporary archive after its extraction step, but inner extraction still needs its own free-space headroom.

A full second target-directory extraction for verification can nearly double E. It is unnecessary for every publication if the same job already validated the producer state and verifies archive digest+manifest after actual remote readback. Separate fresh-run engine qualification must still demonstrate that the complete state is reusable and contained.

Measure wall time as:

    build + inner pack + preflight outer pack + action outer pack + upload + readback download +
    hash/manifest verification + optional inner extraction

This includes a full extra readback transfer. Combined jobs reduce persistent duplicate output but extend wall time. No design should promise speedup until measured against ordinary cold runs, and every combined job's cold path must remain within the hosted six-hour limit. Mandatory package commands cannot be skipped to fit a cache budget.

## 6. Replacement lifecycle without a new receipt service

Use one job-wide repository concurrency group for every write-capable cache job, queue:max, cancel-in-progress:false. This serializes cooperating producers/pruners; it does not create global atomicity. A writer needing readback uses cache-mode:write, not write-only, and GITHUB_TOKEN contents:read/actions:read. It receives no Actions:write deletion permission.

Within that job:

1. Finish required producer commands and create the frozen payload.
2. Confirm current runtime's U; read full inventory/settings; include migration/in-flight bytes; admit old+new+headroom.
3. Save under its deterministic immutable candidate key with the existing pinned action.
4. Query inventory for the exact key/ref/version, while treating an existing entry separately from an upload by this attempt.
5. Remove only the local transport archive; keep the expected digest/manifest identity in job memory/output.
6. Perform a real exact restore into the now-empty fixed transport path; require exact matched key and verify payload digest/inner manifest.
7. Reconcile actual API size_in_bytes against U and the repository inventory. If actual exceeds U, disable subsequent saves for this runtime, retain prior baseline and report the model violation.
8. Emit the verified replacement tuple and exact observed predecessor IDs through existing report/control metadata. A separate checkout-free cleanup job with Actions:write and cache-mode:none enters the same group, rechecks replacement presence/ownership/current active intent, and deletes only still-eligible IDs. It then re-inventories. Failed or delayed cleanup retains both entries and blocks future candidates if necessary.

This is an actual fresh local-path remote readback, not lookup-only or a restore that can accidentally inspect the preexisting local archive. The writer keeps the cooperation group active through verification but does not receive Actions:write; cleanup runs separately with deletion authority and no checkout/compiler execution. No durable “verified” pointer service is needed. Queue adjacency is not guaranteed; subsequent writers charge full inventory while cleanup waits. A separate fresh-job/cross-run restore remains a release qualification test for engine portability.

If a save appears successful but inventory/readback cannot confirm it, keep the previous generation. A timeout or API failure cannot authorize deletion. If a new generation is good but cleanup fails, charge both. If one unverified candidate already consumes the group's provisional slot, retry verification or remove that exact abandoned candidate under the trusted policy before minting another; do not emit run-ID keys.

## 7. Migration and external pressure

Before enabling publishers:

- Inventory every prefix/ref/version, including legacy MBX exports, source caches, existing Cargo targets, tool snapshots and PR caches.
- Disable/drain old write-capable workflows and obsolete in-flight jobs. The new concurrency group does not govern an old workflow that lacks it.
- Restore-only consumers need not be drained for byte admission, although deleting an archive can race a reader. Cold fallback must handle that.
- Delete only specifically owned superseded/migration entries with an approved retention policy; do not remove foreign caches solely to make the new design look under budget.
- A10GB settings check cannot establish repository usage. A delayed aggregate usage endpoint cannot replace a paginated byte inventory.
- Known foreign occupancy is charged fully. Unbounded foreign writes cannot be made safe by choosing a fixed H from historical variation. That is a governance prerequisite or an explicitly accepted best-effort exposure.

If current inventory plus the replacement cannot fit while retaining the predecessor, skip the replacement. Do not delete the only useful predecessor first. If the new state is required for correctness, cache storage is the wrong dependency: required CI must build it cold.

## 8. Decisions for the root design

| Question | Decision |
|---|---|
| PR/merge/tag/preview publication | None; explicit read-only tokens. |
| Persistent MBX objects/exports | None; avoid storing a second representation of the same computation. |
| Cache packaging policy | One frozen standard tar.gz payload from existing Rust tar/flate2 per admitted family/group; official action transports it. |
| Pre-upload storage unit | Qualified upper bound of outer stored archive, not inner bytes or du. |
| Unknown U/runtime/inventory | Skip publication; required CI stays cold-correct. |
| Retention | One current entry; one predecessor only until actual readback verifies replacement; count both meanwhile. |
| Replacement proof | Empty-path real restore + digest/manifest; exact API ref/key/version/bytes; no save output claim. |
| Coordination | Same repository group for all writer-capable jobs, queue:max/cancel:false; not a distributed lock. |
| Operating threshold | Provisional8e9 operating ceiling/≥2e9 reserve, tightened using actual foreign/in-flight/drift and replacement envelopes;8GB is not a fit claim. |
| Fit claim | Not established for any target repository by this review. |
| Absolute instantaneous10GB claim | Impossible to establish from these APIs/action alone, even with exact archive measurement. |

## Sources and source limitations

1. Pinned actions/cache executable at55cc8345863c7cc4c66a329aec7e433d2d1c52a9, save-only blob b3a8aa37f9f7a608d7d5a63a8990b1fd4c043759. Its tar command uses --posix and packages paths internally; v2 saves/finalizes the internally produced byte size. https://github.com/actions/cache/blob/55cc8345863c7cc4c66a329aec7e433d2d1c52a9/dist/save-only/index.js
2. GitHub dependency caching reference (opened2026-10-25): retention, save-before-eviction and default10GB; web ref turn40view0. https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching
3. GitHub cache REST reference (opened2026-10-25): integer stored sizes, pagination, delayed aggregate usage, management permissions; turn42view0. https://docs.github.com/en/rest/actions/cache
4. GitHub runner specifications and Actions limits (opened2026-10-25):14GB advertised standard SSD and six-hour hosted jobs; turn47view3/turn42view1. https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job and https://docs.github.com/en/actions/reference/limits
5. Zstandard1.5.7 official API manual (opened2026-10-25), single-pass scope of compressBound; turn56view0. https://facebook.github.io/zstd/doc/api_manual_latest.html
6. Upstream zstd compression implementation (opened2026-10-25), streaming/flush caveat; turn56view1. https://github.com/facebook/zstd/blob/dev/lib/compress/zstd_compress.c
7. Current upstream zstd CLI programs/fileio.c was inspected via official GitHub connector; it drives streaming compression. This dev source is not proof of the actual hosted runner binary/version. https://github.com/facebook/zstd/blob/dev/programs/fileio.c

No actual runner tar/zstd versions, strict outer-size bound, repository inventory, complete source/state sizes, live peak disk or end-to-end timing were established. That is why publication remains qualification-gated. The provisional8e9 ceiling is a chosen policy and must be tightened if measured envelopes/pressure require it; it is not a validated capacity result.


## Frozen command-lane scope

Root’s initial Cargo state preserves separate build/test, clippy and doc lanes, bundled with an authenticated tracked-input source projection and real metadata for workspace/path dependencies. Charge every lane’s complete target/build directory in the inner payload; sharing a transport file does not deduplicate bytes. Do not delete a lane, trim incremental data or alter Cargo command semantics merely to meet the threshold. If this complete state cannot fit with sources/tools/predecessor/reserve, decline its cache publication and report the measured capacity result. A later lane consolidation requires semantic evidence independent of this capacity review.

## Reader plus conditional fallback writer refinement

The refined topology is compatible with this capacity policy: a read-only combined job restores and validates the complete state before deciding whether to execute; when a trusted default run lacks required cache state, it exits with a needs_prepare control result before running any package commands; a separate serialized writer rechecks and executes the exact suite. PR/tag/preview/merge consumers recover cold in their read-only jobs. No cache bytes move through workflow artifacts.

The reader must validate actual restored payloads, not lookup-only presence. The writer takes the common group before its new inventory/admission check. If another writer populated the state while it waited, it still executes this run’s required suite and simply skips redundant publication. Reader and writer must not both execute or both omit the suite; final required-check aggregation needs outcome-aware handling of a skipped fallback and one complete expected unit ledger. Matrix outputs cannot be treated as a reliable aggregate if multiple children reuse the same output name.

Cache-mode restrictions on reusable calls need explicit split: a reader caller capped at read cannot call a writer callee requesting write. Place the concurrency group on the actual mutation-owning job, not simultaneously on a waiting caller and its nested writer, which could self-block. All bootstrap/pruning publishers must use the same repository group. The extra conditional job per group counts toward the real generated topology and queue pressure; queue:max still has100 waiting slots and is not lossless.

A cache service outage that causes many default readers to request preparation can serialize otherwise independent work. The writer needs a defined cache-unavailable outcome: execute required work cold, skip unqualified save, and return the normal complete unit ledger. Cache publication must not become a correctness prerequisite or a reason to alter mandatory commands. The qualification benchmark must report both steady warm behavior and this outage/cold queue behavior.

Root accepted checkout-free per-group cleanup after this review. The compiler job remains Actions:read; only cleanup holds Actions:write. Cleanup lag, concurrent outstanding replacements and stale-plan active-coverage checks must be charged/qualified; never credit proposed deletion.

Stale intent guard: accept unchanged default HEAD directly; otherwise recompute current desired compatibility/coverage using existing pure planning/input-identity code against accepted default source, without executing tasks. Mutate only still-active/still-superseded identities. An unavailable intent check or retired coverage skips publication/cleanup; required checks continue. Application-only HEAD changes do not by themselves retire the dependency generation. Never infer current identity from created_at.
