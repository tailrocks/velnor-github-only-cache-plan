# Goal workspace

Start here before starting the goal. This file maps the workspace only.
It is not part of the implementation contract.

## Location

`~/velnor-workspace` (`/Users/donbeave/velnor-workspace`).

## Clones

All clones are pristine full clones at their default branches, taken 2026-10-25.
T01 refreshes the nine source revisions before any edit, so do not pin SHAs by hand.

| Directory | Source repository | Purpose |
|---|---|---|
| `velnor-github-only-cache-plan/` | [tailrocks/velnor-github-only-cache-plan](https://github.com/tailrocks/velnor-github-only-cache-plan) | This plan. Read [GOAL.md](GOAL.md) to start. |
| `velnor-new/` | [tailrocks/velnor-new](https://github.com/tailrocks/velnor-new) | Implementation target. All code, test, and generator edits land here. |
| `jackin/` | [jackin-project/jackin](https://github.com/jackin-project/jackin) | Consumer repository. |
| `blockchain-explorer/` | [ChainArgos/blockchain-explorer](https://github.com/ChainArgos/blockchain-explorer) | Consumer repository. |
| `tron-grpc-server/` | [ChainArgos/tron-grpc-server](https://github.com/ChainArgos/tron-grpc-server) | Consumer repository. |
| `eth-grpc-server/` | [ChainArgos/eth-grpc-server](https://github.com/ChainArgos/eth-grpc-server) | Consumer repository. |
| `bitcoin-grpc-server/` | [ChainArgos/bitcoin-grpc-server](https://github.com/ChainArgos/bitcoin-grpc-server) | Consumer repository. |
| `tron-processor-rust/` | [ChainArgos/tron-processor-rust](https://github.com/ChainArgos/tron-processor-rust) | Consumer repository. |
| `eth-processor-rust/` | [ChainArgos/eth-processor-rust](https://github.com/ChainArgos/eth-processor-rust) | Consumer repository. |
| `bitcoin-processor-rust/` | [ChainArgos/bitcoin-processor-rust](https://github.com/ChainArgos/bitcoin-processor-rust) | Consumer repository. |

## Environment

Verified 2026-10-25, no repo was modified:

- `mise` 2026.10.19, `mise doctor` reports no problems.
- `cargo`/`rustc` 1.99.1 through mise and mbx in all nine implementation clones.
- `mbx doctor` reports 0 failures and 0 warnings.
- Known note, not fixed: `mise install` in `velnor-new` exits 1 at the lock phase (`failed to resolve java for macos-x64: no metadata found for version temurin-27.0.0+35 on macos-x64`). All 23 tools are already installed and the clone is untouched. Fixing the lock entry belongs to the goal, not to setup.

## Do not use the old tree

The previous checkout at `~/velnor-new` is dirty and on a diverged feature branch.
Start the goal from `~/velnor-workspace/velnor-new` instead.
