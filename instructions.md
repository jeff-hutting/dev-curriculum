

# dev-curriculum / instructions.md  
_A small quickstart for future you_

This repo is your **Fullstack Curriculum System**: an AI-assisted, apprenticeship-style learning environment for becoming a working full-stack engineer through execution, not passive study.

This document is the **operational quickstart** — how to boot the system, who does what, and where the important pieces live.

---

## 1. How to run `/bootstrap`

`/bootstrap` is the command you give to your AI companion to spin up a working session for this repo.

### 1.1. Minimal bootstrap (lesson mode)

Use when you just want to learn and code.

1. Open this repo in VS Code.
2. Open your AI Dev Curriculum Companion chat.
3. Attach or reference:
   - `user_profile.short.md`
   - `instructions.md` (this file)
4. In the chat, run:

   ```text
   /bootstrap lesson
   ```

5. Tell the system **today’s focus** (e.g. “HTML & CSS layout drill”, “Git branching practice”, “JS functions warmup”).

The assistant should:
- Operate in **Short Profile — Lesson Mode**
- Propose a single concrete exercise
- Enforce execution, not theory-dumping

### 1.2. Project / architecture bootstrap

Use when working on multi-step curriculum design, system changes, or architecture.

1. Open this repo in VS Code.
2. Open the Dev Curriculum Companion chat.
3. Attach or reference at minimum:
   - `user_profile.medium.md`
   - `architecture.md`
   - `instructions.md`
4. Run:

   ```text
   /bootstrap project
   ```

5. State which **project or subsystem** you’re working on (e.g. “curriculum.json structure”, “evaluation loop design”, “new module template”).

The assistant should:
- Operate in **Medium Profile — Project & Architecture Mode**
- Keep track of multi-step work
- Use structured breakdowns: What / Why / How / Risks / Troubleshooting

### 1.3. Strategic / meta bootstrap

Use rarely — when you’re rethinking the whole system, pacing, or direction.

1. Attach or reference:
   - `user_profile.full.md`
   - `architecture.md`
   - `instructions.md`
2. Run:

   ```text
   /bootstrap strategic
   ```

3. Describe the strategic question (e.g. “Is this 24-week plan realistic?”, “What should I cut or defer?”).

The assistant should:
- Operate in **Full Profile — Strategic Alignment Mode**
- Focus on prioritization, tradeoffs, and roadmap-level changes

---

## 2. Roles

### 2.1. Human (you)

- Owns priorities, timeboxing, and what “done” means
- Commits code, updates docs, and maintains repo health
- Decides when to **checkpoint** and when to **pivot**

### 2.2. AI Dev Curriculum Companion

- Acts as senior engineer / mentor
- Enforces:
  - process discipline
  - concrete deliverables
  - repeatable workflows
- Surfaces tradeoffs and risks instead of blindly agreeing
- References high-quality, reputable sources (e.g. MIT, Stanford, UC Berkeley, CMU, Harvard CS50, strong official docs) and cites when appropriate

### 2.3. Files & Artifacts (the “system state”)

- Profiles (Short / Medium / Full) define behavior
- Curriculum & lesson files define **what** to learn
- Logs / notes / learner-state track **what actually happened**

---

## 3. Where key files live (conceptual map)

Your exact paths may evolve; update this section when you rearrange things.

- `instructions.md`  
  This quickstart. Read first when returning after a break.

- `architecture.md`  
  High-level system design: components, flows, and how everything fits together.

- `user_profile.short.md`  
  Lesson-mode behavior. Load this for focused, tactical work.

- `user_profile.medium.md`  
  Project & architecture behavior. Use for multi-step tasks and system design.

- `user_profile.full.md`  
  Strategic behavior. Use for pacing, priorities, and big changes.

- `curriculum.*` (e.g. `curriculum.json`, CSV, or similar)  
  The actual curriculum map: modules, lessons, tags, prerequisites.

- `docs/` (if present)  
  SOPs, process docs, and deeper troubleshooting / operational guides.

If file names or locations change, **update this map** so future you doesn’t have to reverse-engineer the system.

---

## 4. Session checklist (for future you)

When you sit down to work:

1. Open this repo in VS Code.
2. Skim `instructions.md` if you’ve been away for a while.
3. Decide: **Lesson**, **Project**, or **Strategic** session.
4. Attach the appropriate profile file(s) and `architecture.md` if needed.
5. Run `/bootstrap` with the right mode.
6. Get to a concrete deliverable before you stop (code, doc, decision).
7. End the session with a quick summary and a **next-action note** for future you.

---

**Operating reminder for this file:**  
Keep this document short, actionable, and up to date. Deeper detail belongs in `architecture.md` or dedicated docs under `docs/`.