# Doqtra MVP Feature List

**Target Launch:** Month 4-6 (March-May 2026)  
**Scope:** Single topic (Excel), Web app only  
**Goal:** Validate procedural generation + curriculum transparency + user agency

---

## Must-Have Features (MVP)

### 1. User Authentication

**Priority:** P0 (Critical)  
**Estimated Effort:** 1 week

**Features:**
- [ ] Email/password signup
- [ ] Email/password login
- [ ] JWT token authentication
- [ ] Password reset via email
- [ ] Session management (24-hour expiry)

**Out of Scope (Post-MVP):**
- OAuth (Google, GitHub)
- Two-factor authentication
- SSO for enterprises

---

### 2. Learning Profile Questionnaire

**Priority:** P0 (Critical)  
**Estimated Effort:** 1 week

**Features:**
- [ ] Multi-step form (5-7 questions)
- [ ] Questions:
  - Current skill level (novice/beginner/intermediate/advanced)
  - Learning style (visual/auditory/hands-on/reading)
  - Goals (career change/efficiency/hobby/certification)
  - Time commitment (5/10/20 hours per week)
  - Excel subtopics (pivot tables, dashboards, Power Query, VBA, etc.)
- [ ] Progress indicator (step 2 of 5)
- [ ] Form validation (required fields)
- [ ] Save profile to database

**Out of Scope:**
- Multiple profiles per user
- Profile editing (locked after curriculum generation)
- Personality assessment (Myers-Briggs, etc.)

---

### 3. Curriculum Generation Engine

**Priority:** P0 (Critical)  
**Estimated Effort:** 2 weeks

**Features:**
- [ ] Claude API integration
- [ ] Curriculum generation prompt (based on user profile)
- [ ] Parse AI response into structured curriculum
- [ ] Database storage (curricula, phases, modules, lessons)
- [ ] Error handling (AI API failures, malformed responses)
- [ ] Loading state (10-30 second wait for generation)

**Curriculum Structure:**
```
Curriculum
└── Phases (2-4)
    └── Modules (3-5 per phase)
        └── Lessons (3-6 per module)
```

**Out of Scope:**
- Multi-topic support (only Excel for MVP)
- Curriculum templates (all procedurally generated)
- Collaborative curricula (team learning)

---

### 4. Curriculum Preview UI

**Priority:** P0 (Critical)  
**Estimated Effort:** 2 weeks

**Features:**
- [ ] Curriculum summary card
  - Total weeks, total lessons, total hours
  - Skill target (e.g., "Advanced Excel for Analytics")
- [ ] Phase cards (expandable/collapsible)
- [ ] Module cards (nested under phases)
- [ ] Lesson cards (nested under modules)
  - Lesson title, duration, learning objectives
- [ ] Expand/collapse all button
- [ ] Skip module button (marks module as skipped)
- [ ] Add module button (opens topic search)
- [ ] Regenerate curriculum button (re-runs AI generation)
- [ ] Save as variant button (creates alternate curriculum)
- [ ] Start learning button (activates curriculum, locks structure)

**Interactions:**
- Click phase → expand/collapse modules
- Click module → expand/collapse lessons
- Hover lesson → show learning objectives tooltip
- Skip module → grayed out, excluded from progress calculation
- Add module → modal with topic search, inserts after selected module

**Out of Scope:**
- Drag-and-drop reordering
- Inline editing (lesson titles, durations)
- Curriculum comparison (side-by-side variants)

---

### 5. Lesson Rendering Engine

**Priority:** P0 (Critical)  
**Estimated Effort:** 2 weeks

**Features:**
- [ ] Markdown to HTML conversion (marked.js)
- [ ] HTML sanitization (DOMPurify)
- [ ] Syntax highlighting (Prism.js)
- [ ] Responsive typography (Tailwind Typography)
- [ ] Image rendering (responsive, lazy-loaded)
- [ ] Code block rendering (with copy button)
- [ ] Table rendering (scrollable on mobile)
- [ ] Lesson navigation (previous/next buttons)
- [ ] Progress bar (% complete in lesson)

**Display Format:**
- Native HTML/CSS rendering (NOT raw Markdown)
- Tailwind Typography styling (prose classes)
- Mobile-responsive (readable on phone)

**Out of Scope:**
- Video embedding
- Interactive diagrams (Mermaid, D3.js)
- Audio narration (TTS)
- Export to PDF/PowerPoint

---

### 6. Checkpoint System

**Priority:** P0 (Critical)  
**Estimated Effort:** 2 weeks

**Features:**
- [ ] Checkpoint question rendering (embedded in lesson)
- [ ] Question types:
  - Multiple choice (radio buttons)
  - Multiple select (checkboxes)
  - Short answer (text input)
- [ ] Answer submission
- [ ] Immediate feedback (correct/incorrect)
- [ ] Hints (expandable on incorrect answer)
- [ ] Explanations (why answer is correct/incorrect)
- [ ] Checkpoint progress (3 of 5 complete)
- [ ] Block lesson completion until all checkpoints answered
- [ ] Save checkpoint responses to database

**Out of Scope:**
- Code execution checkpoints (run Python/Excel in browser)
- Peer review checkpoints (submit for human review)
- Adaptive difficulty (easier/harder based on performance)

---

### 7. Lesson Generation (JIT with Caching)

**Priority:** P0 (Critical)  
**Estimated Effort:** 2 weeks

**Features:**
- [ ] Content library search (find matching cached lessons)
- [ ] Matching algorithm:
  - Exact match (topic + skill + learning style) → Use cached
  - Partial match (topic + skill) → Adapt for learning style
  - No match → Generate new lesson
- [ ] Lesson generation prompt (based on lesson metadata + user profile)
- [ ] Parse AI response (extract Markdown content + checkpoints)
- [ ] Save to content library (for future reuse)
- [ ] Personalization (insert user's name, custom examples)

**Caching Logic:**
- First user for topic → Generate ($0.02 cost)
- Subsequent users → Cached ($0.00 cost)
- Quality threshold: Only cache lessons rated 4+ stars

**Out of Scope:**
- Community contributions (expert-created lessons)
- Lesson remixing (fork and modify)
- A/B testing (compare generated vs. human-written)

---

### 8. Progress Dashboard

**Priority:** P1 (High)  
**Estimated Effort:** 1 week

**Features:**
- [ ] Overall progress (% complete across curriculum)
- [ ] Phase progress (% complete per phase)
- [ ] Current lesson indicator ("You are here")
- [ ] Lessons completed count
- [ ] Total time invested
- [ ] Estimated time remaining
- [ ] Confidence trend chart (line chart over time)
- [ ] Next lesson button (jumps to next incomplete lesson)

**Out of Scope:**
- Skill gap analysis
- Learning velocity tracking
- Peer comparison (how you rank vs. others)
- Streak tracking (consecutive days)

---

### 9. Confidence Rating

**Priority:** P1 (High)  
**Estimated Effort:** 3 days

**Features:**
- [ ] Post-lesson confidence question (1-5 scale)
- [ ] Visual rating selector (emoji faces or star rating)
- [ ] Save rating to database
- [ ] Display average confidence in dashboard
- [ ] Adaptive curriculum suggestion (if confidence < 3, suggest review)

**Scale:**
- 1 = "I'm lost, need to redo this"
- 2 = "Struggled, barely understood"
- 3 = "Got the basics, need more practice"
- 4 = "Comfortable, ready to move on"
- 5 = "Mastered, could teach someone else"

**Out of Scope:**
- Skill-specific confidence (separate ratings per skill)
- Confidence prediction (AI estimates before lesson)

---

### 10. Payment Integration (Stripe)

**Priority:** P1 (High)  
**Estimated Effort:** 1 week

**Features:**
- [ ] Stripe account setup
- [ ] Payment form (credit card input)
- [ ] Subscription plans:
  - Free: 5 lessons/month
  - Pro: $20/month unlimited
- [ ] Payment processing (Stripe Checkout)
- [ ] Subscription management (upgrade, downgrade, cancel)
- [ ] Payment confirmation email
- [ ] Billing portal (view invoices, update payment method)

**Out of Scope:**
- Multiple payment methods (PayPal, crypto)
- Annual plans (discount for yearly)
- Team plans (bulk pricing)
- Refund handling (manual for MVP)

---

### 11. Content Library Management

**Priority:** P1 (High)  
**Estimated Effort:** 1 week

**Features:**
- [ ] Lesson storage (content_library table)
- [ ] Lesson matching algorithm (exact/partial)
- [ ] Lesson rating aggregation (average of user ratings)
- [ ] Quality threshold enforcement (only serve 4+ star lessons)
- [ ] Regeneration trigger (if rating drops below 3.0)
- [ ] Usage tracking (times_used counter)

**Out of Scope:**
- Manual curation (admin approves lessons)
- Version control (track lesson edits over time)
- Lesson analytics (which lessons convert best)

---

### 12. Basic Admin Panel

**Priority:** P2 (Medium)  
**Estimated Effort:** 1 week

**Features:**
- [ ] View all users
- [ ] View user curricula
- [ ] View lesson ratings
- [ ] Flag lessons for regeneration
- [ ] View payment history (Stripe dashboard link)

**Out of Scope:**
- User impersonation (login as user)
- Lesson editing (WYSIWYG editor)
- Analytics dashboard (charts, graphs)
- A/B test management

---

## Nice-to-Have Features (Post-MVP)

### 1. OAuth Login
- Google, GitHub, Microsoft SSO
- Reduces friction, improves signup conversion

### 2. Lesson Export
- Download lessons as Markdown, PDF, HTML
- Enables offline study, sharing

### 3. Community Ratings & Comments
- Users rate lessons (1-5 stars)
- Users leave comments (helpful feedback)
- Improves content quality over time

### 4. Mobile App (React Native)
- iOS and Android native apps
- Push notifications for lesson reminders
- Offline mode (download lessons)

### 5. Desktop App (Electron)
- Git integration (auto-commit on lesson complete)
- Local file storage (lessons as Markdown files)
- VS Code integration ("Open in editor" button)

### 6. Advanced Personalization
- Adaptive difficulty (adjust mid-lesson)
- Learning style detection (analyze user behavior)
- Spaced repetition (review old lessons)

### 7. Multi-Topic Support
- Python, Notion, Figma, Slack, etc.
- Topic switching (work on multiple curricula)
- Cross-topic skills (Excel + Python → data analysis)

---

## Out of Scope (Future Product)

### 1. User-Generated Content
- Expert contributors (create lessons)
- Lesson marketplace (buy/sell curricula)
- Revenue share (30% platform fee)

### 2. Team Features
- Team dashboard (manager view)
- Team progress tracking
- Team curriculum (shared learning paths)

### 3. White-Label Licensing
- Companies rebrand Doqtra as their LMS
- Custom domains, branding
- API access for integrations

### 4. AI Tutoring (Live Chat)
- Chatbot answers questions in real-time
- Integrated with lesson content
- Escalate to human tutor if needed

### 5. Certification Programs
- Accredited certifications (partner with universities)
- Proctored exams
- LinkedIn badge integration

---

## MVP Technical Stack Summary

### Frontend
- React 18 + TypeScript
- Zustand (state management)
- React Router v6
- shadcn/ui + Tailwind CSS
- TanStack Query (data fetching)
- marked.js (Markdown → HTML)
- Prism.js (syntax highlighting)

### Backend
- Python 3.11 + FastAPI
- SQLAlchemy 2.0 (ORM)
- PostgreSQL 15
- Redis 7 (caching)
- Anthropic Claude API
- Stripe API (payments)

### Infrastructure
- AWS ECS Fargate (containers)
- AWS RDS (PostgreSQL)
- AWS ElastiCache (Redis)
- CloudFront (CDN)
- GitHub Actions (CI/CD)

---

## Development Timeline (6 Weeks)

### Week 1: Foundation
- Set up repositories (frontend + backend)
- Configure databases (PostgreSQL + Redis)
- User authentication (signup, login, JWT)
- Learning profile questionnaire

### Week 2-3: Curriculum Engine
- Curriculum generation (Claude API integration)
- Curriculum preview UI
- Skip/add module interactions
- Database schema (curricula, phases, modules, lessons)

### Week 4-5: Lesson System
- Lesson generation (JIT with caching)
- Lesson rendering (Markdown → HTML)
- Checkpoint system (questions, feedback)
- Content library (matching algorithm)

### Week 6: Polish & Payments
- Progress dashboard
- Confidence rating
- Stripe integration (payments)
- Testing and bug fixes

### Week 7-8: Beta & Launch
- Beta testing (50 users)
- Bug fixes based on feedback
- Landing page (marketing)
- Launch publicly

---

## Success Metrics (MVP)

**Activation:**
- 80% of signups complete questionnaire
- 70% of questionnaires generate curriculum
- 60% of curricula result in starting Lesson 1

**Engagement:**
- 80% complete first 3 lessons
- Average session time: 30+ minutes
- 3+ lessons per week

**Retention:**
- Week 1: 85% retention
- Week 2: 70% retention
- Week 4: 50% retention

**Quality:**
- Average lesson rating: 4.0+ stars
- Average confidence: 3.5+ (out of 5)
- <5% flag lessons for regeneration

**Monetization:**
- 10% conversion free → Pro ($20/month)
- $500 MRR by end of Month 6
- Average LTV: $100+ (5 months retention)

---

## Risks & Mitigation

### Risk 1: AI generates poor-quality lessons
**Mitigation:**
- Manual review of first 20 lessons (Excel topic)
- Community ratings surface bad lessons
- Regenerate lessons with <3.0 rating

### Risk 2: Curriculum generation too slow (>30s)
**Mitigation:**
- Show loading animation with tips
- Cache curricula for common profiles
- Optimize prompts to reduce token count

### Risk 3: Users don't trust AI-generated content
**Mitigation:**
- Transparent sourcing (cite references)
- Preview curriculum before committing
- Human expert endorsements (testimonials)

### Risk 4: Low conversion to paid (free tier sufficient)
**Mitigation:**
- Limit free tier to 5 lessons (forces upgrade)
- Showcase Pro features (advanced topics, exports)
- Offer discount for annual plan

---

## Next Steps

### After Completing CatchBook P01-P03

**Month 4 (March 2026):**
1. Week 1: Set up dev environment, user auth
2. Week 2-3: Curriculum engine + preview UI
3. Week 4: Lesson generation + rendering

**Month 5 (April 2026):**
1. Week 1: Checkpoint system
2. Week 2: Progress dashboard + confidence rating
3. Week 3: Stripe payments
4. Week 4: Testing and bug fixes

**Month 6 (May 2026):**
1. Week 1-2: Beta testing (50 users)
2. Week 3: Marketing prep (landing page, content)
3. Week 4: Launch publicly

**Goal:** 100 users, $500 MRR, 4.0+ average rating by end of Month 6

---

**This is the blueprint. Execute one feature at a time.**
