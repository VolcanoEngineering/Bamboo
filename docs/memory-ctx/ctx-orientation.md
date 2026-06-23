# Bamboo.md — Context Orientation

The running per-Knob log for this repository. Each Bump (commit, version push, state transition) earns a one-to-two paragraph summary with date. Brief, concrete, no bloat — any agent or human reading this should be able to trace what happened at any Knob and why.

Read in reverse chronological order — newest at the top, active Knob first. The current Knob plus recent history stay hot here — four Knobs (current + last three) is the target, six is the hard max. When that ceiling is exceeded (or per-Knob entries cross 5000 characters), the oldest entries migrate to `ctx-ori-summary-2.md` (then `-3`, `-4`, `-5`) as cold storage.

---

## Knob: Relaxed the hot-log Knob ceiling to a 4-6 band — Monday, June 22, 2026

The max-4 hot-log rule shipped one Knob ago turned every new Knob into a forced migrate-and-trim: land the fifth, CI fails, move the oldest to `ctx-ori-summary-2.md`, repeat — a tax on every single Bump. Replaced the hard ceiling in `pltrf-check.yml` with a band. Four Knobs (active + last three) stays the target; five or six emit a non-failing `::warning::`; only a seventh fails the gate. Net effect is a batch-migrate roughly every third Knob instead of every one, while a cold-start agent still never reads more than six hot Knobs.

Mirrored the band into `ctx-rules.md` Rule 4 and this log's header so the doc and the gate state the same thing. Scoped deliberately to the count ceiling only. The separate 5000-character rollover trigger is a different mechanism — it isn't CI-enforced, and a grep showed it referenced across eight live files including the theory section in `Documentation.md` and two still-unaudited folders (`workflows/`, `skills/`), plus a -v2 naming drift in `workflows/project-context.md`. That purge is tracked as its own workstream, not bundled here, so the char clause stays in the header and Rule 5 for now. Tested both ways: passes at four, five, and six Knobs; fails at seven. This Knob is the fifth in the hot log — the first Bump to land without a forced migrate, which is the entire point.

- `.github/workflows/pltrf-check.yml` — count check now bands: warn at 5-6, fail at >6
- `behavior/ctx-rules.md` — Rule 4 states the 4-target / 6-max band
- `docs/memory-ctx/ctx-orientation.md` — header reflects the band

---
---

## Knob: Widened the PLTRF gate to close its blind spots — Monday, June 22, 2026

The CI gate passed green all night while the repo carried the exact fragmentation it's named for — because its checks only looked where the drift wasn't. Rebuilt `pltrf-check.yml` to cover the gaps. The prefix allowlist now includes `development/` and drops the phantom `bamboo-os/`. The broken-pointer scan reads every doc folder instead of just the root and `behavior/`, while excluding the orientation log and summaries since those reference deleted paths by design. The duplicate-home detector now catches any basename living in two places across the whole repo — not just the `behavior/ctx-* vs context-*` pair it checked before — and it's stub-aware, so one canonical doc plus its pointer stubs passes while two real copies fails.

Added two orientation-log guards turning the tiering rule into physics: rollover-due (fails if the hot log holds more than four Knobs) and descending-date order (fails if any Knob sits above an older one). Deliberately did NOT add an auto-Knob writer — a workflow can stamp a template but can't write the rationale, and auto-appending to canon collides with the Ratification and tiering rules. The log stays human/agent-authored; CI guards that it exists and stays well-formed. Every check was tested both ways before shipping: passes clean on the current repo, and fails on an injected duplicate, out-of-order Knob, fifth hot Knob, broken pointer, and missing identity block.

- Rewrote `.github/workflows/pltrf-check.yml` — prefix fix, full-folder scan, stub-aware cross-folder dup detection, rollover + order guards

---
---

## Knob: Cold-start spine + behavior + root hardening pass — Monday, June 22, 2026

Ran a full consistency and accuracy sweep across the cold-start cascade, the behavior layer, the root files, and the repo map. Most of what got fixed was inherited drift, not new breakage — the kind that doesn't announce itself. The Session Identity in `AGENT.md` was hardcoded to a personal laptop path, so every fork failed its own step-zero check; swapped it for a portable "repo root containing Bamboo.md and AGENT.md" rule and propagated the same wording into `Bamboo.md` Rules 1, 3, and the Minimum Repo Contract. The orientation-log path was wrong in several places — pointing at the fork default `docs/ctx-orientation.md` instead of this repo's `docs/memory-ctx/ctx-orientation.md` — fixed in `Bamboo.md`, `ctx-lexicon.md`, and `ctx-rules.md`. The lexicon was missing a CRUD entry the cascade promises; added it. `ctx-rules.md` had two sections both numbered 4 and never stated the newest-on-top ordering or the 5000-char rollover rule, so those went into the Knob format section where they belong.

The three sibling specs (entropy, window, token-limits) referenced each other by the wrong filename casing (`Context-entropy.md` instead of `ctx-entropy.md`) — corrected so the cross-references actually resolve. `ctx-entropy.md` also said "two axes" while listing three, plus a couple of real typos. The `behavior/` map (`ctx-utility.md`) was missing `persona-layer.md`; added it. `repo-organization.md` had drifted off the tree — re-audited it to match all 8 behavior files and all 7 development files, renamed the stale root, and listed `Documentation.md`. `CLAUDE.md` was missing the entire `development/` folder from its layout, count, and cold-start order; added it, and fixed a glossary pointer still aimed at the old `ctx-rules.md` home. `README.md` had five citation superscripts with no reference list — added it. `Documentation.md` had a corrupted, duplicated tail — removed it. Functional fixes only throughout; the manifesto voice in the behavior docs was left untouched on purpose, including the deliberate imperfections.

- `AGENT.md`, `Bamboo.md` — portable Session Identity, consistent log paths
- `behavior/ctx-lexicon.md` — CRUD entry, log path
- `behavior/ctx-rules.md` — section renumber, log path, Knob ordering + rollover rules
- `behavior/ctx-entropy.md`, `ctx-window.md`, `ctx-token-limits.md` — axes count, filename casing, typos
- `behavior/ctx-utility.md` — persona-layer.md map entry
- `docs/repo-organization.md` — re-audited map
- `CLAUDE.md` — development/ folder added, glossary pointer
- `README.md` — references list
- `Documentation.md` — corrupted tail removed

---
---
---

## Knob: Retired the duplicate orientation log — Monday, June 22, 2026

`behavior/ctx-orientation.md` was a second running Knob log competing with the canonical one at `docs/memory-ctx/ctx-orientation.md`. The log had migrated to `docs/memory-ctx/` — that's where AGENT.md, Bamboo.md, ctx-rules, and the lexicon all now point, and where the recent Knobs live — but the old `behavior/` copy never got removed, leaving five May Knobs stranded in it. Three of those (the May 28 entries) were already preserved in `ctx-ori-summary-2.md`; the two May 31 Knobs existed only in the stale file.

Moved the two unique May 31 Knobs into `ctx-ori-summary-2.md` alongside their May siblings, in reverse-chronological order, then deleted `behavior/ctx-orientation.md`. The repo now has one orientation log with one cold archive — the One Home rule PLTRF is built on. This also closes the `ctx-utility.md` map gap: the file no longer exists, so it needs no map entry. Worth noting the duplicate-home detector in `pltrf-check.yml` never caught this, because it only compares `behavior/ctx-* ` against `behavior/context-*` and doesn't look across folders — a CI blind spot for a later phase.

- Deleted `behavior/ctx-orientation.md` (stale duplicate log)
- Preserved its two unique May 31 Knobs in `docs/memory-ctx/ctx-ori-summary-2.md`
- Canonical log unchanged: `docs/memory-ctx/ctx-orientation.md`

---
---
---

## Knob: Collapsed the references mirror — Monday, June 22, 2026

The `repo-cognition` Skill's `references/` folder was still carrying four full `context-*.md` docs — the old mirror of the `behavior/ctx-*` canon that `SKILL.md` itself calls out as Drift fuel. The migration that was supposed to replace that mirror with thin pointer stubs only got half done: the `ctx-*` stubs landed, but the original fat copies never got deleted. They'd drifted 2–84 lines off the `behavior/` canon, and nothing referenced them as a live path — the only mentions were a historical note in `fork-resync.md` and an unrelated prose phrase in `Documentation.md`. So we deleted them.

`behavior/` is now the single home for the `ctx-*` specs, which is what PLTRF's One Home rule wanted all along. The `ctx-*` pointer stubs stay for back-compat exactly as `SKILL.md` describes. This kills the duplicate cluster that let the entropy, window, rules, and token-limits specs each be answered two or three different ways depending on which file an agent happened to open.

- Deleted `skills/repo-cognition/references/context-entropy.md`, `context-rules.md`, `context-window.md`, `context-token-limits.md` (stale mirror)
- Canonical home unchanged: `behavior/ctx-*.md`
- Pointer stubs retained: `skills/repo-cognition/references/ctx-*.md`

---
---

---

Older entries moved to `docs/memory-ctx/ctx-ori-summary-2.md` as cold storage. Pull that file only when the current Knob references older scaffolding or prior release history.