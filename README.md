# dev-curriculum

A Git-native, Claude-assisted full-stack engineering curriculum system built around **Helm**, a real production project. This system transforms learning from passive consumption into active building—every lesson produces shippable code, every module completes a feature, and every phase advances Helm toward launch.

---

## Overview

**Helm** is an AI-powered fishing journal app that uses photo capture + EXIF data + computer vision to auto-populate catch details. Target: 10 seconds to log a catch vs. 3-5 minutes in competing apps.

This curriculum spans **28 phases, 139 modules, and approximately 850 hours** of hands-on learning. At 10-20 hours per week, you'll build Helm from concept to production launch in 10-20 months.

**Core Innovation:** No throwaway exercises. Every module produces a real, shippable feature for Helm. You're not just learning full-stack development—you're building a launchable product from day 1.

---

## What Makes This Different

### Traditional Learning

- Disconnected tutorials and exercises
- Theoretical knowledge without application
- Toy projects that don't compound
- Passive consumption, minimal retention
- No portfolio coherence

### This System

- **File-backed state:** Repository is source of truth, not AI memory
- **Artifact-first delivery:** Clean copy/paste workflow via Claude artifacts
- **Real project spine:** Helm drives every lesson (no throwaway code)
- **Git-native workflow:** Every session produces commits with proper messages
- **Just-in-time curriculum:** Generate lessons as needed, adapt based on progress
- **Role-based operation:** Specialized AI roles for teaching, advising, designing, evaluating
- **Production stakes:** Build best practices from day 1 (testing, CI/CD, documentation)

---

## How the System Works

### Architecture Overview

```text
Phases (28) → Modules (139) → Lessons (variable)
     ↓              ↓                ↓
 P01.json    P01-M01.json    P01-M01-L01.json
```

**Hierarchy:**

- **Phase:** Major learning section (e.g., "Foundations", "Backend Development")
- **Module:** Focused skill area (e.g., "Git fundamentals", "React basics")
- **Lesson:** Individual teaching unit (45-90 minutes each)

**Example:**

- Phase 1: Foundations
  - Module 1.1: Git fundamentals (6 hours) → Helm repo setup
  - Module 1.2: Branching and PRs (6 hours) → First PR workflow
  - Module 1.3: Commit conventions (6 hours) → Professional repo hygiene
  - Module 1.4: GitHub Issues + Projects (6 hours) → Feature board + milestones

### The Five Roles

Claude operates in specialized roles, each defined in `roles/*.md`:

| Role | Purpose | Primary Outputs |
|------|---------|----------------|
| **Architect** | System design, schema management, structure validation | Schemas, architecture docs, validation reports |
| **Curriculum Designer** | Generate modules and lessons just-in-time | Phase files, module files, lesson files (JSON) |
| **Professor** | Deliver lessons with guided checkpoints | Lesson documents, summaries, state updates |
| **Advisor** | Progress tracking, next-step recommendations, pacing | Recommendation reports, weekly plans |
| **Evaluator** | Assess lesson quality, code quality, learning outcomes | Evaluation reports, improvement proposals |

### Session Workflow

1. **Bootstrap:** Claude loads curriculum context and current progress
2. **Role Selection:** Activate appropriate role for the task
3. **Generation/Teaching:** Claude produces artifacts (JSON, Markdown, code)
4. **Copy & Save:** You copy artifacts to VS Code and save files
5. **Commit:** Commit with Claude's proposed message (Conventional Commits)
6. **Push:** Push to GitHub (MCP reads state next session)
7. **Repeat:** Next lesson builds on previous work

**Key Point:** Artifacts are temporary transport vehicles. Once copied to files and committed to Git, they can be deleted. GitHub is the source of truth.

---

## Helm: The Project Spine

### Tech Stack

- **Frontend:** React + TypeScript (web), React Native or SwiftUI (mobile)
- **Backend:** Python + FastAPI
- **Database:** PostgreSQL + PostGIS
- **AI:** Claude API for species identification and recommendations
- **Mobile:** Progressive Web App (PWA) → Native mobile app

### Product Vision

**Problem:** Existing fishing apps require excessive manual data entry (3-5 minutes per catch).

**Solution:** Helm uses AI to auto-populate 90% of catch data from photos:

- Snap photo → AI identifies species
- EXIF data → GPS location, timestamp, camera settings
- APIs → Weather, tide state, moon phase, solunar periods
- User confirms → Catch logged in 10 seconds

**Unique Value:**

- Zero-friction logging (10 seconds vs. 3-5 minutes)
- Predictive intelligence ("Tomorrow morning at Delta Coves: 85% success probability")
- Equipment tracking (which lures work when/where)
- Privacy-first (location sharing is opt-in)

### Helm Curriculum Roadmap

| Phase | Focus | Hours | Key Helm Deliverables |
|-------|-------|-------|----------------------------|
| P01 | Foundations | 24 | Repo setup, Git workflow, tooling |
| P02 | Professional Tooling | 24 | Linting, environment config, project structure |
| P03 | Frontend Basics | 46 | Landing page, responsive design, photo gallery |
| P04 | Python Fundamentals | 52 | CLI tools, EXIF parser, weather API |
| P05 | Data Structures | 58 | Optimized data handling for catches |
| P06 | Modern JavaScript | 40 | Async photo upload, state management |
| P07 | TypeScript | 32 | Type-safe frontend codebase |
| P08 | Backend API | 52 | REST API, database, file uploads |
| P09 | Database Design | 50 | PostgreSQL schema, relationships, queries |
| P10 | Auth & Security | 52 | User auth, JWT, OAuth, OWASP compliance |
| P11 | React Fundamentals | 58 | Component library, SPA routing |
| P12 | React + TypeScript | 40 | Type-safe React components |
| P13 | Node.js | 40 | Express API (comparison to FastAPI) |
| P14 | SQL & Analytics | 44 | Catch analytics, reports, visualizations |
| P15 | AI Integration | 44 | Species ID, prompt engineering |
| P16 | Advanced AI | 52 | RAG, recommendations, streaming |
| P17 | External APIs | 40 | Weather, tides, solunar data |
| P18 | Equipment Tracking | 42 | Gear database, recommendations |
| P19 | Testing | 50 | Unit, integration, E2E tests |
| P20 | Performance | 46 | Image compression, caching, CDN |
| P21 | DevOps | 48 | CI/CD, Docker, deployment |
| P22 | Monitoring | 40 | Logging, error tracking, metrics |
| P23 | PWA | 38 | Offline mode, camera API, push notifications |
| P24 | CS Fundamentals | 44 | Systems, networking, distributed systems |
| P25 | Architecture | 52 | Design patterns, SOLID principles |
| P26 | Accessibility | 36 | WCAG compliance, internationalization |
| P27 | Native Mobile | 58 | React Native/SwiftUI, app store deployment |
| P28 | Launch | 50 | Product Hunt, blog, community, open source |

**Total:** ~850 hours

See `curriculum.json` for complete module breakdown.

See `projects/helm-product-spec.md` for full product specification.

---

## Repository Structure

```text
dev-curriculum/
├── curriculum/
│   ├── curriculum.json              # Top-level Helm curriculum design
│   ├── phases/
│   │   ├── P01.json                 # Phase 1: Foundations
│   │   ├── P02.json                 # Phase 2: Professional Tooling
│   │   └── ...                      # P03-P28 (generated just-in-time)
│   ├── modules/
│   │   ├── P01-M01.json             # Module: Git fundamentals
│   │   ├── P01-M02.json             # Module: Branching and PRs
│   │   └── ...                      # Generated just-in-time as needed
│   └── lessons/
│       ├── P01-M01-L01/             # Lesson directory (nested structure)
│       │   ├── lesson.json          # Lesson schema/data
│       │   ├── lesson.md            # Human-readable lesson document
│       │   └── completion.md        # Checkpoint responses + evaluation
│       ├── P01-M01-L02/
│       │   ├── lesson.json
│       │   ├── lesson.md
│       │   └── completion.md
│       └── ...                      # Generated just-in-time by Curriculum Designer
├── projects/
│   ├── helm-product-spec.md    # Complete Helm specification
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
│   ├── lesson-summary.template.md   # Deprecated (now completion.md)
│   ├── reflection.template.md
│   └── commit-message.template.txt
├── snapshots/
│   ├── 2025-12-02-pre-module.zip    # State backups for rollback
│   └── ...
├── tools/
│   ├── validate.py                  # Schema validation script
│   └── migrate_lessons.py           # Migration script for nested structure
├── .github/
│   └── workflows/
│       └── validate.yml             # CI validation
├── curriculum.json      # Master curriculum (28 phases, 139 modules)
├── user-profile.md                  # Learner profile (Jeff)
├── quickstart.md                    # Beginner-friendly entry point
├── instructions.md                  # Operational reference
├── ARCHITECTURE.md                  # Complete system design
└── README.md                        # This document
```

---

## Getting Started

### Prerequisites

- macOS (or Linux/Windows with adjustments)
- Claude Desktop app installed
- GitHub account with personal access token
- VS Code installed
- Git installed
- Basic terminal comfort

### Setup (15 minutes)

#### 1. Install Claude Desktop

Download from: <https://claude.ai/download>

#### 2. Configure MCP (Model Context Protocol)

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

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

1. Go to <https://github.com/settings/tokens>
2. Generate new token (classic)
3. Scopes: `repo`, `read:org`
4. Copy token and paste into config above

#### 3. Restart Claude Desktop

Close and reopen Claude Desktop. MCP connections should be active.

#### 4. Clone This Repository

```bash
git clone git@github.com:jeff-hutting/dev-curriculum.git
cd dev-curriculum
```

#### 5. Verify MCP Connection

Open Claude Desktop, start new chat, type:

```text
Can you list the contents of my dev-curriculum repository?
```

Expected: Claude reads repo structure and lists files.

---

## Quick Start: Your First Lesson (30 minutes)

### 1. Bootstrap the System

In Claude Desktop:

```text
/bootstrap
```

Claude will load your curriculum and show current position within the 28-phase Helm roadmap.

### 2. Start Your First Lesson

```text
/teach P01-M01-L01
```

Claude activates Professor mode and generates a lesson document as an artifact.

### 3. Complete the Lesson

- Read lesson document (concepts + examples)
- Answer checkpoint questions in chat
- Complete hands-on exercise (e.g., create Helm repo)
- Review lesson summary artifact

### 4. Save State Updates

Claude generates 4 artifacts:

1. Lesson summary → Copy to `lesson-summaries/P01-M01-L01-summary.md`
2. `current.json` update → Copy to `learner-state/current.json`
3. `completed/P01-M01-L01.json` → Copy to `learner-state/completed/`
4. `skills.json` update → Copy to `learner-state/skills.json`
5. `metrics.json` update → Copy to `learner-state/metrics.json`

### 5. Commit

```bash
git add .
git commit -m "feat(lesson): complete P01-M01-L01 version control concepts"
git push
```

### 6. What's Next?

```text
/next
```

Claude activates Advisor and recommends your next lesson based on progress and Helm priorities.

---

## Core Commands

| Command | Purpose |
|---------|---------|
| `/bootstrap` | Initialize session, load context |
| `/teach {lesson_id}` | Start a lesson with Professor |
| `/next` | Get Advisor recommendation for next step |
| `/status` | View progress dashboard |
| `/validate` | Run schema validation |
| `/snapshot {name}` | Create state backup |
| `/rollback {name}` | Restore previous state |
| `/help` | Show all commands |

---

## Workflow Philosophy

### File-Backed State

All progress lives in Git, not AI memory:

- **Current position:** `learner-state/current.json`
- **Completed lessons:** `learner-state/completed/*.json`
- **Skill levels:** `learner-state/skills.json`
- **Metrics:** `learner-state/metrics.json`

Claude reads these files via MCP at session start. No hidden state, no surprises.

### Artifact-First Delivery

Claude generates structured content as **artifacts**:

- Lesson documents (Markdown)
- Lesson summaries (Markdown)
- State updates (JSON)
- Module files (JSON)
- Schemas (JSON)

**Workflow:**

1. Claude generates artifact
2. You copy artifact content
3. Paste into VS Code
4. Save file
5. Commit to Git
6. **Artifacts can be deleted after commit** (Git is source of truth)

No manual file creation, no typos, clean copy/paste.

### Just-In-Time Curriculum

Curriculum files are generated as needed, not all upfront:

- **Phase files:** Generated when approaching new phase
- **Module files:** Generated when phase starts
- **Lesson files:** Generated just before teaching

**Why?**

- **Flexibility:** Adjust curriculum based on learner progress
- **Efficiency:** Don't pre-generate 850 hours of content
- **Focus:** Keep repository lean
- **Iteration:** Lessons improve based on actual experience

**Curriculum Designer** (separate chat) generates files using `curriculum.json` as source of truth.

### Git-Native Workflow

Every session produces commits:

- **Conventional Commits format:** `feat(lesson): complete P01-M01-L01`
- **Atomic commits:** State updates grouped logically
- **Clean history:** Easy to track progress over time

Claude proposes commit messages following best practices. You review and execute.

### Role Specialization

Different tasks require different AI behavior:

- **Teaching?** Use Professor role
- **Need recommendation?** Use Advisor role
- **Generating curriculum?** Use Curriculum Designer role (separate chat)
- **Validating structure?** Use Architect role
- **Assessing quality?** Use Evaluator role

Each role has specific constraints and outputs defined in `roles/*.md`.

---

## Timeline & Milestones

### Estimated Timeline

**Total Hours:** ~850 hours

**At 10 hrs/week:** 85 weeks (~20 months)

**At 15 hrs/week:** 57 weeks (~13 months)

**At 20 hrs/week:** 43 weeks (~10 months)

**Recommended Pace:** 15 hours/week = Helm launch in ~1 year

### Major Milestones

| Milestone | Target Week | Significance |
|-----------|-------------|--------------|
| First Commit | Week 1 | Helm repo initialized |
| Module 1 Complete | Week 2 | Git proficiency established |
| Phase 1 Complete | Week 4 | Foundations mastery |
| Phase 3 Complete | Week 10 | Helm landing page live |
| Phase 8 Complete | Week 20 | Helm API functional |
| Phase 11 Complete | Week 30 | Helm SPA prototype |
| Phase 15 Complete | Week 40 | Species ID working |
| Phase 21 Complete | Week 50 | Helm MVP live |
| Phase 28 Complete | Week 60-80 | Helm v1.0 launched |

---

## Success Metrics

Tracked in `learner-state/metrics.json`:

- **Total Time Investment** (minutes)
- **Lessons Completed** (count)
- **Modules Completed** (count)
- **Phases Completed** (count)
- **Helm Features Shipped** (count)
- **Reflections Written** (count)
- **Average Confidence** (1-5 scale)
- **Consistency Score** (0-1, based on weekly activity)

View anytime with `/status` command.

---

## File Naming Conventions

**Phases:** `P01.json`, `P02.json`, ..., `P28.json` (zero-padded)

**Modules:** `P01-M01.json`, `P01-M02.json`, ..., `P28-M05.json`

**Lessons:** `P01-M01-L01.json`, `P01-M01-L02.json`, ..., `P28-M05-L03.json`

**Completed State:** `P01-M01-L01.json` (in `learner-state/completed/`)

**Summaries:** `P01-M01-L01-summary.md` (in `lesson-summaries/`)

**Rationale:**

- Zero-padding ensures correct alphabetical sorting (P01 before P10)
- Hyphenation shows clear hierarchy (Phase-Module-Lesson)
- Consistency across all file types

---

## Validation

### Pre-Commit Validation

Claude validates all JSON artifacts against schemas before output. Only valid JSON is generated.

### CI Validation

GitHub Actions runs `tools/validate.py` on every push:

- Validates all JSON files against schemas
- Checks file structure consistency
- Fails build if violations found

Run locally anytime:

```bash
python tools/validate.py
```

Or via Claude:

```text
/validate
```

---

## Recovery & Rollback

### Snapshots

Create backup before risky operations:

```text
/snapshot pre-module-P02-M01
```

Claude creates ZIP of entire `learner-state/` directory in `snapshots/`.

### Rollback

Restore previous state:

```text
/rollback pre-module-P02-M01
```

Claude extracts snapshot and generates artifacts. You copy to files and commit.

### Redo Lesson

Re-attempt a lesson:

```text
/redo P01-M01-L02
```

Claude removes lesson from completed state, reverts skill levels, decrements metrics. You can now teach the lesson fresh.

---

## Best Practices

### Daily Workflow

1. Open VS Code to `dev-curriculum/`
2. Open Claude Desktop, new chat
3. Run `/bootstrap`
4. Run `/next` to get recommendation
5. Run `/teach {lesson_id}` to start lesson
6. Complete lesson, copy artifacts, commit
7. Write reflection (optional but recommended)
8. Push to GitHub

### Weekly Review

1. Run `/status` to view progress
2. Review reflections for the week
3. Identify patterns (struggles, misconceptions)
4. Adjust pacing if needed
5. Plan next week's modules

### Commit Discipline

- **Commit after every lesson** (state + summary)
- **Follow Conventional Commits** (use Claude's proposed messages)
- **Group related changes** (state updates together)
- **Write clear messages** (future you will thank you)

### State Management

- **Never edit state files manually** unless necessary
- **Always run `/validate` after manual edits**
- **Create snapshots before major changes**
- **Trust Git as source of truth** (not chat history)

---

## Troubleshooting

### MCP Connection Fails

**Problem:** Claude can't read repository

**Solution:**

1. Check `~/Library/Application Support/Claude/claude_desktop_config.json`
2. Verify GitHub token is valid (<https://github.com/settings/tokens>)
3. Restart Claude Desktop
4. Test connection: `/bootstrap`

### Schema Validation Fails

**Problem:** `/validate` shows errors

**Solution:**

1. Read error message (shows file + line)
2. Fix JSON manually in VS Code
3. Run `/validate` again
4. If stuck, activate Architect role for help

### Lost Progress

**Problem:** State files corrupted or lost

**Solution:**

1. Check `snapshots/` for recent backup
2. Run `/rollback {snapshot_name}`
3. If no snapshot, restore from Git history:

```bash
git log --oneline learner-state/
git checkout {commit_hash} -- learner-state/
```

### Curriculum Files Missing

**Problem:** Lesson file doesn't exist when `/teach` is called

**Solution:**

1. Activate Curriculum Designer (separate chat)
2. Request lesson generation for that module
3. Copy generated artifacts to repository
4. Commit lesson files
5. Return to teaching chat, retry `/teach`

---

## Advanced Topics

### Custom Curriculum

Want to modify the curriculum?

1. Edit `curriculum.json`
2. Activate Curriculum Designer (separate chat)
3. Request regeneration of affected files
4. Validate with `/validate`
5. Commit changes

### Multiple Projects

Helm is the primary spine, but you can add supplementary projects:

1. Add project spec to `projects/supplementary/`
2. Create module files that reference new project
3. Update lesson files to include new project context

### Metrics Export

Export metrics for external visualization:

```bash
# Convert JSON to CSV
python tools/export_metrics.py
```

(Tool to be created in future iteration)

---

## Contributing

This is a personal learning system, but if you're building something similar:

1. Fork the repository
2. Adapt for your project (replace Helm with your app)
3. Modify schemas to match your needs
4. Share learnings and improvements

---

## Resources

### Core Documentation

- `ARCHITECTURE.md` — Complete system design
- `instructions.md` — Operational reference
- `quickstart.md` — Beginner-friendly guide

### Role Definitions

- `roles/architect.md`
- `roles/curriculum-designer.md`
- `roles/professor.md`
- `roles/advisor.md`
- `roles/evaluator.md`

### Helm Documentation

- `projects/helm-product-spec.md` — Full product specification
- `curriculum.json` — Master curriculum breakdown

### External Resources

- Claude Desktop: <https://claude.ai/download>
- Model Context Protocol: <https://modelcontextprotocol.io/>
- Conventional Commits: <https://www.conventionalcommits.org/>

---

## Status

**Current Version:** 2.0

**Current State:** Architecture complete, ready for Phase 1 generation

**Next Actions:**

1. Activate Curriculum Designer (separate chat)
2. Generate Phase 1 curriculum files (`P01.json` + modules)
3. Generate initial lessons for Module 1.1
4. Begin teaching with `/teach P01-M01-L01`

---

## Philosophy

### Execution Over Consumption

Don't collect tutorials—ship features.

### Small, Shippable Steps

Every lesson produces a commit. Every commit advances Helm.

### Process Over Memory

Git stores state, not AI memory. System works 6 months from now without context loss.

### Architecture Before Implementation

Design decisions documented before code written. Prevents rework.

### Compounding Over Intensity

Sustainable pace (15 hrs/week) beats burnout sprints. Build Helm in 1 year, not 3 months of chaos.

---

## Contact

**Project Owner:** Jeff Hutting

**Repository:** <https://github.com/jeff-hutting/dev-curriculum> (private)

**Feedback:** Open an issue or update documentation directly

---

**Ready to build Helm?** Start with `quickstart.md` or dive into `ARCHITECTURE.md`.

**Let's ship.**
