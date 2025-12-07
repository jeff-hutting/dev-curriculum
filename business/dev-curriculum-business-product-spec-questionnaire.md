# Product Spec Questionnaire: Dev-Curriculum Business

**Purpose:** Define the business vision for monetizing the dev-curriculum system as a marketplace → B2B SaaS product.

**Status:** Draft for refinement

**Owner:** Jeff Hutting

**Date:** 2025-12-06

---

## Section 1: Core Product Vision

### 1.1 Problem Statement

**Question:** What specific problem does this product solve that no existing solution addresses?

**Prompt:**
- Who experiences this problem? (personas)
- What are they doing today? (current workarounds)
- What's the cost of not solving it? (pain quantification)
- Why hasn't this been solved yet? (market gap)

**Example Answer:**
> _"Developers struggle to maintain motivation during long learning journeys because tutorials are disconnected from real projects. They complete courses but have no portfolio to show. Current solutions (bootcamps, Udemy, freeCodeCamp) teach in isolation—students build toy apps that get abandoned. The cost: 6-12 months of effort with minimal employability improvement. This hasn't been solved because no one has integrated AI-assisted learning with real production codebases in a file-backed, Git-native system."_

**Your Answer:**
[Fill in]

---

### 1.2 Solution Statement

**Question:** In one sentence, what does this product do?

**Prompt:**
- What's the core mechanic? (the "magic")
- Who gets value? (target user)
- What's the outcome? (end state)

**Example Answer:**
> _"Dev-curriculum transforms any software project into a structured learning path where every lesson produces shippable code, ensuring developers build real portfolio projects while mastering full-stack skills."_

**Your Answer:**
[Fill in]

---

### 1.3 Unique Value Proposition

**Question:** Why would someone choose this over alternatives?

**Prompt:**
List 3-5 unique advantages:
- What can you do that competitors can't?
- What's 10x better than current solutions?
- What's your unfair advantage?

**Example Answer:**
> 1. _Only system that integrates learning with production codebases (not toy apps)_
> 2. _AI-native workflow with artifacts and role-based operation (10x faster iteration)_
> 3. _File-backed state eliminates vendor lock-in (Git is source of truth)_
> 4. _Real project spine ensures motivation (compound learning, not isolated lessons)_
> 5. _Just-in-time curriculum generation adapts to learner progress_

**Your Answer:**
1. [Fill in]
2. [Fill in]
3. [Fill in]
4. [Fill in]
5. [Fill in]

---

## Section 2: Target Market

### 2.1 Primary Customer Segments

**Question:** Who are the first customers you'll sell to?

**Prompt:**
For each segment, define:
- **Who:** Job title, company size, industry
- **Pain:** Specific problem they face
- **Value:** What they'll pay for
- **Channel:** How you'll reach them

**Example Segments:**

| Segment | Who | Pain | Value | Channel |
|---------|-----|------|-------|---------|
| **Self-taught developers** | Career changers, bootcamp grads, hobbyists | Lack of portfolio, tutorial hell, no direction | Structured path to real project, $299 one-time | Twitter/X, Dev.to, YouTube |
| **Tech startups (10-50 employees)** | Engineering managers, CTOs | Slow onboarding (6 months), no standardized learning | Faster ramp-up, $10K/year | Cold outreach, YC network, founder communities |
| **Bootcamps/universities** | Curriculum directors, instructors | Outdated curriculum, poor job placement | Modern pedagogy, better outcomes, $50K/year | LinkedIn, conference sponsorships, academic partnerships |

**Your Segments:**

| Segment | Who | Pain | Value | Channel |
|---------|-----|------|-------|---------|
| [Name] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |
| [Name] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |
| [Name] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |

---

### 2.2 Ideal Customer Profile (ICP)

**Question:** If you could only serve ONE customer type, who would it be?

**Prompt:**
Describe in detail:
- Demographics (age, location, education, experience level)
- Psychographics (goals, fears, values, learning style)
- Behaviors (how they learn today, tools they use, communities they're in)
- Budget (what they've spent on learning before, willingness to pay)

**Your Answer:**
[Fill in detailed ICP description]

---

### 2.3 Market Size

**Question:** How big is the opportunity?

**Prompt:**
Estimate:
- **TAM (Total Addressable Market):** All potential customers globally
- **SAM (Serviceable Addressable Market):** Customers you can realistically reach
- **SOM (Serviceable Obtainable Market):** Customers you can capture in 3 years

**Example:**
> _TAM: 27 million professional developers globally (Stack Overflow 2024) × $500 avg spend = $13.5B_
> _SAM: 2 million self-taught/bootcamp devs actively learning × $300 = $600M_
> _SOM: 10,000 users in 3 years × $300 = $3M_

**Your Estimates:**
- TAM: [Fill in]
- SAM: [Fill in]
- SOM: [Fill in]

---

## Section 3: Product Features

### 3.1 MVP Feature List (Marketplace Launch)

**Question:** What's the minimum feature set to launch the marketplace?

**Prompt:**
List features required for first paid customer:
- Must-have (deal-breaker if missing)
- Should-have (strong differentiator)
- Could-have (nice-to-have)

**Example MVP:**

**Must-Have:**
- [ ] Template packaging system (ZIP with curriculum files, schemas, role definitions)
- [ ] Product spec questionnaire (generates custom `project-spec.md`)
- [ ] Curriculum generation from questionnaire (outputs `curriculum.csv`)
- [ ] Payment processing (Stripe checkout)
- [ ] Download delivery (email with secure link)
- [ ] Basic documentation (setup guide, quickstart)

**Should-Have:**
- [ ] Template preview (screenshots, video walkthrough)
- [ ] Customization wizard (name your project, choose tech stack)
- [ ] Example projects gallery (3-5 templates: SaaS, mobile, ML)

**Could-Have:**
- [ ] Community forum (Discord)
- [ ] Video tutorials (YouTube playlist)
- [ ] Template ratings/reviews

**Your MVP Features:**

**Must-Have:**
- [ ] [Fill in]
- [ ] [Fill in]
- [ ] [Fill in]

**Should-Have:**
- [ ] [Fill in]
- [ ] [Fill in]

**Could-Have:**
- [ ] [Fill in]
- [ ] [Fill in]

---

### 3.2 V2 Feature List (B2B SaaS Transition)

**Question:** What features unlock B2B enterprise sales?

**Prompt:**
Features that enable $50K-200K contracts:

**Example V2:**
- [ ] Multi-tenant architecture (one instance per company)
- [ ] Admin dashboard (track learner progress, export reports)
- [ ] Team management (invite users, assign roles, permissions)
- [ ] SSO/SAML authentication (Okta, Azure AD)
- [ ] Custom curriculum authoring UI (non-technical curriculum designers)
- [ ] Integration APIs (Slack, Jira, Linear, Notion)
- [ ] White-labeling (remove dev-curriculum branding, apply company logo)
- [ ] SLA-backed support (priority bug fixes, dedicated CSM)
- [ ] Audit logs (compliance for SOC 2, GDPR)

**Your V2 Features:**
- [ ] [Fill in]
- [ ] [Fill in]
- [ ] [Fill in]

---

### 3.3 Product Roadmap (3-Year Vision)

**Question:** What does the product look like in 3 years?

**Prompt:**
Break down by timeline:
- **Year 1:** Marketplace MVP → 1,000 users
- **Year 2:** B2B SaaS → 10 enterprise clients
- **Year 3:** Platform ecosystem → third-party integrations, API marketplace

**Example Roadmap:**

**Year 1 (Months 1-12):**
- Q1: Launch marketplace, 3 templates (SaaS, mobile, ML)
- Q2: 100 paid users, launch community forum
- Q3: 500 users, YouTube series (50K subs)
- Q4: 1,000 users, $30K MRR, pilot B2B with 3 companies

**Year 2 (Months 13-24):**
- Q1: B2B SaaS beta, close 5 enterprise deals ($250K ARR)
- Q2: Multi-tenant platform, admin dashboard, SSO
- Q3: 10 enterprise clients ($500K ARR), hire sales rep
- Q4: 20 enterprise clients ($1M ARR), white-label launched

**Year 3 (Months 25-36):**
- Q1: API marketplace (third-party templates, integrations)
- Q2: 50 enterprise clients ($2M ARR), Series A fundraising
- Q3: International expansion (EU, APAC)
- Q4: 100 enterprise clients ($5M ARR), CurriculumCon conference

**Your Roadmap:**

**Year 1:**
- Q1: [Fill in]
- Q2: [Fill in]
- Q3: [Fill in]
- Q4: [Fill in]

**Year 2:**
- [Fill in]

**Year 3:**
- [Fill in]

---

## Section 4: Business Model

### 4.1 Revenue Streams

**Question:** How will you make money?

**Prompt:**
For each revenue stream, define:
- **What:** Product or service sold
- **Who:** Customer type
- **Price:** Amount charged
- **Frequency:** One-time, monthly, annual

**Example Revenue Streams:**

| Stream | What | Who | Price | Frequency | Year 1 Revenue |
|--------|------|-----|-------|-----------|----------------|
| **Template sales** | Pre-built curriculum templates | Individual devs | $49-299 | One-time | $150K |
| **Marketplace subscription** | Unlimited template access | Individual devs | $19/month | Monthly | $50K |
| **Pro subscription** | Custom curriculum generation | Power users | $99/month | Monthly | $30K |
| **Enterprise SaaS** | Multi-tenant platform | Companies | $50K-200K/year | Annual | $250K (pilot) |
| **Implementation services** | Custom curriculum design | Enterprises | $10K-50K | One-time | $50K |

**Total Year 1 Revenue:** $530K

**Your Revenue Streams:**

| Stream | What | Who | Price | Frequency | Year 1 Revenue |
|--------|------|-----|-------|-----------|----------------|
| [Name] | [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |
| [Name] | [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |
| [Name] | [Fill in] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |

---

### 4.2 Pricing Strategy

**Question:** How did you arrive at these prices?

**Prompt:**
For each price point, justify:
- **Competitor pricing:** What do alternatives charge?
- **Value-based pricing:** What's the ROI for customer?
- **Willingness to pay:** What have customers paid historically?
- **Cost structure:** What are your costs to deliver?

**Example Justification (Template Sales at $299):**
> _Competitor pricing: Udemy courses = $50-200, bootcamp curricula = $0 (don't sell standalone). Value-based: If template saves 20 hours of curriculum design at $100/hr = $2,000 value. Willingness to pay: Notion templates sell for $50-500, Figma templates $100-300. Cost to deliver: $0 marginal cost (digital download). Conclusion: $299 is anchored to high-value templates, justified by time savings._

**Your Pricing Justifications:**

**[Product/Service Name]:**
- Competitor pricing: [Fill in]
- Value-based pricing: [Fill in]
- Willingness to pay: [Fill in]
- Cost structure: [Fill in]
- **Conclusion:** [Fill in final price + rationale]

**[Repeat for each revenue stream]**

---

### 4.3 Unit Economics

**Question:** Is each sale profitable?

**Prompt:**
Calculate for each customer segment:
- **CAC (Customer Acquisition Cost):** Marketing + sales cost per customer
- **LTV (Lifetime Value):** Total revenue per customer over lifetime
- **LTV:CAC Ratio:** Target 3:1 or higher
- **Payback Period:** Months to recover CAC

**Example Unit Economics:**

| Segment | CAC | LTV | LTV:CAC | Payback Period |
|---------|-----|-----|---------|----------------|
| **Marketplace users** | $50 (ads, content) | $300 (avg purchase) | 6:1 | 1 month |
| **Pro subscribers** | $200 (content marketing) | $1,188 (avg 12 months) | 5.9:1 | 2 months |
| **Enterprise** | $15,000 (sales + demos) | $150,000 (avg 3-year contract) | 10:1 | 12 months |

**Your Unit Economics:**

| Segment | CAC | LTV | LTV:CAC | Payback Period |
|---------|-----|-----|---------|----------------|
| [Name] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |
| [Name] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |

---

### 4.4 Financial Projections (3-Year)

**Question:** What does revenue growth look like?

**Prompt:**
Project:
- Revenue by segment
- Operating expenses (salaries, tools, marketing)
- Net income (revenue - expenses)
- Headcount growth

**Example Projections:**

| Year | Marketplace Revenue | B2B Revenue | Total Revenue | Operating Expenses | Net Income | Headcount |
|------|---------------------|-------------|---------------|--------------------| -----------|-----------|
| 1    | $230K               | $250K       | $480K         | $300K              | $180K      | 2 (you + 1 hire) |
| 2    | $500K               | $1M         | $1.5M         | $800K              | $700K      | 6 (sales, eng, support) |
| 3    | $1M                 | $4M         | $5M           | $2.5M              | $2.5M      | 20 (full teams) |

**Your Projections:**

| Year | Marketplace Revenue | B2B Revenue | Total Revenue | Operating Expenses | Net Income | Headcount |
|------|---------------------|-------------|---------------|--------------------| -----------|-----------|
| 1    | [Fill in]           | [Fill in]   | [Fill in]     | [Fill in]          | [Fill in]  | [Fill in] |
| 2    | [Fill in]           | [Fill in]   | [Fill in]     | [Fill in]          | [Fill in]  | [Fill in] |
| 3    | [Fill in]           | [Fill in]   | [Fill in]     | [Fill in]          | [Fill in]  | [Fill in] |

---

## Section 5: Go-To-Market Strategy

### 5.1 Customer Acquisition Channels

**Question:** How will you get your first 100 customers?

**Prompt:**
For each channel, define:
- **Tactic:** Specific action you'll take
- **Timeline:** When you'll execute
- **Budget:** Cost to execute
- **Expected Result:** Customers acquired

**Example Channels:**

| Channel | Tactic | Timeline | Budget | Expected Result |
|---------|--------|----------|--------|-----------------|
| **Content Marketing** | Publish 50 blog posts on Dev.to, Medium, personal site (SEO-optimized) | Months 1-6 | $0 (your time) | 500 email subs, 50 sales |
| **YouTube** | Record 20 videos: "Build X from Scratch" series | Months 3-9 | $1K (equipment) | 10K subs, 100 sales |
| **Twitter/X** | Daily threads on learning strategies, build in public | Months 1-12 | $0 | 5K followers, 30 sales |
| **Product Hunt** | Launch day campaign | Month 6 | $500 (upvotes) | 2K visitors, 50 sales |
| **Reddit** | Answer questions in r/learnprogramming, r/webdev | Months 1-12 | $0 | 1K visitors, 20 sales |
| **Cold Outreach (B2B)** | Email 200 CTOs/VPs of Eng at YC companies | Months 6-9 | $500 (email tools) | 20 demos, 3 pilots |

**Total Year 1 Customer Acquisition:** 253 customers (B2C) + 3 pilots (B2B)

**Your Channels:**

| Channel | Tactic | Timeline | Budget | Expected Result |
|---------|--------|----------|--------|-----------------|
| [Name] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |
| [Name] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |
| [Name] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |

---

### 5.2 Content Marketing Strategy

**Question:** What content will you create to drive awareness?

**Prompt:**
Plan content themes:
- **Educational:** Teach concepts (how to build, best practices)
- **Inspirational:** Success stories, case studies
- **Tactical:** Tools, templates, checklists

**Example Content Calendar (Year 1):**

**Blog Posts (50 total):**
- "Why Traditional Coding Tutorials Fail (And What to Do Instead)"
- "How to Build a Full-Stack App in 850 Hours"
- "The CatchBook Curriculum: A Case Study in Project-Based Learning"
- "Git-Native Learning: Why File-Backed State Beats LMS Platforms"
- [... 46 more titles]

**YouTube Videos (20 total):**
- Episode 1: "I'm Building a Fishing App to Learn Full-Stack Development"
- Episode 2: "Git Fundamentals: Setting Up CatchBook Repository"
- Episode 5: "React + TypeScript: Building CatchBook's UI"
- Episode 10: "FastAPI Backend: CatchBook's REST API"
- [... 16 more episodes]

**Twitter Threads (100 total):**
- "10 lessons I learned building CatchBook from scratch"
- "How to stay motivated during long learning journeys"
- "The ultimate Git workflow for solo developers"
- [... 97 more threads]

**Your Content Plan:**
[Fill in specific titles, themes, and quantities]

---

### 5.3 Partnership Strategy

**Question:** Who can help you reach customers faster?

**Prompt:**
Identify potential partners:
- **Distribution partners:** Who has your audience? (bootcamps, YouTubers, communities)
- **Technology partners:** What tools integrate with yours? (GitHub, Notion, Linear)
- **Affiliate partners:** Who will promote for commission?

**Example Partnerships:**

| Partner Type | Partner Name | Value Proposition | Terms |
|--------------|--------------|-------------------|-------|
| **Bootcamp** | Lambda School, Hack Reactor | Offer dev-curriculum as alumni resource | 20% revenue share |
| **YouTuber** | Fireship, Web Dev Simplified | Sponsored video on dev-curriculum | $5K sponsorship |
| **Community** | Dev.to, Hashnode | Featured article placement | Cross-promotion |
| **Tool Integration** | Notion, Linear, Jira | Two-way integration (curriculum ↔ project management) | Joint marketing |

**Your Partnerships:**

| Partner Type | Partner Name | Value Proposition | Terms |
|--------------|--------------|-------------------|-------|
| [Type] | [Name] | [Fill in] | [Fill in] |
| [Type] | [Name] | [Fill in] | [Fill in] |

---

## Section 6: Competitive Analysis

### 6.1 Direct Competitors

**Question:** Who else is solving this problem?

**Prompt:**
List competitors and compare:
- **Name:** Product name
- **Approach:** How they solve the problem
- **Strengths:** What they do well
- **Weaknesses:** Where they fall short
- **Pricing:** What they charge

**Example Competitor Analysis:**

| Competitor | Approach | Strengths | Weaknesses | Pricing |
|------------|----------|-----------|------------|---------|
| **freeCodeCamp** | Free curriculum, toy projects | Massive community, free, structured | Generic projects, no real production code | $0 |
| **Codecademy Pro** | Interactive browser-based coding | Instant feedback, beginner-friendly | Toy projects, no portfolio value | $20/month |
| **Lambda School (now Bloom Institute)** | Full-time bootcamp, ISA model | Job placement focus, mentorship | $30K cost (ISA), generic curriculum, not customizable | ISA (18% salary for 2 years) |
| **Udemy** | Course marketplace | Affordable, variety | No integration, passive learning, toy projects | $50-200/course |

**Your Competitive Analysis:**

| Competitor | Approach | Strengths | Weaknesses | Pricing |
|------------|----------|-----------|------------|---------|
| [Name] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |
| [Name] | [Fill in] | [Fill in] | [Fill in] | [Fill in] |

---

### 6.2 Competitive Advantages

**Question:** Why will customers choose you over competitors?

**Prompt:**
List 5+ unique advantages:
- What do you do that they can't?
- What's 10x better?
- What's your moat? (defensibility)

**Example Advantages:**
1. _Only system that integrates learning with real production codebases (not toy apps)_
2. _AI-native workflow with artifacts and role-based operation (10x faster iteration)_
3. _File-backed state eliminates vendor lock-in (Git is source of truth)_
4. _Customizable curriculum for ANY project (not just generic web apps)_
5. _Just-in-time generation adapts to learner progress (personalized learning)_
6. _Open source core (trust, community, extensibility)_
7. _First-mover advantage in AI-assisted, project-based learning_

**Your Advantages:**
1. [Fill in]
2. [Fill in]
3. [Fill in]
4. [Fill in]
5. [Fill in]

---

### 6.3 Positioning Statement

**Question:** In one paragraph, how do you position against competitors?

**Prompt:**
Format: "For [target customer], who [need/pain], [product name] is a [category] that [unique benefit]. Unlike [competitors], [product name] [key differentiator]."

**Example:**
> _"For self-taught developers and tech teams who struggle with generic tutorials and slow onboarding, dev-curriculum is an AI-assisted learning platform that transforms any software project into a structured curriculum where every lesson produces shippable code. Unlike Udemy, Codecademy, and bootcamps that use toy projects, dev-curriculum integrates learning directly with production codebases, ensuring learners build real portfolio projects and teams onboard engineers 3x faster."_

**Your Positioning:**
[Fill in]

---

## Section 7: Product Customization System

### 7.1 Customization Questionnaire Design

**Question:** What questions will you ask users to generate their custom curriculum?

**Prompt:**
Design a questionnaire with 3 sections:
1. **Project Details:** What are they building?
2. **Learning Style:** How do they learn best?
3. **Technical Preferences:** What tech stack, tools, constraints?

**Example Questionnaire:**

**Section 1: Project Details**
1. What's your project name? (text input)
2. What problem does it solve? (textarea, 2-3 sentences)
3. Who are your users? (text input)
4. What are the 3 core features? (3 text inputs)
5. What's your target launch date? (date picker)
6. What's your time commitment? (dropdown: 5-10 hrs/week, 10-20 hrs/week, 20+ hrs/week)

**Section 2: Learning Style**
7. How do you learn best? (multiple choice: visual, hands-on, reading, videos, mix)
8. What's your prior experience? (checkboxes: HTML/CSS, JavaScript, Python, Git, databases, APIs)
9. What's your confidence level with code? (slider: 1-10)
10. Do you prefer detailed explanations or quick tutorials? (multiple choice)
11. How do you track progress? (checkboxes: notes, journals, checklists, none)

**Section 3: Technical Preferences**
12. Frontend framework? (dropdown: React, Vue, Svelte, vanilla JS, other)
13. Backend language? (dropdown: Python, Node.js, Go, Ruby, Java, other)
14. Database? (dropdown: PostgreSQL, MySQL, MongoDB, SQLite, other)
15. Deployment platform? (dropdown: Vercel, Netlify, AWS, Heroku, DigitalOcean, other)
16. Mobile app? (yes/no, if yes: React Native, SwiftUI, Flutter)
17. AI integration? (yes/no, if yes: OpenAI, Anthropic, open source models)

**Your Questionnaire:**
[Fill in your questions, organized by section]

---

### 7.2 Curriculum Generation Logic

**Question:** How will you translate questionnaire answers into a curriculum?

**Prompt:**
Define rules:
- **If X, then Y:** Conditional logic (e.g., "If frontend = React, generate React modules")
- **Skill dependencies:** Prerequisite chains (e.g., "Git before branching")
- **Time allocation:** Hours per module based on time commitment
- **Feature mapping:** How project features map to modules

**Example Logic:**

**Rule 1: Frontend Framework Selection**
- If `frontend = React` → Generate modules: "React Basics", "React Hooks", "React Router", "React + TypeScript"
- If `frontend = Vue` → Generate modules: "Vue Basics", "Vue Composition API", "Vue Router", "Pinia State Management"
- If `frontend = Svelte` → Generate modules: "Svelte Basics", "Svelte Stores", "SvelteKit Routing"

**Rule 2: Backend Language Selection**
- If `backend = Python` → Generate modules: "Python Fundamentals", "FastAPI", "SQLAlchemy", "Pydantic Validation"
- If `backend = Node.js` → Generate modules: "Node Fundamentals", "Express", "TypeORM", "Zod Validation"

**Rule 3: Time Commitment Pacing**
- If `time_commitment = 5-10 hrs/week` → Allocate 6-8 hours per module (12-16 weeks per phase)
- If `time_commitment = 10-20 hrs/week` → Allocate 10-16 hours per module (6-10 weeks per phase)
- If `time_commitment = 20+ hrs/week` → Allocate 20-30 hours per module (3-5 weeks per phase)

**Rule 4: Feature-to-Module Mapping**
- If `core_feature_1 = "User authentication"` → Generate modules: "Password Hashing", "JWT Tokens", "OAuth 2.0", "Session Management"
- If `core_feature_2 = "Photo uploads"` → Generate modules: "File Uploads", "Image Processing", "Cloud Storage", "CDN Integration"

**Your Generation Logic:**
[Fill in your conditional rules and mappings]

---

### 7.3 Output Artifacts

**Question:** What files will be generated for each custom curriculum?

**Prompt:**
List all output files:
- Product spec (Markdown)
- Curriculum overview (CSV)
- Phase files (JSON)
- Module files (JSON)
- Lesson files (JSON)
- State templates (JSON)
- README (Markdown)
- Other?

**Example Output:**

**Generated Files for "PetTracker" Project:**
```
pet-tracker-curriculum/
├── projects/
│   └── pet-tracker-product-spec.md       # Auto-generated from questionnaire
├── curriculum/
│   ├── curriculum.json                    # Top-level design
│   ├── pet-tracker-curriculum-v1.csv      # Master curriculum
│   ├── phases/
│   │   ├── P01.json                       # Phase 1: Foundations
│   │   ├── P02.json                       # Phase 2: React Fundamentals
│   │   └── ...
│   ├── modules/
│   │   ├── P01-M01.json                   # Module: Git basics
│   │   └── ...
│   └── lessons/
│       └── (generated just-in-time)
├── learner-state/
│   ├── current.json                       # Initial state
│   ├── skills.json                        # Initial skill levels
│   └── metrics.json                       # Starting metrics
├── schemas/                               # Standard schemas (unchanged)
├── roles/                                 # Standard roles (unchanged)
├── templates/                             # Standard templates (unchanged)
├── README.md                              # Customized for PetTracker
└── quickstart.md                          # Customized for PetTracker
```

**Your Output Structure:**
[Fill in your file structure and customization approach]

---

## Section 8: Success Metrics

### 8.1 Product Metrics (What to Track)

**Question:** How will you measure product success?

**Prompt:**
Define metrics for:
- **Acquisition:** How many people discover the product?
- **Activation:** How many complete onboarding?
- **Engagement:** How often do they use it?
- **Retention:** How many stick around?
- **Revenue:** How much do they pay?
- **Referral:** How many refer others?

**Example Metrics:**

| Metric | Definition | Target (Year 1) |
|--------|------------|-----------------|
| **Website visitors** | Unique visitors to landing page | 50K/month |
| **Email signups** | Newsletter subscribers | 10K total |
| **Template purchases** | Paid conversions | 1K customers |
| **Conversion rate** | Purchases / visitors | 2% |
| **NPS (Net Promoter Score)** | Customer satisfaction | 50+ |
| **Churn rate** | Subscribers who cancel | <5%/month |
| **LTV (Lifetime Value)** | Avg revenue per customer | $300 |
| **CAC (Customer Acquisition Cost)** | Marketing cost / customer | $50 |

**Your Metrics:**

| Metric | Definition | Target (Year 1) |
|--------|------------|-----------------|
| [Name] | [Fill in] | [Fill in] |
| [Name] | [Fill in] | [Fill in] |
| [Name] | [Fill in] | [Fill in] |

---

### 8.2 Learning Outcome Metrics

**Question:** How will you measure if learners are succeeding?

**Prompt:**
Define metrics for learner success:
- **Completion rate:** % of learners who finish curriculum
- **Time to completion:** Avg days to finish
- **Confidence improvement:** Before/after self-assessment
- **Job placement:** % who get hired (if applicable)
- **Project completion:** % who ship their real project

**Example Learner Metrics:**

| Metric | Definition | Target (Year 1) |
|--------|------------|-----------------|
| **Lesson completion rate** | % of started lessons completed | 70% |
| **Module completion rate** | % of started modules completed | 60% |
| **Full curriculum completion rate** | % who finish all phases | 30% |
| **Avg time to first commit** | Days from start to first Git commit | <7 days |
| **Project shipping rate** | % who deploy their project live | 50% |
| **Confidence improvement** | Avg rating increase (1-5 scale) | +2 points |

**Your Learner Metrics:**

| Metric | Definition | Target (Year 1) |
|--------|------------|-----------------|
| [Name] | [Fill in] | [Fill in] |
| [Name] | [Fill in] | [Fill in] |

---

## Section 9: Risks & Mitigation

### 9.1 Key Risks

**Question:** What could go wrong?

**Prompt:**
Identify risks in:
- **Market risk:** What if customers don't want this?
- **Technical risk:** What if it's too hard to build?
- **Competition risk:** What if someone copies you?
- **Execution risk:** What if you can't deliver?
- **Financial risk:** What if you run out of money?

**Example Risks:**

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| **Low initial demand** (customers don't buy) | Medium | High | Pre-sell templates before building, validate with 50 customer interviews |
| **AI changes break workflow** (Claude updates break artifacts) | Low | Medium | Abstract AI layer, support multiple LLMs (GPT-4, Gemini), maintain fallback to manual |
| **Competitor launches similar product** | Low | Medium | Speed to market, build community moat, patent key innovations |
| **Can't scale to B2B** (enterprise sales too complex) | Medium | High | Hire experienced enterprise sales rep in Year 2, partner with established platforms |
| **Burn rate too high** (run out of cash) | Low | High | Bootstrap Year 1, raise pre-seed ($500K) in Year 2 only if traction proven |

**Your Risks:**

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| [Name] | [Low/Med/High] | [Low/Med/High] | [Fill in] |
| [Name] | [Low/Med/High] | [Low/Med/High] | [Fill in] |
| [Name] | [Low/Med/High] | [Low/Med/High] | [Fill in] |

---

## Section 10: Next Actions

### 10.1 Validation Experiments (Before Building)

**Question:** What's the cheapest way to validate this idea?

**Prompt:**
Design 3 experiments to test key assumptions:
- **Assumption 1:** People want this (demand validation)
- **Assumption 2:** People will pay this price (pricing validation)
- **Assumption 3:** You can deliver this (technical validation)

**Example Experiments:**

**Experiment 1: Landing Page Pre-Sale**
- **Goal:** Validate demand + pricing
- **Hypothesis:** 50 people will pay $299 for a CatchBook-style template
- **Method:** Build landing page, run $500 Google Ads, offer pre-order discount ($199 early bird)
- **Success Criteria:** 10+ pre-orders in 2 weeks
- **Timeline:** 2 weeks
- **Budget:** $500 ads + $100 landing page

**Experiment 2: Manual Curriculum Generation**
- **Goal:** Validate technical feasibility
- **Hypothesis:** You can generate custom curriculum in <2 hours per project
- **Method:** Find 5 developers on Twitter/X, offer free custom curriculum in exchange for feedback
- **Success Criteria:** Generate 5 curricula, avg <2 hours each, 4/5 say "I'd pay for this"
- **Timeline:** 2 weeks
- **Budget:** $0 (your time)

**Experiment 3: YouTube Proof-of-Concept**
- **Goal:** Validate content distribution channel
- **Hypothesis:** Building in public attracts audience
- **Method:** Record 3 videos: "I'm Building a Curriculum System", "How It Works", "Generate Your Own Curriculum"
- **Success Criteria:** 1K views, 100 email subs, 5 comments asking "When can I buy this?"
- **Timeline:** 3 weeks
- **Budget:** $0 (your time)

**Your Validation Experiments:**

**Experiment 1:**
- Goal: [Fill in]
- Hypothesis: [Fill in]
- Method: [Fill in]
- Success Criteria: [Fill in]
- Timeline: [Fill in]
- Budget: [Fill in]

**Experiment 2:**
[Fill in]

**Experiment 3:**
[Fill in]

---

### 10.2 Immediate Next Steps (This Month)

**Question:** What should you do in the next 30 days?

**Prompt:**
Prioritize 5-10 actions:
- High-impact, low-effort tasks
- De-risking critical assumptions
- Building momentum

**Example Next Steps:**

**Week 1 (Days 1-7):**
- [ ] Refine product spec questionnaire (this document)
- [ ] Design landing page wireframe (Figma or pen+paper)
- [ ] Write 3 blog post drafts (Dev.to, Medium)
- [ ] Set up Twitter/X account, post daily threads

**Week 2 (Days 8-14):**
- [ ] Build landing page (Webflow, Carrd, or custom HTML)
- [ ] Launch landing page with pre-order (Gumroad checkout)
- [ ] Run $500 Google Ads campaign
- [ ] Publish first blog post

**Week 3 (Days 15-21):**
- [ ] Record first YouTube video (proof-of-concept)
- [ ] Conduct 10 customer interviews (validate demand)
- [ ] Generate 2 manual curricula (test feasibility)
- [ ] Publish second blog post

**Week 4 (Days 22-30):**
- [ ] Analyze pre-order results (did 10+ people buy?)
- [ ] Decide: Proceed with MVP or pivot?
- [ ] If proceed: Start building template packaging system
- [ ] If pivot: Adjust positioning, re-test

**Your Next Steps:**

**Week 1:**
- [ ] [Fill in]
- [ ] [Fill in]
- [ ] [Fill in]

**Week 2:**
- [ ] [Fill in]
- [ ] [Fill in]

**Week 3:**
- [ ] [Fill in]
- [ ] [Fill in]

**Week 4:**
- [ ] [Fill in]
- [ ] [Fill in]

---

## Section 11: Open Questions

### 11.1 Unresolved Questions

**Question:** What don't you know yet?

**Prompt:**
List questions that need answers before proceeding:
- **Customer questions:** What do they actually want?
- **Technical questions:** How will you build this?
- **Business questions:** What's the best model?
- **Operational questions:** How will you scale?

**Example Open Questions:**

1. **Customer:** Do B2B customers prefer SaaS or managed service? (Impacts build vs. buy decision)
2. **Technical:** Should curriculum generation be AI-native (Claude API) or rule-based? (Impacts cost structure)
3. **Business:** Should templates be one-time purchase or subscription? (Impacts LTV)
4. **Operational:** Should you hire sales rep in Year 1 or Year 2? (Impacts cash flow)
5. **Market:** Is there demand for templates beyond web apps (ML pipelines, mobile apps, blockchain)? (Impacts template roadmap)
6. **Legal:** Do you need to patent the curriculum generation system? (Impacts IP protection)
7. **Partnership:** Should you partner with bootcamps or compete? (Impacts distribution strategy)

**Your Open Questions:**
1. [Fill in]
2. [Fill in]
3. [Fill in]
4. [Fill in]
5. [Fill in]

---

## Section 12: Decision Log

### 12.1 Key Decisions Made

**Question:** What have you decided definitively?

**Prompt:**
Document decisions with rationale:
- **Decision:** What was decided
- **Rationale:** Why
- **Date:** When
- **Owner:** Who decided

**Example Decisions:**

| Decision | Rationale | Date | Owner |
|----------|-----------|------|-------|
| **Start with marketplace, not B2B SaaS** | Lower build effort, faster validation, test product-market fit before enterprise sales | 2025-12-06 | Jeff |
| **CatchBook stays private, use generic example publicly** | Protect IP, mitigate risk of idea theft, allow public curriculum teaching | 2025-12-06 | Jeff |
| **Focus on customization as unique feature** | Competitors offer generic curricula, customization is true differentiation | 2025-12-06 | Jeff |
| **Target self-taught devs first, then B2B** | Faster sales cycle, lower CAC, build community before enterprise sales | 2025-12-06 | Jeff |

**Your Decisions:**

| Decision | Rationale | Date | Owner |
|----------|-----------|------|-------|
| [Fill in] | [Fill in] | [Fill in] | [Fill in] |
| [Fill in] | [Fill in] | [Fill in] | [Fill in] |

---

## Conclusion

This questionnaire serves as your product spec foundation. Fill in all sections, iterate based on customer feedback, and update regularly as you learn.

**Next Steps:**
1. Complete all [Fill in] sections
2. Conduct 10 customer interviews to validate assumptions
3. Run validation experiments (landing page, manual curriculum generation)
4. Decide: Proceed with MVP or pivot?
5. If proceed: Build marketplace MVP (template packaging, payment, delivery)

**Remember:**
- Execution > Ideas (protect CatchBook, but move fast on dev-curriculum)
- Validation > Building (pre-sell before building)
- Iteration > Perfection (launch imperfect, improve based on feedback)

**Status:** Draft — Requires completion by Jeff

**Owner:** Jeff Hutting

**Last Updated:** 2025-12-06

---

**End of Product Spec Questionnaire**
