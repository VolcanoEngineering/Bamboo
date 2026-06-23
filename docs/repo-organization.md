# Repo Organization

A map of this repository. It describes what each folder is for, what lives inside it, and the order an agent (or a human) should consult things when picking the repo up cold. Pair this with `AGENT.md` at the root, which is the operational cold-start file. `AGENT.md` tells an agent *how* to enter the repo. This file tells it *where things are*.

This is `Bamboo.md`. Not a project repo. It is the canonical library of `.md` files that get forked into projects to give AI agents a consistent set of standards across vendors. `Bamboo.md` at the repo root is the policy source. `README.md` is the human overview. `AGENT.md` is the cold-start router.

---

## Top-level layout

Bamboo/
├── Bamboo.md                   # Canonical operating spec for repos using this system
├── README.md                   # What this repo is, who it's for, what it does
├── AGENT.md                    # Cold-start router for any agent landing in the repo
├── CLAUDE.md                   # Claude-specific cold-start overlay (sits on top of AGENT.md)
├── Documentation.md            # Long-form framework documentation and rationale
├── REPORTING_TEMPLATE.md       # The Layered Reporting Template
├── LICENSE
├── behavior/                   # The rules an agent obeys. Cold-start required.
│   ├── ctx-rules.md            # Hard operational rules and constraints.
│   ├── ctx-lexicon.md          # The decoder ring (3-Concept Canon).
│   ├── ctx-entropy.md          # The preservation view (LTIP/PLTRF).
│   ├── ctx-window.md           # The active-memory view (CWM).
│   ├── ctx-token-limits.md     # The Token-economy view (CTL).
│   ├── ctx-utility.md          # Map of behavior/ — points at where each concept lives.
│   ├── persona-layer.md        # Identity boundaries and placement.
│   └── user-model.md           # User behavior and psychology modeling.
├── development/                # Implementation standards and engine specs.
│   ├── app-development.md       # Generic app standards.
│   ├── nextjs-development.md    # Next.js standards.
│   ├── react-development.md     # React standards.
│   ├── swift-development.md     # Swift / Apple-platform standards.
│   ├── unity-development.md     # Structural discipline for Unity.
│   ├── unrealengine-development.md # Governance for UE5.
│   └── web-development.md       # Generic web standards.
├── docs/                        # Operational memory for this repo itself
│   ├── repo-organization.md     # ← this file. The map.
│   └── memory-ctx/
│       ├── ctx-orientation.md   # Hot per-Knob change log.
│       └── ctx-ori-summary-2.md # Cold storage for older Knobs.
├── architecture/                # ADVANCED ADD-ON. ADM/RAG, Watchdog, workflow tools.
│   ├── workflow-tools.md        # Tool/workflow memory friction.
│   └── memory/                  # Memory operating layer.
├── skills/                      # Portable AI capabilities. Cross-vendor.
├── workflows/                   # DevOps and project lifecycle patterns.
└── design/                      # Project-specific UI/UX rules.

---

## behavior/

The foundational rules. Everything an agent has to internalize before it touches the rest of the repo. Read this first on cold start.
- `ctx-window.md` — the active-memory view. Context window as virtual RAM; saturation, drift, compression.
- `ctx-token-limits.md` — the Token-economy view. Wayfinding, scoring, conservation at runtime.
- `ctx-utility.md` — the map of `behavior/`. Points at where each concept's canonical home lives.

---

## Private Extensions

High-fidelity implementation components (scripts, schemas, and advanced multi-agent topology) are managed via the **BAMBOO-OS** private repository.

---

## Maintenance rules

- New folder or moved file gets map updates in the same change.
- One canonical home per concept (PLTRF).
- Broken pointers are build failures.
- This file gets re-audited every few Knobs. Stale maps are worse than no map.
