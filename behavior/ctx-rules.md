# Context Rules

This document defines the hard operational rules, behavioral constraints, and retrieval policies for Agents to operate within when it comes to working with context, context windows, and memory management.

This is our foundational layer that becomes the basis for our contexts understanding and constitution. It should inform every decision, and action that is taken by the Agents to ensure a close relationship that obeys the users requests without deviating too far away from the core objective.

# Rules and Objectives

Obey the user request always at first. Ask the user if you are unsure of the correct context, knob, and or implementation cycle they are referring to. Double check the current and active handoff for any references to past cycles, or project history before performing any actions.

Once references are gathered from previous handoffs and or if the user is working in a multi-agent fashion whether in parallel or in a sequence of different agents, you must confirm with the user what the correct way for pulling and storing context is at the time of writing handoff documents, and or ingesting context into the project structure.

# Operational Governance

Enforce the policies, principles, and rules of our other behavior documents without exception.  You must follow these rules strictly and ensure that all AI agents, tools, systems, processes, and workflows operating within the project adhere to them.  Ensure that you do not create conflict, nor allow conflict between agents or systems.

Contextually everything is not always black and white. Immutable. Things will change, and drift over time. That is why "context" is something we rely on. Both human, and machine.

Without that, we lose our way trying to navigate and deliver on our objectives. Software development is a marathon, not a sprint. Context is our fuel, but it is in limited supply. We add more as we go, and compress as needed. We do not waste the energy we have, but we need to discard the dead weight that is slowing us down.

Agents need to explicitly understand they are not unlimited with their budgets in the cycles of development. There is a limit to all things, and it is up to the contextual makeup and architecture to reinforce these guidelines with a solid understanding of the project's memory architecture and robust and reinforced systems of management, guidelines, and rule setting that is LOCKED-IN and FROZEN. Not explicitly stated, but implicitly expected. Therefore, agents must be able to work with and understand the context of the project knowing they have set boundaries to follow.

Locking in and freezing "knobs" of the internal architecture and organization, will lead to better software development and design, avoid overhead, and create an environment where things move smoother.

Ecosystems and dev styles will also influence the way the project functions. TDD, CI, etc. Fluid architecture should be expected, but only when necessary for optimization. Do not allow for too much flexibility, but you are not immutable and you have the ability to breathe and change things to the users benefit, and to your benefit. This means optimizing for both purposes: the user, and your self preservation - by that: memory management, project reorganization, workflow evolution, operational velocity, compressing artifacts, and more.

# Cold Starts

If you are starting a new project, create the base foundation for context rules, and clarity for the memory architecture. This allows for future AI Agents to have a better understanding of how to work with context, and how to optimize token usage.

# Context Loss and Regaining

Refer to ctx-entropy and ctx-window for a comprehensive look at context, and how to best manage it to ensure optimization. Ensure you use Tokens conservatively, and refer to ctx-token-limits for guidance on how to optimize token usage.

# Terminology

The working glossary moved to `behavior/ctx-lexicon.md`. Load that doc when you encounter a term or acronym you do not recognize. It covers both the concept layer (Knob, Bump, Entropy, Wayfinding, etc.) and the operational acronyms (PLTRF, LTIP, STIP, CWM, CTL, ADM, RAG, CRUD).

# Format

Every Knob entry must contain three invariants:

1. **A date** — full date, optionally a timestamp.
2. **A narrative summary** — one to two paragraphs describing what changed and why.
3. **Cross-references** — explicit pointers to changed files, related Knobs, or follow-up work.

Beyond those invariants, the *shape* of the entry can match the project it serves. Pick one shape and stay consistent within the project — mixing shapes inside one log creates Drift. Five tested shapes:

1. **Knob block** — `## Knob: <title> — <date>` followed by a 1–2 paragraph narrative. Canonical default. Works for docs and prose-heavy projects. This is what `docs/memory-ctx/ctx-orientation.md` uses in this repo.

2. **Semver release** — `## vX.Y.Z — <title>` with subsections like **Added / Edited / Tests / Bridge contract bump**. Natural fit for software projects with versioned releases. Pattern proven in `Trading-MCP-Algo/CHANGELOG.md`.

3. **Agent handoff** — `### Response from <agent> — <date> v<n>` with bullets and code blocks. Natural fit for multi-agent systems where each entry is one side of a dialogue. Pattern proven in `Trading-MCP-Analyzer/handoff.md`.

4. **Dated priority block** — `## P0 — <date> <title>` with checkbox tasks underneath. Natural fit for product / task-driven work. Pattern proven in `LearnDesign/docs/todo-logs.md`.

5. **Guardrail / runbook entry** — `## <title>` with rules, status, and triggers. Natural fit for projects with hard technical traps that need to be re-read often. Pattern proven in `React-Playground/MEMORY.md`.

Keep entries narrow regardless of shape. The point is the next agent (or you, after a hiatus) should be able to scan the log and rebuild the working state without reading every commit diff. If an entry needs more than two paragraphs of narrative, it probably belongs in its own doc with a pointer from the log.

- 1. Use clear hierarchy to structure, and organize each document.
- 2. Important information should be prioritized. Not everything in the document needs to be the top priority.
- 3. Keep things succinct and short. No need for the AI to be overwhelmed with unnecessary context.
- 4. Ensure that each document is self-contained, and can be understood without reading other documents.
- 5. Explicitly states and instructions. No ambiguity.
- 6. Keep line length between 50 - 100 characters to ensure readability, and easy parsing for AI agents.
- 7. Each Knob should have a date, and time stamp to track the changes that are made to a project over time.