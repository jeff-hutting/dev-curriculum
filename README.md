# dev-curriculum

A structured, AI-assisted apprenticeship system for developing into a production-capable full-stack engineer through real deliverables, documented workflows, and compounding skill growth.

This repo serves as a learning operating system, not a loose collection of tutorials. It integrates engineering discipline, automation, documentation, and curriculum design into a repeatable, scalable process.

---

## Purpose

- Convert fragmented learning into structured execution
- Build real engineering habits (architecture, Git workflows, documentation, testing)
- Produce real projects rather than passive knowledge
- Maintain long-term traction with systems that reinforce themselves
- Enable self-directed learning with senior-engineer-level guidance via AI

---

## How the System Works

The system operates in three intentional modes, controlled through profile selection and the slash command bootstrap startup workflow.

Modes and profiles table:

Mode: Lesson Mode
Use: Focused drills, fast iteration, coding practice
Profile file: user_profile.short.md

Mode: Project / Architecture Mode
Use: Multi-step work, system design, workflow scaffolding
Profile file: user_profile.medium.md

Mode: Strategic Mode
Use: Roadmap, pacing, prioritization, direction changes
Profile file: user_profile.full.md

Session startup examples (type directly into the AI companion):

/bootstrap lesson
/bootstrap project
/bootstrap strategic

---

## Key Files and Structure

instructions.md — Quickstart for operating the system and running sessions
architecture.md — High-level system design and structure
user_profile.short.md — Lesson-mode behavioral rules
user_profile.medium.md — Project and architecture profile
user_profile.full.md — Strategic-alignment profile
curriculum.* — Learning roadmap (modules, lessons, dependencies)
schemas/*.schema.json — Validation schemas for curriculum structure and automation
docs/ — SOPs, troubleshooting, deep operational documentation

---

## Session Workflow

1. Open repo in VS Code
2. Decide mode: Lesson, Project, or Strategic
3. Load the correct profile file(s)
4. Run the appropriate bootstrap command
5. Produce a concrete deliverable before stopping (code, documentation, or decision)
6. Summarize progress and define the next-action note for future you
7. Use slash checkpoint when shifting context

---

## Tech Context

Designed to operate within:
macOS, zsh, VS Code
JavaScript / TypeScript, Swift, Python, HTML / CSS
GitHub Flow, Conventional Commits, Git LFS, GitHub CLI
Notion for documentation, Obsidian for research capture

---

## Philosophy

Execution over consumption
Small, shippable steps
Process over memory
Architecture before implementation
Compounding over intensity

---

## Status

v0.x — active construction phase
Curriculum architecture build-out
Evaluation loop and session structure
Module and SOP template refinement

---

Engage.
