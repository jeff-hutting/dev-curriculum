# Doqtra: Universal AI-Powered Learning Platform

**Status:** Pre-development (documentation phase)  
**Timeline:** MVP launch target Month 4-6 (March-May 2026)  
**Last Updated:** December 13, 2025

---

## Vision Statement

Doqtra is a universal learning platform that uses procedural AI generation to create personalized curricula for any topic — from Excel to software engineering. Like Minecraft generates unique worlds for each player, Doqtra generates unique learning paths for each student.

**Core Innovation:** Just-in-time curriculum generation with full transparency. Users see and control their entire learning roadmap before starting.

---

## The Problem We're Solving

**Existing adaptive learning platforms:**
- ❌ One-size-fits-all content with minor adaptations
- ❌ Black box AI (no visibility into learning path)
- ❌ Static curricula (can't adjust based on progress)
- ❌ Separate tools for different topics
- ❌ No learner agency (system decides everything)

**Doqtra's approach:**
- ✅ Procedurally generated curricula (unique per learner)
- ✅ Transparent roadmap (see all phases, modules, lessons upfront)
- ✅ Dynamic adaptation (curriculum evolves with learner)
- ✅ Universal platform (Excel, coding, design, productivity, etc.)
- ✅ Learner control (skip, add, regenerate modules anytime)

---

## Market Opportunity

**Total Addressable Market:** 530M+ users
- 500M knowledge workers (Excel, productivity, design, etc.)
- 30M software developers

**Market Validation:**
- Adaptive learning market growing 52.7% YoY ($2.87B → $4.39B in 2025)
- 57% of higher-ed institutions prioritizing AI in 2025 (up from 49%)
- 63% of K-12 teachers using generative AI

**Competitive Advantage:**
- No competitor uses procedural generation (all adapt existing content)
- No competitor shows full curriculum roadmap upfront
- No competitor allows mid-journey curriculum regeneration

---

## Product Architecture

### Single Universal App (Three Deployment Targets)

**1. Web App (doqtra.io)** — Primary platform, all users
- Progressive Web App (offline-capable)
- React + TypeScript frontend
- Python + FastAPI backend
- PostgreSQL database

**2. Desktop App (Electron)** — Power users, developers
- Git integration (auto-commit on lesson complete)
- Local file storage (lessons as native files)
- VS Code integration ("Open in editor" button)
- Offline-first mode

**3. Mobile App (React Native)** — Phase 2
- iOS and Android
- On-the-go learning
- Push notifications

---

## User Experience Flow

### 1. Sign Up & Questionnaire
```
User creates account → Answers learning profile questions:
- Learning style (visual/auditory/hands-on/reading)
- Current skill level (novice/beginner/intermediate/advanced)
- Goals (career change/efficiency/hobby/certification)
- Time commitment (5/10/20 hours per week)
- Topic selection (with sub-topics)
```

### 2. Curriculum Generation & Preview
```
AI generates custom curriculum → User sees full roadmap:
- All phases, modules, lessons visible
- Estimated duration and hours
- Expandable/collapsible detail levels
- Can skip modules ("I already know this")
- Can add modules ("Include advanced topics")
- Can regenerate with different parameters
- Can save multiple curriculum variants
```

### 3. Learning Journey
```
User confirms curriculum → Lessons appear in browser:
- Native display format (HTML/CSS rendering, not raw Markdown)
- Interactive checkpoints throughout lesson
- Progress auto-saves to cloud
- After each lesson: confidence rating
- System adapts: struggled? Add review lesson
- System adapts: mastered quickly? Skip next basic lesson
```

### 4. Periodic Re-evaluation
```
Every 5 lessons → System checks in:
"You're progressing faster than expected. Would you like to:
- Skip Module X (already mastered)?
- Add Module Y (ready for advanced topics)?
- Keep current path?"
```

### 5. Completion & Export
```
User completes curriculum → Receives:
- Certificate of completion
- Exportable progress (JSON)
- Optional: Lesson content (Markdown, PDF, HTML, PowerPoint)
```

---

## Technical Architecture

### Frontend (React + TypeScript)
- Component-based UI
- State management: Context API or Zustand
- Offline support: IndexedDB for local caching
- Responsive design (desktop + mobile web)

### Backend (Python + FastAPI)
- RESTful API
- Claude API integration (lesson generation)
- Content library (cached lessons)
- User authentication (JWT)

### Database (PostgreSQL)
- User profiles
- Curriculum state
- Lesson library (reusable content)
- Progress tracking

### Lesson Rendering
- **Display format:** HTML/CSS (native web rendering)
- **Generation format:** Markdown (easy to generate with AI)
- **Conversion:** Markdown → HTML/CSS at render time
- **Export options:** Markdown, PDF, HTML, PowerPoint (future)

**Why this approach:**
- Markdown is easy for AI to generate (structured text)
- HTML/CSS gives full design control for display
- Export flexibility for offline use or sharing
- Native web rendering = fast, accessible, responsive

---

## Content Library Model

### Procedural Generation with Caching

**Phase 1: Cold Start (First User)**
```
User 1 learns Excel pivot tables
→ Doqtra generates lesson procedurally (Claude API cost: $0.02)
→ Lesson saved to content library
→ User 1 completes lesson, provides rating
```

**Phase 2: Warm Cache (Subsequent Users)**
```
User 2 wants to learn Excel pivot tables
→ Same learning style + skill level as User 1
→ Doqtra pulls from library (cost: $0.00)
→ Slight personalization (name, examples) via template
```

**Phase 3: Quality Control**
```
- Only cache lessons rated 4+ stars
- Auto-regenerate lessons with <3 stars
- Expert review for high-traffic lessons
- Community can flag outdated content
```

**Benefits:**
- Reduces API costs dramatically (80%+ savings at scale)
- Improves quality over time (crowd-sourced refinement)
- Faster lesson delivery (no generation wait)
- Network effects (more users = better library)

---

## Pricing Strategy

### Freemium Model

**Free Tier:**
- 5 lessons per month
- Single curriculum
- Basic topics only
- Community support

**Pro Tier ($20/month):**
- Unlimited lessons
- Multiple curricula (parallel learning)
- All topics (Excel, coding, design, etc.)
- Advanced personalization
- Export options (PDF, PowerPoint)
- Priority support

**Team Tier ($15/user/month, 10+ seats):**
- Everything in Pro
- Team dashboard (manager view)
- Custom topics (company-specific training)
- API access (integrate with LMS)
- Dedicated support

---

## Development Roadmap

### Pre-Development (Month 1-3): Current Phase
**Focus:** Complete CatchBook P01-P03, document Doqtra in parallel

**Deliverables:**
- ✅ Doqtra documentation (this folder)
- ⏳ User research (20 interviews with Excel learners)
- ⏳ Competitive analysis
- ⏳ Technical prototypes (curriculum generation, lesson rendering)

### MVP Development (Month 4-6): March-May 2026
**Focus:** Ship Doqtra Web with single topic (Excel)

**Features:**
- User authentication
- Learning profile questionnaire
- Curriculum generation + preview UI
- Lesson rendering (native HTML/CSS display)
- Checkpoint system
- Progress dashboard
- Content library (caching + reuse)
- Stripe payments

**Scope:**
- Excel curriculum only (validate concept)
- 10-15 lessons generated
- Basic personalization
- Web app only (no desktop/mobile)

### V1.0 Launch (Month 7-9): June-August 2026
**Focus:** Multi-topic expansion, community features

**New features:**
- 5 additional topics (Notion, Slack, Figma, Python, React)
- Community ratings and comments
- Advanced personalization (learning style adaptation)
- Lesson export (Markdown, PDF)
- Referral program

### V2.0 (Month 10-12): September-November 2026
**Focus:** Desktop app, mobile app, marketplace

**New features:**
- Electron desktop app (Git integration, local files)
- React Native mobile app (iOS + Android)
- User-generated content (expert contributors)
- Lesson marketplace (buy/sell curricula)
- Advanced analytics (time tracking, skill gaps)

---

## Success Metrics

### Beta Launch (Month 6)
- 100 users
- 80% complete first 3 lessons
- 4.0+ average lesson rating
- <5% churn after first month

### V1.0 Launch (Month 9)
- 1,000 users
- $10K MRR (monthly recurring revenue)
- 5 topics live
- 85% week-1 retention

### V2.0 (Month 12)
- 10,000 users
- $100K MRR
- 20 topics live
- Desktop + mobile apps launched

---

## Key Documents

### Documentation (`/doqtra/docs/`)
- `vision.md` — Product vision and core innovation
- `architecture.md` — Technical architecture deep dive
- `competitive-analysis.md` — Market research and differentiation
- `ux-flow.md` — Complete user experience wireframes
- `content-pipeline.md` — Lesson generation and rendering

### Research (`/doqtra/research/`)
- `market-validation.md` — Market window analysis
- `user-interviews.md` — Interview notes and insights
- `competitor-tracking.md` — Ongoing competitive monitoring

### Backlog (`/doqtra/backlog/`)
- `mvp-features.md` — MVP feature list with priorities
- `future-features.md` — Post-MVP ideas and enhancements

---

## Next Actions (After Completing CatchBook P01-P03)

### Week 1 (Month 4)
1. Set up development environment
2. Initialize React + TypeScript project
3. Set up FastAPI backend
4. Configure PostgreSQL database

### Week 2-3
1. Build user authentication
2. Create questionnaire UI
3. Implement curriculum generation API (Claude integration)

### Week 4-5
1. Build curriculum preview UI
2. Implement lesson rendering (Markdown → HTML/CSS)
3. Create checkpoint system

### Week 6-8
1. Build progress dashboard
2. Implement content library (caching)
3. Add Stripe payments
4. Deploy MVP to production

### Week 9-12
1. Beta testing (50 users)
2. Bug fixes and refinements
3. Marketing prep (landing page, content)
4. Launch publicly

---

## Repository Structure

```
doqtra/
├── README.md                    # This file
├── docs/
│   ├── vision.md                # Product vision
│   ├── architecture.md          # Technical architecture
│   ├── competitive-analysis.md  # Market research
│   ├── ux-flow.md              # User experience design
│   └── content-pipeline.md     # Lesson generation details
├── research/
│   ├── market-validation.md    # Market window analysis
│   ├── user-interviews.md      # User research notes
│   └── competitor-tracking.md  # Competitive monitoring
└── backlog/
    ├── mvp-features.md         # MVP feature list
    └── future-features.md      # Post-MVP ideas
```

---

## Questions to Revisit

1. **Curriculum generation algorithm:** What parameters drive lesson creation?
2. **Quality control:** How do we ensure generated lessons are accurate?
3. **Pricing validation:** Is $20/month the right price point?
4. **Topic prioritization:** Excel first, but what's second?
5. **Community features:** When to add ratings, comments, user contributions?

---

**This is the foundation. Build from here.**
