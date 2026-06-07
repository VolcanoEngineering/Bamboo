# Documentation.md — Context Orientation

The running per-Knob log for this repository. Each Bump (commit, version push, state transition) earns a one-to-two paragraph summary with date and timestamp. Brief, concrete, no bloat. Any agent (or human) reading this file should be able to trace what happened at any Knob in the repo's history and why.

When this file crosses 5000 characters of per-Knob entries, spawn `ctx-ori-summary-2.md` and continue here. Then `-3.md`, `-4.md`, `-5.md` as the repo grows. The current Knob and the last three stay hot in this file. Older entries migrate to the numbered summary files as cold storage.

Read in reverse chronological order — newest at the top. The active Knob is whatever appears first.

---

## Knob: fork-resync workflow doc — Sunday, June 7, 2026, 04:35 AM CDT

Wrote `workflows/fork-resync.md` — the procedure for catching a fork up to a canonical structural change. Covers when to resync (rename, folder move, new doc family, discipline shift), the pre-flight checklist (read the canonical Knob entry, check PLTRF CI is green, clean working tree, note fork-specific deviations), the procedure itself (single atomic commit per fork, no orphan pointers, no rewriting historical Knob entries), and the anti-patterns to avoid.

The honest take: I'm not touching the seven downstream forks directly. Each one has its own state — local changes, in-flight branches, custom adaptions — and resyncing them is a per-fork judgment call I shouldn't make alone. The doc gives you the recipe so any fork can be brought current when you're ready, on whatever schedule you decide.

Cross-referenced from `project-setup.md` (first-time bootstrap, see fork-resync for every sync after) and surfaced in `docs/repo-organization.md` under the workflows section. New forks land in setup; existing forks needing catch-up land here.

---

## Knob: ctx-rules.md voice tightening — Sunday, June 7, 2026, 04:20 AM CDT

Tightened the Operational Governance section in `behavior/ctx-rules.md`. The block was drifting into metaphor — *Software development is a marathon, not a sprint*, *Context is our fuel*, *LOCKED-IN and FROZEN* in all caps. Cold-start material should be terser than that.

Kept the Matt-isms that earned their place — "we lose our way," "Context is the fuel. Limited supply.", "discard the dead weight." Cut the cliché. Killed the LOCKED-IN ALL CAPS. Collapsed the meandring "Therefore, agents must be able to work with..." sentence into something direct. Net result is shorter, sharper, still sounds like me. Section dropped from roughly 480 words to about 210.

The doc is agent-facing rules content; voice tweaks belong in author-voiced surfaces, not in canonical doctrine that other agents read as instructions.

---

## Knob: log migration — hot file back under cap — Sunday, June 7, 2026, 04:05 AM CDT

The hot orientation log was sitting at over 10,000 characters — twice the 5000-char threshold. Time to migrate. Pulled the ten oldest Knobs out of `docs/memory-ctx/ctx-orientation.md` and prepended them at the top of `docs/memory-ctx/ctx-ori-summary-2.md` in newest-first order so the cold archive stays scannable. The hot file now holds the current Knob plus the last three — exactly what the discipline calls for.

Worth noting: this Knob itself triggers another migration in the same shape. With this entry added, the hot file goes back over the count, so the oldest of that set (structural moves) gets moved to summary-2 in the same commit. Steady-state behvaior — every Bump moves one out the bottom. Keeps the hot file lean automatically as long as the discipline holds.

No other changes in this Knob. Pure log hygiene.

---

## Knob: PLTRF GitHub Action — safety net closes the sequence — Sunday, June 7, 2026, 03:45 AM CDT

Last one in the sequence. Shipped `.github/workflows/pltrf-check.yml`. Runs on every push and PR. Scans the cold-start cascade (`CLAUDE.md`, `AGENT.md`, `Documentation.md`, `README.md`, `docs/repo-organization.md`, and all `behavior/ctx-*.md`) and asserts every repo-relative file path mentioned actually exists on disk. If any reference is broken, the build fails with a clear annotation pointing at which source doc references which missing file.

The matching is deliberatly scoped to paths that start with a known top-level folder (`behavior/`, `architecture/`, `agent-architecture/`, `docs/`, `skills/`, `workflows/`, `design/`, `.github/`). Bare filenames in prose like "see SKILL.md", sequence patterns like `-3.md`, template placeholders like `ctx-NAME.md`, and external-fork examples like `Trading-MCP-Algo/CHANGELOG.md` all get ignored — resolving them needs context the check doesn't have. Intentional placeholders (downstream-fork defaults, Backlog files) live in a `SKIP_LIST` at the top of the action.

Tested locally against the current state of the repo and it passes clean. Zero broken pointers. Confirmed it would catch a fake broken reference during development by introducing one and watching it fail.

PLTRF was discipline-only until this Knob — every rename, every new file, every move depended on me or the agent being meticulous. Now it's discipline plus a safety net. Broken pointers get caught in CI instead of waiting for a fresh agent to stumble into them six weeks later. README and Documentation.md got short notes mentioning the check is automated.

This wraps the 5-Knob refinement sequence post-Vision Synthesis Report. Across the arc: agent-mms filled (1), mirror layer killed (2), workflows split + entropy metrics relocated + CPP own home (3), Watchdog persona doc + Skill upgrade (4), and now CI enforcement (5). Five Knobs, five concrete refinements. The repo is materially less drift-prone than it was at the start of yesterday.

---

Older entries moved to `docs/memory-ctx/ctx-ori-summary-2.md` as cold storage. Pull that file only when the current Knob references older scaffolding or prior release history.
