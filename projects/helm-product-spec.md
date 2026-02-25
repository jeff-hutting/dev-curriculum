# Helm — Product Specification
> *"Find your rhythm and steer through rough seas."*

**Status:** Draft v0.1
**Owner:** Jeff Hutting
**Date:** 2026-02-25
**Template:** Vibe Coding Product Spec (WonderDome vault)

---

## 1. High-Level "Vibe"

> **Concept:** A personal productivity tool built around a weekly planning ritual — capture tasks, see your week, drag tasks onto time blocks, and sync everything to Google Calendar. ClickUp's planner tab, without the $20/mo and the bloat.
> **Core Aesthetic:** Clean, fast, minimal. Functional over fancy. Dark mode preferred.
> **Primary User:** Jeff — a busy developer-in-training juggling a day job, family, and learning projects who needs one place to see everything and plan his week in 15 minutes.

---

## 2. The "Non-Negotiables" (Tech Stack)

- **Frontend:** React + TypeScript, Tailwind CSS
- **Backend:** Python + FastAPI
- **Database:** PostgreSQL
- **Auth:** Simple (single user — no multi-tenant needed at v1)
- **Mobile:** Progressive Web App (PWA) — mobile-accessible without a native app build
- **Calendar Integration:** Google Calendar API (read + write)
- **Deployment:** Local first (runs on your machine), cloud later

---

## 3. Core User Stories

*As Jeff, I want to...*

- **Capture tasks quickly:** Add a task with a name, optional project, optional due date, and optional time estimate — in under 5 seconds on mobile or desktop.
- **See my week at a glance:** Open a weekly calendar view that shows my Google Calendar events (work shifts, family) alongside any time blocks I've planned.
- **Plan my week by dragging:** Select tasks due this week from a sidebar list and drag them onto time slots in the calendar view. The block duration defaults to the task's estimated time.
- **Sync to Google Calendar:** Time blocks I create in Helm appear in my Google Calendar so my wife and anyone else sees my planned commitments.
- **Organize by project:** Group tasks under projects (e.g., Dev Curriculum, Home, CatchBook, Personal) so I can filter and focus.
- **Mark tasks done:** Check off tasks from anywhere — the list, the calendar block, or mobile.
- **See what's overdue and upcoming:** A simple filtered view showing: overdue, due today, due this week.

---

## 4. Technical Constraints & Logic

**Data Model:**
```
Project
  - id, name, color, archived

Task
  - id, title, project_id, due_date, estimated_minutes
  - priority (low/normal/high/urgent), status (todo/in_progress/done)
  - notes (optional), created_at

TimeBlock
  - id, task_id (nullable — blocks can exist without tasks)
  - start_time, end_time (datetime)
  - google_calendar_event_id (for sync tracking)
```

**Key Logic:**
- A task can have zero or many time blocks (one task can be worked across multiple sessions)
- Time blocks sync to Google Calendar as events — title = task title, description = project name
- Google Calendar events (work shifts, family) are pulled in as read-only context — Helm does not modify them
- Dragging a task onto the calendar creates a TimeBlock; duration snaps to estimated_minutes or defaults to 30 min
- Marking a task done marks all its incomplete time blocks as done too

**API Integrations:**
- Google Calendar API (OAuth 2.0 — read events from all calendars, write to a dedicated "Helm" calendar)

---

## 5. UI/UX Map

**Page 1 — Weekly Planner (primary view):**
- Left sidebar: Task list, filterable by project / due date / status
- Main area: 7-day calendar grid (Mon–Sun), time slots per day
- Google Calendar events shown as read-only blocks (greyed out)
- Helm time blocks shown in project color
- Drag task from sidebar → drop on time slot → creates block

**Page 2 — Task List / Inbox:**
- Full task list with filters: All / Today / This Week / Overdue / by Project
- Quick-add bar at top (title + optional project + optional due date)
- Inline edit for due date, priority, estimate

**Page 3 — Projects:**
- List of projects with task counts
- Archive completed projects

**Mobile (PWA):**
- Simplified task list view with quick-add
- Tap a task to see/edit details
- Week view accessible but planner drag-and-drop is desktop-primary

---

## 6. Success Metrics — "Done" Definition for MVP

- [ ] Tasks can be created, edited, and marked done
- [ ] Tasks are organized by project
- [ ] Weekly calendar view shows Google Calendar events (read-only)
- [ ] Tasks can be dragged from the sidebar onto calendar time slots
- [ ] Time blocks sync back to Google Calendar as events
- [ ] Overdue / this week filters work correctly
- [ ] PWA installable on iPhone (usable for quick capture)
- [ ] Runs locally without an internet connection (except Google Calendar sync)

---

## 7. Out of Scope for v1 (Revisit Later)

- Recurring tasks (manual for now)
- Time tracking / actual vs. estimated
- Collaboration / sharing with Nicole
- Notifications / reminders
- Sub-tasks
- Integrations beyond Google Calendar (GitHub, Obsidian, etc.)
- Analytics / productivity insights

---

## 8. The "Constitution" — Rules for AI-Assisted Development

*(Following vibe coding best practices — these are immutable rules for all coding sessions)*

1. **Single user only at v1** — no auth complexity, no multi-tenant architecture
2. **Local-first** — runs on localhost, no cloud deployment required until Jeff decides to ship it
3. **No over-engineering** — if it can be a simple CRUD operation, keep it simple
4. **TypeScript strict mode** — no `any` types
5. **Conventional Commits** — all commits follow P01-M03 conventions
6. **Mobile-accessible** — every feature must be usable on a phone, even if not optimized for it
7. **Google Calendar is read-only except for the dedicated "Helm" calendar** — never modify imported events

---

## 9. Suggested Name

**Helm** — you're at the helm, steering through the week. Fits the nautical metaphors you've been using ("rough seas," "smoother sailing," "finding a rhythm"). Open to alternatives.

Other candidates: *Anchor*, *Cadence*, *Tide*
