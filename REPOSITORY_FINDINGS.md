# ChainArgos current repository evidence — GitHub-only cache redesign

Read-only inspection on 2026-10-25. This report records current source and available historical executions; it does not propose task sequencing, modify repositories, dispatch runs, delete caches, change settings, or purchase capacity.

## Coverage and access

All seven named repositories are now accessible through the connected GitHub app. Repository metadata reports private visibility, pull/push/maintain permissions, and admin=false. The earlier four-service 404 results are historical access results and must not be carried forward as current absence. All seven current default branches contain Rust projects generated with Velnor Actions 0.1.41 at upstream release commit `90e7d4dda2925dc22308ec48f6c09c1876dc4997`.

| Repository | Current source commit | Available runs | Current Rust crates |
|---|---|---:|---:|
| bitcoin-grpc-server | [cd0a5bfb9253](https://github.com/ChainArgos/bitcoin-grpc-server/commit/cd0a5bfb92538c230d1762b0ab7fafb52282fc33) | 41 | 2 |
| bitcoin-processor-rust | [d9115d1d42c8](https://github.com/ChainArgos/bitcoin-processor-rust/commit/d9115d1d42c881b23e6a5dd2f0dcd2dab5f3babd) | 26 | 4 |
| blockchain-explorer | [4b9fc98f2970](https://github.com/ChainArgos/blockchain-explorer/commit/4b9fc98f29705541d74e181dcc52c717c21e6075) | 25 | 1 |
| eth-grpc-server | [4b97aa1a0cf8](https://github.com/ChainArgos/eth-grpc-server/commit/4b97aa1a0cf8c15f7a2ab75435c7c6da270b2ea6) | 28 | 2 |
| eth-processor-rust | [c08aa7d5232e](https://github.com/ChainArgos/eth-processor-rust/commit/c08aa7d5232e43466fcfd4fa6929ef7dec7bb76c) | 25 | 4 |
| tron-grpc-server | [9143caa03214](https://github.com/ChainArgos/tron-grpc-server/commit/9143caa0321469ca6627a9feb638e20da714dcb5) | 31 | 2 |
| tron-processor-rust | [0e2a1050b342](https://github.com/ChainArgos/tron-processor-rust/commit/0e2a1050b34284530047a49d9a65fff333cecaed) | 25 | 4 |

The repository run listings were requested with `per_page=50`; every total is below 50 and all reported records were returned. They contain only `push` and `pull_request` events. Current workflow trees contain `ci.yml` and `cache-prune.yml`. `merge_group` is configured in current CI but has no observed execution in these complete available listings. One retired publication workflow is discussed below. These listings do not establish that deleted/expired executions never existed.

The chosen current candidates are the latest PR execution and the subsequent merged-main push for every repository. All are attempt 1. Every job and step was retrieved with the attempt-specific jobs endpoint and `per_page=100`; the largest pipeline has nine jobs. Seven latest prune executions and the one available historical publication execution were also captured. Total evidence: **22 executions, 117 jobs, 2,727 step records, 82 full job logs, and 223 pinned source files**. Full logs are compressed as `job-<id>.log.gz`; the historical publication logs are plain `.log`. The other 35 jobs are skipped seeds or required-verdict/gate jobs, whose full step metadata is present; their logs were not needed for cache claims.

Cache inventory, usage, and settings URLs were rejected by the connector URL allowlist with HTTP 400 before a repository permission check. `cache-probes.json` preserves this limitation. These results are not GitHub 403 permission denials and do not demonstrate that caches or settings are absent. Current total stored bytes, cache counts, eviction history, configured purchased capacity, and billing usage remain unknown.

## Selected execution comparison

These are **source/tool-warm, persistent-MBX-cold candidates**, not a controlled cold/warm benchmark. Every relevant selected current job reports `sources hit, skipping fetch` and `sources downloaded=0`, while all 45 selected Rust/seed jobs report an MBX bundle miss. PR and push have different head SHAs and different job sets. Their timing difference is not attributable to cache efficacy.

Times below are run-created to the last selected pipeline job end, including optional seed tails. Summed job time is the sum of observed non-skipped job start/end intervals, not billed minutes. Each linked execution includes all its jobs in the evidence.

| Repository | PR run / wall | Push run / wall | PR / push summed job time | Push seed time | Seed export reported by MBX |
|---|---|---|---|---|---|
| bitcoin-grpc-server | [39884632686](https://github.com/ChainArgos/bitcoin-grpc-server/actions/runs/39884632686) / 5:10 | [39885224758](https://github.com/ChainArgos/bitcoin-grpc-server/actions/runs/39885224758) / 5:37 | 6:21 / 10:54 | [4:06](https://github.com/ChainArgos/bitcoin-grpc-server/actions/runs/39885224758/job/120192041513) | 953.8 MiB; save refused |
| bitcoin-processor-rust | [39883761013](https://github.com/ChainArgos/bitcoin-processor-rust/actions/runs/39883761013) / 12:54 | [39885044506](https://github.com/ChainArgos/bitcoin-processor-rust/actions/runs/39885044506) / 13:06 | 22:10 / 33:39 | [11:49](https://github.com/ChainArgos/bitcoin-processor-rust/actions/runs/39885044506/job/120191516239) | 3.0 GiB; save refused |
| blockchain-explorer | [39886098283](https://github.com/ChainArgos/blockchain-explorer/actions/runs/39886098283) / 14:26 | [39887554049](https://github.com/ChainArgos/blockchain-explorer/actions/runs/39887554049) / 14:16 | 14:30 / 24:22 | [13:04](https://github.com/ChainArgos/blockchain-explorer/actions/runs/39887554049/job/120199531751) | 3.3 GiB; save refused |
| eth-grpc-server | [39884643630](https://github.com/ChainArgos/eth-grpc-server/actions/runs/39884643630) / 12:46 | [39885911570](https://github.com/ChainArgos/eth-grpc-server/actions/runs/39885911570) / 13:12 | 14:08 / 23:55 | [9:24](https://github.com/ChainArgos/eth-grpc-server/actions/runs/39885911570/job/120194263371) | 3.1 GiB; save refused |
| eth-processor-rust | [39883770173](https://github.com/ChainArgos/eth-processor-rust/actions/runs/39883770173) / 14:05 | [39885149307](https://github.com/ChainArgos/eth-processor-rust/actions/runs/39885149307) / 18:15 | 23:25 / 38:21 | [9:42](https://github.com/ChainArgos/eth-processor-rust/actions/runs/39885149307/job/120191891359) | 3.3 GiB; save refused |
| tron-grpc-server | [39884653246](https://github.com/ChainArgos/tron-grpc-server/actions/runs/39884653246) / 12:43 | [39885921996](https://github.com/ChainArgos/tron-grpc-server/actions/runs/39885921996) / 10:48 | 14:05 / 20:27 | [8:26](https://github.com/ChainArgos/tron-grpc-server/actions/runs/39885921996/job/120194343363) | 3.0 GiB; save refused |
| tron-processor-rust | [39883783663](https://github.com/ChainArgos/tron-processor-rust/actions/runs/39883783663) / 13:21 | [39885158639](https://github.com/ChainArgos/tron-processor-rust/actions/runs/39885158639) / 13:55 | 22:23 / 36:06 | [12:12](https://github.com/ChainArgos/tron-processor-rust/actions/runs/39885158639/job/120191915927) | 3.1 GiB; save refused |

**All seven seed exports exceed the current 384 MiB family ceiling and are discarded.** The source uses `du -sk` of the exported directory, rejects above 393,216 KiB, and does not upload the bundle. The native MBX export messages above describe local exported data, not compressed GitHub cache storage. A family ceiling of 384 MiB is neither a total repository storage limit nor evidence that 384 MiB is currently stored.

The seed and consumers all depend on `Plan`; consumers do not depend on the seed. A new seed cannot warm consumers that restore concurrently in that execution. The optional seed is also excluded from the Required verdict dependency set. For explorer, Required finishes at 02:15:35 while the seed ends at 02:18:38; workflow wall time and required-check latency therefore answer different questions.

Native MBX statistics distinguish hits, misses, not-looked-up actions, bypasses, and local storage. In explorer seed, the first test lane reports 0 hits, 0 misses, 567 not looked up, 7 bypassed; its later documentation lane reports 292 hits, 28 misses, 91 not looked up, 6 bypassed. Those later hits occur inside the same job after earlier compilation, despite the persistent bundle miss. Similar same-job reuse appears in every seed. Neither `0 misses` nor a later positive hit count establishes cross-run warmth. `jobs-summary.json` retains every native MBX summary.

Cargo `Compiling` message counts are retained only as `compiling_message_count`. They are not actual rustc invocation counts. Actual compiler invocations, native compiler work, codegen reuse boundaries, and paid/billed minutes are unknown. No `Compiling` count is presented as a speedup measurement.

## Current storage families and policy

| Family | Observed current behavior | Scope and gap |
|---|---|---|
| Cargo source archives | Registry index, registry cache, Cargo git database; exact lock snapshot plus trusted prefix fallback. All selected jobs hit already-existing archives. | Sources writer is Plan. Protected default-branch pushes write trusted keys; nonfork PRs may write separate PR keys. PR snapshot fallback to identical trusted snapshot suppresses redundant save. No expanded registry `src`, target output, or private extracted release assets are in the cache paths. |
| Mise / Rust tools | Four distinct identities for lint, Plan, seed, and Rust execution. Restore requires an exact cache hit or separately validated seed. Existing mise action automatic cache is disabled. | Saved tree includes mise installation data and, where present, Rustup/Cargo bins. Tool caches are not pruned by the current generated prune workflow. They replicate substantial Rust material across identities and repositories. |
| MBX object bundles | Official MBX action with local backend, action-owned native MBX 1.26.0, export group `velnor`, 384 MiB directory ceiling; seed-only export/save. | All selected persistent restores miss; all seven seed exports exceed ceiling. Consumer outputs are cleaned, never exported by current consumers. Same compatibility identity is used across workspace crate jobs within a repository, but GitHub storage remains repo-scoped. |
| Native/build-script/codegen outputs | Generated CI sets `MBX_BUILD_SCRIPT_EXECUTION=0`, `MBX_CC=0`, `MBX_SHARE_OUT_DIR=0`, `MBX_GC_AUTO=0`. | These settings are not evidence that native/codegen work is absent. Crate sources and lockfiles include native dependencies and protobuf/codegen build scripts. Current evidence cannot justify forcing broader reuse without a compatible identity and native MBX support. |
| Test container images | Existing tests use Testcontainers. Postgres is explicitly `18-alpine`; processors also use RabbitMQ and ETH/TRON use Redis defaults from the pinned module version. | No current image cache restore/save or Docker-layer cache appears in these generated workflows. Actual pulled image digests, bytes, and durations are not measured by this evidence. No image-cache budget can be inferred from absent Dockerfiles. |
| Other dependency families | No current Bun, Python venv, Tofu provider, dbt, Ansible or Playwright task/cache consumer appears in these seven projects. Existing generic prune code nevertheless includes their prefixes. | They are dormant here, not absent from Velnor or from other repositories. Root analysis must include active families elsewhere. Python helper scripts and ruff/tool pins do not make a current Python venv cache. |
| Workflow artifacts | Plan and diagnostic/crate/final report artifacts are uploaded/downloaded. | They carry orchestration and reports. No inspected current workflow uses Actions artifacts to transfer dependencies or compiled output. Report retention is 30 days and is distinct from dependency-cache storage. |

Current prune retains 3 source and Tofu snapshots, 2 Bun/Playwright/dbt/Python/Ansible snapshots, and 1 MBX snapshot per compatibility group on the current trusted ref. It requests up to 1,000 cache records by each named key prefix. It does not prune Mise identities, PR source keys, or retired compatibility groups, and does not total bytes. The latest prune logs show no deletions and no printed inventory. Thus current pruning cannot prove a hard aggregate 10 GB bound.

### Restored archive sizes (not inventory totals)

Each repository restored four distinct tool archives and one source archive in the chosen executions. The tools are approximately 65 MB lint, 352 MB Plan, 348 MB seed, and 359 MB Rust (decimal bytes rounded). The following exact source archive bytes came from `actions/cache` restore logs. They are transfer/archive observations, not a fresh account inventory:

| Repository | Observed source archive bytes | Unique observed tools + source archive bytes |
|---|---:|---:|
| bitcoin-grpc-server | 132,583,887 | 1,256,630,728 |
| bitcoin-processor-rust | 112,810,554 | 1,236,902,711 |
| blockchain-explorer | 115,877,889 | 1,240,054,926 |
| eth-grpc-server | 110,667,874 | 1,234,711,274 |
| eth-processor-rust | 113,543,918 | 1,237,412,710 |
| tron-grpc-server | 110,307,111 | 1,234,406,153 |
| tron-processor-rust | 113,522,727 | 1,237,576,104 |

The summed observation deduplicates by restored key, but cache versions, old keys, PR scopes, other compatibility identities, and any concurrent/current changes are not inventoried. It must not be used as the current total or as evidence of spare paid capacity.

## Build and dependency variants that must survive migration

All current workers run `ubuntu-26.04`; Rust is pinned at 1.99.1, MBX at 1.26.0, cargo-nextest at 0.9.149, jactionlint at 2.3.0, shellcheck at 0.11.0, and mise action at version 2026.10.17. `mise.toml` declares both aarch64 and x86_64 Linux Rust targets; the current generated task manifest does not execute a cross-target/release matrix. An installed target is not an observed product build.

Every crate has six declared default tasks: build/list Nextest binaries with Nextest `ci` profile, format, Clippy all-targets with warnings denied, Nextest tests with `ci` profile, doctests, and docs with warnings denied. Clippy uses `target/velnor-clippy`; docs use `target/velnor-doc`; tests/doctests use the normal target context. The workspace seed compiles test binaries, Clippy, and docs for the workspace; the consumer tasks select individual packages. Feature unification and command/profile distinctions must therefore be kept in identity or proven safely reusable by MBX. Nextest `ci` is a test-runner profile, not a Cargo release profile.

| Repository group | Existing distinguishing inputs |
|---|---|
| Explorer | One crate; GraphQL Cynic schema/query codegen and protobuf clients. Private build/dev dependencies span grpc servers, legacy migration, ETH migration; release assets are legacy migrations and ETH SQL. |
| ETH/TRON gRPC | Two crates each (server + proto). Tonic/prost and protify validation codegen uses checked-in `proto`/`proto_deps`, vendored protoc, and a child process carrying PROTOC. Private migration crate and SQL release asset. |
| Bitcoin gRPC | Two crates; protobuf codegen with vendored protoc. No configured private-source section. `[profile.dev] debug="line-tables-only"` and dependencies `debug=false`; unlike the other six, no explicit test-profile override. |
| Three processors | Four crates each (app, model proto, migrations, fixtures). Locked private `processor-shared-rust` dependencies and existing `amq-protocol-types` git patch; existing patch is unrelated to MBX. Four release-asset bundles each: chain protos, SQL, fixtures, shared tailrocks protos. Existing native-tls/OpenSSL, aws-lc test dependencies, and ETH/TRON zstd variants remain relevant. |
| ETH/TRON processors | `test-helpers` feature declared and enabled by self dev-dependency; Redis-enabled integration tests. All processor and explorer/ETH/TRON server test profiles set debug=0 and incremental=false. |

All codegen uses the existing `protoc-bin-vendored = 3.3.0` dependency. This is pre-existing application configuration and is not a proposal to vendor or patch MBX. Private release assets are pinned by commit and SHA-256 in `.velnor/deps.lock`, fetched into `.velnor/deps/<extract_to>`, and are not a new external storage/cache service. Their source identities must remain in an immutable content key if their reuse is designed.

Current tests use `test-threads=2` in the Nextest CI profile; comments still mention sccache, but generated task execution uses native MBX. Comments are not evidence that sccache executes.

## Generator ownership and exact migration surfaces

All seven `.github/AGENTS.md` files state that Velnor owns its declared outputs, the complete `.github/workflows/` namespace, and marked shared action definitions. A generic cache change must be made upstream, released, then consumed through the existing generation inputs. Do not hand-edit generated workflows or insert repository-specific shims. The upstream implementation mapping belongs in the integrated root design; this repository evidence records the consuming surfaces.

Repository inputs outside `.github/`: `.velnor/config.toml`, `.velnor/deps.lock` where present, `.velnor/release-manifest.json` for the attested release asset, `Cargo.toml`/workspace manifests, `Cargo.lock`, `mise.toml`, `mise.lock`, `rust-toolchain.toml`, `build.rs`/codegen inputs, `.config/nextest.toml`, `.cargo/config.toml` (six projects), and existing private-source pins. Keep project semantics and current tool/action versions unless the integrated design explicitly requires a supported existing change.

Current emitted paths to regenerate include `.github/workflows/ci.yml`, `.github/workflows/cache-prune.yml`, `.github/actions/declared-task-0/action.yml`, `.github/actions/u26/action.yml`, `.github/actions/velnor-tool-seed/action.yml`, `.github/actions/velnor-tools-cache-restore/action.yml`, `.github/actions/velnor-tools-prelude-u26/action.yml`, `.github/scripts/velnor-tools-cache-identity.sh`, `.github/velnor/task-execution-manifest-v1.json`, and generated `.github/AGENTS.md`/`CLAUDE.md`/lint configuration. Their file headers all identify 0.1.41. Exact pinned URLs and blob SHAs for every fetched file are in `source-manifest.json`.

No task plan should be derived merely by increasing the 384 MiB cap. A GitHub-only replacement must bound every writer and compatibility generation together, account for immutable-key overlap and old/PR/tool entries, preserve current command/feature/native identity, and measure persistent warm reuse before making performance claims. The present source makes no aggregate admission check. No execution or mutation is authorized by this report.

## Actual historical publication product

Bitcoin gRPC has one available [Velnor Publish run 39512990012](https://github.com/ChainArgos/bitcoin-grpc-server/actions/runs/39512990012), push attempt 1, at commit `c0842d3d132207fec7485807b15cd1afdf2120a9` on 2026-10-20. Its pinned [publish.yml](https://github.com/ChainArgos/bitcoin-grpc-server/blob/c0842d3d132207fec7485807b15cd1afdf2120a9/.github/workflows/publish.yml) was generated by 0.1.31. Both jobs are captured: default-branch authority succeeded; Create tags and releases failed because release-plz received GitHub 403 when reading commit-associated PRs. That historical execution does not demonstrate successful binary release or a compiled release-cache lane. The current 0.1.41 tree has no publish workflow. No other publication/release run is present in the seven complete available listings.

## Evidence index

- `source-manifest.json`: repo/path/current source commit/Git blob SHA/local SHA-256/source URL for 223 fetched files.
- `<repo>/repo.json`, `head.json`, `tree.json`, `runs.json`: current access metadata, pinned head, complete tree, and complete available run list.
- `<repo>/source/`: pinned source snapshots; no repository write was made.
- `<repo>/runs/<run>/jobs.json`: complete run identity plus every job and step for the selected attempt.
- `<repo>/runs/<run>/job-<job>.log.gz`: full inspected logs; companion `*-evidence.json` holds searchable selected lines and original line numbers. The full gzip is authoritative if extraction filters omit a line.
- `pipelines.json` / `.csv`: run identity, event, attempt, SHA, all-job wall and sum, required-gate latency.
- `jobs-summary.json`: per-job timing, Cargo message counts explicitly labeled, native MBX stats, persistent bundle misses, export observations, restored archive sizes.
- `steps.json` / `.csv`: all 2,727 recorded step summaries and durations.
- `repository-facts.json`: task argv/env, feature/profile/workspace/private-source variants.
- `cache-probes.json`: connector allowlist rejection; stored-byte/account-setting facts remain unknown.

Previously recovered processor evidence is not used as a substitute for fresh retrieval here. Current head/source/run/log retrieval independently confirms the same 0.1.41 behavior where the earlier observations overlap. No claimed improvement has been measured.

## Additional isolation and verification requirements from existing repositories

The six repositories with private sources use the configured variable `VELNOR_DEPS_APP_ID` and secret `VELNOR_DEPS_APP_PRIVATE_KEY` to mint a repository-scoped read-only contents token, fetch, and revoke it. The token is passed only to the private-fetch/revoke boundary. Ordinary compile commands explicitly unset GitHub/OIDC/runtime token variables. Bitcoin gRPC has no private-source configuration. Secret values were never read. A snapshot must preserve private source availability while excluding credential configuration/token material; it must not broaden the source audience beyond the repository's existing access rules.

Private fetch summaries report one Cargo root plus 2 assets for explorer, 1 asset each for ETH/TRON gRPC, and 4 assets each for the processors. They do not distinguish an actual network download from verified local presence; do not multiply these counts into claimed downloads or network bytes. `.cargo/config.toml` declares relative source paths and is now included in pinned evidence: explorer has `ETH_SQL_DIR` and `LEGACY_MIGRATIONS_DIR`; ETH/TRON gRPC have their chain SQL directory; processors have chain `*_MODEL_PROTO_DIR`, `*_SQL_DIR`, `*_PROCESSOR_FIXTURES_DIR`, plus `TAILROCKS_TYPE_PROTOS_DIR`. Those paths feed build scripts and migration/fixture code. Preserve their content identity and stable path mapping in a complete Cargo snapshot group.

Observed Linux compile diagnostics include `openssl-sys 0.9.117` in all seven main application jobs; the six projects other than Bitcoin gRPC also show `aws-lc-sys 0.46.0`, `cmake 0.1.58`, and `clang-sys 1.9.1`. ETH/TRON processors also show `zstd-sys 2.1.2+zstd.1.5.7`. This establishes relevant crate inputs, not exact system OpenSSL, C/C++, linker, libclang or CMake binary versions. The latter are not emitted as a complete native toolchain manifest and remain an identity/validation gap for a warm proof. Multi-platform vendored protoc package names appearing in a Linux Cargo log do not establish execution on those other architectures.

The selected existing task manifests are the authoritative verification command inventory. Commands are locked/offline and package-specific, with current warning policy preserved. The generic forms are: `mbx nextest list --profile ci --list-type binaries-only --locked --offline --manifest-path <manifest> --package <package>`; `mbx clippy --locked --offline --manifest-path <manifest> --package <package> --all-targets -- -D warnings`; `mbx nextest run --profile ci --locked --offline --manifest-path <manifest> --package <package>`; `mbx test --locked --offline --manifest-path <manifest> --package <package> --doc`; `mbx doc --locked --offline --manifest-path <manifest> --package <package> --no-deps`; and formatting. The complete argv, environment, matrix/execution digests and source links are saved, so implementation should derive commands from those entries rather than this prose shorthand.

Existing local repository gates are `hk check --all` through the pinned hk/mise configuration, `sh scripts/check-rust-toolchain-mirror.sh`, and clean `velnor-actions generate` output. The hk configuration includes Rust fmt/check/Clippy/deny, jactionlint, shellcheck, secret-scanning and owner-standard lint steps; explorer additionally has ruff steps. The generated Plan executes `Check generated files`. These commands were inspected, not executed in this planning-only audit. No new dependency, tool, action, workflow dispatch, or live experiment was introduced.

No current repository is blocked by inaccessible source or absent generator ownership. All seven have an explicit generator owner and supported input/config surfaces. A repository-specific edit to generated `.github` files would violate the existing ownership policy. The hard 10 GB acceptance check is blocked by unavailable live cache inventory/settings evidence, not by source access. Current evidence also cannot verify a proposed complete Cargo snapshot's compressed size, fresh-process warmth, native identity, or behavior after eviction; these are future validation obligations, not migration successes.
