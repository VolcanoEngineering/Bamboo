# Fork Resync

This workflow covers how to resync a downstream fork to a canonical change. Use it when the canonical `Bamboo.md` repo introduces a structural change — a rename, a new doc family, a moved folder, an acronym shift — and the fork has not yet adopted it.

Forks in this system are snapshots, not live tracks. They do not automatically pull canonical changes. That is intentional — it lets each project move at its own pace. But the longer a fork lags, the harder the eventual catch-up. This doc keeps the catch-up cheap.

Pairs with `workflows/project-setup.md` (first-time bootstrap) and `workflows/project-context.md` (ongoing governance). Setup is the first sync. This doc is every sync after.

---

## When to resync

Resync when canonical introduces a change that affects the fork's structure:

- **Filename or prefix change.** Canonical renamed `context-*.md` to `ctx-*.md`, for example. Forks on the old name lag the new convention.
- **Folder rename.** Canonical moved `docs/memory-context/` to `docs/memory-ctx/`. Forks on the old path lag.
- **New canonical doc the fork should adopt.** Canonical spawned `ctx-lexicon.md` or `watchdog-persona.md`. Forks running the old shape don't have it.
- **Discipline change.** Canonical's Knob entry format loosened, or a new directive (like narrate-compression) landed. Forks should pick it up.
- **Acronym or vocabulary shift.** A new term entered the lexicon and the fork's docs should reflect it.

Skip resync when canonical's change is internal-only (touching its own `docs/memory-ctx/` for example) — that doesn't reach the fork contract.

---

## Pre-resync checklist

Before touching anything in the fork:

1. **Read the relevant canonical Knob entry.** Find the Bump in canonical's `ctx-orientation.md` that introduced the change. That entry names what moved and why.
2. **Check the canonical's PLTRF CI.** If the canonical run is green, the canonical map is consistent and the resync target is stable.
3. **Confirm the fork's working tree is clean.** Stash or commit any local changes first. Resync touches paths — uncommitted work makes it ambiguous.
4. **Note the fork's deviation from canonical.** Forks evolve their own shape (semver releases, agent dialogue, dated tasks, guardrails). Resync touches structure, not voice. If the fork has its own Knob log format, keep it.

---

## Procedure

The resync is a single atomic commit per fork — PLTRF discipline. Multiple small commits across files invite drift.

1. **Mirror the canonical move locally.** If canonical renamed files, `git mv` the equivalent files in the fork. If canonical added a doc, copy it from canonical and adjust paths inside it to match the fork's layout.
2. **Update every reference inside the fork.** Run `grep -rEn "<old-pattern>" --include="*.md" .` to find every mention. Update each in lockstep. No orphan pointers.
3. **Update the fork's cold-start docs.** `AGENT.md`, `CLAUDE.md` (if present), `README.md`, and any `Bamboo.md` copy in the fork. These point at structural paths; the points must move with the structure.
4. **Add a Knob entry to the fork's orientation log.** Whatever format the fork uses (Knob block, semver, agent handoff, task list, guardrail). Name the resync, name the canonical Bump it tracks, name what moved.
5. **Run the fork's verification.** `grep -rEn "<old-pattern>" --include="*.md" .` should return zero hits inside the fork. If the fork has its own CI or PLTRF check, run it.
6. **Single atomic commit.** Stage everything. Commit. No `Co-Authored-By: Claude` trailer (the canonical policy applies to forks too unless the fork has overridden it).
7. **Push.**

---

## Handling Knob log references to old names

Existing Knob entries in the fork's orientation log may reference the old structure (`context-rules.md`, `memory-context/`, etc). Those are *historical record* — leave them alone. The discipline:

- **Don't rewrite past Knob entries.** They describe what was true at that Bump. Rewriting them lies about history.
- **The new Knob entry references both states.** The resync entry says "renamed X to Y per canonical Bump <SHA>." That gives future agents the trace.
- **The PLTRF check (if the fork has one) skips Knob log entries.** The `context-orientation.md` and `ctx-ori-summary-N.md` files are read-mostly. Some references in them will look broken but they describe historical state.

---

## Cross-fork batch resync

If you maintain multiple forks and they all need the same resync, resist the temptation to script it across all repos at once. Each fork has its own state — local changes, in-flight branches, custom adaptations. Run the procedure above on each fork individually, one at a time. The atomicity is per-fork, not across the fleet.

If you have many forks (5+) and want a faster pattern, consider:

- Drafting the canonical change on a fork first, verifying it works in practice, then merging upstream.
- Building a small script that emits the rename pattern as a diff per fork (not a direct edit), so a human can review before applying.
- Accepting that some forks may never resync — they live on a different branch of the discipline. That's fine as long as the lag is intentional, not forgotten.

---

## Anti-patterns

- Editing files across multiple commits instead of one atomic resync per fork. Recipe for orphan pointers.
- Resyncing without reading the canonical Knob entry first. You miss the *why* and the resync is mechanical instead of informed.
- Rewriting historical Knob entries to match new naming. Lies about what was true.
- Force-pushing to a fork's main without notifying anyone else who works on it.

---

## Cross-references

- `workflows/project-setup.md` — first-time fork bootstrap.
- `workflows/project-context.md` — ongoing fork governance.
- `behavior/ctx-entropy.md` — PLTRF (the discipline this workflow implements).
- `behavior/ctx-lexicon.md` — vocabulary the resync surfaces.
- `.github/workflows/pltrf-check.yml` — the canonical's automated check, pattern a fork can adopt.
