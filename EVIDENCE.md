# Evidence and access

Observation date: 2026-10-25.
This audit is read-only. No workflow was dispatched and no cache or setting was changed.

## Scope

The evidence index contains **39 selected executions and 504 job records**.
It includes the four original Jackin executions and all jobs in each selected pipeline.
Current reinspection adds 35 selected executions and 373 job records.
The original four retain 131 job records and 125 previously retrieved executed logs.
Current work retrieved 322 relevant job logs: Jackin 158, Velnor 82, and ChainArgos 82.
Some ChainArgos verdict jobs were inspected through complete job/step metadata without fetching their logs.
No claim depends on uninspected child output in those jobs.

All nine repositories are now accessible.
Earlier service-repository HTTP 404 results remain historical access results.
They do not establish that a project or product was absent.

Cache inventory, usage, and settings requests fail through this connector's endpoint allowlist with HTTP 400.
This is not a repository permission denial.
Actual stored totals, configured allowance, retention setting, and paid usage remain unknown.
The plan does not authorize any increase or paid overflow.

## Current source revisions

| Repository | Current inspected source | Generator | Access |
|---|---|---|---|
| [jackin-project/jackin](https://github.com/jackin-project/jackin) | `faa2ab6c12e3de45a76ab6b98df0c64dac7aac6e` | 0.1.52 | source and selected jobs readable; public |
| [tailrocks/velnor-new](https://github.com/tailrocks/velnor-new) | `e851b39e3bedc664f8bd6470c629e7bac36c561c` | 0.1.53 | source and selected jobs readable; public |
| [ChainArgos/bitcoin-grpc-server](https://github.com/ChainArgos/bitcoin-grpc-server) | `cd0a5bfb92538c230d1762b0ab7fafb52282fc33` | 0.1.41 | source and selected jobs readable; private |
| [ChainArgos/bitcoin-processor-rust](https://github.com/ChainArgos/bitcoin-processor-rust) | `d9115d1d42c881b23e6a5dd2f0dcd2dab5f3babd` | 0.1.41 | source and selected jobs readable; private |
| [ChainArgos/blockchain-explorer](https://github.com/ChainArgos/blockchain-explorer) | `4b9fc98f29705541d74e181dcc52c717c21e6075` | 0.1.41 | source and selected jobs readable; private |
| [ChainArgos/eth-grpc-server](https://github.com/ChainArgos/eth-grpc-server) | `4b97aa1a0cf8c15f7a2ab75435c7c6da270b2ea6` | 0.1.41 | source and selected jobs readable; private |
| [ChainArgos/eth-processor-rust](https://github.com/ChainArgos/eth-processor-rust) | `c08aa7d5232e43466fcfd4fa6929ef7dec7bb76c` | 0.1.41 | source and selected jobs readable; private |
| [ChainArgos/tron-grpc-server](https://github.com/ChainArgos/tron-grpc-server) | `9143caa0321469ca6627a9feb638e20da714dcb5` | 0.1.41 | source and selected jobs readable; private |
| [ChainArgos/tron-processor-rust](https://github.com/ChainArgos/tron-processor-rust) | `0e2a1050b34284530047a49d9a65fff333cecaed` | 0.1.41 | source and selected jobs readable; private |

Current source means the pinned snapshot inspected during this audit.
Later commits can exist. Implementation must refresh the exact source and instructions.

## Original requested executions

The original preview 40076991878 used generator 0.1.48 at c98f5f5fdd831e6075e38fde93b9713575406140.
The original PR runs 40078359402 and 40078628319 also used 0.1.48.
The original main run 40078851667 used 0.1.52.
These generator headers were fetched again at each exact source revision.
Their earlier logs remain historical evidence, not current size measurements.

The preview had 11 jobs and 3,159 visible Cargo crate-download records.
The other three runs had 40 jobs each.
Their repeated Cargo progress messages cannot establish actual compiler-process counts.
Successful named checks could suppress child stdout and stderr.

## Current failure mechanisms

| Mechanism | Current evidence | Implication |
|---|---|---|
| Oversized export | Jackin rejects 7.5 GiB; Velnor rejects 4.0 GiB and 5.2 GiB; all seven ChainArgos seeds reject 953.8 MiB–3.3 GiB. | The 384 MiB raw-directory gate prevents publication. These are not stored archive sizes. |
| Producer race | Seeds and Rust consumers depend on Plan, not on each other. | A later seed cannot warm a consumer that already restored. |
| Sources without compiled state | Current Jackin and Velnor ordinary CI source probes are warm while compiled bundles miss. | Source success cannot establish compiler reuse. |
| Disposable homes | prepare_check creates private Cargo/tool homes and later removes them. | Outer restored paths can be unused by named/native children. |
| Immutable incomplete identity | Save suppression follows exact keys rather than complete requested coverage. | Key identity cannot establish output completeness. |
| Recipe mismatch | Seeds use workspace commands; consumers use package-specific commands. | Feature and compiler-action coverage can differ. |
| Repeated helpers | Current Velnor Plan and image candidate/attestation build source-bound control tools. | Whole-pipeline costs extend beyond crate jobs. |
| Hidden observations | Successful check_runtime children return evidence without their full output. | Absent diagnostics mean unknown work. |
| Fragmented budget | Current pruning omits Mise and qualification identities and uses per-family counts. | It does not establish repository-wide byte admission. |

Relevant current source: [check_prepare](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-orchestrator/src/check_prepare.rs), [seed planner](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-orchestrator/src/dependency_seed.rs), [cache family policy](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-contract/src/workflow/cache_family.rs), [pruning](https://github.com/tailrocks/velnor-new/blob/e851b39e3bedc664f8bd6470c629e7bac36c561c/crates/velnor-actions-workflow-renderer/src/cache_prune.rs).

## Jackin current sample

Main 40181913046 has 50 jobs and 42 ordinary Rust consumers.
All 42 consumers miss their MBX bundle.
The job-duration sum is 8,434 seconds; run creation to last job completion is 826 seconds.
The logs report 22,287,765,916 cache archive transfer bytes across the pipeline.
These are repeated network transfers, not repository occupancy or billed seconds.
The seed again rejects its displayed 7.5 GiB export.

Preview 40182853202 has 14 jobs, 11 executed logs, and three skips.
Its six native build jobs, assembly, signing, and publishing succeed.
A later tap-preparation job fails.
The logs contain 3,243 visible crate-download records.
Actual origin bytes and per-dependency compiler executions remain unknown.

The current config defines Jackin's four targets and Capsule's two Linux targets.
Preview and stable have different LTO settings.
The plan preserves those real variants and the native xcode-27-arm64 environment.
It does not treat absent successful stable evidence as an absent stable product.

Sources: [main](https://github.com/jackin-project/jackin/actions/runs/40181913046), [preview](https://github.com/jackin-project/jackin/actions/runs/40182853202), [current config](https://github.com/jackin-project/jackin/blob/faa2ab6c12e3de45a76ab6b98df0c64dac7aac6e/.velnor/config.toml), [profiles](https://github.com/jackin-project/jackin/blob/faa2ab6c12e3de45a76ab6b98df0c64dac7aac6e/Cargo.toml).

## Velnor current sample

The PR/main pair has 36 ordinary Rust consumers. All 36 miss the compiled bundle.
Root and nested-runner seeds reject displayed 4.0 GiB and 5.2 GiB exports.
The selected product release has 27 jobs and 2,934 visible crate-download records.
Of those records, 1,957 occur in four deliberate clean-qualification jobs.
The release fails in Homebrew macOS qualification. Three downstream jobs skip.
Preserve deliberate clean qualification and account for its separate work.

Image candidate and attestation each show 105 crate-download records and source-bound helper compilation diagnostics.
Current product-release attestation/publication jobs do not show the older audit's archive-guard compilation pattern.
Do not repeat that historical claim as a current observation.

Sources: [CI](https://github.com/tailrocks/velnor-new/actions/runs/40184071097), [product release](https://github.com/tailrocks/velnor-new/actions/runs/40185476122), [image candidate](https://github.com/tailrocks/velnor-new/actions/runs/40184071131).

## ChainArgos current sample

All seven projects are Rust projects with generator 0.1.41, Rust 1.99.1, MBX 1.26.0, and Nextest 0.9.149.
Their selected runs contain 45 Rust consumer/seed jobs; all 45 miss their compiled bundle.
All 59 source probes report hits and downloaded=0.
All seven seeds reject their exports before publication.
The fleet has 19 crates and six declared task families per crate.

Keep protobuf/codegen, OpenSSL, AWS-LC/CMake/clang, and applicable zstd inputs.
Keep ETH/TRON self dev-dependencies with test-helpers enabled.
Keep Bitcoin gRPC's distinct dev debug profile.
Keep six projects' private source and immutable asset identities.
Private-fetch summaries do not prove network download counts or bytes.
Testcontainers origins are present, but no current image-cache producer was observed in these workflows.

Current workflow trees contain CI and Cache prune.
Bitcoin gRPC also has a real historical Velnor Publish run 39512990012 at generator 0.1.31.
It fails on GitHub authorization while reading associated PRs.
Do not recreate this retired workflow or describe it as a successful binary release.

The detailed per-repository source, native-input, timing, and policy report is `REPOSITORY_FINDINGS.md`.

## Complete pipeline index

Every selected execution below has its complete job set in `evidence/jobs.json`.
Events are observed run events, not all configured triggers.
All selected executions are attempt 1. Rerun behavior remains future qualification.

| Repository | Run | Event | Attempt | Generator | Source SHA | Jobs |
|---|---|---|---:|---|---|---:|
| jackin-project/jackin | [40168639046](https://github.com/jackin-project/jackin/actions/runs/40168639046) | schedule | 1 | 0.1.52 | `1bfda388903865b65d028485b2878951937fe5e7` | 4 |
| jackin-project/jackin | [40170178415](https://github.com/jackin-project/jackin/actions/runs/40170178415) | schedule | 1 | 0.1.52 | `da22db16f5ae99afdc1f3ded10d8f8a55590a526` | 4 |
| jackin-project/jackin | [40175310710](https://github.com/jackin-project/jackin/actions/runs/40175310710) | push | 1 | 0.1.52 | `323fcd1bbd561eaccdb4cd8681f951696c54b398` | 45 |
| jackin-project/jackin | [40178992378](https://github.com/jackin-project/jackin/actions/runs/40178992378) | pull_request | 1 | 0.1.52 | `54d699725d0b153603dd5668de3bf78d7770c47f` | 50 |
| jackin-project/jackin | [40181913019](https://github.com/jackin-project/jackin/actions/runs/40181913019) | push | 1 | 0.1.52 | `faa2ab6c12e3de45a76ab6b98df0c64dac7aac6e` | 1 |
| jackin-project/jackin | [40181913046](https://github.com/jackin-project/jackin/actions/runs/40181913046) | push | 1 | 0.1.52 | `faa2ab6c12e3de45a76ab6b98df0c64dac7aac6e` | 50 |
| jackin-project/jackin | [40182853202](https://github.com/jackin-project/jackin/actions/runs/40182853202) | workflow_run | 1 | 0.1.52 | `faa2ab6c12e3de45a76ab6b98df0c64dac7aac6e` | 14 |
| tailrocks/velnor-new | [40184071097](https://github.com/tailrocks/velnor-new/actions/runs/40184071097) | push | 1 | 0.1.53 | `e851b39e3bedc664f8bd6470c629e7bac36c561c` | 28 |
| tailrocks/velnor-new | [40182223763](https://github.com/tailrocks/velnor-new/actions/runs/40182223763) | pull_request | 1 | 0.1.53 | `327170b1724eafcd0c966322d6454d2e0b4033a0` | 28 |
| tailrocks/velnor-new | [40185476122](https://github.com/tailrocks/velnor-new/actions/runs/40185476122) | workflow_dispatch | 1 | 0.1.53 | `e851b39e3bedc664f8bd6470c629e7bac36c561c` | 27 |
| tailrocks/velnor-new | [40184071131](https://github.com/tailrocks/velnor-new/actions/runs/40184071131) | push | 1 | 0.1.53 | `e851b39e3bedc664f8bd6470c629e7bac36c561c` | 3 |
| tailrocks/velnor-new | [40184071101](https://github.com/tailrocks/velnor-new/actions/runs/40184071101) | push | 1 | 0.1.53 | `e851b39e3bedc664f8bd6470c629e7bac36c561c` | 1 |
| tailrocks/velnor-new | [40184071655](https://github.com/tailrocks/velnor-new/actions/runs/40184071655) | pull_request | 1 | 0.1.53 | `327170b1724eafcd0c966322d6454d2e0b4033a0` | 1 |
| ChainArgos/bitcoin-grpc-server | [39512990012](https://github.com/ChainArgos/bitcoin-grpc-server/actions/runs/39512990012) | push | 1 | 0.1.31 | `c0842d3d132207fec7485807b15cd1afdf2120a9` | 2 |
| ChainArgos/bitcoin-grpc-server | [39884632686](https://github.com/ChainArgos/bitcoin-grpc-server/actions/runs/39884632686) | pull_request | 1 | 0.1.41 | `ba9dbb08044822a4e3232b7d1c917b3df8006211` | 7 |
| ChainArgos/bitcoin-grpc-server | [39885224739](https://github.com/ChainArgos/bitcoin-grpc-server/actions/runs/39885224739) | push | 1 | 0.1.41 | `cd0a5bfb92538c230d1762b0ab7fafb52282fc33` | 1 |
| ChainArgos/bitcoin-grpc-server | [39885224758](https://github.com/ChainArgos/bitcoin-grpc-server/actions/runs/39885224758) | push | 1 | 0.1.41 | `cd0a5bfb92538c230d1762b0ab7fafb52282fc33` | 7 |
| ChainArgos/bitcoin-processor-rust | [39883761013](https://github.com/ChainArgos/bitcoin-processor-rust/actions/runs/39883761013) | pull_request | 1 | 0.1.41 | `f12e8927e007a1097ddeb5f8f43956d0a1e93258` | 9 |
| ChainArgos/bitcoin-processor-rust | [39885044479](https://github.com/ChainArgos/bitcoin-processor-rust/actions/runs/39885044479) | push | 1 | 0.1.41 | `d9115d1d42c881b23e6a5dd2f0dcd2dab5f3babd` | 1 |
| ChainArgos/bitcoin-processor-rust | [39885044506](https://github.com/ChainArgos/bitcoin-processor-rust/actions/runs/39885044506) | push | 1 | 0.1.41 | `d9115d1d42c881b23e6a5dd2f0dcd2dab5f3babd` | 9 |
| ChainArgos/blockchain-explorer | [39886098283](https://github.com/ChainArgos/blockchain-explorer/actions/runs/39886098283) | pull_request | 1 | 0.1.41 | `cc62973ea0482f483c6d472a246f23bdb39d148a` | 6 |
| ChainArgos/blockchain-explorer | [39887554049](https://github.com/ChainArgos/blockchain-explorer/actions/runs/39887554049) | push | 1 | 0.1.41 | `4b9fc98f29705541d74e181dcc52c717c21e6075` | 6 |
| ChainArgos/blockchain-explorer | [39887554085](https://github.com/ChainArgos/blockchain-explorer/actions/runs/39887554085) | push | 1 | 0.1.41 | `4b9fc98f29705541d74e181dcc52c717c21e6075` | 1 |
| ChainArgos/eth-grpc-server | [39884643630](https://github.com/ChainArgos/eth-grpc-server/actions/runs/39884643630) | pull_request | 1 | 0.1.41 | `376286f07fba3cbd65c8e2c089489f09929e32f1` | 7 |
| ChainArgos/eth-grpc-server | [39885911545](https://github.com/ChainArgos/eth-grpc-server/actions/runs/39885911545) | push | 1 | 0.1.41 | `4b97aa1a0cf8c15f7a2ab75435c7c6da270b2ea6` | 1 |
| ChainArgos/eth-grpc-server | [39885911570](https://github.com/ChainArgos/eth-grpc-server/actions/runs/39885911570) | push | 1 | 0.1.41 | `4b97aa1a0cf8c15f7a2ab75435c7c6da270b2ea6` | 7 |
| ChainArgos/eth-processor-rust | [39883770173](https://github.com/ChainArgos/eth-processor-rust/actions/runs/39883770173) | pull_request | 1 | 0.1.41 | `4faced40efa6efe6129b6a96ab73fe351a8e9bcb` | 9 |
| ChainArgos/eth-processor-rust | [39885149301](https://github.com/ChainArgos/eth-processor-rust/actions/runs/39885149301) | push | 1 | 0.1.41 | `c08aa7d5232e43466fcfd4fa6929ef7dec7bb76c` | 1 |
| ChainArgos/eth-processor-rust | [39885149307](https://github.com/ChainArgos/eth-processor-rust/actions/runs/39885149307) | push | 1 | 0.1.41 | `c08aa7d5232e43466fcfd4fa6929ef7dec7bb76c` | 9 |
| ChainArgos/tron-grpc-server | [39884653246](https://github.com/ChainArgos/tron-grpc-server/actions/runs/39884653246) | pull_request | 1 | 0.1.41 | `728bce7ea1d9a2bdb1598d79a601b42464e17e8b` | 7 |
| ChainArgos/tron-grpc-server | [39885921905](https://github.com/ChainArgos/tron-grpc-server/actions/runs/39885921905) | push | 1 | 0.1.41 | `9143caa0321469ca6627a9feb638e20da714dcb5` | 1 |
| ChainArgos/tron-grpc-server | [39885921996](https://github.com/ChainArgos/tron-grpc-server/actions/runs/39885921996) | push | 1 | 0.1.41 | `9143caa0321469ca6627a9feb638e20da714dcb5` | 7 |
| ChainArgos/tron-processor-rust | [39883783663](https://github.com/ChainArgos/tron-processor-rust/actions/runs/39883783663) | pull_request | 1 | 0.1.41 | `81123f9b639dfcbdb4ef4582ede4ba33c6bb526e` | 9 |
| ChainArgos/tron-processor-rust | [39885158639](https://github.com/ChainArgos/tron-processor-rust/actions/runs/39885158639) | push | 1 | 0.1.41 | `0e2a1050b34284530047a49d9a65fff333cecaed` | 9 |
| ChainArgos/tron-processor-rust | [39885158713](https://github.com/ChainArgos/tron-processor-rust/actions/runs/39885158713) | push | 1 | 0.1.41 | `0e2a1050b34284530047a49d9a65fff333cecaed` | 1 |
| jackin-project/jackin | [40076991878](https://github.com/jackin-project/jackin/actions/runs/40076991878) | workflow_run | 1 | 0.1.48 | `c98f5f5fdd831e6075e38fde93b9713575406140` | 11 |
| jackin-project/jackin | [40078359402](https://github.com/jackin-project/jackin/actions/runs/40078359402) | pull_request | 1 | 0.1.48 | `9971e26249c2a601912419c84aad99980f88d28b` | 40 |
| jackin-project/jackin | [40078628319](https://github.com/jackin-project/jackin/actions/runs/40078628319) | pull_request | 1 | 0.1.48 | `e42f3f33abcea63d4178a6f90b9feca2d7169fa3` | 40 |
| jackin-project/jackin | [40078851667](https://github.com/jackin-project/jackin/actions/runs/40078851667) | push | 1 | 0.1.52 | `e737f4b5eb7c1a0d15ba6595fc260407ad178452` | 40 |

## Measured and pending fields

Measured from source/log/API evidence: source revisions, generator headers, events, attempts, all job metadata, command recipes, displayed exports, reported cache transfers, and job intervals.
Pending: true controlled cold/warm comparisons, eligible compiler process ledgers, complete native observation, actual origin bytes, complete stored inventory, retention/generation occupancy, duplicate content, and peak disk.
No replacement archive has been built, uploaded, restored, or timed.
No current evidence proves a ten-GB fit or the new zero-work contract.
