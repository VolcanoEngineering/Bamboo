# Documentation.md — Context Orientation

The running per-Knob log for this repository. Each Bump (commit, version push, state transition) earns a one-to-two paragraph summary with date and timestamp. Brief, concrete, no bloat. Any agent (or human) reading this file should be able to trace what happened at any Knob in the repo's history and why.

When this file crosses 5000 characters of per-Knob entries, spawn `context-ori-summary-2.md` and continue here. Then `-3.md`, `-4.md`, `-5.md` as the repo grows. The current Knob and the last three stay hot in this file. Older entries migrate to the numbered summary files as cold storage.

Read in reverse chronological order — newest at the top. The active Knob is whatever appears first.

---

## Knob: commit attribution policy + history scrub — Saturday, June 6, 2026, 05:49 PM CDT

Added an explicit **Commit attribution** directive to `CLAUDE.md` under "Claude-shaped operating notes": no `Co-Authored-By: Claude` (or any Anthropic-noreply) trailers on commits in this repo. The rule overrides the system-default trailer injection and covers amend, rebase, squash, and all future commits. Scope is Claude-only by user preference; `AGENT.md` and the other vendor overlays were intentionally left alone.

History scrub paired with the policy: the trailer existed on exactly one commit, `67ba545` (docs: add user-model.md + LTRP retirement + architecture/ cold-start integration, May 28). That commit was not on `main` — it was the tip of an unmerged exploratory branch `knob/memory-split-ltip-canonical` carrying 352 lines of un-merged content (user-model.md, memory-drift.md, memory-watchdog.md, workflow-tools.md, and supporting edits). Ran `git filter-branch --msg-filter` on that branch only, stripped the trailer, force-pushed back to origin. New SHA `3a8d7bd` replaces `67ba545`. Branch and its content preserved; trailer gone. Two surfaces — the historical artifact and the forward-looking rule — closed in the same Knob.

---

## Knob: memory-context normalization + agent topology — Thursday, June 4, 2026, 04:44 AM CDT

Normalized this repo's internal memory path to `docs/memory-context/` and propagated the rename through the cold-start docs, canonical maps, and memory Skills. `README.md`, `AGENT.md`, `Documentation.md`, `CLAUDE.md`, `docs/repo-organization.md`, and the relevant workflow and Skill docs now distinguish between this repo's internal memory layout and the default downstream template contract, which still points project forks at `docs/context-orientation.md` unless they intentionally adopt the same folder structure.

Added `agent-architecture/agent-topology.md` as the source of truth for multi-agent squad structure. The new doc defines a practical startup tech-squad topology with core lanes, optional lanes, ownership boundaries, handoff expectations, escalation rules, and anti-conflict rules for parallel work. Also added a light cross-reference in `agent-identity.md` so identity stays about persona while topology owns coordination.

---

## Knob: canonical Documentation root + thinner fork contract — Wednesday, June 3, 2026, 09:18 PM CDT

Added a literal root `Documentation.md` and made it the canonical operating spec for this repository pattern. `README.md` now stays human-facing, `AGENT.md` is reduced to cold-start routing, and generic policy was pulled out of `workflows/project-setup.md` so setup procedure no longer competes with the source of truth.

This also tightened the fork contract. Downstream repos are expected to carry the minimum governance layer, copy only the modules they actively need, and add real working folders early so the repo does not become mostly process docs. Updated `docs/repo-organization.md` to reflect the new root file and cold-start order.

---

## Knob: memory Skills + map hygiene — Thursday, May 28, 2026, 07:52 PM CDT

Added two separate Skills instead of bloating `repo-cognition`: `memory-context` for Knob-aware retrieval, ADM/RAG alignment, hot/warm/cold memory, and handoffs; `memory-watchdog` for stale maps, broken references, missing Knob entries, duplicate concepts, and memory rot. Updated `skills/skill-map.md` so Skills are now mapped instead of living behind a stub.

Added Map Hygiene rules to `docs/repo-organization.md`. New folders, moved files, new Skills, and new architecture memory docs now have explicit map-update expectations. This is the OSS governance edge of the repo: if the map lies, the memory system rots.

---

## Knob: ADM/RAG memory folder — Thursday, May 28, 2026

Moved the memory architecture docs into `architecture/memory/` so Memory, Drift, Watchdog, ADM, RAG, and CRUD live in one place instead of scattering across the top of `architecture/`. `workflow-tools.md` stays directly under `architecture/` because it is about tool friction and workflow surfaces, not the memory store itself.

Added the first pass of ADM, RAG, and CRUD memory docs. ADM carries episodic chapters and active memory banks. RAG carries semantic and procedural memory. CRUD is the keep-it-alive loop so stale memory gets created, read, updated, or destroyed instead of quietly rotting.

---

## Knob: architecture map + PLTRF cleanup — Thursday, May 28, 2026, 06:53 PM CDT

Added `architecture/` to the repo's cold-start map as the fifth working folder. It now shows up in `README.md`, `AGENT.md`, `CLAUDE.md`, and `docs/repo-organization.md`, but it is selective cold-start material. Agents load it when memory itself is the work: drift, Watchdog, audits, workflow governance, or memory architecture. Otherwise it stays cold so the Token budget does not get eaten just because a folder exists.

Cleaned up early PLTRF drift before it became normal. Fixed the broken `references/context-token-limits.md` pointers, corrected the long-term preservation acronym split, synced the repo-cognition reference mirrors back to canonical `behavior/`, and turned the Codex/Claude/Gemini overlays into thin wrappers around `SKILL.md`. Same hooks, fewer duplicated rules, less chance the repo becomes the thing the agent fights.

---

Older entries moved to `docs/memory-context/context-ori-summary-2.md` as cold storage. Pull that file only when the current Knob references older scaffolding or prior release history.
