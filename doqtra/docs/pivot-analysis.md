# Pivot Analysis: CatchBook → Doqtra

**Date:** December 13, 2025  
**Decision:** Hybrid Approach (CatchBook P01-P03 → Doqtra MVP Month 4-6)  
**Status:** Documentation complete, ready to execute after P01-P03

---

## The Pivot Conversation

### What Triggered This

**Original Plan:**
- Build CatchBook (AI-powered fishing diary app)
- 28 phases, 850 hours, 10-20 months
- Validate dev-curriculum system while building real product

**New Insight:**
- dev-curriculum system itself has massive market potential
- Broader market (500M knowledge workers vs. niche fishing app)
- Real innovation: Procedural generation (Minecraft for learning)
- Working automation pipeline (lesson.md → reveal.js → TTS)

**Question:**
> "What if we pivot from CatchBook to building Doqtra (the learning platform) as the primary product?"

---

## Key Realizations During Discussion

### 1. Git-Native Workflow is NOT Universal

**Original Architecture (dev-curriculum):**
- File-backed state via Git
- Learners clone repo, commit progress
- Works great for software development curriculum
- **FAILS for Excel, productivity, design topics**

**Problem:**
- Excel user doesn't need to learn Git
- "Clone the repo" = instant churn for non-developers
- Forcing Git adds friction, not value

**Solution:**
- Two-tier architecture:
  - **Tier 1:** Web/Desktop app (consumers, no Git required)
  - **Tier 2:** CLI (developers, Git-native workflow)
- File-backed state via IndexedDB + cloud sync (not Git)
- Git integration optional (Electron desktop app for developers)

---

### 2. Curriculum Preview is CRITICAL

**Original UX Flow (Missing Step):**
```
1. Sign up
2. Answer questionnaire
3. Lessons appear ❌ (No visibility into roadmap)
```

**Corrected UX Flow:**
```
1. Sign up at doqtra.io
2. Answer questionnaire (learning style, goals, time)
3. AI generates curriculum roadmap ← NEW STEP
   - User sees all phases, modules, lessons
   - Can expand/collapse for detail
   - Can skip/add modules
   - Can regenerate with different parameters
4. User confirms curriculum (or modifies)
5. Lessons appear in browser
6. Complete checkpoints, auto-save progress
7. Periodic re-evaluation (adapt curriculum mid-journey)
8. Download certificates, export progress
```

**Why This Matters:**
- Transparency builds trust (no black box AI)
- User agency (control over learning path)
- Sets expectations (realistic timelines)
- Enables planning (fits life schedule)

---

### 3. Native Display Format (NOT Raw Markdown)

**Original Thinking:**
- Lessons generated as Markdown
- Displayed as Markdown in browser

**Problem:**
- Markdown is for AI generation (easy to create)
- NOT ideal for user display (limited styling)

**Solution:**
- **Generation format:** Markdown (AI-friendly)
- **Storage format:** Markdown (database)
- **Display format:** HTML/CSS (native web rendering)
- **Export options:** Markdown, PDF, HTML, PowerPoint (future)

**Pipeline:**
```
Claude API → Markdown → Database
                ↓
          Markdown → HTML (marked.js)
                ↓
          HTML + CSS → Browser (Tailwind Typography)
```

**Benefits:**
- Markdown easy for AI to generate
- HTML/CSS gives full design control
- Native web rendering = fast, accessible
- Export flexibility for offline use

---

### 4. Content Library with Network Effects

**Original Approach:**
- Generate every lesson fresh for every user
- High cost ($0.02 per lesson × 100 users = $2.00)

**Better Approach:**
- **Phase 1 (Cold Start):** First user → Generate lesson → Cache
- **Phase 2 (Warm Cache):** Next user → Pull from cache → Personalize
- **Phase 3 (Quality Control):** High ratings → Keep, Low ratings → Regenerate

**Benefits:**
- Reduces AI costs by 80%+ at scale
- Improves quality over time (community ratings)
- Faster delivery (no generation wait)
- Network effects (more users = better library)

---

## The Hybrid Decision

### Why NOT Full Pivot?

**Arguments against abandoning CatchBook now:**
- Only 1 module complete (5.5 hours invested)
- Haven't validated curriculum end-to-end
- P01-P03 teach skills needed for Doqtra anyway (Git, tooling, React)
- CatchBook landing page = portfolio piece
- 3 months isn't much delay (~40-50 hours)

**Arguments for continuing CatchBook (P01-P03):**
- ✅ Dogfooding validates system through full experience
- ✅ React proficiency from P03 needed for Doqtra frontend
- ✅ Tooling skills from P02 needed for Doqtra development
- ✅ Portfolio coherence ("I built Doqtra by using it to build CatchBook")
- ✅ Risk mitigation (if Doqtra fails, CatchBook still viable)

---

### The Hybrid Plan

**Month 1-3: CatchBook P01-P03 + Doqtra Documentation**
- Complete 3 phases of CatchBook (foundations, tooling, frontend)
- Document Doqtra in parallel (15 min/day)
- Interview 20 Excel learners (validate demand)
- Build reveal.js automation pipeline
- Create product spec, architecture docs, competitive analysis

**Month 4-6: Doqtra Web MVP**
- Pause CatchBook (resume later or pivot to case study)
- Build Doqtra web app (single topic: Excel)
- Features: Auth, questionnaire, curriculum generation, lesson rendering, checkpoints, progress, payments
- Beta launch with 50-100 users
- Target: $500 MRR, 4.0+ rating, 80% completion of first 3 lessons

**Month 7+: Scale Doqtra**
- Add 5 more topics (Notion, Slack, Figma, Python, React)
- Community features (ratings, comments)
- Desktop app (Electron with Git integration)
- Mobile app (React Native)
- Marketing (content, ads, partnerships)

---

## Market Window Analysis

### Current Status: 🟢 OPEN

**No competitor has:**
- Procedural curriculum generation (Minecraft model)
- Full roadmap transparency (see everything upfront)
- Mid-journey curriculum changes (skip/add modules)
- Universal platform (Excel + coding + design + productivity)

**Market is HOT:**
- Adaptive learning: $2.87B → $4.39B (52.7% growth in 2025)
- 63% of K-12 teachers using generative AI
- 57% of higher-ed prioritizing AI (up from 49%)

**Estimated Window:**
- 6-12 months before someone announces similar system
- 12-18 months before competitor MVP
- 18-24 months before market saturation

**Monitoring Strategy:**
- Weekly: Google Alerts, ProductHunt, Hacker News (15 min)
- Monthly: Competitor tracking, funding announcements (1 hour)
- Quarterly: Deep analysis, research scan, decision checkpoint (3 hours)

**Triggers to Pivot NOW:**
- Competitor raises $5M+ Series A for procedural generation
- Google/Microsoft acquires similar startup
- Y Combinator invests in direct competitor
- TechCrunch features "AI curriculum generation platform"

---

## Product Architecture Summary

### Single Universal App (Three Platforms)

**1. Web App (doqtra.io) — Primary MVP**
- Progressive Web App (offline-capable)
- React + TypeScript + Tailwind
- Native HTML/CSS lesson rendering
- IndexedDB local storage + PostgreSQL cloud sync

**2. Desktop App (Electron) — Phase 2**
- Git integration (optional auto-commit)
- Local file storage
- VS Code integration
- Offline-first mode

**3. Mobile App (React Native) — Phase 3**
- iOS and Android
- Push notifications
- On-the-go learning

**No CLI.** Desktop app IS the power-user version.

---

### Tech Stack

**Frontend:**
- React 18 + TypeScript
- Zustand (state)
- shadcn/ui + Tailwind CSS
- marked.js (Markdown → HTML)
- Prism.js (syntax highlighting)

**Backend:**
- Python 3.11 + FastAPI
- SQLAlchemy 2.0 + PostgreSQL
- Redis (caching)
- Anthropic Claude API
- Stripe (payments)

**Infrastructure:**
- AWS ECS Fargate
- AWS RDS (PostgreSQL)
- AWS ElastiCache (Redis)
- CloudFront (CDN)

---

## Target Market

### Primary: Knowledge Workers (500M)

**Personas:**
- Sarah, Data Analyst (wants Excel mastery)
- Marcus, Small Business Owner (wants Notion automation)
- Priya, Career Switcher (wants Python for data science)

### Secondary: Software Developers (30M)

**Personas:**
- Alex, Junior Developer (wants React + TypeScript)
- Jordan, Self-Taught Engineer (wants CS fundamentals)

**Total TAM:** 530M potential users

---

## Pricing Strategy

**Free Tier:**
- 5 lessons/month
- Single curriculum
- Community support

**Pro Tier ($20/month):**
- Unlimited lessons
- Multiple curricula
- All topics
- Export options
- Priority support

**Team Tier ($15/user/month, 10+ seats):**
- Everything in Pro
- Team dashboard
- Custom topics
- API access

**Target Revenue (Month 6):**
- 100 users, 25% conversion = 25 Pro users
- 25 × $20 = $500 MRR

---

## Success Metrics

### MVP (Month 6)
- 100 beta users
- 80% complete first 3 lessons
- 4.0+ average lesson rating
- <5% churn in first month
- $500 MRR

### V1.0 (Month 12)
- 10,000 active users
- $100K MRR
- 20 topics live
- 85% week-1 retention

---

## Key Insights Captured

### 1. Procedural Generation is the Innovation
- Like Minecraft: unique world per player
- Like Netflix: same content for everyone
- **Doqtra is Minecraft, not Netflix**

### 2. Transparency Builds Trust
- Show full roadmap before starting
- User controls path (skip, add, regenerate)
- No black box AI

### 3. File-Backed State ≠ Git-Native
- File structure works for state management
- Git is optional (not required for all users)
- IndexedDB + cloud sync for web/mobile
- Git integration for developers only

### 4. Content Library Reduces Costs
- First user pays generation cost
- Subsequent users get cached lessons
- Quality improves over time

### 5. Native Display Beats Raw Markdown
- Generate in Markdown (AI-friendly)
- Render as HTML/CSS (user-friendly)
- Export flexibility (future feature)

---

## What We Learned About CatchBook

**CatchBook is still valuable:**
- Solves real problem (fishing diary friction)
- Portfolio piece (shipping real app)
- Validates dev-curriculum through dogfooding
- React skills needed for Doqtra

**But Doqtra has bigger potential:**
- 530M TAM vs. niche fishing market
- Broader impact (help millions learn)
- More fundable (VCs love AI + education)
- Less seasonality (fishing is seasonal)

**Hybrid plan gives us both:**
- CatchBook P01-P03 = portfolio + skills
- Doqtra MVP = scalable business
- 6 months to both products

---

## Next Actions

### This Week (After completing this session)

1. **Commit Doqtra documentation**
   ```bash
   git add doqtra/
   git commit -m "docs(doqtra): initialize documentation for learning platform pivot
   
   - Create doqtra/ directory structure
   - Document product vision and core innovation
   - Technical architecture with native display format
   - Market validation and competitive analysis
   - MVP feature list and development roadmap
   - Capture pivot analysis and strategic reasoning"
   git push
   ```

2. **Continue CatchBook curriculum**
   - Start P01-M02-L01 (Branching workflow)
   - Apply learnings to Doqtra repo structure thinking

3. **Set up monitoring**
   - Google Alerts (5 keywords)
   - ProductHunt education notifications
   - Crunchbase saved searches

---

### Month 1-3 (December 2025 - February 2026)

**CatchBook work:**
- Complete P01 (4 modules, ~18 hours)
- Complete P02 (4 modules, ~24 hours)
- Complete P03 (5 modules, ~46 hours)
- **Total:** 88 hours over 3 months (~7 hours/week)

**Doqtra work (parallel, 15 min/day):**
- Interview 20 Excel learners
- Refine product spec
- Build content pipeline prototype
- Create landing page (waitlist)
- Test curriculum generation prompts

---

### Month 4-6 (March - May 2026)

**Doqtra MVP development:**
- Week 1: User auth, questionnaire
- Week 2-3: Curriculum generation, preview UI
- Week 4-5: Lesson rendering, checkpoints
- Week 6: Progress dashboard, payments
- Week 7-8: Beta testing, launch

**Target:** 100 users, $500 MRR, 4.0+ rating

---

## Conclusion

**Decision:** Hybrid approach is optimal.

**Reasoning:**
- 3 months to complete P01-P03 isn't much delay
- React skills from P03 needed for Doqtra anyway
- Dogfooding validates curriculum end-to-end
- Portfolio coherence ("built Doqtra by using it")
- Risk mitigation (two viable products)

**Market window:** 6-18 months (still open, but monitor)

**Execution plan:** CatchBook → Doqtra → Scale

**Commitment:** Ship both products in 6 months.

---

## Repository Structure Created

```
doqtra/
├── README.md                          # Overview and quickstart
├── docs/
│   ├── vision.md                      # Product vision
│   ├── architecture.md                # Technical architecture
│   ├── ux-flow.md                     # (To be created)
│   └── content-pipeline.md            # (To be created)
├── research/
│   ├── market-validation.md           # Market window analysis
│   ├── user-interviews.md             # (To be created)
│   └── competitor-tracking.md         # (To be created)
└── backlog/
    ├── mvp-features.md                # MVP feature list
    └── future-features.md             # (To be created)
```

**Status:** Documentation complete, ready to build after P01-P03.

---

**Let's ship both.**
