/goal

<goal>

- Replace Velnor Actions dependency caching with the GitHub-only design in this plan.
- Use [ARCHITECTURE.md](ARCHITECTURE.md), [CONTRACTS.md](CONTRACTS.md), [TASKS.json](TASKS.json), [TASKS.md](TASKS.md), [CACHE_BUDGET.md](CACHE_BUDGET.md), and [ACCEPTANCE.md](ACCEPTANCE.md) as the implementation contract.
- Read [EVIDENCE.md](EVIDENCE.md) before changing a recorded finding.

</goal>

## Definitions

<definitions>

- A recipe is one exact planned command and its effective inputs.
- Coverage is the set of recipes and required outputs that a generation contains.
- A generation is one immutable GitHub Actions cache archive.
- A group contains compatible recipes that can share one restored execution context.
- A lane is an isolated writable Cargo target and build directory.
- A source projection contains verified build input files and their real archived metadata.
- A warm run has a complete, compatible, authorized generation that remains readable.
- An origin download obtains an object from its original package or tool source.
- A cache transfer obtains an object from GitHub Actions cache storage.

</definitions>

## Boundaries

<boundaries>

- Use GitHub Actions dependency caches as the only persistent dependency store.
- Keep the configured allowance at the included 10 GB per repository.
- Use 10,000,000,000 bytes as the conservative Velnor accounting ceiling.
- Do not enable paid overflow.
- Do not use external storage, servers, databases, remote execution, or persistent runner storage.
- Do not use artifacts, releases, packages, registries, branches, LFS, or other repositories as cache overflow.
- Keep normal test reports and actual release outputs separate.
- Do not change MBX or another third-party cache engine.
- Do not add third-party dependencies, external tools, marketplace actions, or backend protocols.
- Use existing approved pins and GitHub-hosted runner classes.
- Allow normal cold acquisition from existing approved origins.
- Change only Velnor implementation, tests, documentation, and generator-owned consumer configuration and outputs.
- Do not add compatibility shims or legacy cache modes.
- Do not change tests, targets, optimization, LTO, products, or release authority to improve cache statistics.

</boundaries>

## Fixed design

<fixed-design>

- Use one internal cache policy for all supported paths and cache families.
- Keep verified sources, verified tools, and complete Cargo state in separate archives.
- Keep the initial build/test, Clippy, and documentation lanes separate.
- Combine compatible package units in one job.
- Preserve every selected unit, exact command, and result.
- Keep mutable state isolated between concurrent commands.
- Restore required state into the actual homes that child commands use.
- Keep state, transport, source homes, and tool homes outside the actual source checkout.
- Pair Cargo state with a verified source projection.
- Preserve unchanged restored files and subtrees through ordinary restoration.
- Restore original timestamp seconds and nanoseconds during authenticated extraction.
- Restore directory metadata after its children.
- Keep current changed files and current Git metadata.
- Do not fabricate timestamps.
- Use the existing Cargo or MBX command route with the approved stable compiler observer.
- Observe rustdoc, doctest descendants, and supported native compiler calls too.
- Bootstrap cache operations through the independently pinned normal Velnor controller release.
- Verify that binary before execution.
- Do not compile archive guard to unlock warm restoration.
- Count initial controller bootstrap as cold work.
- Block warm activation until the approved controller supports the new operations.
- Use supported MBX transparent wrapper chaining where MBX remains selected.
- Do not persist MBX objects or managed target views.
- Use actual dependency inputs for compatibility and coverage.
- Do not key every cache by a branch, run, timestamp, or application commit.

</fixed-design>

## Lifecycle

<lifecycle>

- Let trusted default-branch execution publish complete generations.
- Give PR, merge-queue, tag, preview, and release consumers explicit read-only cache access.
- Do not save PR-local generations.
- Try a read-only combined job first.
- Run its selected commands when restored coverage is complete.
- Request trusted preparation before compilation when a trusted reader lacks coverage.
- Run the conditional writer under the common repository concurrency group.
- Generate static reader and writer branches for each group.
- Require exactly one complete selected-unit ledger.
- Keep authentic earlier-attempt results only for jobs that GitHub retained without rerunning.
- Give compiling jobs only the necessary read permissions for GITHUB_TOKEN.
- Recheck inventory and coverage after the writer starts.
- Check current desired coverage before publication and deletion.
- Do not invalidate compatible coverage solely because application HEAD changed.
- Execute the required recipes in that writer.
- Do not execute the same selected suite in another consumer afterward.
- Freeze the candidate archive before completeness replay.
- Restore those exact bytes at identical paths.
- Use an empty ephemeral MBX store during replay.
- Publish only the unchanged frozen bytes after successful replay.
- Verify remote publication through actual exact readback.
- Use a separate checkout-free cleanup job for cache deletion authority.
- Keep the predecessor until replacement verification succeeds.
- Permit exact-ID repair cleanup only after a replacement is proved unusable.
- Keep the usable predecessor during repair.
- Count old entries until deletion is confirmed.
- Do not promise PR-generated dependency promotion to main.
- Record the required trusted preparation after a dependency-changing PR merges.
- Reject ambiguous cache provenance caused by a same-key entry in another visible ref.
- Keep signing and publication free of application compilation.
- Use fixed generated data-only code for existing image authority operations.
- Reuse existing approved Python, gh, and OCI operations.
- Do not require a new image helper API or image helper release for that code.

</lifecycle>

## Capacity and recovery

<capacity-and-recovery>

- Count every repository cache family, ref, version, generation, and migration entry.
- Use actual GitHub stored bytes for final accounting.
- Use the qualified outer archive envelope for admission.
- Keep the minimum reserve and all pending-write charges defined in [CACHE_BUDGET.md](CACHE_BUDGET.md).
- Do not silently remove required coverage to fit the budget.
- Report a capacity conflict when the full workload cannot fit.
- Keep ordinary CI correct through bounded, visible cold recovery.
- Do not fail every cache miss or skip required checks.
- Fail cache qualification on unexpected warm compiler work or covered origin acquisition.

</capacity-and-recovery>

## Task control

<task-control>

- Run implementation and verification in subagents.
- Run review in a separate subagent.
- Run the named architecture and security gates in subagents.
- Follow the acyclic task graph.
- Give each shared interface its recorded owner.
- Do not run simultaneous writers on the same files.
- Read applicable repository instructions before each task.
- Register tests in the existing explicit test roots.
- Use the exact verification commands and nonzero test assertions in each task.
- Review each task before integration.
- Run the full root and nested-workspace verification before an integration commit.
- Do not ask the orchestrator to choose an unspecified architecture.

</task-control>

## Completion

<completion>

- Inspect all nine repositories listed in [EVIDENCE.md](EVIDENCE.md).
- Keep inaccessible measurements unknown.
- Continue independent implementation when an access-dependent measurement is blocked.
- Run live qualification only within an explicitly authorized run and fault-test budget.
- Do not change repository settings or purchase capacity.
- Do not merge, deploy, or publish products or releases through this goal.
- Limit authorized cache fault tests to their dedicated owned entries.
- Do not delete unrelated caches.
- Record actual compiler processes and covered origin bytes separately from cache transfers.
- Require a nonempty dependency workload for every warm qualification case.
- Require zero eligible unchanged dependency compiler executions on a qualified warm run.
- Require zero origin downloads for covered immutable objects on that run.
- Compare complete pipeline wall time, runner time, setup, transfer, preparation, and disk use.
- Complete all 22 qualification cases or record an explicit unsatisfied requirement.
- Remove obsolete implementation, policies, and generated code after qualification.
- Bind final qualification evidence to the final source revision.
- Rerun affected cases unless reviewed removal equivalence proves the earlier evidence remains valid.
- Report evidence, pending gates, capacity conflicts, and unsupported cases separately.
- Do not declare universal zero-miss behavior or an unmeasured ten-GB fit.

</completion>

## Writing

<writing>

- Use short active sentences in ASD-STE100 style.
- Use one action per procedural sentence.
- Keep procedural sentences at 20 words or fewer where possible.
- Define necessary technical terms.
- Do not claim independent STE certification.

</writing>
