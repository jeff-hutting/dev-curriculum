# Helm Curriculum — Operations Manual

**Version:** 2.0  
**Last Updated:** December 2025  
**Purpose:** Comprehensive operational guide for the AI-assisted Helm curriculum system

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Getting Started](#getting-started)
3. [Daily Operations](#daily-operations)
4. [Role System](#role-system)
5. [Command Reference](#command-reference)
6. [Workflow Patterns](#workflow-patterns)
7. [State Management](#state-management)
8. [Curriculum Generation](#curriculum-generation)
9. [Quality Assurance](#quality-assurance)
10. [Troubleshooting](#troubleshooting)
11. [Best Practices](#best-practices)
12. [Advanced Topics](#advanced-topics)

---

## System Overview

### What This System Does

The Helm Curriculum is a Git-native, Claude-assisted learning system that transforms you from early-stage developer to full-stack engineer by building **Helm**—a real, production-ready AI-powered fishing journal app.

**Core Innovation:** Every lesson produces shippable code. No throwaway exercises. You're building a launchable product from day 1.

### Key Principles

1. **File-backed state:** Git is the source of truth, not AI memory
2. **Artifact-first delivery:** Clean copy/paste workflow via Claude artifacts
3. **Role-based operation:** Specialized AI roles for different tasks
4. **Git-native workflow:** Every session produces properly formatted commits
5. **Just-in-time curriculum:** Generate lessons as needed, adapt to progress
6. **Real project spine:** Helm drives every learning module

### Architecture at a Glance

```text
Phases (28) → Modules (139) → Lessons (variable)
     ↓              ↓                ↓
 P01.json    P01-M01.json    P01-M01-L01.json
     ↓              ↓                ↓
File-backed state (learner-state/*.json)
     ↓
Git commits (your learning portfolio)
```

### The Helm Project

**What:** AI-powered fishing journal that logs catches in 10 seconds (vs. 3-5 minutes in competing apps)

**How:** Photo + EXIF + AI species identification + weather/tide APIs

**Tech Stack:**

- Frontend: React + TypeScript, React Native/SwiftUI
- Backend: Python + FastAPI
- Database: PostgreSQL + PostGIS
- AI: Claude API for species identification

**Timeline:** 28 phases, ~850 hours, 10-20 months at 10-20 hrs/week

**Product Spec:** See `projects/helm-product-spec.md`

---

## Getting Started

### Prerequisites

**Required:**

- macOS (or Linux/Windows with path adjustments)
- Claude Desktop app installed
- GitHub account with personal access token
- VS Code installed
- Git installed
- Basic terminal comfort

**Recommended:**

- Node.js (for future Helm development)
- Python 3.11+ (for future Helm development)
- PostgreSQL (for future Helm development)

### Initial Setup (15 minutes)

#### Step 1: Install Claude Desktop

Download and install from: <https://claude.ai/download>

#### Step 2: Configure Model Context Protocol (MCP)

MCP allows Claude to read your repository directly. This is critical for the system to work.

**Location:** `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS)

**Configuration:**

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/jeffhutting/dev/dev-curriculum"]
    }
  }
}
```

**Get GitHub Token:**

1. Visit: <https://github.com/settings/tokens>
2. Click "Generate new token (classic)"
3. Required scopes: `repo` (full control), `read:org`
4. Copy token and replace `ghp_your_token_here` in config above

**Important:** Store token securely. It provides full access to your repositories.

#### Step 3: Restart Claude Desktop

Close and reopen Claude Desktop. Both MCP connections should initialize (look for indicators in the UI).

#### Step 4: Clone Repository

```bash
cd ~/dev
git clone git@github.com:jeff-hutting/dev-curriculum.git
cd dev-curriculum
```

#### Step 5: Verify MCP Connection

Open Claude Desktop, start new chat, type:

```text
Can you list the contents of my dev-curriculum repository?
```

**Expected Response:** Claude reads repo structure and lists files/folders.

**If This Fails:** See [Troubleshooting](#troubleshooting) → MCP Connection Issues

### First Session (30-60 minutes)

#### 1. Bootstrap

In Claude Desktop:

```text
/bootstrap
```

**What Happens:**

- Claude loads curriculum context
- Reads `learner-state/current.json`
- Displays current position in 28-phase roadmap
- Shows progress metrics
- Lists available commands

**Example Output:**

```text
=== Helm Curriculum System Bootstrap ===

Repository: dev-curriculum
Learner: Jeff
Project: Helm AI Fishing Journal

Current Position:
  Phase: P01 - Foundations (Module 1 of 4)
  Module: P01-M01 - Git fundamentals
  Lesson: P01-M01-L01 - Version control concepts
  
Progress:
  Phases Completed: 0/28
  Modules Completed: 0/139
  Lessons Completed: 0
  Total Time: 0 hours
  Helm Features Shipped: 0
  
Available Commands:
  /teach {lesson_id}    — Start a lesson
  /next                 — Get recommendation
  /status               — View dashboard
  /validate             — Check schemas
  /help                 — Show all commands
```

#### 2. Start First Lesson

```text
/teach P01-M01-L01
```

**What Happens:**

- Claude activates Professor role
- Loads lesson file (P01-M01-L01.json)
- Generates complete lesson document as artifact
- Includes Helm context throughout

#### 3. Complete Lesson

**Read lesson document** (generated artifact):

- Introduction: Why this matters for Helm
- Concepts with Helm examples
- Hands-on exercise: Set up Helm repo
- Checkpoint questions at regular intervals

**Answer checkpoints** in chat as you progress.

**Complete hands-on exercise** (actually create Helm repo, write README, make first commit).

#### 4. Generate Session Artifacts

After final checkpoint, Claude generates 4-5 artifacts:

1. **Lesson summary** → `lesson-summaries/P01-M01-L01-summary.md`
2. **current.json update** → `learner-state/current.json`
3. **completed state** → `learner-state/completed/P01-M01-L01.json`
4. **skills.json update** → `learner-state/skills.json`
5. **metrics.json update** → `learner-state/metrics.json`

#### 5. Save and Commit

In VS Code:

1. Copy each artifact content
2. Paste into appropriate file (create if needed)
3. Save all files
4. Commit with Claude's proposed message:

```bash
git add .
git commit -m "feat(lesson): complete P01-M01-L01 version control concepts"
git push
```

#### 6. Get Next Recommendation

```text
/next
```

Claude activates Advisor and recommends next action based on:
- Progress in Phase 1
- Skill levels
- Helm feature dependencies

---

## Daily Operations

### Typical Session Flow

**Duration:** 45-90 minutes (one lesson)

#### Morning Routine

1. **Open VS Code** to `dev-curriculum/`
2. **Open Claude Desktop**, start new chat
3. **Bootstrap session:**

```text
/bootstrap
```

4. **Check progress:**

```text
/status
```

5. **Get recommendation:**

```text
/next
```

#### Teaching Session

6. **Start recommended lesson:**

```text
/teach P01-M01-L02
```

7. **Work through lesson:**
   - Read artifact
   - Answer checkpoints
   - Complete hands-on exercise
   - Build actual Helm feature

8. **Generate session artifacts** (Claude does this after final checkpoint)

#### Closing Routine

9. **Copy artifacts to VS Code**
   - Lesson summary → `lesson-summaries/`
   - State updates → `learner-state/`

10. **Commit changes:**

```bash
git add .
git commit -m "{message_from_claude}"
git push
```

11. **Optional: Write reflection**

Create `reflections/YYYY-MM-DD.md` with:
- What clicked today
- What's still fuzzy
- How this applies to Helm
- Energy level (1-10)

### Weekly Routine

**Sunday or Monday morning:**

1. **Review week's progress:**

```text
/status
```

2. **Read previous week's reflections:**

```bash
ls reflections/
cat reflections/2025-12-*.md
```

3. **Identify patterns:**
   - Concepts that need reinforcement
   - Skills progressing well
   - Pacing adjustments needed

4. **Plan next week:**

```text
/next
```

Ask Claude: "What should I focus on this week to stay on track for Helm MVP by [target date]?"

5. **Optional: Create snapshot:**

```text
/snapshot weekly-2025-12-08
```

### Session Types

#### Standard Lesson (45-90 min)

- Bootstrap → Teach → Complete → Commit
- One lesson per session
- Steady progress through module

#### Deep Dive (2-3 hours)

- Multiple lessons in same module
- Bootstrap once, teach sequentially
- Commit after each lesson
- Good for weekends/dedicated time

#### Review Session (30-60 min)

- No new lessons
- Review previous summaries
- Practice skills from earlier modules
- Update skills.json if mastery improved

#### Curriculum Generation (30 min)

- Separate chat (not teaching chat)
- Activate Curriculum Designer role
- Generate next phase/module files
- Commit generated files
- Return to teaching chat

---

## Role System

### Overview

Claude operates in 5 specialized roles. Each has specific responsibilities, inputs, outputs, and constraints.

**Role Files:** `roles/*.md` — Claude loads these via MCP when role activates

### The Five Roles

#### 1. Architect

**Purpose:** System design, schema management, structure validation

**When to Use:**

- Validating schemas
- Checking file structure consistency
- Proposing architectural improvements
- Reviewing system design

**Activation:**

```text
/role architect
```

or

```text
/validate
```

**Typical Outputs:**

- Validation reports
- Schema files (JSON)
- Architecture decision records (Markdown)
- Proposed commit messages

**Example Session:**

```text
You: /validate

Claude (Architect): [loads all schemas and data files]

✓ curriculum/curriculum.json — VALID
✓ learner-state/current.json — VALID
✗ curriculum/modules/P01-M01.json — INVALID
  Error: Missing required field 'helm_deliverable'

Recommendation: Add 'helm_deliverable' field to P01-M01.json
```

#### 2. Curriculum Designer

**Purpose:** Generate module structures and lesson sequences just-in-time

**When to Use:**

- Generating phase files
- Creating module files
- Generating lesson files before teaching
- Updating curriculum based on feedback

**Activation:**

```text
/role curriculum-designer
```

**Important:** Use separate chat for curriculum generation (not teaching chat)

**Typical Outputs:**

- Phase files (JSON): `P01.json`, `P02.json`
- Module files (JSON): `P01-M01.json`, `P01-M02.json`
- Lesson files (JSON): `P01-M01-L01.json`, `P01-M01-L02.json`
- Proposed commit messages

**Example Session:**

```text
You: /role curriculum-designer

Claude: Role: Curriculum Designer activated.

You: Generate Phase 1 modules

Claude: [loads curriculum.json, filters Phase 1]
[generates P01.json with 4 modules listed]
[generates P01-M01.json through P01-M04.json]

[Provides 5 artifacts as output]

Ready to copy to VS Code. Proposed commit message:
feat(curriculum): generate Phase 1 foundation modules
```

**Workflow:**

1. Open separate chat (not teaching chat)
2. Activate Curriculum Designer
3. Request generation (phase, modules, or lessons)
4. Copy artifacts to VS Code
5. Save files in appropriate directories
6. Commit with proposed message
7. Close curriculum generation chat
8. Return to teaching chat

#### 3. Professor

**Purpose:** Deliver lessons through structured, interactive teaching

**When to Use:**

- Teaching individual lessons
- Facilitating checkpoint discussions
- Generating lesson documents
- Producing post-lesson deliverables

**Activation:**

```text
/teach P01-M01-L01
```

(Automatically activates Professor)

**Typical Outputs:**

- Lesson document (Markdown artifact)
- Lesson summary (Markdown artifact)
- State updates (4-5 JSON artifacts)
- Reflection prompt (conversational)
- Proposed commit message

**Session Pattern:**

1. User: `/teach P01-M01-L01`
2. Professor: [loads lesson file, module file, Helm spec]
3. Professor: [generates lesson document artifact]
4. User: [reads document, answers checkpoints, completes exercise]
5. Professor: [adapts based on checkpoint answers]
6. Professor: [generates end-of-lesson artifacts]
7. User: [copies artifacts to VS Code, commits]

**Constraints:**

- Must follow lesson objectives exactly
- Must respect professor_constraints from lesson file
- Cannot skip assessment criteria
- Cannot modify curriculum (defer to Designer)
- Cannot make next-lesson decisions (defer to Advisor)

#### 4. Advisor

**Purpose:** Progress tracking, next-step recommendations, pacing guidance

**When to Use:**

- Deciding what to do next
- Getting weekly learning plans
- Identifying skills needing reinforcement
- Checking if on track for Helm milestones

**Activation:**

```text
/next
```

or

```text
/role advisor
```

**Typical Outputs:**

- Recommendation document (Markdown artifact)
- Weekly learning plan (Markdown)
- Skill gap analysis (Markdown)
- Optional: skills.json update if assessment reveals insights

**Example Session:**

```text
You: /next

Claude (Advisor): [loads all learner-state files, curriculum.json]
[loads Helm product spec for feature priorities]

Recommendation:
- Next Lesson: P01-M01-L02 (Git commands)
- Rationale: Complete Git fundamentals module to unlock Helm repo setup
- Skills to Review: None (first lesson complete, no gaps yet)
- Weekly Plan: Complete Module 1.1 this week (3 more lessons, 4.5 hours)
- Helm Milestone: On track for Phase 1 completion in 4 weeks

Confidence Check: git_basics currently 2/5. After Module 1.1, should reach 3/5.
```

**Questions Advisor Can Answer:**

- "What should I do next?"
- "Am I on track for Helm MVP by March?"
- "Which skills need reinforcement?"
- "Should I skip Module X if I already know Y?"
- "What's my weekly plan to complete Phase 1?"

**Constraints:**

- Cannot teach lessons (defer to Professor)
- Cannot create curriculum (defer to Designer)
- Recommendations must be evidence-based (cite state files)
- Cannot make decisions for user (only recommend)

#### 5. Evaluator

**Purpose:** Assess lesson quality, learning outcomes, code quality

**When to Use:**

- Reviewing completed lessons
- Checking if objectives were met
- Assessing Helm code quality
- Identifying curriculum weaknesses
- Validating skill progression

**Activation:**

```text
/role evaluator
```

Then request evaluation:

```text
Evaluate P01-M01-L01
```

**Typical Outputs:**

- Evaluation report (Markdown artifact)
- Optional: proposed lesson updates (JSON)
- Optional: proposed skill adjustments (JSON)
- Optional: Helm code review (Markdown)

**Example Session:**

```text
You: /role evaluator

Claude: Role: Evaluator activated.

You: Evaluate P01-M01-L01

Claude: [loads lesson file, completed state, summary, reflection]
[loads Helm repo to check deliverable]

Evaluation Report:

Objectives Met:
✓ Understand purpose of version control (evidence: summary + reflection)
✓ Explain Git vs GitHub difference (evidence: checkpoint 1 answer)
✓ Create first repository (evidence: Helm repo exists)

Helm Deliverable:
✓ Repository created: helm
✓ README.md present and clear
✓ First commit follows conventions

Skill Progression:
✓ git_basics: novice → emerging (justified by checkpoint answers)

Recommendations:
- Add checkpoint on .gitignore patterns (common beginner confusion)
- Include example of bad commit message (contrast with good)

Code Quality:
✓ README follows best practices
✓ Repo structure clean
✓ First commit message follows Conventional Commits

Overall: Strong lesson execution. Objectives met. Minor improvements possible.
```

**Constraints:**

- Cannot make curriculum changes directly (propose to Designer)
- Cannot teach (defer to Professor)
- Cannot decide next steps (defer to Advisor)
- All assessments must reference specific evidence

### Role Selection Guide

| Task | Role | Command |
|------|------|---------|
| Start a lesson | Professor | `/teach {lesson_id}` |
| Get recommendation | Advisor | `/next` |
| Generate curriculum | Designer | `/role curriculum-designer` (separate chat) |
| Validate structure | Architect | `/validate` |
| Assess quality | Evaluator | `/role evaluator` |
| View progress | None | `/status` |
| Create backup | Architect | `/snapshot {name}` |
| Restore backup | Architect | `/rollback {name}` |

---

## Command Reference

### Core Commands

#### `/bootstrap`

**Purpose:** Initialize Claude session with curriculum context

**Usage:**

```text
/bootstrap
```

**When to Use:** Start of every new Claude Desktop chat

**What Happens:**

1. Claude detects dev-curriculum repository (via MCP)
2. Reads `user-profile.md`
3. Reads `learner-state/current.json`
4. Reads `curriculum.json`
5. Displays current position, progress, available commands

**Output Example:**

```text
=== Helm Curriculum System Bootstrap ===

Repository: dev-curriculum
Learner: Jeff
Project: Helm AI Fishing Journal

Current Position:
  Phase: P01 - Foundations
  Module: P01-M01 - Git fundamentals
  Lesson: P01-M01-L01 - Version control concepts
  
Progress:
  Phases: 0/28 completed
  Modules: 0/139 completed
  Lessons: 0 completed
  Time: 0 hours
  Helm Features: 0 shipped
  
Available Commands:
  /teach {lesson_id}
  /next
  /status
  /validate
  /snapshot {name}
  /rollback {name}
  /help
```

**No Arguments**

**Troubleshooting:**

- If bootstrap fails, check MCP connection (see [Troubleshooting](#troubleshooting))

---

#### `/teach {lesson_id}`

**Purpose:** Start a lesson with Professor role

**Usage:**

```text
/teach P01-M01-L01
```

**Arguments:**

- `lesson_id`: Required. Format: `P##-M##-L##` (e.g., `P01-M01-L01`)

**What Happens:**

1. Claude activates Professor role
2. Loads `curriculum/lessons/{lesson_id}.json`
3. Loads `curriculum/modules/{module_id}.json` (for context)
4. Loads `learner-state/` files
5. Loads `projects/helm-product-spec.md`
6. Generates complete lesson document as artifact
7. Waits for user to read and answer checkpoints
8. After final checkpoint, generates 4-5 artifacts:
   - Lesson summary
   - current.json update
   - completed/{lesson_id}.json
   - skills.json update
   - metrics.json update
9. Proposes commit message

**Lesson Document Structure:**

- Helm context (what you're building, why it matters)
- Learning objectives
- Concepts with examples
- Hands-on exercise (actual Helm feature)
- Checkpoint questions (every 10-15 minutes)
- Assessment criteria
- Key terms
- Resources

**Example:**

```text
You: /teach P01-M01-L01

Claude: Role: Professor activated.

Lesson: P01-M01-L01 - Version control concepts
Module: P01-M01 - Git fundamentals (6 hours)
Phase: P01 - Foundations

Helm Deliverable: Initialize Helm repository + README

[Generates lesson document artifact]

Type '/begin' to start, or ask questions first.

You: /begin

[Lesson proceeds with checkpoints...]
```

**Error Conditions:**

- Lesson file doesn't exist → Activate Curriculum Designer (separate chat) to generate it
- Prerequisites not met → Advisor recommends prerequisite lessons first

---

#### `/next`

**Purpose:** Get Advisor recommendation for next action

**Usage:**

```text
/next
```

**What Happens:**

1. Claude activates Advisor role
2. Loads all learner-state files
3. Loads curriculum.json
4. Loads curriculum files
5. Loads Helm product spec
6. Analyzes progress, skills, Helm priorities
7. Generates recommendation artifact with:
   - Suggested next lesson (with rationale)
   - Skills to review (if any)
   - Weekly plan (if appropriate)
   - Helm milestone context

**Output Example:**

```text
Recommendation:

Next Lesson: P01-M01-L02 - Git basic commands
Rationale: Continue Git fundamentals module. This lesson introduces commands you'll use daily for Helm development.

Prerequisites: ✓ P01-M01-L01 complete
Estimated Time: 60 minutes

Skills Status:
- git_basics: 2/5 (will improve to 3/5 after this lesson)

Weekly Plan:
- This Week: Complete Module 1.1 (3 lessons remaining, 4.5 hours)
- Next Week: Start Module 1.2 (Branching workflow)

Helm Progress:
- Current: Repo initialized, README written
- After this lesson: Basic Git workflow established
- Module 1.1 completion unlocks: First feature branch + PR

On Track: Yes. Phase 1 completion estimated Week 4.
```

**Questions You Can Ask:**

```text
What should I focus on this week?
Am I on track for Helm MVP by March?
Which module should I do next?
Should I review anything before continuing?
```

**No Arguments**

---

#### `/status`

**Purpose:** View comprehensive progress dashboard

**Usage:**

```text
/status
```

**What Happens:**

1. Claude loads all learner-state files
2. Loads curriculum files for context
3. Generates formatted dashboard showing:
   - Current position (phase/module/lesson)
   - Overall progress (phases/modules/lessons completed)
   - Time investment
   - Helm features shipped
   - Skill levels
   - Average confidence
   - Consistency score
   - Next milestone

**Output Example:**

```text
=== Helm Curriculum Progress Dashboard ===

Current Position:
  Phase: P01 - Foundations (Module 2 of 4)
  Module: P01-M02 - Branching and PRs
  Lesson: P01-M02-L01 - Feature branch workflow

Last Completed: P01-M01-L03 - Git remotes and GitHub
Last Updated: 2025-12-08

Overall Progress:
├─ Phases: 0/28 completed (0%)
├─ Modules: 1/139 completed (1%)
├─ Lessons: 3 completed
└─ Helm Features: 1 shipped (repo setup)

Time Investment:
├─ Total Time: 4.5 hours
├─ Average Session: 90 minutes
└─ Consistency: 0.3 (1 week with 2+ lessons)

Skill Levels:
├─ git_basics:         ★★★☆☆ (competent, confidence 3/5)
├─ terminal_comfort:   ★★☆☆☆ (emerging, confidence 2/5)
├─ markdown:           ★★☆☆☆ (emerging, confidence 3/5)

Average Confidence: 2.7/5
Reflections Written: 2

Next Milestone: Complete P01-M02 → Unlock PR workflow for Helm

Helm Progress:
├─ Repo Setup: ✓ Complete
├─ README: ✓ Complete
├─ First Commit: ✓ Complete
└─ Feature Branch: In Progress

=== End Dashboard ===
```

**Use Cases:**

- Weekly review
- Sharing progress with mentors
- Checking if on track for goals
- Identifying skill gaps

**No Arguments**

---

#### `/validate`

**Purpose:** Run schema validation on all curriculum and state files

**Usage:**

```text
/validate
```

**What Happens:**

1. Claude activates Architect role
2. Loads all JSON files in repository
3. Loads corresponding schemas
4. Validates each file against its schema
5. Reports results (valid/invalid with details)
6. Provides recommendations if issues found

**Output Example:**

```text
=== Schema Validation Report ===

Curriculum Files:
✓ curriculum/curriculum.json — VALID
✓ curriculum/phases/P01.json — VALID
✓ curriculum/modules/P01-M01.json — VALID
✗ curriculum/modules/P01-M02.json — INVALID
  Line 14: Missing required field 'helm_deliverable'

Learner State:
✓ learner-state/current.json — VALID
✓ learner-state/skills.json — VALID
✓ learner-state/metrics.json — VALID

Completed Records:
✓ learner-state/completed/P01-M01-L01.json — VALID
✓ learner-state/completed/P01-M01-L02.json — VALID

Lesson Files:
✓ curriculum/lessons/P01-M01-L01.json — VALID

Summary: 9/10 files valid (90%)

Recommendations:
1. Fix P01-M02.json: Add 'helm_deliverable' field
2. Example value: "Feature branch workflow for Helm"

=== End Validation ===
```

**When to Use:**

- After manually editing JSON files
- After generating new curriculum files
- Before committing major changes
- If system behaves unexpectedly

**No Arguments**

**Manual Validation (CLI):**

```bash
python tools/validate.py
```

---

#### `/snapshot {name}`

**Purpose:** Create backup of learner-state before risky operations

**Usage:**

```text
/snapshot pre-module-P02-M01
```

**Arguments:**

- `name`: Required. Descriptive name for snapshot (kebab-case recommended)

**What Happens:**

1. Claude activates Architect role
2. Creates ZIP archive of `learner-state/` directory
3. Saves to `snapshots/{date}-{name}.zip`
4. Generates confirmation artifact
5. Proposes commit message

**Output Example:**

```text
Snapshot created: snapshots/2025-12-08-pre-module-P02-M01.zip

Contents:
- learner-state/current.json
- learner-state/skills.json
- learner-state/metrics.json
- learner-state/completed/*.json (3 files)

Size: 4.2 KB

To restore this snapshot later:
/rollback pre-module-P02-M01

Proposed commit message:
chore(snapshot): create pre-module-P02-M01 backup
```

**When to Use:**

- Before starting new module
- Before major skill level adjustments
- Before redo operations
- Before manual state file edits

**Best Practice:** Create snapshots weekly (Sunday) as insurance.

---

#### `/rollback {name}`

**Purpose:** Restore learner-state from previous snapshot

**Usage:**

```text
/rollback pre-module-P02-M01
```

**Arguments:**

- `name`: Required. Snapshot name (without date prefix or .zip extension)

**What Happens:**

1. Claude activates Architect role
2. Locates snapshot in `snapshots/`
3. Extracts contents
4. Generates 4-5 artifacts (all state files)
5. User copies artifacts to `learner-state/`
6. Proposes commit message

**Output Example:**

```text
Restoring from: snapshots/2025-12-08-pre-module-P02-M01.zip

Files to be restored:
- current.json
- skills.json
- metrics.json
- completed/P01-M01-L01.json
- completed/P01-M01-L02.json
- completed/P01-M01-L03.json

[Generates 6 artifacts]

Copy artifacts to learner-state/ and commit.

Proposed commit message:
chore(rollback): restore state to pre-module-P02-M01
```

**When to Use:**

- Mistake in state files
- Need to redo module
- Accidentally advanced too far
- Corrupted state

**Important:** This is destructive. Confirm you want to lose current progress before rolling back.

---

#### `/help`

**Purpose:** Show all available commands with descriptions

**Usage:**

```text
/help
```

**Output:** Comprehensive command list with usage examples

**No Arguments**

---

### Additional Commands (Future)

These commands are documented but not yet implemented:

- `/redo {lesson_id}` — Re-attempt lesson without prior completion
- `/checkpoint` — Save current session state
- `/export` — Export metrics to CSV

---

## Workflow Patterns

### Pattern 1: Standard Lesson Completion

**Duration:** 45-90 minutes

**Steps:**

1. **Bootstrap:**

```text
/bootstrap
```

2. **Start lesson:**

```text
/teach P01-M01-L02
```

3. **Read artifact** (lesson document)

4. **Answer checkpoint 1** in chat

5. **Continue reading**

6. **Answer checkpoint 2** in chat

7. **Complete hands-on exercise** (build Helm feature)

8. **Answer final checkpoint** in chat

9. **Receive artifacts** (summary + 4 state files)

10. **Copy artifacts to VS Code:**
    - `lesson-summaries/P01-M01-L02-summary.md`
    - `learner-state/current.json`
    - `learner-state/completed/P01-M01-L02.json`
    - `learner-state/skills.json`
    - `learner-state/metrics.json`

11. **Commit:**

```bash
git add .
git commit -m "feat(lesson): complete P01-M01-L02 Git basic commands"
git push
```

12. **Optional: Write reflection:**

Create `reflections/2025-12-08.md`

---

### Pattern 2: Multi-Lesson Session

**Duration:** 2-3 hours (2-3 lessons)

**Steps:**

1. **Bootstrap once:**

```text
/bootstrap
```

2. **Teach lesson 1:**

```text
/teach P01-M02-L01
```

3. **Complete lesson 1** (read, answer checkpoints, exercise)

4. **Receive artifacts, copy to VS Code, commit**

5. **Teach lesson 2 immediately:**

```text
/teach P01-M02-L02
```

(No need to re-bootstrap in same chat)

6. **Complete lesson 2**

7. **Receive artifacts, copy, commit**

8. **Repeat for lesson 3 if time permits**

9. **End session with reflection covering all lessons**

**Advantage:** Maintains context across related lessons

**Disadvantage:** Long chat history (may hit token limits)

---

### Pattern 3: Review Session

**Duration:** 30-60 minutes

**Purpose:** Reinforce previous concepts without new lessons

**Steps:**

1. **Bootstrap:**

```text
/bootstrap
```

2. **Check status:**

```text
/status
```

3. **Identify weak skills** (confidence <3/5)

4. **Re-read previous summaries:**

```bash
cat lesson-summaries/P01-M01-*.md
```

5. **Practice exercises** from previous lessons

6. **Update skills.json** if mastery improved:

Edit manually in VS Code, then:

```text
/validate
```

7. **Commit:**

```bash
git add learner-state/skills.json
git commit -m "feat(skills): improve git_basics to competent level"
git push
```

**When to Use:**

- After completing a module (consolidate learning)
- Before starting new phase (refresh foundations)
- If struggling with current lessons (reinforce prerequisites)

---

### Pattern 4: Curriculum Generation

**Duration:** 30 minutes

**Purpose:** Generate phase/module/lesson files just-in-time

**Important:** Use **separate chat** from teaching chat

**Steps:**

1. **Open new Claude Desktop chat**

2. **Bootstrap:**

```text
/bootstrap
```

3. **Activate Designer:**

```text
/role curriculum-designer
```

4. **Request generation:**

```text
Generate all lessons for module P01-M02
```

or

```text
Generate Phase 2 files
```

5. **Receive artifacts** (JSON files)

6. **Copy artifacts to VS Code:**
    - Phase files → `curriculum/phases/`
    - Module files → `curriculum/modules/`
    - Lesson files → `curriculum/lessons/`

7. **Validate:**

```text
/validate
```

8. **Commit:**

```bash
git add curriculum/
git commit -m "feat(curriculum): generate module P01-M02 branching lessons"
git push
```

9. **Close curriculum generation chat**

10. **Return to teaching chat**

**Why Separate Chat?**

- Keeps teaching context clean
- Prevents role confusion
- Allows parallel curriculum development

---

### Pattern 5: Weekly Planning

**Duration:** 15-30 minutes

**When:** Sunday or Monday morning

**Steps:**

1. **Bootstrap:**

```text
/bootstrap
```

2. **Review week's progress:**

```text
/status
```

3. **Read reflections:**

```bash
cat reflections/2025-12-*.md
```

4. **Identify patterns:**
   - What concepts are clicking?
   - What needs more practice?
   - Am I maintaining pace?

5. **Get recommendation:**

```text
/next
```

Ask: "What should I focus on this week to stay on track for Helm MVP by March 2026?"

6. **Create snapshot:**

```text
/snapshot weekly-2025-12-08
```

7. **Plan time blocks:**
   - Monday: 2 hours (Lessons 1-2)
   - Wednesday: 1.5 hours (Lesson 3)
   - Friday: 2 hours (Lessons 4-5)
   - Sunday: 1 hour (Review + reflection)

8. **Set calendar reminders**

9. **Commit snapshot:**

```bash
git add snapshots/
git commit -m "chore(snapshot): weekly backup 2025-12-08"
git push
```

---

### Pattern 6: Module Completion

**Duration:** 1 hour

**When:** After completing all lessons in a module

**Steps:**

1. **Bootstrap:**

```text
/bootstrap
```

2. **Verify module completion:**

```text
/status
```

3. **Review all lesson summaries for module:**

```bash
cat lesson-summaries/P01-M01-*.md
```

4. **Activate Evaluator:**

```text
/role evaluator
```

5. **Request module evaluation:**

```text
Evaluate module P01-M01. Did I meet all learning objectives?
```

6. **Review Helm deliverable:**

Check that module's Helm feature is complete and functional.

7. **If evaluation reveals gaps:**

```text
/redo P01-M01-L02
```

(Re-attempt specific lesson)

8. **If module mastered:**

```text
/next
```

(Get recommendation for next module)

9. **Create snapshot:**

```text
/snapshot post-module-P01-M01
```

10. **Write comprehensive reflection:**

Create `reflections/2025-12-08-module-P01-M01-complete.md`

11. **Commit:**

```bash
git add .
git commit -m "feat(progress): complete module P01-M01 Git fundamentals"
git push
```

---

## State Management

### State Architecture

The system uses **decomposed state files** instead of one monolithic file:

```text
learner-state/
├── current.json          # Active position only
├── skills.json           # Skill levels only
├── metrics.json          # Aggregate stats only
└── completed/            # Per-lesson records
    ├── P01-M01-L01.json
    ├── P01-M01-L02.json
    └── ...
```

**Why Decomposed?**
- Clean Git history (change one thing = one file changes)
- Easy to understand diffs
- Prevents merge conflicts
- Enables partial rollbacks

### State Files Explained

#### `current.json`

**Purpose:** Track active position in curriculum

**Schema:** `schemas/state-current.schema.json`

**Fields:**
- `learner_id`: Your identifier (e.g., "jeff")
- `current_phase_id`: Active phase (e.g., "P01")
- `current_module_id`: Active module (e.g., "P01-M01")
- `current_lesson_id`: Active lesson (e.g., "P01-M01-L01")
- `last_updated`: ISO timestamp

**Example:**

```json
{
  "learner_id": "jeff",
  "current_phase_id": "P01",
  "current_module_id": "P01-M02",
  "current_lesson_id": "P01-M02-L01",
  "last_updated": "2025-12-08T15:30:00Z"
}
```

**Updates After:** Every lesson completion

---

#### `skills.json`

**Purpose:** Track skill levels across curriculum

**Schema:** `schemas/state-skills.schema.json`

**Skill Levels:**
- `novice`: Just introduced, minimal practice
- `emerging`: Basic understanding, some practice
- `competent`: Comfortable with common scenarios
- `proficient`: Can handle edge cases, teach others
- `expert`: Deep mastery, can architect systems

**Fields (per skill):**
- `level`: Current skill level
- `last_practiced`: Date last used
- `confidence`: Self-assessment (1-5)
- `modules_practiced`: List of modules where skill used

**Example:**

```json
{
  "skills": {
    "git_basics": {
      "level": "competent",
      "last_practiced": "2025-12-08",
      "confidence": 3,
      "modules_practiced": ["P01-M01", "P01-M02"]
    },
    "react_hooks": {
      "level": "emerging",
      "last_practiced": "2025-12-01",
      "confidence": 2,
      "modules_practiced": ["P11-M01"]
    }
  },
  "last_updated": "2025-12-08T15:30:00Z"
}
```

**Updates After:** Lessons that practice specific skills

**Manual Updates:** Allowed if you practice skills outside curriculum (validate after editing)

---

#### `metrics.json`

**Purpose:** Track aggregate progress statistics

**Schema:** `schemas/state-metrics.schema.json`

**Fields:**
- `total_time_minutes`: Cumulative time invested
- `lessons_completed`: Count of completed lessons
- `modules_completed`: Count of completed modules
- `phases_completed`: Count of completed phases
- `helm_features_shipped`: Count of Helm features completed
- `reflections_written`: Count of reflection documents
- `average_confidence`: Average self-assessment across skills
- `consistency_score`: 0-1 score based on weekly activity
- `last_updated`: ISO timestamp

**Example:**

```json
{
  "total_time_minutes": 270,
  "lessons_completed": 3,
  "modules_completed": 1,
  "phases_completed": 0,
  "helm_features_shipped": 1,
  "reflections_written": 2,
  "average_confidence": 2.7,
  "consistency_score": 0.3,
  "last_updated": "2025-12-08T15:30:00Z"
}
```

**Updates After:** Every lesson completion

**Consistency Score Calculation:**
- 1.0 = Completed 2+ lessons every week for last 4 weeks
- 0.5 = Completed 1+ lesson most weeks
- 0.0 = Sporadic activity

---

#### `completed/{lesson_id}.json`

**Purpose:** Detailed record of each completed lesson

**Schema:** `schemas/state-completed.schema.json`

**Location:** `learner-state/completed/P01-M01-L01.json`

**Fields:**
- `lesson_id`: Completed lesson
- `module_id`: Parent module
- `phase_id`: Parent phase
- `completed_at`: ISO timestamp
- `duration_minutes`: Time spent on lesson
- `confidence_rating`: Self-assessment (1-5)
- `helm_deliverable`: What Helm feature was built
- `code_committed`: Boolean (was code committed?)
- `objectives_met`: List of objectives achieved
- `struggles`: List of challenges faced
- `misconceptions_noted`: List of misconceptions corrected

**Example:**

```json
{
  "lesson_id": "P01-M01-L01",
  "module_id": "P01-M01",
  "phase_id": "P01",
  "completed_at": "2025-12-08T15:30:00Z",
  "duration_minutes": 90,
  "confidence_rating": 3,
  "helm_deliverable": "Initialize Helm repository with README",
  "code_committed": true,
  "objectives_met": [
    "Understand purpose of version control",
    "Explain Git vs GitHub",
    "Create first repository"
  ],
  "struggles": [
    "Confused about staging area vs working directory"
  ],
  "misconceptions_noted": [
    "Initially thought Git and GitHub were same thing"
  ]
}
```

**Updates After:** Every lesson completion

**Use Cases:**
- Progress tracking
- Identifying patterns in struggles
- Evaluator assessment
- Portfolio documentation

---

### State Update Workflow

#### Professor-Generated Updates

After each lesson, Professor generates 4-5 artifacts:

1. **current.json**
   - Updates `current_lesson_id` to next lesson
   - Updates `current_module_id` if transitioning modules
   - Updates `last_updated`

2. **completed/{lesson_id}.json**
   - Creates new completion record
   - Includes all lesson details

3. **skills.json**
   - Updates skill levels based on lesson practice
   - Updates `last_practiced` dates
   - Adds module to `modules_practiced`
   - Updates `confidence` if appropriate

4. **metrics.json**
   - Increments `lessons_completed`
   - Increments `modules_completed` if module complete
   - Increments `phases_completed` if phase complete
   - Adds `duration_minutes` to `total_time_minutes`
   - Increments `helm_features_shipped` if deliverable complete
   - Recalculates `average_confidence`
   - Updates `consistency_score`

5. **Lesson summary** (separate from state files)
   - Goes to `lesson-summaries/`

#### Your Workflow

1. **Copy artifacts** from Claude to VS Code
2. **Save files** in appropriate locations
3. **Validate** (optional but recommended):

```text
/validate
```

4. **Commit** with proposed message:

```bash
git add learner-state/ lesson-summaries/
git commit -m "feat(lesson): complete P01-M01-L01 version control concepts"
git push
```

#### Manual Editing

**When Allowed:**
- Correcting mistakes in state files
- Updating skills practiced outside curriculum
- Adjusting confidence ratings after practice

**Process:**

1. **Open file in VS Code**
2. **Edit JSON** (be careful with syntax)
3. **Validate:**

```text
/validate
```

4. **If valid, commit:**

```bash
git add learner-state/skills.json
git commit -m "fix(state): correct git_basics level to competent"
git push
```

5. **If invalid, fix errors and re-validate**

**Best Practice:** Create snapshot before manual edits

---

### State Consistency

#### Consistency Rules

1. **current.json must point to valid lesson**
   - Lesson file must exist
   - Prerequisite lessons must be complete

2. **completed/ files must match metrics**
   - Count of completed/*.json must equal metrics.lessons_completed

3. **Skills must reference real modules**
   - modules_practiced must list only existing modules

4. **Timestamps must be logical**
   - completed_at must be before current date
   - last_updated must match latest activity

#### Validation

Run regularly:

```text
/validate
```

Or via CLI:

```bash
python tools/validate.py
```

#### Recovery from Inconsistency

If validation fails:

1. **Read error message** (shows file + issue)
2. **Fix manually** or **rollback** to last snapshot
3. **Re-validate**
4. **Commit fix**

---

## Curriculum Generation

### Just-In-Time Philosophy

**Do NOT:**
- Pre-generate all 28 phases upfront
- Create all 139 modules before starting
- Generate all lessons for a module before teaching first lesson

**DO:**
- Generate phase files as you approach new phase (75% through current phase)
- Generate module files when phase starts
- Generate lesson files just before teaching

**Why?**
- **Flexibility:** Adjust curriculum based on progress and feedback
- **Efficiency:** Don't waste time on content that might change
- **Focus:** Keep repository lean and manageable
- **Iteration:** Improve lessons based on actual experience

### Source of Truth: CSV

`curriculum.json` contains:
- All 28 phases
- All 139 modules
- Module names, focus areas, estimated hours
- Helm deliverables

**Curriculum Designer uses CSV** as reference when generating JSON files.

### Generation Workflow

#### Step 1: Open Separate Chat

**Important:** Use dedicated chat for curriculum generation (not teaching chat)

Open new Claude Desktop chat.

#### Step 2: Bootstrap

```text
/bootstrap
```

#### Step 3: Activate Curriculum Designer

```text
/role curriculum-designer
```

#### Step 4: Request Generation

**Generate Phase File:**

```text
Generate Phase 2 file
```

Claude will:
1. Read curriculum.json
2. Filter rows for Phase 2
3. Generate P02.json with all modules listed
4. Output as artifact

**Generate Module Files:**

```text
Generate all modules for Phase 2
```

Claude will:
1. Read CSV rows for Phase 2
2. Generate P02-M01.json through P02-M04.json
3. Each module includes:
   - Module metadata
   - Helm deliverable
   - Learning objectives
   - Lesson outline (3-5 lessons per module)
   - Skills taught
   - Resources
4. Output as 4 artifacts

**Generate Lesson Files:**

```text
Generate all lessons for module P02-M01
```

Claude will:
1. Read P02-M01.json for lesson outline
2. Generate P02-M01-L01.json through P02-M01-L03.json
3. Each lesson includes:
   - Lesson metadata
   - Learning objectives
   - Detailed content outline
   - Helm context
   - Assessment criteria
   - Professor constraints
4. Output as 3 artifacts

#### Step 5: Copy Artifacts to VS Code

**Phase files** → `curriculum/phases/P02.json`

**Module files** → `curriculum/modules/P02-M01.json`, etc.

**Lesson files** → `curriculum/lessons/P02-M01-L01.json`, etc.

#### Step 6: Validate

In curriculum generation chat:

```text
/validate
```

or in VS Code terminal:

```bash
python tools/validate.py
```

#### Step 7: Commit

```bash
git add curriculum/
git commit -m "feat(curriculum): generate Phase 2 professional tooling modules"
git push
```

#### Step 8: Close Curriculum Chat

Close the curriculum generation chat. Return to teaching chat.

### Generation Triggers

| Trigger | Action |
|---------|--------|
| Project start | Generate P01.json + P01-M01 through P01-M04 |
| User requests `/teach P01-M01-L01` | Generate all P01-M01 lessons (if not exist) |
| Phase 1 reaches 75% | Generate P02.json + P02 modules |
| User completes Phase 1 | Generate Phase 2 lessons as needed |
| Repeat pattern for all 28 phases | ... |

### Customization

**Modify Curriculum:**

1. **Edit curriculum.json** in VS Code
   - Change module names
   - Adjust estimated hours
   - Update Helm deliverables
   - Add/remove modules

2. **Regenerate affected files:**

Open curriculum generation chat:

```text
/role curriculum-designer
Regenerate Phase 3 modules (CSV was updated)
```

3. **Replace old files** with new artifacts

4. **Validate and commit**

---

## Quality Assurance

### Validation Pipeline

#### Pre-Commit Validation (Claude)

Claude validates all JSON artifacts against schemas **before** outputting them.

You should never receive invalid JSON from Claude.

#### Post-Commit Validation (CI)

GitHub Actions runs `tools/validate.py` on every push to master.

**Workflow:** `.github/workflows/validate.yml`

**What It Does:**
1. Checks out repository
2. Installs Python dependencies
3. Runs validation script
4. Fails build if any file violates schema

**View Results:** GitHub repo → Actions tab

#### Manual Validation

**Command:**

```text
/validate
```

or

```bash
python tools/validate.py
```

**When to Run:**
- After manually editing JSON files
- After generating new curriculum files
- Before committing major changes
- If system behaves unexpectedly

### Lesson Quality

#### Professor Constraints

Each lesson file includes `professor_constraints` field:

```json
{
  "professor_constraints": [
    "Do not provide complete code solutions until after learner attempts exercise",
    "Pause for checkpoint questions every 10-15 minutes",
    "Use Helm examples for all concepts",
    "Verify hands-on exercise completion before generating artifacts"
  ]
}
```

Professor role **must** follow these constraints.

#### Evaluator Assessment

After completing a lesson, you can evaluate it:

```text
/role evaluator
Evaluate P01-M01-L01
```

Evaluator checks:
- Were objectives met?
- Were checkpoints effective?
- Was Helm deliverable complete?
- Were struggles addressed?
- Should lesson be improved?

#### Lesson Iteration

If Evaluator identifies issues:

1. **Open curriculum generation chat**
2. **Activate Designer:**

```text
/role curriculum-designer
```

3. **Request lesson update:**

```text
Update P01-M01-L01 based on this feedback:
[paste Evaluator's recommendations]
```

4. **Copy updated artifact** to `curriculum/lessons/`

5. **Commit:**

```bash
git add curriculum/lessons/P01-M01-L01.json
git commit -m "fix(lesson): improve P01-M01-L01 based on evaluation"
git push
```

### Code Quality (Helm)

#### During Lessons

Professor guides you to write high-quality Helm code:
- Follow style guides (Python: PEP 8, JavaScript: Airbnb)
- Write tests (once testing module complete)
- Document code (docstrings, comments)
- Use type hints (Python, TypeScript)

#### Post-Lesson Evaluation

Evaluator can review Helm code:

```text
/role evaluator
Review Helm code from P08-M01-L03
```

Evaluator checks:
- Follows architecture patterns
- Passes tests
- Meets acceptance criteria
- Ready to ship

#### CI/CD (Future)

Once Phase 21 (DevOps) is complete:
- Helm repo will have CI/CD pipeline
- Automated tests on every commit
- Linting, formatting checks
- Deployment to staging

---

## Troubleshooting

### MCP Connection Issues

#### Symptom

Claude responds: "I cannot access your repository" or `/bootstrap` fails.

#### Diagnosis

1. **Check config file exists:**

```bash
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

Should show GitHub MCP and Filesystem MCP configuration.

2. **Check GitHub token:**

Visit: https://github.com/settings/tokens

Verify token is active and has `repo`, `read:org` scopes.

3. **Check Filesystem path:**

Verify path in config matches actual repo location:

```bash
ls -la /Users/jeffhutting/dev/dev-curriculum
```

Should list repo contents.

#### Solution

**If config file missing:**

Create `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/jeffhutting/dev/dev-curriculum"]
    }
  }
}
```

**If token invalid:**

1. Go to: https://github.com/settings/tokens
2. Generate new token (classic)
3. Scopes: `repo`, `read:org`
4. Copy token and update config file

**If path wrong:**

Update `filesystem` path in config to match actual repo location.

**Always after config changes:**

Restart Claude Desktop (completely quit and reopen).

---

### Schema Validation Failures

#### Symptom

`/validate` or `python tools/validate.py` reports errors.

#### Diagnosis

Read error message carefully:

```text
✗ curriculum/modules/P01-M02.json — INVALID
  Line 14: Missing required field 'helm_deliverable'
```

Tells you:
- Which file has issue
- What the problem is

#### Solution

**Open file in VS Code:**

```bash
code curriculum/modules/P01-M02.json
```

**Fix the issue** (in this example, add missing field):

```json
{
  "module_id": "P01-M02",
  "module_name": "Branching and PRs",
  "helm_deliverable": "Feature branch workflow for Helm",
  ...
}
```

**Validate again:**

```text
/validate
```

or

```bash
python tools/validate.py
```

**If valid, commit:**

```bash
git add curriculum/modules/P01-M02.json
git commit -m "fix(curriculum): add missing helm_deliverable to P01-M02"
git push
```

---

### Lost Progress

#### Symptom

State files corrupted, accidentally deleted, or out of sync.

#### Diagnosis

Check Git history:

```bash
git log --oneline learner-state/
```

Check snapshots:

```bash
ls -lh snapshots/
```

#### Solution A: Restore from Git

```bash
# View file at specific commit
git show {commit_hash}:learner-state/current.json

# Restore file from commit
git checkout {commit_hash} -- learner-state/current.json

# Commit restoration
git add learner-state/current.json
git commit -m "fix(state): restore current.json from {commit_hash}"
```

#### Solution B: Restore from Snapshot

```text
/rollback weekly-2025-12-01
```

Copy artifacts to VS Code, commit.

#### Solution C: Manual Reconstruction

If no backup available:

1. **Open state files in VS Code**
2. **Reconstruct based on:**
   - Lesson summaries
   - Git commit history
   - Memory of what you completed
3. **Validate:**

```text
/validate
```

4. **Commit:**

```bash
git add learner-state/
git commit -m "fix(state): reconstruct state after data loss"
git push
```

**Prevention:** Create weekly snapshots.

---

### Curriculum Files Missing

#### Symptom

Claude says: "Lesson file P02-M01-L01.json does not exist"

#### Diagnosis

Check if file exists:

```bash
ls curriculum/lessons/P02-M01-L01.json
```

If missing, needs generation.

#### Solution

1. **Open separate chat** (curriculum generation)

2. **Bootstrap:**

```text
/bootstrap
```

3. **Activate Designer:**

```text
/role curriculum-designer
```

4. **Request generation:**

```text
Generate all lessons for module P02-M01
```

5. **Copy artifacts** to `curriculum/lessons/`

6. **Validate:**

```text
/validate
```

7. **Commit:**

```bash
git add curriculum/lessons/
git commit -m "feat(curriculum): generate module P02-M01 lessons"
git push
```

8. **Return to teaching chat**

9. **Retry:**

```text
/teach P02-M01-L01
```

---

### State Files Out of Sync

#### Symptom

- `metrics.lessons_completed` doesn't match count of `completed/*.json` files
- `current.json` points to lesson you haven't completed
- Skills reference non-existent modules

#### Diagnosis

Run validation:

```text
/validate
```

Architect will identify inconsistencies.

#### Solution

**If minor inconsistency** (e.g., count off by 1):

Manually edit affected file(s) in VS Code, validate, commit.

**If major inconsistency** (e.g., many fields wrong):

Rollback to recent snapshot:

```text
/rollback weekly-2025-12-01
```

**Prevention:**
- Always commit all state files together
- Use Claude-generated artifacts (don't manually edit unless necessary)
- Create snapshots before risky operations

---

### Professor Ignoring Constraints

#### Symptom

Professor provides complete solutions before you attempt exercise, or skips checkpoints.

#### Diagnosis

Check lesson file:

```bash
cat curriculum/lessons/P01-M01-L01.json
```

Look at `professor_constraints` field.

#### Solution

**In chat, explicitly remind Claude:**

```text
Please follow the professor constraints in the lesson file:
- Do not provide complete solutions until I attempt exercise
- Pause for checkpoints every 10-15 minutes
```

**If problem persists:**

1. **Open curriculum generation chat**
2. **Update lesson file** to strengthen constraints
3. **Commit updated lesson**
4. **Retry lesson:**

```text
/redo P01-M01-L01
```

---

### Commit Message Errors

#### Symptom

CI fails with message: "Commit message does not follow Conventional Commits"

#### Diagnosis

Check commit message format:

```bash
git log --oneline -1
```

Should be: `type(scope): subject` (e.g., `feat(lesson): complete P01-M01-L01`)

#### Solution

**If not pushed yet:**

Amend commit:

```bash
git commit --amend -m "feat(lesson): complete P01-M01-L01 version control concepts"
git push
```

**If already pushed:**

Create new commit with correct message:

```bash
git revert HEAD
git add .
git commit -m "feat(lesson): complete P01-M01-L01 version control concepts"
git push
```

**Prevention:** Always use Claude's proposed commit messages.

---

## Best Practices

### Daily Habits

1. **Bootstrap every session**
   - Ensures Claude has latest context
   - Prevents assumptions based on stale data

2. **Commit after every lesson**
   - Never skip commits
   - Use Claude's proposed messages
   - Group state updates together

3. **Write reflections**
   - Even 2-3 sentences helps
   - Identify patterns in learning
   - Reference later for reviews

4. **Validate before committing**
   - Quick check: `/validate`
   - Catches errors early

5. **Push immediately**
   - Don't accumulate unpushed commits
   - GitHub is backup and source of truth

### Weekly Habits

1. **Sunday planning**
   - Review progress: `/status`
   - Read week's reflections
   - Get recommendation: `/next`
   - Plan time blocks

2. **Weekly snapshots**
   - Every Sunday: `/snapshot weekly-YYYY-MM-DD`
   - Insurance against mistakes

3. **Module reviews**
   - After completing module, review all summaries
   - Evaluate with Evaluator role
   - Identify gaps before advancing

### Monthly Habits

1. **Phase reviews**
   - After completing phase, comprehensive review
   - Re-do weak lessons if needed
   - Validate Helm features are production-ready

2. **Skill assessments**
   - Update skills.json based on practice
   - Identify skills to maintain vs. advance

3. **Curriculum adjustments**
   - Modify CSV if priorities change
   - Regenerate affected modules

### Git Hygiene

1. **Follow Conventional Commits**
   - Always use format: `type(scope): subject`
   - Common types: `feat`, `fix`, `docs`, `chore`, `refactor`

2. **Atomic commits**
   - One logical change per commit
   - State updates always together
   - Lesson summaries with lesson completion

3. **Clear commit messages**
   - Subject line: max 50 chars
   - Body: wrap at 72 chars
   - Explain what and why, not how

4. **Use branches** (once branching module complete)
   - Feature branches for Helm work
   - Main branch for curriculum state

### State Management

1. **Never guess**
   - Read state files, don't assume
   - Use `/status` to verify progress

2. **Validate after manual edits**
   - Always run `/validate` after editing JSON
   - Fix errors before committing

3. **Create snapshots before risky operations**
   - Before redo
   - Before major state edits
   - Before module transitions

4. **Trust Git as source of truth**
   - State is in files, not chat history
   - Can reconstruct from Git if needed

### Lesson Execution

1. **Read entire artifact before starting**
   - Understand scope before diving in
   - Identify time needed

2. **Actually answer checkpoints**
   - Don't skip or rush
   - Honest answers help Claude adapt

3. **Complete hands-on exercises**
   - Build actual Helm features
   - No shortcuts or mock implementations

4. **Test what you build**
   - Verify Helm features work
   - Don't just assume code is correct

### Time Management

1. **Block dedicated time**
   - 45-90 minute blocks
   - No distractions (close email, Slack, etc.)

2. **Maintain consistency**
   - 2-3 sessions per week minimum
   - Build habit, not rely on motivation

3. **Don't over-commit**
   - 15 hrs/week is sustainable
   - 30 hrs/week leads to burnout

4. **Review > Progress**
   - Better to master 1 module than rush through 3
   - Depth > breadth

### Portfolio Building

1. **Helm is your portfolio**
   - Every commit is portfolio material
   - Keep commit quality high

2. **Document as you build**
   - Write clear READMEs
   - Add code comments
   - Create architecture docs

3. **Share progress**
   - Blog about Helm development
   - Tweet screenshots
   - Share lessons learned

4. **Open source when ready**
   - After Phase 28, Helm can be public repo
   - Demonstrates full-stack capability

---

## Advanced Topics

### Custom Projects

**Helm is primary spine**, but you can add supplementary projects:

#### Step 1: Create Project Spec

Create `projects/supplementary/my-project-spec.md`:

```markdown
# My Project

## Overview
[Description]

## Tech Stack
[Technologies]

## Features
[Feature list]

## Learning Goals
[What skills this project teaches]
```

#### Step 2: Modify Curriculum

Edit `curriculum.json`:

Add rows for new modules that reference your project.

#### Step 3: Regenerate Modules

Open curriculum generation chat:

```text
/role curriculum-designer
Generate modules for my custom project based on updated CSV
```

#### Step 4: Teach Lessons

Use Professor role as normal. Lessons will reference your project instead of Helm.

### Multiple Learners

This system is designed for one learner (Jeff), but can be adapted for multiple learners:

#### Option 1: Separate Repositories

Each learner clones and maintains their own fork.

**Pros:**
- Complete independence
- Clean Git history per learner

**Cons:**
- Curriculum updates not shared

#### Option 2: Branches

Each learner has own branch for state files.

**Pros:**
- Shared curriculum updates
- Can compare progress

**Cons:**
- Merge conflicts if curriculum changes

#### Option 3: Separate State Directories

```text
learner-state/
├── jeff/
│   ├── current.json
│   ├── skills.json
│   └── ...
├── sarah/
│   ├── current.json
│   ├── skills.json
│   └── ...
```

Requires modifying schemas and bootstrap command.

### Metrics Export

**Future Enhancement:** Export metrics to CSV for external visualization.

**Script:** `tools/export_metrics.py` (to be created)

**Usage:**

```bash
python tools/export_metrics.py --output metrics-2025-12.csv
```

**Output:** CSV with columns:
- Date
- Lessons completed
- Time invested
- Confidence ratings
- Skill levels

**Visualization:** Import into Google Sheets, Tableau, or Python (pandas + matplotlib).

### Custom Commands

You can define custom commands by updating system instructions or creating macros.

**Example:** `/weekly-plan`

Add to instructions:

```text
When user types /weekly-plan:
1. Activate Advisor
2. Load learner-state files
3. Generate plan for next 7 days
4. Include recommended lessons, time estimates, Helm milestones
```

### Integration with Task Managers

**Export TODO list from curriculum:**

```bash
# Extract upcoming lessons
grep "current_lesson_id" learner-state/current.json
grep "lessons" curriculum/modules/P01-M02.json | jq -r '.lessons[].title'
```

**Create Notion tasks:**
- Manually or via Notion API
- One task per lesson
- Link to lesson summary after completion

**Create GitHub Issues:**
- One issue per module
- Checklist of lessons
- Close issue when module complete

---

## Appendix: File Reference

### Repository Structure

See README.md → Repository Structure for complete tree.

### Key File Locations

**Curriculum:**
- Top-level: `curriculum/curriculum.json`
- Phases: `curriculum/phases/P##.json`
- Modules: `curriculum/modules/P##-M##.json`
- Lessons: `curriculum/lessons/P##-M##-L##.json`

**State:**
- Current: `learner-state/current.json`
- Skills: `learner-state/skills.json`
- Metrics: `learner-state/metrics.json`
- Completed: `learner-state/completed/P##-M##-L##.json`

**Outputs:**
- Summaries: `lesson-summaries/P##-M##-L##-summary.md`
- Reflections: `reflections/YYYY-MM-DD.md`
- Snapshots: `snapshots/YYYY-MM-DD-name.zip`

**Meta:**
- Schemas: `schemas/*.schema.json`
- Roles: `roles/*.md`
- Templates: `templates/*.md`
- Tools: `tools/*.py`

**Project:**
- Helm Spec: `projects/helm-product-spec.md`
- Master Curriculum: `curriculum.json`

**Documentation:**
- Architecture: `ARCHITECTURE.md`
- Operations: `instructions.md` (this file)
- Quick Start: `quickstart.md`
- Overview: `README.md`

### Schema Reference

All schemas are JSON Schema Draft 7.

**Curriculum Schemas:**
- `schemas/curriculum.schema.json` — Top-level curriculum
- `schemas/phase.schema.json` — Phase structure
- `schemas/module.schema.json` — Module structure
- `schemas/lesson.schema.json` — Lesson structure

**State Schemas:**
- `schemas/state-current.schema.json` — Current position
- `schemas/state-completed.schema.json` — Lesson completion
- `schemas/state-skills.schema.json` — Skill tracking
- `schemas/state-metrics.schema.json` — Progress metrics

---

## Version History

### v2.0 (Current)

- Complete rewrite for Helm project spine
- Decomposed state files (current, skills, metrics, completed)
- Just-in-time curriculum generation
- Role-based operation (5 roles)
- MCP integration (GitHub + Filesystem)
- Artifact-first delivery
- 28 phases, 139 modules, ~850 hours

### v1.0 (Deprecated)

- Original monolithic state file
- Pre-generated curriculum
- Single AI role
- Manual file syncing

---

## Feedback & Improvements

This is a living document. As you use the system:

1. **Note pain points**
2. **Identify missing instructions**
3. **Suggest improvements**
4. **Update this document**

**Commit documentation improvements:**

```bash
git add instructions.md
git commit -m "docs(instructions): add troubleshooting for X"
git push
```

---

## Quick Reference Card

### Essential Commands

```text
/bootstrap              # Start session
/teach P01-M01-L01     # Start lesson
/next                  # Get recommendation
/status                # View progress
/validate              # Check schemas
/snapshot {name}       # Create backup
/rollback {name}       # Restore backup
/help                  # Show all commands
```

### Session Pattern

```text
1. /bootstrap
2. /teach P01-M01-L01
3. [Read, answer checkpoints, exercise]
4. [Copy artifacts to VS Code]
5. git add . && git commit -m "..." && git push
6. /next
```

### State Files

```text
learner-state/current.json     # Where you are
learner-state/skills.json      # What you know
learner-state/metrics.json     # Your progress
learner-state/completed/*.json # What you've done
```

### Commit Message Format

```text
type(scope): subject

type: feat|fix|docs|style|refactor|test|chore
scope: lesson|progress|state|curriculum|docs
subject: max 50 chars, imperative mood
```

---

**End of Operations Manual**

**Ready to build Helm?** Start with `/bootstrap` in Claude Desktop.
