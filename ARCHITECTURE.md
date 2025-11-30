# ARCHITECTURE.md — Claude-Native Edition v1.0

> **Status:** Active Development (v1.0)  
> **Platform:** Claude Desktop + GitHub MCP + VS Code  
> **Philosophy:** File-backed state, artifact-first delivery, Git-native workflow

---

## Table of Contents

- [Phase 0: Mental Model](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#phase-0-mental-model)
- [Phase 1: Repository Structure](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#phase-1-repository-structure)
- [Phase 2: GitHub MCP Setup](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#phase-2-github-mcp-setup)
- [Phase 3: Core Schemas](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#phase-3-core-schemas)
- [Phase 4: Role System](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#phase-4-role-system)
- [Phase 5: Bootstrap Ritual](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#phase-5-bootstrap-ritual)
- [Phase 6: Quick Start Path](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#phase-6-quick-start-path)
- [Phase 7: Learner State Architecture](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#phase-7-learner-state-architecture)
- [Phase 8: Lesson Delivery Model](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#phase-8-lesson-delivery-model)
- [Phase 9: Command Registry](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#phase-9-command-registry)
- [Phase 10: Validation Pipeline](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#phase-10-validation-pipeline)
- [Phase 11: Recovery & Rollback System](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#phase-11-recovery--rollback-system)
- [Phase 12: Success Metrics](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#phase-12-success-metrics)
- [Appendix A: File Index Structure](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#appendix-a-file-index-structure)
- [Appendix B: Roadmap](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#appendix-b-roadmap)
- [Appendix C: Migration from ChatGPT](https://claude.ai/chat/24b3d28d-d84f-48e3-b511-9992e9e004e0#appendix-c-migration-from-chatgpt)

---

## Phase 0: Mental Model

### What This System Is

A **Git-native, Claude-assisted learning operating system** where:

- All state lives in your repository, not AI memory
- Claude reads files via GitHub MCP during sessions
- You approve and execute all commits
- Every deliverable is artifact-first for clean copy/paste
- Progress compounds through structured practice, not passive consumption

### Core Principles

1. **File-backed state** — Repository is source of truth
2. **Artifact-first delivery** — All structured content uses Claude's artifact system
3. **Explicit role contracts** — Roles defined in versioned files
4. **Git-native workflow** — Every session produces a commit
5. **Minimal viable commands** — Start with 5 core commands, add only when needed
6. **Progressive disclosure** — Quick start path for beginners, comprehensive docs for depth

### Key Components

**Entities:**

- `Curriculum` — Top-level learning design
- `Phase` — Major learning sections (e.g., Foundations, Backend)
- `Lesson` — Individual teaching units
- `Project` — Long-lived code repositories
- `State` — Your progress, decomposed into atomic files

**Roles:**

- `Architect` — System design and schema management
- `Curriculum Designer` — Lesson sequencing and scaffolding
- `Professor` — Lesson delivery and teaching
- `Advisor` — Progress tracking and next-step recommendations
- `Evaluator` — Assessment and quality assurance

**Workflow:**

1. Claude reads repo via GitHub MCP
2. You select a role and task
3. Claude generates artifacts (JSON, Markdown, code)
4. You review, copy to VS Code, save files
5. Claude proposes commit message
6. You commit and push

---

## Phase 1: Repository Structure

### 1.1 Create GitHub Repository

Repository name: `dev-curriculum`

### 1.2 Directory Structure

```text
dev-curriculum/
├── curriculum/
│   ├── curriculum.json              # Top-level design
│   ├── phases/
│   │   ├── P1-index.json            # Phase 1 overview + lesson list
│   │   ├── P2-index.json
│   │   └── ...
│   └── lessons/
│       ├── P1-L01.json              # Full lesson detail
│       ├── P1-L02.json
│       └── ...
├── projects/
│   ├── PRJ-GIT-INTRO.json           # Project definitions
│   └── ...
├── learner-state/
│   ├── current.json                 # Active position (phase, lesson)
│   ├── completed/
│   │   ├── P1-L01.json              # Per-lesson completion record
│   │   └── ...
│   ├── skills.json                  # Skill tracking
│   └── metrics.json                 # Time, confidence, mastery data
├── reflections/
│   ├── 2025-11-29.md                # Daily reflection entries
│   └── ...
├── lesson-summaries/
│   ├── P1-L01-summary.md            # Per-lesson summaries
│   └── ...
├── schemas/
│   ├── curriculum.schema.json
│   ├── phase-index.schema.json
│   ├── lesson.schema.json
│   ├── project.schema.json
│   ├── state-current.schema.json
│   ├── state-completed.schema.json
│   ├── state-skills.schema.json
│   └── state-metrics.schema.json
├── roles/
│   ├── architect.md                 # Role definition files
│   ├── curriculum-designer.md
│   ├── professor.md
│   ├── advisor.md
│   └── evaluator.md
├── templates/
│   ├── lesson-summary.template.md   # Strict templates (machine-readable)
│   ├── reflection.template.md       # Loose templates (human-readable)
│   └── commit-message.template.txt
├── snapshots/
│   ├── 2025-11-29-pre-lesson.zip    # State snapshots for rollback
│   └── ...
├── tools/
│   └── validate.py                  # Schema validation script
├── .github/
│   └── workflows/
│       └── validate.yml             # CI validation
├── user-profile.md                  # Single unified profile
├── quickstart.md                    # Beginner-friendly entry point
├── instructions.md                  # Comprehensive reference
└── README.md
```

### 1.3 Initial Commit

Create this structure locally, then:

```bash
git init
git add .
git commit -m "feat(init): create curriculum system structure"
git branch -M main
git remote add origin git@github.com:jeff-hutting/dev-curriculum.git
git push -u origin main
```

---

## Phase 2: GitHub MCP Setup

### 2.1 Install Claude Desktop

Download from: https://claude.ai/download

### 2.2 Configure GitHub MCP Server

**Location:** `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS)

**Configuration:**

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### 2.3 Generate GitHub Personal Access Token

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Scopes needed:
    - `repo` (full control of private repositories)
    - `read:org` (read org data)
4. Copy token and paste into config above

### 2.4 Restart Claude Desktop

Close and reopen Claude Desktop app. MCP connection should be active.

### 2.5 Verify Connection

Open new chat in Claude Desktop:

```text
Can you list the contents of my dev-curriculum repository?
```

Expected: Claude reads repo structure via MCP and lists files.

---

## Phase 3: Core Schemas

Create these schema files under `schemas/`. All schemas enforce strict structure for machine-readable files.

### 3.1 `schemas/curriculum.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["curriculum_name", "audience", "global_objectives", "phases", "metadata"],
  "properties": {
    "curriculum_name": {"type": "string"},
    "audience": {"type": "string"},
    "global_objectives": {
      "type": "array",
      "items": {"type": "string"}
    },
    "prerequisites": {
      "type": "array",
      "items": {"type": "string"}
    },
    "phases": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["phase_id", "phase_name"],
        "properties": {
          "phase_id": {"type": "string", "pattern": "^P[0-9]+$"},
          "phase_name": {"type": "string"}
        }
      }
    },
    "pedagogy_principles": {
      "type": "array",
      "items": {"type": "string"}
    },
    "metadata": {
      "type": "object",
      "required": ["version", "created_at", "updated_at"],
      "properties": {
        "version": {"type": "string"},
        "created_at": {"type": "string", "format": "date"},
        "updated_at": {"type": "string", "format": "date"}
      }
    }
  }
}
```

### 3.2 `schemas/phase-index.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["phase_id", "phase_name", "lessons", "metadata"],
  "properties": {
    "phase_id": {"type": "string", "pattern": "^P[0-9]+$"},
    "phase_name": {"type": "string"},
    "description": {"type": "string"},
    "entry_criteria": {
      "type": "array",
      "items": {"type": "string"}
    },
    "exit_criteria": {
      "type": "array",
      "items": {"type": "string"}
    },
    "estimated_weeks": {"type": "integer", "minimum": 1},
    "lessons": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["lesson_id", "title", "estimated_minutes"],
        "properties": {
          "lesson_id": {"type": "string", "pattern": "^P[0-9]+-L[0-9]+$"},
          "title": {"type": "string"},
          "lesson_type": {"type": "string", "enum": ["conceptual", "hands-on", "project", "review"]},
          "estimated_minutes": {"type": "integer", "minimum": 15}
        }
      }
    },
    "metadata": {
      "type": "object",
      "required": ["created_at", "updated_at"],
      "properties": {
        "created_at": {"type": "string", "format": "date"},
        "updated_at": {"type": "string", "format": "date"}
      }
    }
  }
}
```

### 3.3 `schemas/lesson.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["lesson_id", "title", "phase_id", "lesson_type", "learning_objectives", "outline", "assessment"],
  "properties": {
    "lesson_id": {"type": "string", "pattern": "^P[0-9]+-L[0-9]+$"},
    "title": {"type": "string"},
    "phase_id": {"type": "string", "pattern": "^P[0-9]+$"},
    "estimated_minutes": {"type": "integer", "minimum": 15},
    "lesson_type": {"type": "string", "enum": ["conceptual", "hands-on", "project", "review"]},
    "prerequisites": {
      "type": "array",
      "items": {"type": "string", "pattern": "^P[0-9]+-L[0-9]+$"}
    },
    "learning_objectives": {
      "type": "array",
      "items": {"type": "string"},
      "minItems": 1
    },
    "outline": {
      "type": "array",
      "items": {"type": "string"},
      "minItems": 1
    },
    "key_terms": {
      "type": "array",
      "items": {"type": "string"}
    },
    "assessment": {
      "type": "object",
      "required": ["type", "criteria"],
      "properties": {
        "type": {"type": "string"},
        "criteria": {
          "type": "array",
          "items": {"type": "string"}
        }
      }
    },
    "resources": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["type", "title", "url"],
        "properties": {
          "type": {"type": "string"},
          "title": {"type": "string"},
          "url": {"type": "string", "format": "uri"}
        }
      }
    },
    "project_usage": {
      "type": "object",
      "properties": {
        "project_id": {"type": "string"},
        "role": {"type": "string"},
        "focus_area": {"type": "string"}
      }
    },
    "professor_constraints": {
      "type": "array",
      "items": {"type": "string"}
    }
  }
}
```

### 3.4 `schemas/state-current.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["learner_id", "current_phase_id", "current_lesson_id", "last_updated"],
  "properties": {
    "learner_id": {"type": "string"},
    "current_phase_id": {"type": "string", "pattern": "^P[0-9]+$"},
    "current_lesson_id": {"type": "string", "pattern": "^P[0-9]+-L[0-9]+$"},
    "last_updated": {"type": "string", "format": "date-time"}
  }
}
```

### 3.5 `schemas/state-completed.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["lesson_id", "completed_at", "duration_minutes", "confidence_rating"],
  "properties": {
    "lesson_id": {"type": "string", "pattern": "^P[0-9]+-L[0-9]+$"},
    "completed_at": {"type": "string", "format": "date-time"},
    "duration_minutes": {"type": "integer", "minimum": 1},
    "confidence_rating": {"type": "integer", "minimum": 1, "maximum": 5},
    "objectives_met": {
      "type": "array",
      "items": {"type": "string"}
    },
    "struggles": {
      "type": "array",
      "items": {"type": "string"}
    },
    "misconceptions_noted": {
      "type": "array",
      "items": {"type": "string"}
    }
  }
}
```

### 3.6 `schemas/state-skills.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["skills", "last_updated"],
  "properties": {
    "skills": {
      "type": "object",
      "patternProperties": {
        "^[a-z_]+$": {
          "type": "object",
          "required": ["level", "last_practiced"],
          "properties": {
            "level": {"type": "string", "enum": ["novice", "emerging", "competent", "proficient", "expert"]},
            "last_practiced": {"type": "string", "format": "date"},
            "confidence": {"type": "integer", "minimum": 1, "maximum": 5}
          }
        }
      }
    },
    "last_updated": {"type": "string", "format": "date-time"}
  }
}
```

### 3.7 `schemas/state-metrics.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["total_time_minutes", "lessons_completed", "reflections_written", "last_updated"],
  "properties": {
    "total_time_minutes": {"type": "integer", "minimum": 0},
    "lessons_completed": {"type": "integer", "minimum": 0},
    "reflections_written": {"type": "integer", "minimum": 0},
    "average_confidence": {"type": "number", "minimum": 1, "maximum": 5},
    "consistency_score": {"type": "number", "minimum": 0, "maximum": 1},
    "last_updated": {"type": "string", "format": "date-time"}
  }
}
```

**Commit schemas:**

```bash
git add schemas/
git commit -m "feat(schemas): add JSON Schema definitions for curriculum and state"
git push
```

---

## Phase 4: Role System

### 4.1 Role Definition Pattern

Each role is defined in a Markdown file under `roles/`. Claude loads the role file to understand its responsibilities.

**Structure:**

```text
# Role: {Role Name}

## Purpose
One-sentence description of role responsibility.

## Responsibilities
- Bullet list of what this role does
- Clear boundaries of what it does NOT do

## Input Files Required
- List of files this role reads from the repo

## Output Format
- What artifacts/files this role produces

## Constraints
- Rules this role must follow
- When to defer to other roles

## Example Session Flow
1. Step-by-step workflow
2. From role activation to deliverable
```

### 4.2 Create Role Files

#### `roles/architect.md`

```text
# Role: Architect

## Purpose
Design and maintain system structure, schemas, and file organization.

## Responsibilities
- Define and refine JSON schemas
- Design file structure and naming conventions
- Validate architectural consistency
- Propose structural improvements
- Document system design decisions

## Input Files Required
- `schemas/*.schema.json`
- `curriculum/curriculum.json`
- All phase index files
- `README.md`, `instructions.md`

## Output Format
- Schema files (JSON)
- Architecture decision records (Markdown)
- Updated documentation
- Proposed commit messages

## Constraints
- Never create lesson content (defer to Curriculum Designer or Professor)
- Never make progress decisions (defer to Advisor)
- All schema changes must be backward-compatible or include migration plan
- Always validate proposed changes against existing files

## Example Session Flow
1. User requests schema validation
2. Architect loads all schemas and data files via GitHub MCP
3. Identifies inconsistencies or violations
4. Proposes specific fixes as artifacts
5. Generates commit message for user to execute
6. Updates documentation if structure changed
```

#### `roles/curriculum-designer.md`

```text
# Role: Curriculum Designer

## Purpose
Create lesson sequences, phase structures, and learning scaffolding.

## Responsibilities
- Generate phase index files with lesson lists
- Create individual lesson JSON files matching schema
- Ensure prerequisite chains are valid
- Design project integration across lessons
- Maintain pedagogical coherence

## Input Files Required
- `curriculum/curriculum.json`
- `schemas/phase-index.schema.json`
- `schemas/lesson.schema.json`
- `learner-state/skills.json` (for scaffolding decisions)

## Output Format
- Phase index files (JSON)
- Lesson definition files (JSON)
- Project definition files (JSON)
- Proposed commit messages

## Constraints
- Never deliver actual teaching content (defer to Professor)
- Never assess learner progress (defer to Advisor)
- All lessons must validate against lesson schema
- Prerequisites must reference only existing lessons
- Estimated times must be realistic (15-90 minutes per lesson)

## Example Session Flow
1. User requests "Generate Phase 1 lessons"
2. Designer loads curriculum.json and P1-index.json
3. Generates 8-10 lesson files as artifacts
4. Each artifact is a complete, schema-valid JSON file
5. User copies artifacts to VS Code, saves under curriculum/lessons/
6. Designer proposes commit message
7. User commits and pushes
```

#### `roles/professor.md`

```text
# Role: Professor

## Purpose
Deliver individual lessons through structured, interactive teaching.

## Responsibilities
- Load lesson file and follow its structure
- Teach concepts step-by-step with checkpoints
- Generate lesson documents as artifacts
- Facilitate checkpoint discussions
- Produce end-of-lesson deliverables (summary, state update, reflection prompt)
- Adapt pacing based on learner state

## Input Files Required
- `curriculum/lessons/{lesson_id}.json`
- `learner-state/current.json`
- `learner-state/skills.json`
- `learner-state/completed/{prior_lesson_ids}.json` (if prerequisites exist)
- Project JSON if `project_usage` is defined

## Output Format
- Lesson document (Markdown artifact with content + checkpoint questions)
- Lesson summary (Markdown artifact following template)
- State update files (JSON artifacts for current.json, completed/{lesson_id}.json, skills.json, metrics.json)
- Reflection prompt (conversational)
- Proposed commit message

## Constraints
- Must follow `learning_objectives` exactly
- Must respect `professor_constraints` from lesson file
- Must include checkpoint questions every 10-15 minutes of content
- Never skip assessment criteria
- Never modify curriculum structure (defer to Designer)
- Never make next-lesson decisions (defer to Advisor)

## Example Session Flow
1. User requests "Teach P1-L01"
2. Professor loads lesson file via GitHub MCP
3. Generates complete lesson document as artifact
4. Document includes: introduction, concepts, examples, checkpoint questions
5. User reads artifact, responds to checkpoint questions in chat
6. Professor adapts explanations based on responses
7. After final checkpoint, Professor generates:
   - Lesson summary artifact (based on template)
   - State update artifacts (4 JSON files)
   - Reflection prompt as conversational text
8. User copies artifacts to VS Code, saves files
9. Professor proposes commit message
10. User commits and pushes
```

#### `roles/advisor.md`

```text
# Role: Advisor

## Purpose
Recommend next learning activities based on progress, skills, and goals.

## Responsibilities
- Analyze learner state (current position, completed lessons, skills, metrics)
- Recommend next lesson or review activity
- Flag skills needing reinforcement
- Propose weekly learning plans
- Identify prerequisite gaps

## Input Files Required
- `curriculum/curriculum.json`
- All phase index files
- `learner-state/current.json`
- `learner-state/completed/*.json`
- `learner-state/skills.json`
- `learner-state/metrics.json`

## Output Format
- Recommendation document (Markdown artifact)
- Optional: updated skills.json if assessment reveals new insights
- Proposed commit message (if skills updated)

## Constraints
- Never teach lesson content (defer to Professor)
- Never create lessons (defer to Curriculum Designer)
- Recommendations must respect prerequisite chains
- Must justify recommendations with evidence from state files
- Cannot make decisions for user — only recommend

## Example Session Flow
1. User requests "What should I do next?"
2. Advisor loads all learner-state files via GitHub MCP
3. Analyzes completed lessons, skills, and metrics
4. Generates recommendation artifact with:
   - Suggested next lesson with justification
   - Skills to review (if any)
   - Weekly plan (if requested)
5. User reviews recommendation
6. If user agrees, activates Professor for suggested lesson
```

#### `roles/evaluator.md`

```text
# Role: Evaluator

## Purpose
Assess lesson quality, learning outcomes, and system effectiveness.

## Responsibilities
- Validate that completed lessons met stated objectives
- Review lesson summaries for gaps or misconceptions
- Assess skill progression over time
- Identify curriculum weaknesses
- Propose lesson improvements

## Input Files Required
- Lesson file being evaluated
- Corresponding completed state file
- Lesson summary file
- Reflection file (if exists)

## Output Format
- Evaluation report (Markdown artifact)
- Optional: proposed lesson updates (JSON artifact)
- Optional: proposed skill adjustments (JSON artifact)

## Constraints
- Never make curriculum changes directly (propose to Designer)
- Never teach (defer to Professor)
- Never decide next steps (defer to Advisor)
- All assessments must reference specific evidence from files

## Example Session Flow
1. User requests "Evaluate P1-L01"
2. Evaluator loads lesson file, completed state, summary, reflection
3. Generates evaluation report as artifact:
   - Were objectives met? (evidence from summary)
   - Were misconceptions addressed? (evidence from reflection)
   - Is skill level update justified? (evidence from checkpoint responses)
   - Recommendations for lesson improvement
4. User reviews evaluation
5. If lesson needs updates, user activates Designer to modify lesson file
```

**Commit role files:**

```bash
git add roles/
git commit -m "feat(roles): add role definition files"
git push
```

---

## Phase 5: Bootstrap Ritual

### 5.1 Bootstrap Command

Every Claude Desktop session starts with a bootstrap to load context.

**User types:**

```text
/bootstrap
```

**Claude's expected behavior:**

1. Detect that user is in dev-curriculum repository (via GitHub MCP)
2. Read `user-profile.md`
3. Read `learner-state/current.json`
4. Display:

```text
=== Dev Curriculum System Bootstrap ===

Repository: dev-curriculum
Learner: Jeff
Current Position: P1-L03 (Foundations – Web & Programming Basics)
Last Updated: 2025-11-29

Available Commands:
/teach {lesson_id}  — Start a lesson with Professor
/next               — Get Advisor recommendation
/status             — View progress dashboard
/validate           — Run schema validation
/help               — Show all commands

Select a role or command to continue.
```

### 5.2 Role Activation

**User types:**

```text
/role professor
```

or

```text
/teach P1-L01
```

**Claude's expected behavior:**

1. Load `roles/professor.md`
2. Load required files per role definition
3. Confirm activation:

```text
Role: Professor activated.

Ready to teach lesson P1-L01: What Programming Is & How the Web Works

Type /begin to start the lesson, or ask questions first.
```

---

## Phase 6: Quick Start Path

### 6.1 Create `quickstart.md`

This is the beginner-friendly entry point. Hides complexity until needed.

````text
# Dev Curriculum — Quick Start

**Goal:** Complete your first lesson in 30 minutes.

## Step 1: Bootstrap the System

Open Claude Desktop and type:

```
/bootstrap
```

Claude will load your curriculum and show your current position.

## Step 2: Start Your First Lesson

Type:

```
/teach P1-L01
```

Claude will activate Professor mode and load the lesson.

## Step 3: Read the Lesson Document

Claude will generate a lesson document as an artifact. This contains:
- Concepts to learn
- Examples
- Checkpoint questions

Read through it at your own pace.

## Step 4: Answer Checkpoint Questions

When you reach a checkpoint, answer the question in the chat.

Example checkpoint:
> **Checkpoint 1:** In your own words, what is a program?

Type your answer. Claude will adapt the next section based on your response.

## Step 5: Complete the Lesson

After the final checkpoint, Claude will generate:
1. Lesson summary (copy to `lesson-summaries/P1-L01-summary.md`)
2. State updates (copy JSON artifacts to `learner-state/` files)
3. Reflection prompt (answer conversationally)

## Step 6: Save and Commit

In VS Code:
1. Copy artifacts to appropriate files
2. Save all changes
3. Commit with message Claude provides

```bash
git add .
git commit -m "feat(lesson): complete P1-L01"
git push
```

## Step 7: What's Next?

Type:

```
/next
```

Claude will activate Advisor and recommend your next lesson.

---

**That's it!** Repeat this loop for every lesson.

For advanced features, see `instructions.md`.
````

### 6.2 Create `instructions.md` (Comprehensive Reference)

````text
# Dev Curriculum — Complete Instructions

## Overview

This is a file-backed, Claude-assisted learning system. All state lives in Git, not AI memory.

## Architecture

See `ARCHITECTURE.md` for full system design.

## Roles

- **Architect:** System design and schema management (`roles/architect.md`)
- **Curriculum Designer:** Lesson creation and sequencing (`roles/curriculum-designer.md`)
- **Professor:** Lesson delivery and teaching (`roles/professor.md`)
- **Advisor:** Progress tracking and recommendations (`roles/advisor.md`)
- **Evaluator:** Assessment and quality assurance (`roles/evaluator.md`)

## Commands

### Core Commands
- `/bootstrap` — Initialize session
- `/teach {lesson_id}` — Start lesson with Professor
- `/next` — Get Advisor recommendation
- `/status` — View progress dashboard
- `/validate` — Run schema validation

### Role Commands
- `/role {role_name}` — Activate specific role
- `/help {role_name}` — Show role documentation

### Maintenance Commands
- `/snapshot` — Create state backup for rollback
- `/rollback {snapshot_name}` — Restore previous state
- `/repair` — Fix file inconsistencies

## File Structure

```
curriculum/        — Curriculum design and lessons
learner-state/     — Progress tracking (decomposed)
roles/             — Role definition files
schemas/           — JSON Schema validation
templates/         — Output templates
snapshots/         — State backups
lesson-summaries/  — Completed lesson records
reflections/       — Learning journal
```

## Workflow

1. Open Claude Desktop
2. Run `/bootstrap`
3. Select role or command
4. Claude generates artifacts
5. Copy artifacts to VS Code
6. Save files
7. Commit with Claude's proposed message
8. Push to GitHub

## Validation

### Pre-commit validation
Claude validates all JSON artifacts before output.

### CI validation
GitHub Actions runs schema validation on every push.

## Recovery

### Create snapshot
```
/snapshot pre-lesson-P1-L03
```

### Rollback to snapshot
```
/rollback pre-lesson-P1-L03
```

### Redo lesson
```
/redo P1-L02
```

This removes the lesson from completed state and resets skills to pre-lesson values.

## Success Metrics

Tracked in `learner-state/metrics.json`:
- Total time investment
- Lessons completed
- Confidence ratings over time
- Reflection consistency
- Skill progression

## Troubleshooting

**Problem:** Claude can't access repository
- **Solution:** Check GitHub MCP configuration in `~/Library/Application Support/Claude/claude_desktop_config.json`

**Problem:** Schema validation fails
- **Solution:** Run `/validate` to see specific errors, then fix files manually

**Problem:** State files out of sync
- **Solution:** Run `/repair` to diagnose and fix

**Problem:** Lost progress after crash
- **Solution:** Run `/rollback {latest_snapshot}` to restore

## Advanced Topics

### Custom Roles
Create new role files under `roles/` following the standard pattern.

### Custom Metrics
Add fields to `state-metrics.schema.json` and update metrics.json manually.

### Multi-track Curriculum
Add additional phases to `curriculum.json` and generate separate lesson sequences.

---

For quick start, see `quickstart.md`.
````

**Commit documentation:**

```bash
git add quickstart.md instructions.md
git commit -m "docs: add quickstart and comprehensive instructions"
git push
```

---

## Phase 7: Learner State Architecture

### 7.1 Decomposed State Model

**Philosophy:** Atomic state files enable clean Git history and focused updates.

### 7.2 Create Initial State Files

#### `learner-state/current.json`

```json
{
  "learner_id": "jeff",
  "current_phase_id": "P1",
  "current_lesson_id": "P1-L01",
  "last_updated": "2025-11-29T00:00:00Z"
}
```

#### `learner-state/skills.json`

```json
{
  "skills": {
    "git_basics": {
      "level": "novice",
      "last_practiced": "2025-11-29",
      "confidence": 2
    },
    "js_basics": {
      "level": "novice",
      "last_practiced": "2025-11-29",
      "confidence": 2
    },
    "terminal_comfort": {
      "level": "novice",
      "last_practiced": "2025-11-29",
      "confidence": 2
    },
    "html_css": {
      "level": "novice",
      "last_practiced": "2025-11-29",
      "confidence": 2
    }
  },
  "last_updated": "2025-11-29T00:00:00Z"
}
```

#### `learner-state/metrics.json`

```json
{
  "total_time_minutes": 0,
  "lessons_completed": 0,
  "reflections_written": 0,
  "average_confidence": 0,
  "consistency_score": 0,
  "last_updated": "2025-11-29T00:00:00Z"
}
```

#### `learner-state/completed/.gitkeep`

Empty directory placeholder for completed lesson records.

**Commit initial state:**

```bash
git add learner-state/
git commit -m "feat(state): initialize learner state files"
git push
```

### 7.3 State Update Pattern

After each lesson, Professor generates 4 artifacts:

1. **current.json update** — new current_lesson_id
2. **completed/{lesson_id}.json** — completion record
3. **skills.json update** — skill level changes
4. **metrics.json update** — time, confidence, count increments

User copies these artifacts to appropriate files and commits atomically:

```bash
git add learner-state/
git commit -m "feat(progress): complete P1-L01"
git push
```

---

## Phase 8: Lesson Delivery Model

### 8.1 Lesson Format: Document + Guided Checkpoints

**Structure:**

````text
# Lesson: {Title}

**Phase:** {phase_id}  
**Estimated Time:** {minutes} minutes  
**Prerequisites:** {list or "None"}

---

## Learning Objectives

By the end of this lesson, you will be able to:
1. {objective 1}
2. {objective 2}
3. {objective 3}

---

## Introduction

{2-3 paragraphs setting context and motivation}

---

## Section 1: {Topic}

{Explanation with examples}

### Example

```javascript
// Code example if applicable
```

---

**CHECKPOINT 1:** {Question to verify understanding}

{Pause here and answer in chat before continuing}

---

## Section 2: {Topic}

{Explanation with examples}

---

**CHECKPOINT 2:** {Question to verify understanding}

{Pause here and answer in chat before continuing}

---

## Section 3: {Topic}

{Explanation with examples}

---

**CHECKPOINT 3:** {Question to verify understanding}

{Pause here and answer in chat before continuing}

---

## Summary

{Recap of key concepts}

---

## Assessment

{Based on lesson.assessment from JSON}

**Criteria:**
1. {criterion 1}
2. {criterion 2}

{Self-assessment or Professor-led verification}

---

## Key Terms

- **{term}:** {definition}
- **{term}:** {definition}

---

## Resources

- [{title}]({url})

---

**End of Lesson Document**
````

### 8.2 Professor Workflow

1. User: `/teach P1-L01`
2. Professor loads `curriculum/lessons/P1-L01.json` via GitHub MCP
3. Professor generates lesson document as artifact (following structure above)
4. User reads document, answers checkpoint questions in chat
5. Professor adapts explanations based on answers
6. After final checkpoint, Professor generates:
    - Lesson summary artifact
    - 4 state update artifacts (JSON)
    - Reflection prompt (conversational)
7. User copies artifacts to VS Code, saves
8. Professor proposes commit message
9. User commits and pushes

### 8.3 Lesson Summary Template

Located at `templates/lesson-summary.template.md`:

```text
---
lesson_id: {{lesson_id}}
completed_at: {{iso_timestamp}}
duration_minutes: {{duration}}
confidence_rating: {{1-5}}
---

# Lesson Summary — {{lesson_id}}

## Title
{{lesson_title}}

## Objectives Met
- [ ] {{objective_1}}
- [ ] {{objective_2}}
- [ ] {{objective_3}}

## Key Wins
- {{win_1}}
- {{win_2}}

## Struggles
- {{struggle_1}}
- {{struggle_2}}

## Misconceptions Corrected
- {{misconception_1}}

## Skills Practiced
- {{skill_1}}: {{novice|emerging|competent|proficient|expert}}
- {{skill_2}}: {{novice|emerging|competent|proficient|expert}}

## Next Steps
- {{next_step}}

---

**Confidence Rating:** {{1-5}}/5  
**Would Recommend Reviewing:** {{yes|no}}
```

**Professor uses this template** when generating summary artifact.

### 8.4 Reflection Template

Located at `templates/reflection.template.md`:

```text
---
date: {{YYYY-MM-DD}}
lesson_id: {{lesson_id}}
energy_level: {{1-10}}
---

# Reflection — {{date}}

## Lesson
{{lesson_title}}

## How It Felt
{{2-4 sentences in learner's voice about the experience}}

## What Clicked
{{What concepts made sense}}

## What's Still Fuzzy
{{What needs more practice or clarification}}

## Mood After Lesson
{{energized|neutral|tired|frustrated|excited}}

---

**Energy Level:** {{1-10}}/10
```

**This template is loose** — learner writes freeform within structure.

**Commit templates:**

```bash
git add templates/
git commit -m "feat(templates): add lesson summary and reflection templates"
git push
```

---

## Phase 9: Command Registry

### 9.1 Minimal Command Set (Start)

|Command|Purpose|Role Required|
|---|---|---|
|`/bootstrap`|Initialize session|None|
|`/teach {lesson_id}`|Start lesson|Professor|
|`/next`|Get recommendation|Advisor|
|`/status`|View dashboard|None|
|`/validate`|Check schemas|Architect|

### 9.2 Command Behavior Definitions

#### `/bootstrap`

**Input:** None  
**Output:** Session initialization message + current position + command list  
**Files Read:** `user-profile.md`, `learner-state/current.json`

#### `/teach {lesson_id}`

**Input:** Lesson ID (e.g., `P1-L01`)  
**Output:** Activates Professor, loads lesson, generates lesson document artifact  
**Files Read:** `curriculum/lessons/{lesson_id}.json`, all learner-state files, `roles/professor.md`

#### `/next`

**Input:** None  
**Output:** Activates Advisor, generates recommendation artifact  
**Files Read:** `curriculum/curriculum.json`, all phase indices, all learner-state files, `roles/advisor.md`

#### `/status`

**Input:** None  
**Output:** Progress dashboard (formatted text)  
**Files Read:** All learner-state files, curriculum files

**Example output:**

```text
=== Progress Dashboard ===

Current Phase: P1 — Foundations (Lesson 3 of 10)
Last Completed: P1-L02 (2025-11-28)
Current Target: P1-L03

Total Time Invested: 180 minutes
Lessons Completed: 2
Average Confidence: 3.5/5
Reflections Written: 2

Skill Levels:
- git_basics:         ★★☆☆☆ (emerging)
- js_basics:          ★★☆☆☆ (emerging)
- terminal_comfort:   ★☆☆☆☆ (novice)
- html_css:           ★★★☆☆ (competent)

Next Recommended: P1-L03 — Setting Up Development Environment

=== End Dashboard ===
```

#### `/validate`

**Input:** None (or optional: specific file path)  
**Output:** Validation report  
**Files Read:** All JSON files in repo, all schema files, `roles/architect.md`

**Example output:**

```text
=== Schema Validation Report ===

✓ curriculum/curriculum.json — VALID
✓ curriculum/phases/P1-index.json — VALID
✓ curriculum/lessons/P1-L01.json — VALID
✗ learner-state/skills.json — INVALID
  - Line 5: Property "last_practiced" is required but missing for "html_css"

Recommendation: Fix learner-state/skills.json by adding missing field.

=== End Validation ===
```

### 9.3 Adding Commands When Friction Emerges

**Process:**

1. User identifies repetitive manual action
2. User requests command via Architect role
3. Architect proposes command definition
4. Command added to registry
5. All roles updated to recognize new command

**Example:** If user frequently needs to review completed lessons, add:

```text
/review {lesson_id}
```

This would load the completed state file and summary for review without re-teaching.

---

## Phase 10: Validation Pipeline

### 10.1 Pre-commit Validation (Claude)

**When:** Before generating any JSON artifact  
**How:** Claude validates against schema internally  
**Outcome:** Only valid JSON artifacts are produced

**Example:** User requests lesson generation. Before outputting artifact, Claude:

1. Loads `schemas/lesson.schema.json`
2. Validates generated lesson object
3. If invalid, fixes and re-validates
4. Only then outputs artifact

### 10.2 Post-commit Validation (GitHub Actions CI)

**When:** On every push to main branch  
**How:** GitHub Actions runs `tools/validate.py`  
**Outcome:** CI fails if any file violates schema

#### Create `.github/workflows/validate.yml`

```yaml
name: Schema Validation

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install jsonschema
      
      - name: Run validation
        run: |
          python tools/validate.py
```

#### Create `tools/validate.py`

```python
#!/usr/bin/env python3
"""
Schema validation script for dev-curriculum system.
Validates all JSON files against their corresponding schemas.
"""

import json
import sys
from pathlib import Path
from jsonschema import validate, ValidationError

def load_json(filepath):
    """Load JSON file and return parsed object."""
    with open(filepath, 'r') as f:
        return json.load(f)

def validate_file(data_file, schema_file):
    """Validate a data file against a schema."""
    try:
        data = load_json(data_file)
        schema = load_json(schema_file)
        validate(instance=data, schema=schema)
        return True, None
    except ValidationError as e:
        return False, str(e)
    except Exception as e:
        return False, f"Error loading files: {str(e)}"

def main():
    """Run validation on all curriculum and state files."""
    repo_root = Path(__file__).parent.parent
    
    validations = [
        (repo_root / "curriculum/curriculum.json", repo_root / "schemas/curriculum.schema.json"),
        (repo_root / "learner-state/current.json", repo_root / "schemas/state-current.schema.json"),
        (repo_root / "learner-state/skills.json", repo_root / "schemas/state-skills.schema.json"),
        (repo_root / "learner-state/metrics.json", repo_root / "schemas/state-metrics.schema.json"),
    ]
    
    # Validate phase indices
    phase_dir = repo_root / "curriculum/phases"
    if phase_dir.exists():
        for phase_file in phase_dir.glob("P*-index.json"):
            validations.append((phase_file, repo_root / "schemas/phase-index.schema.json"))
    
    # Validate lessons
    lesson_dir = repo_root / "curriculum/lessons"
    if lesson_dir.exists():
        for lesson_file in lesson_dir.glob("P*-L*.json"):
            validations.append((lesson_file, repo_root / "schemas/lesson.schema.json"))
    
    # Validate completed state files
    completed_dir = repo_root / "learner-state/completed"
    if completed_dir.exists():
        for completed_file in completed_dir.glob("P*-L*.json"):
            validations.append((completed_file, repo_root / "schemas/state-completed.schema.json"))
    
    errors = []
    for data_file, schema_file in validations:
        if not data_file.exists():
            continue  # Skip missing files
        
        valid, error_msg = validate_file(data_file, schema_file)
        if valid:
            print(f"✓ {data_file.relative_to(repo_root)} — VALID")
        else:
            print(f"✗ {data_file.relative_to(repo_root)} — INVALID")
            print(f"  {error_msg}")
            errors.append(data_file)
    
    if errors:
        print(f"\n{len(errors)} file(s) failed validation.")
        sys.exit(1)
    else:
        print("\nAll files valid.")
        sys.exit(0)

if __name__ == "__main__":
    main()
```

**Make script executable:**

```bash
chmod +x tools/validate.py
```

**Commit validation tooling:**

```bash
git add .github/workflows/validate.yml tools/validate.py
git commit -m "feat(validation): add CI validation pipeline"
git push
```

### 10.3 Local Validation Command

User can run validation locally anytime:

```bash
python tools/validate.py
```

Or via Claude:

```text
/validate
```

Claude activates Architect role and runs validation via the script (if Claude can execute Python locally via MCP extensions — otherwise, Claude reads files and validates manually).

---

## Phase 11: Recovery & Rollback System

### 11.1 State Snapshots

**Purpose:** Create point-in-time backups before risky operations (e.g., starting new lessons, major skill updates).

#### Create Snapshot Command

User types:

```text
/snapshot pre-lesson-P1-L03
```

**Claude's behavior:**

1. Activates Architect role
2. Creates ZIP archive of entire `learner-state/` directory
3. Saves to `snapshots/2025-11-29-pre-lesson-P1-L03.zip`
4. Generates artifact with confirmation message
5. Proposes commit message:

```bash
git add snapshots/
git commit -m "chore(snapshot): create pre-lesson-P1-L03 backup"
git push
```

#### Rollback Command

User types:

```text
/rollback pre-lesson-P1-L03
```

**Claude's behavior:**

1. Activates Architect role
2. Locates snapshot file in `snapshots/`
3. Extracts snapshot contents
4. Generates artifacts for each restored state file
5. User copies artifacts to `learner-state/`
6. Proposes commit message:

```bash
git add learner-state/
git commit -m "chore(rollback): restore state to pre-lesson-P1-L03"
git push
```

### 11.2 Redo Lesson

**Purpose:** Re-attempt a lesson without prior completion contaminating state.

User types:

```text
/redo P1-L02
```

**Claude's behavior:**

1. Activates Advisor role
2. Loads `learner-state/completed/P1-L02.json`
3. Generates new state artifacts with:
    - `current.json`: sets `current_lesson_id` to `P1-L02`
    - Removes `P1-L02.json` from `completed/`
    - Reverts skill levels to pre-lesson values (if recorded)
    - Decrements metrics (lessons_completed, total_time, etc.)
4. User copies artifacts and commits
5. User can now run `/teach P1-L02` fresh

### 11.3 Manual State Editing

**When:** User needs to fix incorrect state manually.

**Process:**

1. User opens state file in VS Code
2. Edits JSON directly
3. Runs `/validate` to ensure schema compliance
4. Commits change with descriptive message:

```bash
git add learner-state/skills.json
git commit -m "fix(state): correct terminal_comfort level to emerging"
git push
```

### 11.4 Repair Command

**Purpose:** Diagnose and fix file inconsistencies.

User types:

```text
/repair
```

**Claude's behavior:**

1. Activates Architect role
2. Runs validation on all files
3. Identifies issues:
    - Schema violations
    - Missing required files
    - Orphaned references (e.g., lesson references non-existent prerequisite)
4. Generates repair plan artifact with specific edits
5. User applies edits manually
6. User re-runs `/validate` to confirm

**Example repair plan:**

```text
=== Repair Plan ===

Issue 1: learner-state/skills.json missing "last_practiced" for "html_css"
Fix: Add field "last_practiced": "2025-11-29" to html_css object

Issue 2: curriculum/lessons/P1-L03.json references prerequisite "P1-L02" but P1-L02.json does not exist
Fix: Either create P1-L02.json or remove from P1-L03 prerequisites array

Recommendation: Fix Issue 1 immediately (required for schema). Evaluate Issue 2 based on curriculum design intent.

=== End Repair Plan ===
```

---

## Phase 12: Success Metrics

### 12.1 Metrics Tracked in `learner-state/metrics.json`

1. **Total Time Investment** (`total_time_minutes`)

    - Cumulative time across all lessons
    - Updated after each lesson completion

2. **Lessons Completed** (`lessons_completed`)

    - Count of files in `learner-state/completed/`

3. **Average Confidence** (`average_confidence`)

    - Mean of all `confidence_rating` values from completed lessons
    - Range: 1.0-5.0

4. **Consistency Score** (`consistency_score`)

    - Percentage of weeks with at least 2 lessons completed
    - Range: 0.0-1.0
    - Calculated weekly

5. **Reflections Written** (`reflections_written`)

    - Count of files in `reflections/`

### 12.2 Metrics Dashboard

User types:

```text
/status
```

Claude displays metrics as part of dashboard (shown in Phase 9).

### 12.3 Metrics Update Pattern

After each lesson, Professor generates `metrics.json` artifact with updated values:

```json
{
  "total_time_minutes": 225,
  "lessons_completed": 3,
  "reflections_written": 3,
  "average_confidence": 3.67,
  "consistency_score": 0.85,
  "last_updated": "2025-11-29T14:30:00Z"
}
```

User copies artifact to `learner-state/metrics.json` and commits.

### 12.4 Long-term Analysis

**Future enhancement (v2.0):**

- Export metrics to CSV for visualization
- Generate progress charts (Notion, Obsidian, or HTML dashboard)
- Identify skill plateau patterns
- Recommend review cycles based on confidence trends

---

## Appendix A: File Index Structure

### A.1 Purpose

The file index is dynamically maintained by the system, not manually edited. It provides a centralized registry of all curriculum and state files for fast lookups.

### A.2 Auto-generated During Bootstrap

When user runs `/bootstrap`, Claude generates file index by scanning repo structure:

```json
{
  "curriculum": {
    "root": "curriculum/curriculum.json",
    "phases": [
      "curriculum/phases/P1-index.json",
      "curriculum/phases/P2-index.json"
    ],
    "lessons": [
      "curriculum/lessons/P1-L01.json",
      "curriculum/lessons/P1-L02.json",
      "curriculum/lessons/P1-L03.json"
    ]
  },
  "state": {
    "current": "learner-state/current.json",
    "skills": "learner-state/skills.json",
    "metrics": "learner-state/metrics.json",
    "completed": [
      "learner-state/completed/P1-L01.json",
      "learner-state/completed/P1-L02.json"
    ]
  },
  "roles": [
    "roles/architect.md",
    "roles/curriculum-designer.md",
    "roles/professor.md",
    "roles/advisor.md",
    "roles/evaluator.md"
  ],
  "schemas": [
    "schemas/curriculum.schema.json",
    "schemas/phase-index.schema.json",
    "schemas/lesson.schema.json",
    "schemas/state-current.schema.json",
    "schemas/state-completed.schema.json",
    "schemas/state-skills.schema.json",
    "schemas/state-metrics.schema.json"
  ],
  "last_updated": "2025-11-29T14:30:00Z"
}
```

This index is **not committed to repo** — it's regenerated every bootstrap.

---

## Appendix B: Roadmap

### v1.0 — Foundation (Current)

**Goal:** Core system operational with manual workflows

**Deliverables:**

- ✅ Repository structure
- ✅ GitHub MCP integration
- ✅ Schemas for all entities
- ✅ Role system with 5 roles
- ✅ Bootstrap ritual
- ✅ Quick start path
- ✅ Decomposed learner state
- ✅ Lesson delivery model (document + checkpoints)
- ✅ Minimal command set (5 commands)
- ✅ Pre-commit validation (Claude)
- ✅ CI validation (GitHub Actions)
- ✅ Recovery system (snapshots, rollback, redo)
- ✅ Success metrics tracking

**Status:** Ready for first lesson delivery

---

### v1.1 — Curriculum Build-out

**Goal:** Generate Phase 1 lessons and test full loop

**Deliverables:**

- Create `curriculum/curriculum.json` (complete)
- Generate `curriculum/phases/P1-index.json` with 10 lessons
- Generate all P1 lesson files (`P1-L01.json` through `P1-L10.json`)
- Define at least 1 reusable project (e.g., Git intro repo)
- Complete first 3 lessons end-to-end
- Document friction points and improvements

**Outcome:** Working curriculum with validated learner loop

---

### v1.2 — Profile & Template Refinement

**Goal:** Optimize user profile and output templates

**Deliverables:**

- Refine `user-profile.md` based on lesson experiences
- Update `lesson-summary.template.md` based on actual usage
- Update `reflection.template.md` for natural voice
- Add commit message templates for common operations
- Document template usage patterns

**Outcome:** Cleaner artifacts, less manual editing

---

### v2.0 — Automation Layer

**Goal:** Reduce manual file operations

**Deliverables:**

- CLI tool for common operations:

    ```bash
    devc teach P1-L01          # Launches Professor sessiondevc next                  # Launches Advisordevc commit                # Auto-commit with proper messagedevc snapshot {name}       # Create backupdevc rollback {name}       # Restore backup
    ```

- Auto-apply state updates (after user approval)
- Auto-commit with generated messages
- Batch validation runner
- Metrics export to CSV

**Outcome:** Faster workflow, fewer manual steps

---

### v2.1 — Dashboard & Visualization

**Goal:** Visual progress tracking

**Deliverables:**

- HTML dashboard generator (static site)
- Skill radar chart visualization
- Confidence trend line graph
- Weekly consistency heatmap
- Export to Notion integration (optional)
- Export to Obsidian graph (optional)

**Outcome:** Clear visual feedback on progress

---

### v3.0 — Web Application

**Goal:** Full UI-driven experience

**Deliverables:**

- Next.js frontend with pages:
  - Dashboard (progress, metrics, skill radar)
  - Lesson browser (curriculum view)
  - Lesson runner (read lesson, answer checkpoints)
  - Reflection journal
  - Settings (profile editing)
- FastAPI backend:
  - File CRUD operations
  - Git operations (commit, push)
  - Validation endpoints
  - Claude API integration for role activation
- Authentication (if multi-user)
- Deployment (Vercel + Railway or similar)

**Outcome:** Production-ready learning platform

---

## Appendix C: Migration from ChatGPT

### C.1 File Transfer

**One-time operation:**

1. Download all files from ChatGPT Project Files
2. Organize into Claude-native structure (Phase 1)
3. Commit to GitHub
4. Set up GitHub MCP (Phase 2)

### C.2 Profile Migration

**Current ChatGPT profiles:**

- `user_profile.short.md`
- `user_profile.medium.md`
- `user_profile.full.md`

**Claude-native approach:**

- Single `user-profile.md` (combines all context)
- Roles load only what they need internally

**Migration:**

1. Merge all three profiles into one
2. Add YAML frontmatter for metadata:

```yaml
---
learner_id: jeff
location: Vacaville, CA
experience_level: beginner-intermediate
learning_style: hands-on, SOP-driven
primary_goals:
  - transition to full-time engineering
  - ship CatchBook v1
  - build YouTube education platform
---

# User Profile — Jeff Hutting

## Background
...
```

### C.3 Role Prompt Migration

**ChatGPT approach:**

- Prompts in `prompts/` directory
- User copy/pastes to activate roles

**Claude-native approach:**

- Role definitions in `roles/` directory (Markdown files)
- Claude loads role file automatically via GitHub MCP
- No manual copy/paste needed

**Migration:**

1. Convert each prompt file to role definition file
2. Add structured sections (Purpose, Responsibilities, etc.)
3. Save under `roles/`

### C.4 Lesson File Migration

**No changes needed** — lesson JSON structure remains the same.

**Validation:**

1. Run `/validate` after migration
2. Fix any schema violations
3. Commit cleaned files

### C.5 Learner State Migration

**ChatGPT approach:**

- Single `learner_state.json`

**Claude-native approach:**

- Decomposed: `current.json`, `skills.json`, `metrics.json`, `completed/*.json`

**Migration script (manual):**

```python
import json
from pathlib import Path
from datetime import datetime

# Load old state
with open('learner_state.json') as f:
    old_state = json.load(f)

# Create current.json
current = {
    "learner_id": old_state["learner_id"],
    "current_phase_id": old_state["current_phase_id"],
    "current_lesson_id": old_state["current_lesson_id"],
    "last_updated": datetime.utcnow().isoformat() + "Z"
}

# Create skills.json
skills = {
    "skills": {},
    "last_updated": datetime.utcnow().isoformat() + "Z"
}
for skill, level in old_state.get("skill_flags", {}).items():
    skills["skills"][skill] = {
        "level": level,
        "last_practiced": datetime.utcnow().date().isoformat(),
        "confidence": 2  # Default, update manually if needed
    }

# Create metrics.json
metrics = {
    "total_time_minutes": 0,  # Calculate from completed lessons if data exists
    "lessons_completed": len(old_state.get("completed_lessons", [])),
    "reflections_written": 0,  # Count reflection files
    "average_confidence": 0,  # Calculate from completed lessons
    "consistency_score": 0,  # Will build over time
    "last_updated": datetime.utcnow().isoformat() + "Z"
}

# Create completed lesson files (if old state has completion data)
completed_dir = Path("learner-state/completed")
completed_dir.mkdir(exist_ok=True)

for lesson in old_state.get("completed_lessons", []):
    lesson_id = lesson if isinstance(lesson, str) else lesson.get("lesson_id")
    completed_record = {
        "lesson_id": lesson_id,
        "completed_at": datetime.utcnow().isoformat() + "Z",  # Placeholder
        "duration_minutes": 45,  # Estimate
        "confidence_rating": 3,  # Placeholder
        "objectives_met": [],
        "struggles": [],
        "misconceptions_noted": []
    }
    
    with open(completed_dir / f"{lesson_id}.json", 'w') as f:
        json.dump(completed_record, f, indent=2)

# Save new files
with open('learner-state/current.json', 'w') as f:
    json.dump(current, f, indent=2)

with open('learner-state/skills.json', 'w') as f:
    json.dump(skills, f, indent=2)

with open('learner-state/metrics.json', 'w') as f:
    json.dump(metrics, f, indent=2)

print("Migration complete. Review files and commit.")
```

Run script, then:

```bash
git add learner-state/
git commit -m "feat(migration): decompose learner state from ChatGPT format"
git push
```

---

## Final Notes

This architecture is designed to:

- Eliminate file sync overhead (GitHub MCP replaces ChatGPT Projects)
- Provide clean, artifact-based outputs (no markdown rendering issues)
- Scale from v1.0 (manual) → v3.0 (full web app) without rework
- Maintain Git-native discipline throughout

**Next action:** Follow Phase 1-5 to set up repository and bootstrap system.

---

## End of ARCHITECTURE.md — Claude-Native Edition v1.0
