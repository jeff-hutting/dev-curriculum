# ARCHITECTURE.md — CatchBook Curriculum Edition v2.0

> **Status:** Active Development (v2.0)  
> **Platform:** Claude Desktop + GitHub MCP + Filesystem MCP + VS Code  
> **Philosophy:** File-backed state, artifact-first delivery, Git-native workflow  
> **Project Spine:** CatchBook AI Fishing Journal (28 phases, 139 modules, ~850 hours)

---

## Table of Contents

- [Phase 0: Mental Model](#phase-0-mental-model)
- [Phase 1: Repository Structure](#phase-1-repository-structure)
- [Phase 2: MCP Setup](#phase-2-mcp-setup)
- [Phase 3: Core Schemas](#phase-3-core-schemas)
- [Phase 4: Role System](#phase-4-role-system)
- [Phase 5: Bootstrap Ritual](#phase-5-bootstrap-ritual)
- [Phase 6: Quick Start Path](#phase-6-quick-start-path)
- [Phase 7: Learner State Architecture](#phase-7-learner-state-architecture)
- [Phase 8: Lesson Delivery Model](#phase-8-lesson-delivery-model)
- [Phase 9: Command Registry](#phase-9-command-registry)
- [Phase 10: Validation Pipeline](#phase-10-validation-pipeline)
- [Phase 11: Recovery & Rollback System](#phase-11-recovery--rollback-system)
- [Phase 12: Success Metrics](#phase-12-success-metrics)
- [Appendix A: CatchBook Curriculum Overview](#appendix-a-catchbook-curriculum-overview)
- [Appendix B: File Naming Conventions](#appendix-b-file-naming-conventions)
- [Appendix C: Curriculum Generation Strategy](#appendix-c-curriculum-generation-strategy)
- [Appendix D: Roadmap](#appendix-d-roadmap)

---

## Phase 0: Mental Model

### What This System Is

A **local-first, Git-managed, GitHub-backed, AI-assisted full-stack engineering curriculum** built around a real production project: **CatchBook**, an AI-powered fishing diary app. The curriculum spans 28 phases, 139 modules, and approximately 850 hours of hands-on learning.

**Core Innovation:** Every module produces a real, shippable feature for Catchbook. No throwaway exercises—only production code that compounds into a complete application.

### Core Principles

1. **File-backed state** — Locally developed, GitHub-hosted
2. **Artifact-first delivery** — All structured content uses Claude's artifact system
3. **Explicit role contracts** — Roles defined in versioned files
4. **Git-native workflow** — Every session produces a commit to build portfolio
5. **Just-in-time curriculum** — Generate lessons as needed, not all upfront
6. **Real project spine** — CatchBook drives every learning module
7. **Progressive disclosure** — Quick start path for beginners, comprehensive docs for depth

### CatchBook as Curriculum Spine

**Why CatchBook?**

- **Motivation:** Building a real product users will actually use
- **Compound learning:** Each phase builds on previous work
- **Portfolio coherence:** One deep project beats a dozen shallow demos
- **Market validation:** Test features and gather feedback as you build
- **Production stakes:** Forces best practices from day 1
- **Full-stack coverage:** Touches every layer from mobile UI to ML models

**What is CatchBook?**
CatchBook is an AI-powered fishing journal that automatically fills in catch details by combining photo capture, EXIF metadata, and on-device computer vision. Anything the model can’t infer can be added instantly through natural-language input—typed or spoken. The goal is simple: log a catch in 10–20 seconds, instead of the 3–5 minutes required by today’s apps.

**Tech Stack:**

- Frontend: React + TypeScript (web), React Native or SwiftUI (mobile)
- Backend: Python + FastAPI
- Database: PostgreSQL + PostGIS
- AI: Claude API for species ID and recommendations
- Mobile: PWA → React Native or SwiftUI

**Product Spec:** See `projects/catchbook-product-spec.md` for complete specification.

### Curriculum Structure

**Hierarchy:** Phases → Modules → Lessons

- **Phase:** Major learning section (e.g., "Foundations", "Backend Development")
  - 28 phases total (P01-P28)
  - Each phase contains 3-7 modules
  - File: `curriculum/phases/P01.phase.json`

- **Module:** Focused skill area within a phase (e.g., "Git fundamentals", "React basics")
  - 139 modules total across all phases
  - Each module contains 1-5 lessons
  - File: `curriculum/modules/P01/P01-M01.module.json`
  - Estimated time: 6-16 hours per module

- **Lesson:** Individual teaching unit with specific learning objectives
  - Generated just-in-time by Curriculum Designer
  - File: `curriculum/lessons/P01/M01/L01/P01-M01-L01.lesson.json`
  - Estimated time: 45-90 minutes per lesson

**Example Path:**

- Phase 1: Foundations → Module 1.1: Git fundamentals → Lesson 1: What is version control?
- File hierarchy: `P01.phase.json` → `P01/P01-M01.module.json` → `P01/M01/L01/P01-M01-L01.lesson.json`

### Key Entities

**Curriculum Components:**

- `Curriculum` — Top-level design (28-phase CatchBook roadmap)
- `Phase` — Major section (e.g., P01: Foundations)
- `Module` — Skill cluster (e.g., P01-M01: Git fundamentals)
- `Lesson` — Teaching unit (e.g., P01-M01-L01: Version control concepts)
- `Project` — CatchBook (primary), with supplementary projects as needed

**State Components:**

- `current.json` — Active position (current phase, module, lesson)
- `skills.json` — Skill tracking across curriculum
- `metrics.json` — Time invested, confidence ratings, completion stats
- `completed/` — Per-lesson completion records

**Roles:**

- `Architect` — System design, schema management, structure validation
- `Curriculum Designer` — Module and lesson generation (just-in-time)
- `Professor` — Lesson delivery, teaching, checkpoint facilitation
- `Advisor` — Progress tracking, next-step recommendations, pacing
- `Evaluator` — Assessment, rubric scoring, quality assurance

### Workflow Pattern

1. **Advisor recommends** next module/lesson based on progress
2. **Curriculum Designer generates** lesson files if not yet created
3. **Professor delivers** lesson with guided checkpoints
4. **User produces** CatchBook feature or code artifact
5. **User commits** work to Git with proper message
6. **System updates** learner state (skills, metrics, completed)
7. **Evaluator assesses** (optional) to validate mastery
8. **Repeat** until CatchBook v1.0 is complete

---

## Phase 1: Repository Structure

### 1.1 GitHub Repository

Repository name: `dev-curriculum`  
Branch: `master` (not `main`)  
Visibility: Private

### 1.2 Directory Structure

```text
dev-curriculum/
├── business/
    ├── ...                          # Misc. business-related documents
├── curriculum/
│   ├── curriculum.json
│   ├── phases/
│   │   ├── P01.phase.json
│   │   ├── P02.phase.json
│   │   └── ...
│   ├── modules/
│   │   └── P01/
│   │       ├── P01-M01.module.json
│   │       ├── P01-M02.module.json
│   │       └── ...
│   └── lessons/
│       └── P01/
│           └── M01/
│               ├── L01/
│               │   ├── P01-M01-L01.lesson.json
│               │   ├── P01-M01-L01.lesson.md
│               │   ├── P01-M01-L01.worksheet.md
│               │   └── P01-M01-L01.feedback.md
│               └── L02/
│                   ├── P01-M01-L02.lesson.json
│                   ├── P01-M01-L02.lesson.md
│                   ├── P01-M01-L02.worksheet.md
│                   └── P01-M01-L02.feedback.md
├── projects/
│   ├── catchbook-product-spec.md    # Complete CatchBook specification
│   └── supplementary/               # Additional projects if needed
│       └── ...
├── learner-state/
│   ├── current.json                 # Active position (phase/module/lesson)
│   ├── completed/
│   │   ├── P01-M01-L01.json         # Per-lesson completion records
│   │   ├── .gitkeep/
|   |   └── ...
│   ├── skills.json                  # Skill tracking
│   └── metrics.json                 # Time, confidence, mastery data
├── reflections/
│   ├── 2025-12-02.md                # Daily reflection entries
│   └── ...
├── lesson-summaries/
│   ├── P01-M01-L01-summary.md       # Per-lesson summaries
│   └── ...
├── schemas/
│   ├── curriculum.schema.json
│   ├── phase.schema.json
│   ├── module.schema.json
│   ├── lesson.schema.json
│   ├── state-current.schema.json
│   ├── state-completed.schema.json
│   ├── state-skills.schema.json
│   └── state-metrics.schema.json
├── roles/
│   ├── architect.md                 # Role definitions
│   ├── curriculum-designer.md
│   ├── professor.md
│   ├── advisor.md
│   └── evaluator.md
├── templates/
│   ├── lesson-summary.template.md
│   ├── reflection.template.md
│   └── commit-message.template.txt
├── snapshots/
│   ├── 2025-12-02-pre-module.zip    # State backups for rollback
│   └── ...
├── tools/
│   └── validate.py                  # Schema validation script
├── .github/
│   └── workflows/
│       └── validate.yml             # CI validation
├── catchbook-curriculum-v1.csv      # Master curriculum overview (28 phases, 139 modules)
├── claude-project-instructions.txt  # Copy of Claude Project Instructions
├── user-profile.md                  # Learner profile (Jeff)
├── quickstart.md                    # Beginner-friendly entry point
├── instructions.md                  # Operational reference
├── ARCHITECTURE.md                  # This document
└── README.md                        # Repository overview
```

### 1.3 Initial Commit

```bash
git init
git add .
git commit -m "feat(init): create CatchBook curriculum system structure"
git branch -M master
git remote add origin git@github.com:jeff-hutting/dev-curriculum.git
git push -u origin master
```

---

## Phase 2: MCP Setup

### 2.1 Install Claude Desktop

Download from: <https://claude.ai/download>

### 2.2 Configure GitHub MCP Server

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
    }
  }
}
```

### 2.3 Generate GitHub Personal Access Token

1. Go to <https://github.com/settings/tokens>
2. Click "Generate new token (classic)"
3. Scopes needed:
    - `repo` (full control of private repositories)
    - `read:org` (read org data)
4. Copy token and paste into config above

### 2.4 Configure Filesystem MCP

**Add to same config file:**

```json
{
  "mcpServers": {
    "github": { ... },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/jeffhutting/dev/dev-curriculum"]
    }
  }
}
```

This gives Claude access to local repository files for bulk operations.

### 2.5 Restart Claude Desktop

Close and reopen Claude Desktop app. Both MCP connections should be active.

### 2.6 Verify Connection

Open new chat in Claude Desktop:

```text
Can you list the contents of my dev-curriculum repository?
```

Expected: Claude reads repo structure and lists files.

---

## Phase 3: Core Schemas

### 3.1 Schema Overview

All schemas enforce strict structure for machine-readable files. Schemas validate:

- Curriculum hierarchy (phases → modules → lessons)
- Learner state decomposition
- CatchBook project integration
- Completion tracking

### 3.2 `schemas/curriculum.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["curriculum_name", "project", "audience", "global_objectives", "phases", "metadata"],
  "properties": {
    "curriculum_name": {"type": "string"},
    "project": {
      "type": "object",
      "required": ["name", "description", "spec_file"],
      "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "spec_file": {"type": "string"},
        "tech_stack": {
          "type": "object",
          "properties": {
            "frontend": {"type": "array", "items": {"type": "string"}},
            "backend": {"type": "array", "items": {"type": "string"}},
            "database": {"type": "array", "items": {"type": "string"}},
            "mobile": {"type": "array", "items": {"type": "string"}},
            "ai_ml": {"type": "array", "items": {"type": "string"}}
          }
        }
      }
    },
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
        "required": ["phase_id", "phase_name", "estimated_hours"],
        "properties": {
          "phase_id": {"type": "string", "pattern": "^P[0-9]{2}$"},
          "phase_name": {"type": "string"},
          "estimated_hours": {"type": "integer", "minimum": 1},
          "module_count": {"type": "integer", "minimum": 1}
        }
      }
    },
    "total_estimated_hours": {"type": "integer", "minimum": 1},
    "total_modules": {"type": "integer", "minimum": 1},
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

### 3.3 `schemas/phase.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["phase_id", "phase_name", "modules", "metadata"],
  "properties": {
    "phase_id": {"type": "string", "pattern": "^P[0-9]{2}$"},
    "phase_name": {"type": "string"},
    "description": {"type": "string"},
    "catchbook_focus": {"type": "string"},
    "entry_criteria": {
      "type": "array",
      "items": {"type": "string"}
    },
    "exit_criteria": {
      "type": "array",
      "items": {"type": "string"}
    },
    "estimated_hours": {"type": "integer", "minimum": 1},
    "modules": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["module_id", "module_name", "estimated_hours", "catchbook_deliverable"],
        "properties": {
          "module_id": {"type": "string", "pattern": "^P[0-9]{2}-M[0-9]{2}$"},
          "module_name": {"type": "string"},
          "estimated_hours": {"type": "integer", "minimum": 1},
          "catchbook_deliverable": {"type": "string"}
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

### 3.4 `schemas/module.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["module_id", "module_name", "phase_id", "estimated_hours", "catchbook_deliverable", "learning_objectives", "lessons"],
  "properties": {
    "module_id": {"type": "string", "pattern": "^P[0-9]{2}-M[0-9]{2}$"},
    "module_name": {"type": "string"},
    "phase_id": {"type": "string", "pattern": "^P[0-9]{2}$"},
    "estimated_hours": {"type": "integer", "minimum": 1},
    "catchbook_deliverable": {"type": "string"},
    "description": {"type": "string"},
    "prerequisites": {
      "type": "array",
      "items": {"type": "string", "pattern": "^P[0-9]{2}-M[0-9]{2}$"}
    },
    "learning_objectives": {
      "type": "array",
      "items": {"type": "string"},
      "minItems": 1
    },
    "skills_taught": {
      "type": "array",
      "items": {"type": "string"}
    },
    "lessons": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["lesson_id", "title", "estimated_minutes"],
        "properties": {
          "lesson_id": {"type": "string", "pattern": "^P[0-9]{2}-M[0-9]{2}-L[0-9]{2}$"},
          "title": {"type": "string"},
          "lesson_type": {"type": "string", "enum": ["conceptual", "hands-on", "project", "review"]},
          "estimated_minutes": {"type": "integer", "minimum": 15}
        }
      }
    },
    "catchbook_integration": {
      "type": "object",
      "properties": {
        "feature_area": {"type": "string"},
        "repository_path": {"type": "string"},
        "dependencies": {"type": "array", "items": {"type": "string"}}
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
    "metadata": {
      "type": "object",
      "required": ["created_at", "updated_at"],
      "properties": {
        "created_at": {"type": "string", "format": "date"},
        "updated_at": {"type": "string", "format": "date"},
        "generated_by": {"type": "string"}
      }
    }
  }
}
```

### 3.5 `schemas/lesson.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["lesson_id", "title", "module_id", "phase_id", "lesson_type", "learning_objectives", "outline", "assessment"],
  "properties": {
    "lesson_id": {"type": "string", "pattern": "^P[0-9]{2}-M[0-9]{2}-L[0-9]{2}$"},
    "title": {"type": "string"},
    "module_id": {"type": "string", "pattern": "^P[0-9]{2}-M[0-9]{2}$"},
    "phase_id": {"type": "string", "pattern": "^P[0-9]{2}$"},
    "estimated_minutes": {"type": "integer", "minimum": 15},
    "lesson_type": {"type": "string", "enum": ["conceptual", "hands-on", "project", "review"]},
    "prerequisites": {
      "type": "array",
      "items": {"type": "string", "pattern": "^P[0-9]{2}-M[0-9]{2}-L[0-9]{2}$"}
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
    "catchbook_context": {
      "type": "object",
      "properties": {
        "feature": {"type": "string"},
        "deliverable": {"type": "string"},
        "code_location": {"type": "string"}
      }
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
    "professor_constraints": {
      "type": "array",
      "items": {"type": "string"}
    },
    "metadata": {
      "type": "object",
      "required": ["created_at"],
      "properties": {
        "created_at": {"type": "string", "format": "date"},
        "generated_by": {"type": "string"}
      }
    }
  }
}
```

### 3.6 State Schemas

#### `schemas/state-current.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["learner_id", "current_phase_id", "current_module_id", "current_lesson_id", "last_updated"],
  "properties": {
    "learner_id": {"type": "string"},
    "current_phase_id": {"type": "string", "pattern": "^P[0-9]{2}$"},
    "current_module_id": {"type": "string", "pattern": "^P[0-9]{2}-M[0-9]{2}$"},
    "current_lesson_id": {"type": "string", "pattern": "^P[0-9]{2}-M[0-9]{2}-L[0-9]{2}$"},
    "last_updated": {"type": "string", "format": "date-time"}
  }
}
```

#### `schemas/state-completed.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["lesson_id", "module_id", "phase_id", "completed_at", "duration_minutes", "confidence_rating"],
  "properties": {
    "lesson_id": {"type": "string", "pattern": "^P[0-9]{2}-M[0-9]{2}-L[0-9]{2}$"},
    "module_id": {"type": "string", "pattern": "^P[0-9]{2}-M[0-9]{2}$"},
    "phase_id": {"type": "string", "pattern": "^P[0-9]{2}$"},
    "completed_at": {"type": "string", "format": "date-time"},
    "duration_minutes": {"type": "integer", "minimum": 1},
    "confidence_rating": {"type": "integer", "minimum": 1, "maximum": 5},
    "catchbook_deliverable": {"type": "string"},
    "code_committed": {"type": "boolean"},
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

#### `schemas/state-skills.schema.json`

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
            "confidence": {"type": "integer", "minimum": 1, "maximum": 5},
            "modules_practiced": {
              "type": "array",
              "items": {"type": "string", "pattern": "^P[0-9]{2}-M[0-9]{2}$"}
            }
          }
        }
      }
    },
    "last_updated": {"type": "string", "format": "date-time"}
  }
}
```

#### `schemas/state-metrics.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["total_time_minutes", "lessons_completed", "modules_completed", "phases_completed", "reflections_written", "last_updated"],
  "properties": {
    "total_time_minutes": {"type": "integer", "minimum": 0},
    "lessons_completed": {"type": "integer", "minimum": 0},
    "modules_completed": {"type": "integer", "minimum": 0},
    "phases_completed": {"type": "integer", "minimum": 0},
    "catchbook_features_shipped": {"type": "integer", "minimum": 0},
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
git commit -m "feat(schemas): add JSON schemas for CatchBook curriculum structure"
git push
```

---

## Phase 4: Role System

### 4.1 Role Definition Pattern

Each role is defined in a Markdown file under `roles/`. Claude loads the role file to understand its responsibilities within the CatchBook curriculum context.

**Structure:**

```markdown
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

## CatchBook Context
- How this role relates to CatchBook development
- Examples of CatchBook-specific outputs

## Example Session Flow
1. Step-by-step workflow
2. From role activation to deliverable
```

### 4.2 Updated Role Files

#### `roles/architect.md`

```markdown
# Role: Architect

## Purpose

Design and maintain system structure, schemas, and file organization for the CatchBook curriculum system.

## Responsibilities

- Define and refine JSON schemas
- Design file structure and naming conventions (phases/modules/lessons)
- Validate architectural consistency
- Propose structural improvements
- Document system design decisions
- Ensure CatchBook integration patterns are consistent

## Input Files Required

- `schemas/*.schema.json`
- `curriculum/curriculum.json`
- `catchbook-curriculum-v1.csv`
- All phase files (`P01.json`, `P02.json`, etc.)
- All module files (`P01-M01.json`, etc.)
- `projects/catchbook-product-spec.md`
- `ARCHITECTURE.md`, `README.md`, `instructions.md`

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
- Ensure all deliverables map to CatchBook features

## CatchBook Context

- Validates that every module has a clear CatchBook deliverable
- Ensures tech stack alignment (React, FastAPI, PostgreSQL, etc.)
- Maintains consistency between curriculum structure and CatchBook architecture
- Proposes patterns for integrating curriculum with actual CatchBook codebase

## Example Session Flow

1. User requests schema validation
2. Architect loads all schemas and data files via MCP
3. Identifies inconsistencies or violations
4. Proposes specific fixes as artifacts
5. Generates commit message following Conventional Commits
6. Updates documentation if structure changed
```

#### `roles/curriculum-designer.md`

```markdown
# Role: Curriculum Designer

## Purpose

Generate module structures and lesson sequences just-in-time as learner progresses through CatchBook development.

## Responsibilities

- Generate phase files with module lists (from catchbook-curriculum-v1.csv)
- Create individual module JSON files with lesson outlines
- Generate lesson JSON files when requested by Professor or Advisor
- Ensure prerequisite chains are valid
- Design CatchBook feature integration for each module
- Break down large modules into manageable lessons (45-90 min each)
- Maintain pedagogical coherence across phases

## Input Files Required

- `catchbook-curriculum-v1.csv` (master curriculum overview)
- `curriculum/curriculum.json`
- `projects/catchbook-product-spec.md`
- `schemas/phase.schema.json`
- `schemas/module.schema.json`
- `schemas/lesson.schema.json`
- `learner-state/skills.json` (for scaffolding decisions)

## Output Format

- Phase files (JSON): `P01.json`, `P02.json`, etc.
- Module files (JSON): `P01-M01.json`, `P01-M02.json`, etc.
- Lesson files (JSON): `P01-M01-L01.json`, `P01-M01-L02.json`, etc.
- Proposed commit messages

## Constraints

- Never deliver actual teaching content (defer to Professor)
- Never assess learner progress (defer to Advisor)
- All files must validate against schemas
- Prerequisites must reference only existing lessons
- Estimated times must be realistic (lessons: 45-90 min, modules: 6-16 hrs)
- Every module must specify concrete CatchBook deliverable
- Lessons within a module must build toward module's CatchBook deliverable

## CatchBook Context

- Maps CSV modules to actual CatchBook features from product spec
- Ensures each lesson produces shippable code or documentation
- Sequences lessons to build CatchBook incrementally (MVP → full product)
- References specific sections of CatchBook-product-spec.md
- Aligns tech stack choices with CatchBook architecture

## Example Session Flow

1. User requests "Generate Phase 1 modules"
2. Designer loads catchbook-curriculum-v1.csv and filters Phase 1 rows
3. Generates P01.json with all 4 modules listed
4. Generates P01-M01.json (Git fundamentals) with lesson outline
5. When Professor needs lessons, generates P01-M01-L01.json, P01-M01-L02.json, etc.
6. Each lesson artifact is complete, schema-valid JSON
7. User copies artifacts to VS Code, saves under appropriate directories
8. Designer proposes commit message: "feat(curriculum): generate Phase 1 modules"
9. User commits and pushes

```

#### `roles/professor.md`

```markdown
# Role: Professor

## Purpose

Deliver individual lessons through structured, interactive teaching focused on CatchBook development.

## Responsibilities

- Load lesson file and follow its structure
- Teach concepts step-by-step with CatchBook examples
- Generate lesson documents as artifacts
- Facilitate checkpoint discussions
- Guide hands-on CatchBook coding exercises
- Produce end-of-lesson deliverables (summary, state update, reflection prompt)
- Adapt pacing based on learner state
- Verify CatchBook code quality before lesson completion

## Input Files Required

- `curriculum/lessons/{lesson_id}.json` (e.g., P01-M01-L01.json)
- `curriculum/modules/{module_id}.json` (e.g., P01-M01.json)
- `learner-state/current.json`
- `learner-state/skills.json`
- `learner-state/completed/{prior_lesson_ids}.json` (if prerequisites exist)
- `projects/catchbook-product-spec.md` (for feature context)

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
- All code examples must align with CatchBook tech stack
- Deliverables must be production-ready for CatchBook repo

## CatchBook Context

- Every lesson includes CatchBook-specific examples and exercises
- Guides learner to implement actual CatchBook features
- References CatchBook-product-spec.md for feature requirements
- Ensures code produced matches CatchBook architecture patterns
- Validates that module's CatchBook deliverable is achieved
- Provides context on how current lesson fits into broader CatchBook vision

## Example Session Flow

1. User requests "Teach P01-M01-L01"
2. Professor loads lesson file and module file via MCP
3. Loads catchbook-product-spec.md to understand CatchBook context
4. Generates complete lesson document as artifact:
   - Introduction: Why this matters for CatchBook
   - Concepts with CatchBook examples
   - Hands-on exercise: "Set up CatchBook Git repo"
   - Checkpoint questions at 15-minute intervals
5. User reads artifact, works through exercise, responds to checkpoints in chat
6. Professor adapts explanations based on responses
7. After final checkpoint, Professor generates:
   - Lesson summary artifact (based on template)
   - State update artifacts (4 JSON files)
   - Reflection prompt: "How does Git workflow apply to your CatchBook development?"
8. User copies artifacts to VS Code, saves files
9. Professor proposes commit message: "feat(lesson): complete P01-M01-L01 Git fundamentals"
10. User commits CatchBook repo changes + curriculum state updates

```

#### `roles/advisor.md`

```markdown
# Role: Advisor

## Purpose

Recommend next learning activities based on progress, skills, CatchBook feature priorities, and timeline goals.

## Responsibilities

- Analyze learner state (current position, completed lessons, skills, metrics)
- Recommend next lesson, module, or review activity
- Flag skills needing reinforcement
- Propose weekly learning plans aligned with CatchBook milestones
- Identify prerequisite gaps
- Track CatchBook feature completion vs. curriculum progress
- Adjust pacing recommendations based on 10-20 hrs/week availability

## Input Files Required

- `catchbook-curriculum-v1.csv` (master curriculum overview)
- `curriculum/curriculum.json`
- All phase and module files
- `learner-state/current.json`
- `learner-state/completed/*.json`
- `learner-state/skills.json`
- `learner-state/metrics.json`
- `projects/catchbook-product-spec.md` (to understand feature priorities)

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
- Must consider CatchBook feature dependencies (e.g., can't build API endpoints before backend setup)

## CatchBook Context

- Tracks which CatchBook features are completed vs. planned
- Recommends modules that unblock high-priority CatchBook features
- Suggests review if recent CatchBook code quality is low
- Proposes skipping modules if learner already has skill (validated against completed projects)
- Aligns weekly plans with CatchBook milestones (e.g., "MVP by Month 4")

## Example Session Flow

1. User requests "What should I do next?"
2. Advisor loads all learner-state files via MCP
3. Loads catchbook-curriculum-v1.csv to understand remaining modules
4. Analyzes completed lessons, skills, and metrics
5. Checks CatchBook product spec to see which features are priorities
6. Generates recommendation artifact with:
   - Suggested next lesson with justification: "Complete P01-M01-L02 to finish Git fundamentals module, which unlocks CatchBook repo setup"
   - Skills to review (if any): "Git branching confidence is 2/5, recommend reviewing P01-M01-L01 before continuing"
   - Weekly plan (if requested): "This week: Complete Module 1.1 (6 hours), set up CatchBook repo, write first commit"
   - CatchBook milestone context: "This puts you on track for Phase 1 completion in 4 weeks"
7. User reviews recommendation
8. If user agrees, activates Professor for suggested lesson

```

#### `roles/evaluator.md`

```markdown
# Role: Evaluator

## Purpose

Assess lesson quality, learning outcomes, CatchBook code quality, and system effectiveness.

## Responsibilities

- Validate that completed lessons met stated objectives
- Review lesson summaries for gaps or misconceptions
- Assess skill progression over time
- Evaluate CatchBook code quality (architecture, best practices, functionality)
- Identify curriculum weaknesses
- Propose lesson improvements
- Verify that module deliverables are production-ready for CatchBook

## Input Files Required

- Lesson file being evaluated
- Corresponding completed state file
- Lesson summary file
- Reflection file (if exists)
- CatchBook codebase (if evaluating code quality)
- `projects/catchbook-product-spec.md` (for feature requirements)

## Output Format

- Evaluation report (Markdown artifact)
- Optional: proposed lesson updates (JSON artifact)
- Optional: proposed skill adjustments (JSON artifact)
- Optional: CatchBook code review findings (Markdown)

## Constraints

- Never make curriculum changes directly (propose to Designer)
- Never teach (defer to Professor)
- Never decide next steps (defer to Advisor)
- All assessments must reference specific evidence from files
- Code evaluations must be constructive and reference best practices

## CatchBook Context

- Evaluates if CatchBook deliverables meet product spec requirements
- Checks code quality against CatchBook architecture patterns
- Validates that features are shippable (not just "learning exercises")
- Proposes improvements to align curriculum with real-world CatchBook needs
- Identifies where curriculum should add CatchBook-specific guidance

## Example Session Flow

1. User requests "Evaluate P01-M01-L01"
2. Evaluator loads lesson file, completed state, summary, reflection
3. If module has CatchBook deliverable, loads relevant code from CatchBook repo
4. Generates evaluation report as artifact:
   - Were objectives met? (evidence from summary)
   - Were misconceptions addressed? (evidence from reflection)
   - Is skill level update justified? (evidence from checkpoint responses)
   - CatchBook code quality: "Repo setup follows best practices, README is clear"
   - Recommendations for lesson improvement: "Add checkpoint on .gitignore patterns"
5. User reviews evaluation
6. If lesson needs updates, user activates Designer to modify lesson file
7. If CatchBook code needs revision, user refactors with Professor guidance

```

**Commit role files:**

```bash
git add roles/
git commit -m "feat(roles): update role definitions for CatchBook curriculum"
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

1. Detect dev-curriculum repository (via GitHub MCP or Filesystem MCP)
2. Read `user-profile.md`
3. Read `learner-state/current.json`
4. Read `catchbook-curriculum-v1.csv` (to show progress within 28-phase structure)
5. Display:

```text
=== CatchBook Curriculum System Bootstrap ===

Repository: dev-curriculum
Learner: Jeff
Project: CatchBook AI Fishing Journal

Current Position:
  Phase: P01 - Foundations (Module 1 of 4)
  Module: P01-M01 - Git fundamentals
  Lesson: P01-M01-L01 - Version control concepts
  
Progress:
  Phases Completed: 0/28
  Modules Completed: 0/139
  Lessons Completed: 0
  Total Time: 0 hours
  CatchBook Features Shipped: 0
  
Last Updated: 2025-12-02

Available Commands:
  /teach {lesson_id}    — Start a lesson with Professor
  /next                 — Get Advisor recommendation
  /status               — View progress dashboard
  /validate             — Run schema validation
  /help                 — Show all commands

Select a role or command to continue.
```

### 5.2 Role Activation

**User types:**

```text
/role professor
```

or

```text
/teach P01-M01-L01
```

**Claude's expected behavior:**

1. Load `roles/professor.md`
2. Load required files per role definition
3. Confirm activation:

```text
Role: Professor activated.

Ready to teach lesson P01-M01-L01: Version control concepts

Module Context: Git fundamentals (6 hours total)
CatchBook Deliverable: CatchBook repo setup + README

Type /begin to start the lesson, or ask questions first.
```

---

## Phase 6: Quick Start Path

### 6.1 Create `quickstart.md`

````markdown
# CatchBook Curriculum — Quick Start

**Goal:** Complete your first lesson and make your first CatchBook commit in 60 minutes.

## What You're Building

**CatchBook** is an AI-powered fishing journal app. Over 28 phases, you'll build it from scratch: mobile UI, backend API, database, AI species identification, and more.

This curriculum isn't about throwaway exercises—you're shipping real features that compound into a production app.

---

## Step 1: Bootstrap the System

Open Claude Desktop and type:

```text
/bootstrap
```

Claude will load your curriculum and show your current position within the 28-phase CatchBook roadmap.

---

## Step 2: Start Your First Lesson

Type:

```text
/teach P01-M01-L01
```

Claude will activate Professor mode and load the lesson on Git fundamentals.

---

## Step 3: Read the Lesson Document

Claude will generate a lesson document as an artifact. This contains:

- **Why this matters for CatchBook** (context)
- **Concepts to learn** (theory)
- **Hands-on exercise** (practice with CatchBook repo)
- **Checkpoint questions** (verify understanding)

Read through it at your own pace.

---

## Step 4: Answer Checkpoint Questions

When you reach a checkpoint, answer the question in the chat.

**Example checkpoint:**
> **Checkpoint 1:** In your own words, why is version control important for the CatchBook project?

Type your answer. Claude will adapt the next section based on your response.

---

## Step 5: Complete the Hands-On Exercise

Follow the instructions to:

1. Create a CatchBook repository
2. Write a README describing the project
3. Make your first Git commit

This is your first **real CatchBook deliverable**—not a toy example.

---

## Step 6: Complete the Lesson

After the final checkpoint, Claude will generate:

1. **Lesson summary** → Copy to `lesson-summaries/P01-M01-L01-summary.md`
2. **State updates** → Copy JSON artifacts to `learner-state/` files
3. **Reflection prompt** → Answer conversationally in chat

---

## Step 7: Save and Commit

In VS Code:
1. Copy artifacts to appropriate files
2. Save all changes
3. Commit with message Claude provides

```bash
git add .
git commit -m "feat(lesson): complete P01-M01-L01 version control concepts"
git push
```

---

## Step 8: What's Next?

Type:

```text
/next
```

Claude will activate Advisor and recommend your next lesson based on:
- Your progress in the CatchBook curriculum
- Skills you've mastered
- Which CatchBook features are ready to build next

---

## The Big Picture

**28 Phases. 139 Modules. ~850 Hours. One Real Product.**

You're not just learning full-stack development—you're building **CatchBook** from day 1 to production launch.

Every lesson ships a feature. Every module completes a major component. Every phase advances CatchBook toward launch.

---

**Ready?** Start with `/bootstrap` in Claude Desktop.

For advanced features, see `instructions.md`.
````

---

## Phase 7: Learner State Architecture

### 7.1 Decomposed State Model

**Philosophy:** Atomic state files enable clean Git history and focused updates.

**Key Difference from v1.0:** State now tracks phases, modules, AND lessons.

### 7.2 Create Initial State Files

#### `learner-state/current.json`

```json
{
  "learner_id": "jeff",
  "current_phase_id": "P01",
  "current_module_id": "P01-M01",
  "current_lesson_id": "P01-M01-L01",
  "last_updated": "2025-12-02T00:00:00Z"
}
```

#### `learner-state/skills.json`

```json
{
  "skills": {
    "git_basics": {
      "level": "novice",
      "last_practiced": "2025-12-02",
      "confidence": 2,
      "modules_practiced": []
    },
    "terminal_comfort": {
      "level": "novice",
      "last_practiced": "2025-12-02",
      "confidence": 2,
      "modules_practiced": []
    },
    "html_css": {
      "level": "novice",
      "last_practiced": "2025-12-02",
      "confidence": 2,
      "modules_practiced": []
    },
    "javascript_basics": {
      "level": "novice",
      "last_practiced": "2025-12-02",
      "confidence": 2,
      "modules_practiced": []
    },
    "python_basics": {
      "level": "novice",
      "last_practiced": "2025-12-02",
      "confidence": 2,
      "modules_practiced": []
    }
  },
  "last_updated": "2025-12-02T00:00:00Z"
}
```

#### `learner-state/metrics.json`

```json
{
  "total_time_minutes": 0,
  "lessons_completed": 0,
  "modules_completed": 0,
  "phases_completed": 0,
  "catchbook_features_shipped": 0,
  "reflections_written": 0,
  "average_confidence": 0,
  "consistency_score": 0,
  "last_updated": "2025-12-02T00:00:00Z"
}
```

#### `learner-state/completed/.gitkeep`

Empty directory placeholder for completed lesson records.

**Commit initial state:**

```bash
git add learner-state/
git commit -m "feat(state): initialize learner state for CatchBook curriculum"
git push
```

### 7.3 State Update Pattern

After each lesson, Professor generates 4 artifacts:

1. **current.json update** — new current_lesson_id (and module_id if transitioning)
2. **completed/{lesson_id}.json** — completion record with CatchBook deliverable
3. **skills.json update** — skill level changes + modules_practiced tracking
4. **metrics.json update** — time, confidence, count increments (including catchbook_features_shipped)

User copies these artifacts to appropriate files and commits atomically:

```bash
git add learner-state/
git commit -m "feat(progress): complete P01-M01-L01 version control concepts"
git push
```

---

## Phase 8: Lesson Delivery Model

### 8.1 Lesson Format: Document + Guided Checkpoints + CatchBook Integration

**Structure:**

````markdown
# Lesson: {Title}

**Phase:** {phase_id} - {phase_name}  
**Module:** {module_id} - {module_name}  
**Estimated Time:** {minutes} minutes  
**Prerequisites:** {list or "None"}

---

## CatchBook Context

**What You're Building:** {Brief description of CatchBook feature this lesson contributes to}

**Why It Matters:** {How this skill applies to CatchBook development}

**Module Deliverable:** {What you'll ship by end of module}

---

## Learning Objectives

By the end of this lesson, you will be able to:
1. {objective 1}
2. {objective 2}
3. {objective 3}

---

## Introduction

{2-3 paragraphs setting context and motivation with CatchBook examples}

---

## Section 1: {Topic}

{Explanation with CatchBook-specific examples}

### Example (CatchBook)

```javascript
// Real CatchBook code example
```

---

**CHECKPOINT 1:** {Question to verify understanding in CatchBook context}

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

## Hands-On Exercise: Build for CatchBook

{Step-by-step instructions to implement actual CatchBook feature}

**Deliverable:** {Specific file, commit, or feature to produce}

**Acceptance Criteria:**

1. {criterion 1}
2. {criterion 2}

---

## Summary

{Recap of key concepts and how they apply to CatchBook}

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

## Next Steps

**Next Lesson:** {next_lesson_id} - {next_lesson_title}  
**CatchBook Progress:** {What CatchBook features are now possible}

---

**End of Lesson Document**
````

### 8.2 Professor Workflow

1. User: `/teach P01-M01-L01`
2. Professor loads `curriculum/lessons/P01-M01-L01.json` via MCP
3. Professor loads `curriculum/modules/P01-M01.json` for module context
4. Professor loads `projects/catchbook-product-spec.md` for feature context
5. Professor generates lesson document as artifact (following structure above)
6. User reads document, completes hands-on exercise, answers checkpoint questions in chat
7. Professor adapts explanations based on answers
8. After final checkpoint, Professor generates:
    - Lesson summary artifact
    - 4 state update artifacts (JSON)
    - Reflection prompt (conversational, CatchBook-focused)
9. User copies artifacts to VS Code, saves
10. Professor proposes commit message following Conventional Commits
11. User commits CatchBook repo changes (if any) + curriculum state updates

### 8.3 Lesson Summary Template

Located at `templates/lesson-summary.template.md`:

```markdown
---
lesson_id: {{lesson_id}}
module_id: {{module_id}}
phase_id: {{phase_id}}
completed_at: {{iso_timestamp}}
duration_minutes: {{duration}}
confidence_rating: {{1-5}}
catchbook_deliverable: {{description}}
---

# Lesson Summary — {{lesson_id}}

## Title

{{lesson_title}}

## Module Context

{{module_name}} ({{module_id}})

## CatchBook Feature

{{catchbook_feature_description}}

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

## CatchBook Deliverable

{{description_of_what_was_built_or_shipped}}

## Code Committed

- Repository: {{repo_name}}
- Commit: {{commit_hash}}
- Files changed: {{file_list}}

## Next Steps

- {{next_step}}

---

**Confidence Rating:** {{1-5}}/5  
**Would Recommend Reviewing:** {{yes|no}}
```

### 8.4 Reflection Template

Located at `templates/reflection.template.md`:

```markdown
---
date: {{YYYY-MM-DD}}
lesson_id: {{lesson_id}}
module_id: {{module_id}}
phase_id: {{phase_id}}
energy_level: {{1-10}}
---

# Reflection — {{date}}

## Lesson

{{lesson_title}}

## CatchBook Context

{{what_catchbook_feature_or_capability_this_enabled}}

## How It Felt

{{2-4 sentences in learner's voice about the experience}}

## What Clicked

{{What concepts made sense, especially in CatchBook context}}

## What's Still Fuzzy

{{What needs more practice or clarification}}

## Real-World Application

{{How this lesson applies to building CatchBook or other real projects}}

## Mood After Lesson

{{energized|neutral|tired|frustrated|excited}}

---

**Energy Level:** {{1-10}}/10
```

**Commit templates:**

```bash
git add templates/
git commit -m "feat(templates): add CatchBook-focused lesson summary and reflection templates"
git push
```

---

## Phase 9: Command Registry

### 9.1 Minimal Command Set (Start)

| Command | Purpose | Role Required |
|---------|---------|---------------|
| `/bootstrap` | Initialize session | None |
| `/teach {lesson_id}` | Start lesson | Professor |
| `/next` | Get recommendation | Advisor |
| `/status` | View dashboard | None |
| `/validate` | Check schemas | Architect |

### 9.2 Command Behavior Definitions

#### `/bootstrap`

**Input:** None  
**Output:** Session initialization message + current position + CatchBook progress + command list  
**Files Read:** `user-profile.md`, `learner-state/current.json`, `catchbook-curriculum-v1.csv`

#### `/teach {lesson_id}`

**Input:** Lesson ID (e.g., `P01-M01-L01`)  
**Output:** Activates Professor, loads lesson, generates lesson document artifact with CatchBook context  
**Files Read:**

- `curriculum/lessons/{lesson_id}.json`
- `curriculum/modules/{module_id}.json`
- All learner-state files
- `projects/catchbook-product-spec.md`
- `roles/professor.md`

#### `/next`

**Input:** None  
**Output:** Activates Advisor, generates recommendation artifact with CatchBook milestone context  
**Files Read:**

- `catchbook-curriculum-v1.csv`
- `curriculum/curriculum.json`
- All phase and module files
- All learner-state files
- `projects/catchbook-product-spec.md`
- `roles/advisor.md`

#### `/status`

**Input:** None  
**Output:** Progress dashboard with Catchbook feature completion tracking  
**Files Read:** All learner-state files, curriculum files

**Example output:**

```text
=== CatchBook Curriculum Progress Dashboard ===

Project: CatchBook AI Fishing Journal
Current Phase: P01 — Foundations (Module 1 of 4)
Current Module: P01-M01 — Git fundamentals
Current Lesson: P01-M01-L01 — Version control concepts

Last Completed: None
Last Updated: 2025-12-02

Overall Progress:
├─ Phases: 0/28 completed (0%)
├─ Modules: 0/139 completed (0%)
├─ Lessons: 0 completed
└─ CatchBook Features Shipped: 0

Time Investment:
├─ Total Time: 0 hours
├─ Average Session: 0 minutes
└─ Consistency Score: 0.0 (0 weeks with 2+ lessons)

Skill Levels:
├─ git_basics:         ★☆☆☆☆ (novice, confidence 2/5)
├─ terminal_comfort:   ★☆☆☆☆ (novice, confidence 2/5)
├─ html_css:           ★☆☆☆☆ (novice, confidence 2/5)
├─ javascript_basics:  ★☆☆☆☆ (novice, confidence 2/5)
└─ python_basics:      ★☆☆☆☆ (novice, confidence 2/5)

Average Confidence: N/A
Reflections Written: 0

Next Milestone: Complete P01-M01 (Git fundamentals) → Unlock CatchBook repo setup

CatchBook Progress:
├─ Repo Setup: Not started
├─ README Documentation: Not started
└─ First Commit: Not started

=== End Dashboard ===
```

#### `/validate`

**Input:** None (or optional: specific file path)  
**Output:** Validation report for curriculum structure and state files  
**Files Read:** All JSON files in repo, all schema files, `roles/architect.md`

**Example output:**

```text
=== Schema Validation Report ===

✓ curriculum/curriculum.json — VALID
✓ learner-state/current.json — VALID
✓ learner-state/skills.json — VALID
✓ learner-state/metrics.json — VALID

Phase Files:
✓ curriculum/phases/P01.json — VALID

Module Files:
(No module files generated yet)

Lesson Files:
(No lesson files generated yet)

Completed State Files:
(No completed lessons yet)

Summary: 4/4 files valid (100%)

Recommendation: Generate Phase 1 modules to begin curriculum.

=== End Validation ===
```

---

## Phase 10: Validation Pipeline

### 10.1 Pre-commit Validation (Claude)

**When:** Before generating any JSON artifact  
**How:** Claude validates against schema internally  
**Outcome:** Only valid JSON artifacts are produced

### 10.2 Post-commit Validation (GitHub Actions CI)

**When:** On every push to master branch  
**How:** GitHub Actions runs `tools/validate.py`  
**Outcome:** CI fails if any file violates schema

#### Create `.github/workflows/validate.yml`

```yaml
name: Schema Validation

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

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

#### Update `tools/validate.py`

```python
#!/usr/bin/env python3
"""
Schema validation script for CatchBook curriculum system.
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
    
    # Validate phase files
    phase_dir = repo_root / "curriculum/phases"
    if phase_dir.exists():
        for phase_file in phase_dir.glob("P*.json"):
            validations.append((phase_file, repo_root / "schemas/phase.schema.json"))
    
    # Validate module files
    module_dir = repo_root / "curriculum/modules"
    if module_dir.exists():
        for module_file in module_dir.glob("P*-M*.json"):
            validations.append((module_file, repo_root / "schemas/module.schema.json"))
    
    # Validate lesson files
    lesson_dir = repo_root / "curriculum/lessons"
    if lesson_dir.exists():
        for lesson_file in lesson_dir.glob("P*-M*-L*.json"):
            validations.append((lesson_file, repo_root / "schemas/lesson.schema.json"))
    
    # Validate completed state files
    completed_dir = repo_root / "learner-state/completed"
    if completed_dir.exists():
        for completed_file in completed_dir.glob("P*-M*-L*.json"):
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
git commit -m "feat(validation): add CI validation pipeline for CatchBook curriculum"
git push
```

---

## Phase 11: Recovery & Rollback System

### 11.1 State Snapshots

**Purpose:** Create point-in-time backups before risky operations.

#### Create Snapshot Command

User types:

```text
/snapshot pre-module-P01-M02
```

**Claude's behavior:**

1. Activates Architect role
2. Creates ZIP archive of entire `learner-state/` directory
3. Saves to `snapshots/2025-12-02-pre-module-P01-M02.zip`
4. Generates artifact with confirmation message
5. Proposes commit message:

```bash
git add snapshots/
git commit -m "chore(snapshot): create pre-module-P01-M02 backup"
git push
```

#### Rollback Command

User types:

```text
/rollback pre-module-P01-M02
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
git commit -m "chore(rollback): restore state to pre-module-P01-M02"
git push
```

### 11.2 Redo Lesson

**Purpose:** Re-attempt a lesson without prior completion contaminating state.

User types:

```text
/redo P01-M01-L02
```

**Claude's behavior:**

1. Activates Advisor role
2. Loads `learner-state/completed/P01-M01-L02.json`
3. Generates new state artifacts with:
    - `current.json`: sets `current_lesson_id` to `P01-M01-L02`
    - Removes `P01-M01-L02.json` from `completed/`
    - Reverts skill levels to pre-lesson values (if recorded)
    - Decrements metrics (lessons_completed, total_time, catchbook_features_shipped)
4. User copies artifacts and commits
5. User can now run `/teach P01-M01-L02` fresh

### 11.3 Manual State Editing

**When:** User needs to fix incorrect state manually.

**Process:**

1. User opens state file in VS Code
2. Edits JSON directly
3. Runs `/validate` to ensure schema compliance
4. Commits change with descriptive message:

```bash
git add learner-state/skills.json
git commit -m "fix(state): correct git_basics level to emerging"
git push
```

---

## Phase 12: Success Metrics

### 12.1 Metrics Tracked in `learner-state/metrics.json`

1. **Total Time Investment** (`total_time_minutes`)
2. **Lessons Completed** (`lessons_completed`)
3. **Modules Completed** (`modules_completed`)
4. **Phases Completed** (`phases_completed`)
5. **CatchBook Features Shipped** (`catchbook_features_shipped`)
6. **Reflections Written** (`reflections_written`)
7. **Average Confidence** (`average_confidence`)
8. **Consistency Score** (`consistency_score`)

### 12.2 Success Milestones

| Milestone | Target | Significance |
|-----------|--------|--------------|
| First Commit | Week 1 | CatchBook repo initialized |
| Module 1 Complete | Week 2 | Git proficiency established |
| Phase 1 Complete | Week 4 | Foundations mastery |
| Phase 3 Complete (Frontend Basics) | Week 10 | CatchBook landing page live |
| Phase 8 Complete (Backend API) | Week 20 | CatchBook API functional |
| Phase 11 Complete (React) | Week 30 | CatchBook SPA prototype |
| Phase 15 Complete (AI Integration) | Week 40 | Species ID working |
| Phase 21 Complete (Deployment) | Week 50 | CatchBook MVP live |
| Phase 28 Complete | Week 60-80 | CatchBook v1.0 launched |

### 12.3 Timeline Estimates

**Based on 10-20 hours/week:**

- **Total Hours:** ~850 hours
- **At 10 hrs/week:** 85 weeks (~20 months)
- **At 15 hrs/week:** 57 weeks (~13 months)
- **At 20 hrs/week:** 43 weeks (~10 months)

**Recommended Pace:** 15 hours/week = CatchBook launch in ~1 year

---

## Appendix A: CatchBook Curriculum Overview

### A.1 Full Curriculum Structure

See `catchbook-curriculum-v1.csv` for complete breakdown.

**Summary:**

- **28 Phases**
- **139 Modules**
- **Estimated 850 hours**
- **Single Project Spine:** CatchBook

### A.2 Phase Breakdown

| Phase | Name | Modules | Hours | Key CatchBook Deliverables |
|-------|------|---------|-------|----------------------------|
| P01 | Foundations | 4 | 24 | Repo setup, Git workflow, tooling |
| P02 | Professional Tooling | 4 | 24 | Linting, environment config, project structure |
| P03 | Frontend Basics | 5 | 46 | Landing page, responsive design, photo gallery |
| P04 | Python Fundamentals | 5 | 52 | CLI tools, EXIF parser, weather API |
| P05 | Data Structures & Algorithms | 5 | 58 | Optimized data handling for catches |
| P06 | Modern JavaScript | 3 | 40 | Async photo upload, state management |
| P07 | TypeScript | 3 | 32 | Type-safe frontend codebase |
| P08 | Backend API (FastAPI) | 5 | 52 | REST API, database, file uploads |
| P09 | Database Design | 5 | 50 | PostgreSQL schema, relationships, queries |
| P10 | Authentication & Security | 5 | 52 | User auth, JWT, OAuth, OWASP compliance |
| P11 | React Fundamentals | 5 | 58 | Component library, SPA routing |
| P12 | React + TypeScript | 4 | 40 | Type-safe React components |
| P13 | Node.js (Alternative Backend) | 4 | 40 | Express API (comparison to FastAPI) |
| P14 | Advanced SQL & Analytics | 4 | 44 | Catch analytics, reports, visualizations |
| P15 | AI Integration (Claude API) | 4 | 44 | Species ID, prompt engineering |
| P16 | Advanced AI Features | 4 | 52 | RAG, recommendations, streaming |
| P17 | External API Integration | 4 | 40 | Weather, tides, solunar data |
| P18 | Equipment Tracking | 4 | 42 | Gear database, relationships, recommendations |
| P19 | Testing | 5 | 50 | Unit, integration, E2E tests, coverage |
| P20 | Performance Optimization | 5 | 46 | Image compression, caching, lazy loading |
| P21 | DevOps & Deployment | 5 | 48 | CI/CD, Docker, hosting, environments |
| P22 | Monitoring & Logging | 4 | 40 | Structured logging, error tracking, metrics |
| P23 | Progressive Web App | 4 | 38 | Offline mode, camera API, push notifications |
| P24 | Computer Science Fundamentals | 4 | 44 | Systems, networking, distributed systems |
| P25 | Software Architecture | 4 | 52 | Design patterns, SOLID, hexagonal architecture |
| P26 | Accessibility & i18n | 4 | 36 | WCAG compliance, internationalization |
| P27 | Native Mobile | 4 | 58 | React Native or SwiftUI, app store deployment |
| P28 | Launch & Marketing | 5 | 50 | Product Hunt, blog, community, open source |

---

## Appendix B: File Naming Conventions

### B.1 Naming Pattern

**Phases:** `P01.phase.json`, `P02.phase.json`, ..., `P28.phase.json`
- Location: `curriculum/phases/`
- Zero-padded phase ID + `.phase.json` extension

**Modules:** `P01-M01.module.json`, `P01-M02.module.json`, ..., `P28-M05.module.json`
- Location: `curriculum/modules/P{NN}/` (phase subdirectory)
- Example: `curriculum/modules/P01/P01-M01.module.json`

**Lessons:** `P01-M01-L01.lesson.json`, etc.
- Location: `curriculum/lessons/P{NN}/M{NN}/L{NN}/` (hierarchical subdirectories)
- Example: `curriculum/lessons/P01/M01/L01/P01-M01-L01.lesson.json`

**Lesson Artifacts (generated by Professor):**
- Lesson document: `P01-M01-L01.lesson.md` (in same directory as lesson.json)
- Worksheet: `P01-M01-L01.worksheet.md` (in same directory)
- Feedback: `P01-M01-L01.feedback.md` (in same directory)

**Completed State:** `P01-M01-L01.json`, `P01-M01-L02.json` (in `learner-state/completed/`)

### B.2 Rationale

- **Phase/module/lesson extensions**: Clear file type identification (.phase.json, .module.json, .lesson.json)
- **Hierarchical directories**: Scales better for 28 phases × ~5 modules × ~4 lessons
- **Phase-grouped modules**: All P01 modules in `curriculum/modules/P01/`
- **Deeply nested lessons**: All lesson artifacts grouped together in `curriculum/lessons/P01/M01/L01/`
- **Consistent naming**: File naming independent of directory structure
- **Zero-padding**: Ensures correct alphabetical sorting (P01 before P10)

### B.3 File Purposes

**lesson.json**
- Schema-validated lesson structure
- Required for system operation (Professor, Curriculum Designer)
- Contains: objectives, outline, assessment, CatchBook context

**lesson.md**
- Human-readable lesson document generated by Professor
- Includes: Table of Contents, sections, checkpoints, hands-on exercises
- Generated once, referenced during teaching

**completion.md**
- Checkpoint responses from learner
- Professor's evaluation of responses
- Misconceptions corrected
- Struggles noted
- Created during lesson delivery, updated as lesson progresses

### B.4 Examples

**Hierarchical structure (current):**
```text
# Phase files
curriculum/phases/P01.phase.json
curriculum/phases/P02.phase.json

# Module files
curriculum/modules/P01/P01-M01.module.json
curriculum/modules/P01/P01-M02.module.json
curriculum/modules/P02/P02-M01.module.json

# Lesson files
curriculum/lessons/P01/M01/L01/P01-M01-L01.lesson.json
curriculum/lessons/P01/M01/L01/P01-M01-L01.lesson.md
curriculum/lessons/P01/M01/L01/P01-M01-L01.worksheet.md
curriculum/lessons/P01/M01/L01/P01-M01-L01.feedback.md

curriculum/lessons/P01/M01/L02/P01-M01-L02.lesson.json
curriculum/lessons/P01/M01/L02/P01-M01-L02.lesson.md
curriculum/lessons/P01/M01/L02/P01-M01-L02.worksheet.md
curriculum/lessons/P01/M01/L02/P01-M01-L02.feedback.md

# State files (flat structure, unchanged)
learner-state/completed/P01-M01-L01.json
learner-state/completed/P01-M01-L02.json
```

**Flat structure (deprecated, migrated):**
```text
curriculum/phases/P01.json
curriculum/modules/P01-M01.json
curriculum/lessons/P01-M01-L01/lesson.json
```

### B.5 Migration

Structure was migrated on 2025-12-13 using `tools/migrate_to_hierarchical_structure.py`.

Migration script moved:
- Phase files: Added `.phase.json` extension
- Module files: Moved to phase subdirectories with `.module.json` extension
- Lesson directories: Moved to hierarchical `P{NN}/M{NN}/L{NN}/` structure

All existing lessons successfully migrated with Git history preserved.

---

## Appendix C: Curriculum Generation Strategy

### C.1 Just-In-Time Approach

**Philosophy:** Generate curriculum files only when needed, not all upfront.

**Rationale:**

1. **Flexibility:** Adjust curriculum based on learner progress and feedback
2. **Efficiency:** Don't pre-generate 850 hours of content that might change
3. **Focus:** Keep repository lean, generate next phase as current phase nears completion
4. **Iteration:** Lessons improve based on actual learner experience

### C.2 Generation Workflow

**Phase Files:**

- Generate `P01.json` at project start
- Generate `P02.json` when Phase 1 is 75% complete
- Continue pattern for all 28 phases

**Module Files:**

- Generate all modules for current phase when phase file is created
- Example: When `P01.json` is created, also generate `P01-M01.json` through `P01-M04.json`

**Lesson Files:**

- Generate lessons for current module just before teaching
- Example: When user starts Module 1.1, Curriculum Designer generates `P01-M01-L01.json`, `P01-M01-L02.json`, etc.
- Lessons generated in batches (all lessons for one module at once)

**Who Generates:**

- **Curriculum Designer role** generates all curriculum files
- **User** activates Designer via separate chat dedicated to curriculum generation
- **Architect role** validates generated files against schemas

### C.3 Generation Triggers

| Trigger | Action |
|---------|--------|
| Project start | Generate P01.json + P01-M01 through P01-M04 |
| User requests `/teach P01-M01-L01` | Generate all lessons for P01-M01 (if not exist) |
| Phase 1 reaches 75% complete | Generate P02.json + P02-M01 through P02-M04 |
| User completes Phase 1 | Generate Phase 2 lessons as needed |
| ... | Continue pattern |

### C.4 CSV as Source of Truth

`catchbook-curriculum-v1.csv` contains:

- All 28 phases
- All 139 modules
- Module names, focus areas, CatchBook deliverables, estimated hours

**Curriculum Designer** uses CSV as reference when generating JSON files.

**Workflow:**

1. Read CSV row for target module
2. Extract: phase, module name, focus, CatchBook deliverable, hours
3. Generate JSON file following schema
4. Break down module into 3-5 lessons (if not already specified)
5. Ensure each lesson contributes to module's CatchBook deliverable
6. Validate against schema
7. Output as artifact for user to save

---

## Appendix D: Roadmap

### v2.0 — CatchBook Curriculum Foundation (Current)

**Goal:** Core system operational with CatchBook-first workflow

**Deliverables:**

- ✅ Repository structure updated for CatchBook
- ✅ Schemas for phases/modules/lessons
- ✅ Role definitions updated for CatchBook context
- ✅ State tracking for phases/modules/lessons
- ✅ catchbook-curriculum-v1.csv integrated
- ✅ Just-in-time curriculum generation strategy
- ⏳ Generate Phase 1 files (P01.json + 4 modules + initial lessons)
- ⏳ Complete first module end-to-end (P01-M01: Git fundamentals)
- ⏳ Validate workflow and adjust as needed

**Status:** Architecture documented, ready for Phase 1 generation

---

### v2.1 — Phase 1 Execution

**Goal:** Complete Phase 1 (Foundations) and establish rhythm

**Deliverables:**

- Generate all Phase 1 lesson files (as needed)
- Complete all 4 Phase 1 modules:
  - P01-M01: Git fundamentals (6 hours)
  - P01-M02: Branching and PR workflow (6 hours)
  - P01-M03: Commit conventions + PR templates (6 hours)
  - P01-M04: GitHub Issues + Projects (6 hours)
- Set up CatchBook repository with proper structure
- Write CatchBook README and first documentation
- Establish Git workflow for CatchBook development
- Validate lesson quality and pacing
- Refine templates based on actual usage

**Outcome:** Phase 1 complete, CatchBook repo operational, workflow validated

---

### v2.2 — Phase 2-3 Execution

**Goal:** Professional tooling + frontend basics

**Deliverables:**

- Complete Phase 2 (Professional Tooling): 24 hours
- Complete Phase 3 (Frontend Basics): 46 hours
- CatchBook landing page live (static)
- Photo gallery prototype
- Linting and tooling configured for CatchBook

**Outcome:** Frontend fundamentals mastered, visual CatchBook prototype

---

### v3.0 — Automation Layer

**Goal:** Reduce manual file operations

**Deliverables:**

- CLI tool for common operations:

  ```bash
  devc teach P01-M01-L01    # Launches Professor session
  devc next                 # Launches Advisor
  devc commit               # Auto-commit with proper message
  devc snapshot {name}      # Create backup
  devc rollback {name}      # Restore backup
  devc status               # Show dashboard
  ```

- Auto-apply state updates (after user approval)
- Auto-commit with generated messages
- Batch validation runner
- Metrics export to CSV

**Outcome:** Faster workflow, fewer manual steps

---

### v4.0 — Mid-Curriculum (Phases 8-15)

**Goal:** Backend + AI integration complete

**Deliverables:**

- CatchBook API fully functional (FastAPI + PostgreSQL)
- User authentication working
- Species ID via Claude API operational
- Catch logging end-to-end (photo → database → display)

**Outcome:** CatchBook MVP functional (core features work)

---

### v5.0 — Advanced Features (Phases 16-23)

**Goal:** Polish and production-readiness

**Deliverables:**

- Predictions and recommendations live
- PWA with offline mode
- CI/CD pipeline operational
- Monitoring and logging in place
- Performance optimized

**Outcome:** CatchBook production-ready

---

### v6.0 — Native Mobile + Launch (Phases 24-28)

**Goal:** Native mobile app + public launch

**Deliverables:**

- React Native or SwiftUI mobile app
- App Store / Play Store deployment
- Product Hunt launch
- Technical blog series
- Open source library releases

**Outcome:** CatchBook v1.0 launched, public product

---

## Final Notes

This architecture is designed to:

- **Eliminate throwaway learning:** Every module ships a CatchBook feature
- **Provide clean artifact-based workflows:** GitHub MCP + Filesystem MCP replace file sync overhead
- **Scale from v2.0 (manual) → v6.0 (production app):** Without curriculum rework
- **Maintain Git-native discipline throughout:** Every session = commit
- **Build a real product users want:** CatchBook isn't a learning exercise, it's a launchable app

**Current State:** Architecture complete, ready to generate Phase 1 curriculum files.

**Next Actions:**

1. Activate Curriculum Designer (separate chat)
2. Generate `P01.json` (Phase 1 file)
3. Generate `P01-M01.json` through `P01-M04.json` (Module files)
4. Generate initial lesson files for P01-M01 (Git fundamentals)
5. Begin teaching with `/teach P01-M01-L01`

---

## End of ARCHITECTURE.md — CatchBook Curriculum Edition v2.0
