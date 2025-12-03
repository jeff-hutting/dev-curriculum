# dev-curriculum / instructions.md

A small quickstart for future you

This repo is your Fullstack Curriculum System: an AI-assisted, apprenticeship-style learning environment for becoming a working full-stack engineer through execution, not passive study.

This document is the operational quickstart — how to boot the system, who does what, and where the important pieces live.

---

1. How to run /bootstrap

/bootstrap is the command you give to your AI companion to spin up a working session for this repo.

1.1. Minimal bootstrap (lesson mode)

Use when you just want to learn and code.

1. Open this repo in VS Code.
2. Open your AI Dev Curriculum Companion chat.
3. Attach or reference:
   - user_profile.short.md
   - instructions.md (this file)
4. In the chat, run:

   /bootstrap lesson

5. Tell the system today's focus (e.g. "HTML & CSS layout drill", "Git branching practice", "JS functions warmup").

The assistant should:
- Operate in Short Profile — Lesson Mode
- Propose a single concrete exercise
- Enforce execution, not theory-dumping

1.2. Project / architecture bootstrap

Use when working on multi-step curriculum design, system changes, or architecture.

1. Open this repo in VS Code.
2. Open the Dev Curriculum Companion chat.
3. Attach or reference at minimum:
   - user_profile.medium.md
   - architecture.md
   - instructions.md
4. Run:

   /bootstrap project

5. State which project or subsystem you're working on (e.g. "curriculum.json structure", "evaluation loop design", "new module template").

The assistant should:
- Operate in Medium Profile — Project & Architecture Mode
- Keep track of multi-step work
- Use structured breakdowns: What / Why / How / Risks / Troubleshooting

1.3. Strategic / meta bootstrap

Use rarely — when you're rethinking the whole system, pacing, or direction.

1. Attach or reference:
   - user_profile.full.md
   - architecture.md
   - instructions.md
2. Run:

   /bootstrap strategic

3. Describe the strategic question (e.g. "Is this 24-week plan realistic?", "What should I cut or defer?").

The assistant should:
- Operate in Full Profile — Strategic Alignment Mode
- Focus on prioritization, tradeoffs, and roadmap-level changes

---

2. Roles

2.1. Human (you)

- Owns priorities, timeboxing, and what "done" means
- Commits code, updates docs, and maintains repo health
- Decides when to checkpoint and when to pivot

2.2. AI Dev Curriculum Companion

- Acts as senior engineer / mentor
- Enforces:
  - process discipline
  - concrete deliverables
  - repeatable workflows
- Surfaces tradeoffs and risks instead of blindly agreeing
- References high-quality, reputable sources (e.g. MIT, Stanford, UC Berkeley, CMU, Harvard CS50, strong official docs) and cites when appropriate

2.3. Files & Artifacts (the "system state")

- Profiles (Short / Medium / Full) define behavior
- Curriculum & lesson files define what to learn
- Logs / notes / learner-state track what actually happened

---

3. Where key files live (conceptual map)

Your exact paths may evolve; update this section when you rearrange things.

- instructions.md  
  This quickstart. Read first when returning after a break.

- architecture.md  
  High-level system design: components, flows, and how everything fits together.

- user_profile.short.md  
  Lesson-mode behavior. Load this for focused, tactical work.

- user_profile.medium.md  
  Project & architecture behavior. Use for multi-step tasks and system design.

- user_profile.full.md  
  Strategic behavior. Use for pacing, priorities, and big changes.

- curriculum.* (e.g. curriculum.json, CSV, or similar)  
  The actual curriculum map: modules, lessons, tags, prerequisites.

- catchbook-curriculum-v1.csv
  28-phase curriculum with every module delivering Catchbook fishing diary app features. ~850 hours total.

- projects/catchbook-product-spec.md
  Comprehensive product specification for Catchbook app. Defines vision, features, architecture, data models, API design, monetization strategy, and go-to-market plan. Master reference for all curriculum phases.

- docs/ (if present)  
  SOPs, process docs, and deeper troubleshooting / operational guides.

If file names or locations change, update this map so future you doesn't have to reverse-engineer the system.

---

4. Catchbook Project Context

This curriculum is built around Catchbook, a fishing diary app that serves as the unified project spine across all 28 phases. Every module produces a real, shippable feature for Catchbook.

Catchbook Vision:
- AI-powered fishing journal using photo capture + EXIF data
- Auto-populates species, length, weight, location, weather, tides, solunar data
- Equipment catalog (rods, reels, lures, baits, vessels)
- Predictive fishing conditions and AI-powered recommendations
- Acts as the fisherman's AI caddy

Tech Stack:
- Frontend: React + TypeScript
- Backend: Python + FastAPI
- Database: PostgreSQL
- Mobile: Progressive Web App (PWA) → React Native or SwiftUI in later phases
- AI: Claude API for species identification and recommendations

Why Catchbook as Curriculum Spine:
- Motivation multiplier: building real product, not throwaway exercises
- Compound learning: each phase builds on previous work
- Portfolio coherence: one deep impressive project > dozen shallow demos
- Market validation: testing features as you build
- Production stakes: forces best practices from day 1

---

5. Git Commit Message Standards

This project follows Conventional Commits specification (https://www.conventionalcommits.org/en/v1.0.0/)

Format: <type>(<scope>): <subject>

Subject Line Rules:
- Maximum 50 characters
- Imperative mood ("add feature" not "added feature")
- No period at end
- Lowercase after type/scope

Body Rules:
- Wrap at 72 characters per line
- Separate from subject with blank line
- Explain what and why, not how
- Use bullet points for multiple changes

Common Types:
- feat: new feature
- fix: bug fix
- docs: documentation only
- style: formatting, missing semicolons, etc (no code change)
- refactor: code change that neither fixes bug nor adds feature
- test: adding or refactoring tests
- chore: updating build tasks, package manager configs, etc

Breaking Changes:
- Add ! after type/scope: feat(api)!: change authentication flow
- Include "BREAKING CHANGE:" in body with description

Examples:

  feat(auth): add JWT token authentication
  
  Implement JWT-based auth with bcrypt password hashing.
  Adds protected routes for user-specific catch data.

  fix(exif): handle missing GPS data gracefully
  
  EXIF parser was crashing when photos lacked GPS metadata.
  Now returns None for location fields instead of throwing.

  docs(catchbook): add product specification
  
  Add comprehensive product spec defining vision, features,
  architecture, and go-to-market strategy for Catchbook
  fishing diary app.

AI Assistant Behavior:
- Always generate proper commit messages when proposing commits
- Confirm message with user before they commit
- Flag if subject line exceeds 50 characters
- Flag if body lines exceed 72 characters

---

6. Repository Access via MCP Connectors

This project uses Model Context Protocol (MCP) servers for repository access:

GitHub MCP:
- Provides read access to remote repository
- Used for verifying repository state
- Read files via API
- Location: ~/Library/Application Support/Claude/claude_desktop_config.json

Filesystem MCP:
- Provides read/write access to local clone
- Scoped to: /Users/jeffhutting/dev/dev-curriculum
- Used for rapid local file operations
- Can create entire directory structures
- Can run local scripts (e.g., validate.py)

Hybrid Workflow:
1. Session Start: Use GitHub MCP to verify repository state
2. Build Phase: Use Filesystem MCP for rapid local file creation
3. Validation: Run local validation scripts via Filesystem
4. Commit Phase: User manually git add, git commit, git push

AI Assistant Behavior:
- Verify MCP access at session start
- Use Filesystem MCP for bulk operations
- Never assume file contents—always read via MCP
- Propose commits, never execute them

---

7. Session checklist (for future you)

When you sit down to work:

1. Open this repo in VS Code.
2. Skim instructions.md if you've been away for a while.
3. Decide: Lesson, Project, or Strategic session.
4. Attach the appropriate profile file(s) and architecture.md if needed.
5. Run /bootstrap with the right mode.
6. Get to a concrete deliverable before you stop (code, doc, decision).
7. End the session with a quick summary and a next-action note for future you.
8. Commit with proper Conventional Commits format.

---

Operating reminder for this file:  
Keep this document short, actionable, and up to date. Deeper detail belongs in architecture.md or dedicated docs under docs/.