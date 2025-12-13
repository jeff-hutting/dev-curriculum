# Doqtra Technical Architecture

**Last Updated:** December 13, 2025

---

## System Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────┐
│              Doqtra Frontend (React)            │
│  - Web App (Progressive Web App)                │
│  - Desktop App (Electron) [Phase 2]             │
│  - Mobile App (React Native) [Phase 3]          │
└─────────────────────────────────────────────────┘
                      ↕ HTTPS/WebSocket
┌─────────────────────────────────────────────────┐
│           Doqtra Backend (FastAPI)              │
│  - REST API endpoints                           │
│  - Authentication (JWT)                         │
│  - Curriculum generation engine                 │
│  - Lesson rendering pipeline                    │
│  - Progress tracking                            │
└─────────────────────────────────────────────────┘
        ↕                   ↕                ↕
┌──────────────┐  ┌─────────────────┐  ┌──────────┐
│  PostgreSQL  │  │  Claude API     │  │  Redis   │
│  (Primary DB)│  │  (AI Generation)│  │  (Cache) │
└──────────────┘  └─────────────────┘  └──────────┘
```

---

## Frontend Architecture

### Technology Stack

**Framework:** React 18+ with TypeScript  
**State Management:** Zustand (lightweight alternative to Redux)  
**Routing:** React Router v6  
**UI Components:** shadcn/ui (Radix UI + Tailwind CSS)  
**Forms:** React Hook Form + Zod validation  
**Data Fetching:** TanStack Query (React Query)  
**Offline Storage:** IndexedDB via Dexie.js  

### Application Structure

```
doqtra-frontend/
├── src/
│   ├── app/                    # Application entry point
│   │   ├── App.tsx
│   │   ├── Router.tsx
│   │   └── providers/          # Context providers
│   ├── features/               # Feature-based organization
│   │   ├── auth/
│   │   │   ├── components/
│   │   │   ├── hooks/
│   │   │   ├── api/
│   │   │   └── store/
│   │   ├── curriculum/
│   │   │   ├── components/
│   │   │   │   ├── CurriculumPreview.tsx
│   │   │   │   ├── PhaseCard.tsx
│   │   │   │   ├── ModuleCard.tsx
│   │   │   │   └── LessonCard.tsx
│   │   │   ├── hooks/
│   │   │   ├── api/
│   │   │   └── store/
│   │   ├── lesson/
│   │   │   ├── components/
│   │   │   │   ├── LessonRenderer.tsx
│   │   │   │   ├── Checkpoint.tsx
│   │   │   │   └── ProgressBar.tsx
│   │   │   ├── hooks/
│   │   │   └── api/
│   │   ├── dashboard/
│   │   └── profile/
│   ├── components/             # Shared components
│   │   ├── ui/                 # shadcn/ui components
│   │   └── layout/
│   ├── lib/                    # Utilities and helpers
│   │   ├── api.ts
│   │   ├── markdown.ts
│   │   └── offline.ts
│   └── types/                  # TypeScript type definitions
└── public/
```

### Key Components

#### 1. CurriculumPreview Component

```typescript
interface CurriculumPreviewProps {
  curriculum: Curriculum;
  onModify: (updates: CurriculumUpdate) => void;
  onStart: () => void;
}

export function CurriculumPreview({ 
  curriculum, 
  onModify, 
  onStart 
}: CurriculumPreviewProps) {
  const [expandedPhases, setExpandedPhases] = useState<string[]>([]);
  
  const skipModule = (moduleId: string) => {
    onModify({ type: 'skip_module', moduleId });
  };
  
  const addModule = (topic: string, afterModuleId: string) => {
    onModify({ type: 'add_module', topic, afterModuleId });
  };
  
  return (
    <div className="curriculum-preview">
      <CurriculumSummary 
        totalWeeks={curriculum.totalWeeks}
        totalLessons={curriculum.totalLessons}
        totalHours={curriculum.totalHours}
      />
      
      {curriculum.phases.map(phase => (
        <PhaseCard
          key={phase.id}
          phase={phase}
          isExpanded={expandedPhases.includes(phase.id)}
          onToggle={() => togglePhase(phase.id)}
          onSkipModule={skipModule}
          onAddModule={addModule}
        />
      ))}
      
      <CurriculumActions
        onRegenerate={() => {/* regenerate with new params */}}
        onSaveVariant={() => {/* save as alternate curriculum */}}
        onStart={onStart}
      />
    </div>
  );
}
```

#### 2. LessonRenderer Component

**Critical:** Displays lessons in native HTML/CSS format, not raw Markdown

```typescript
interface LessonRendererProps {
  lessonId: string;
  onComplete: (confidence: number) => void;
}

export function LessonRenderer({ lessonId, onComplete }: LessonRendererProps) {
  const { data: lesson, isLoading } = useLesson(lessonId);
  const [currentCheckpoint, setCurrentCheckpoint] = useState(0);
  
  // Markdown to HTML conversion happens here
  const htmlContent = useMemo(() => {
    if (!lesson) return '';
    return markdownToHtml(lesson.content, {
      syntax highlighting: true,
      tables: true,
      images: true,
      codeBlocks: true
    });
  }, [lesson]);
  
  return (
    <div className="lesson-renderer">
      {/* Native HTML/CSS rendering */}
      <div 
        className="lesson-content prose prose-lg"
        dangerouslySetInnerHTML={{ __html: htmlContent }}
      />
      
      {/* Interactive checkpoints */}
      {lesson.checkpoints[currentCheckpoint] && (
        <Checkpoint
          checkpoint={lesson.checkpoints[currentCheckpoint]}
          onAnswer={(answer) => handleCheckpointAnswer(answer)}
        />
      )}
      
      {/* Progress indicator */}
      <ProgressBar 
        current={currentCheckpoint} 
        total={lesson.checkpoints.length} 
      />
    </div>
  );
}
```

### Lesson Display Format

**Generation → Storage → Display Pipeline:**

```
1. AI generates lesson (Markdown format)
   └─ Easy for Claude to generate structured text
   └─ Stored in database as Markdown string

2. Backend serves lesson (JSON with Markdown content)
   └─ { id: "...", content: "# Lesson Title\n\n...", ... }

3. Frontend receives lesson
   └─ Converts Markdown → HTML at render time
   └─ Uses marked.js or remark for conversion

4. Display in browser (Native HTML/CSS)
   └─ Tailwind Typography (prose classes)
   └─ Syntax highlighting (Prism.js or Shiki)
   └─ Interactive elements (checkpoints, quizzes)
   └─ Responsive design (desktop + mobile)
```

**Example Markdown → HTML conversion:**

```typescript
import { marked } from 'marked';
import DOMPurify from 'dompurify';
import Prism from 'prismjs';

function markdownToHtml(markdown: string): string {
  // Configure marked for code syntax highlighting
  marked.setOptions({
    highlight: (code, lang) => {
      if (Prism.languages[lang]) {
        return Prism.highlight(code, Prism.languages[lang], lang);
      }
      return code;
    }
  });
  
  // Convert Markdown to HTML
  const rawHtml = marked.parse(markdown);
  
  // Sanitize HTML to prevent XSS attacks
  const cleanHtml = DOMPurify.sanitize(rawHtml);
  
  return cleanHtml;
}
```

**Rendered output styling (Tailwind Typography):**

```tsx
<div className="prose prose-lg max-w-none dark:prose-invert">
  {/* Heading styles */}
  <h1>Lesson Title</h1>         {/* 2xl, bold, mb-4 */}
  <h2>Section Header</h2>        {/* xl, bold, mb-3 */}
  
  {/* Paragraph styles */}
  <p>Lesson content here...</p>  {/* Base text, mb-4 */}
  
  {/* Code block styles */}
  <pre className="language-python">
    <code>print("Hello")</code>   {/* Syntax highlighted */}
  </pre>
  
  {/* List styles */}
  <ul>                           {/* Bullet points, mb-4 */}
    <li>Point 1</li>
    <li>Point 2</li>
  </ul>
  
  {/* Image styles */}
  <img src="..." alt="..." />    {/* Responsive, rounded */}
</div>
```

### Export Options (Future Feature)

**User can export lessons in multiple formats:**

```typescript
function exportLesson(lessonId: string, format: ExportFormat) {
  switch (format) {
    case 'markdown':
      // Direct download of Markdown source
      return lesson.content;
      
    case 'pdf':
      // Convert HTML → PDF using jsPDF or Puppeteer
      return generatePDF(htmlContent);
      
    case 'html':
      // Standalone HTML file with embedded CSS
      return generateStandaloneHTML(htmlContent);
      
    case 'pptx':
      // Convert to PowerPoint using reveal.js → PPTX export
      return generatePowerPoint(htmlContent);
      
    case 'docx':
      // Convert to Word doc using docx.js
      return generateWord(htmlContent);
  }
}
```

### Offline Support

**Progressive Web App (PWA) capabilities:**

```typescript
// Service Worker caches lessons for offline access
self.addEventListener('fetch', (event) => {
  if (event.request.url.includes('/api/lessons/')) {
    event.respondWith(
      caches.match(event.request).then(response => {
        return response || fetch(event.request).then(response => {
          return caches.open('lessons-v1').then(cache => {
            cache.put(event.request, response.clone());
            return response;
          });
        });
      })
    );
  }
});

// IndexedDB stores curriculum state locally
import Dexie from 'dexie';

class DoqtraDB extends Dexie {
  curricula: Dexie.Table<Curriculum, string>;
  lessons: Dexie.Table<Lesson, string>;
  progress: Dexie.Table<Progress, string>;
  
  constructor() {
    super('DoqtraDB');
    this.version(1).stores({
      curricula: 'id, userId, createdAt',
      lessons: 'id, curriculumId, status',
      progress: 'id, lessonId, completedAt'
    });
  }
}

export const db = new DoqtraDB();
```

---

## Backend Architecture

### Technology Stack

**Framework:** FastAPI (Python 3.11+)  
**ORM:** SQLAlchemy 2.0  
**Database:** PostgreSQL 15+  
**Cache:** Redis 7+  
**Task Queue:** Celery with Redis broker  
**AI API:** Anthropic Claude API  
**Authentication:** JWT with PyJWT  
**Validation:** Pydantic v2  

### Application Structure

```
doqtra-backend/
├── app/
│   ├── main.py                 # FastAPI application entry
│   ├── config.py               # Configuration management
│   ├── api/
│   │   ├── v1/
│   │   │   ├── auth.py
│   │   │   ├── curriculum.py
│   │   │   ├── lessons.py
│   │   │   ├── progress.py
│   │   │   └── users.py
│   ├── core/
│   │   ├── security.py         # JWT, password hashing
│   │   ├── dependencies.py     # FastAPI dependencies
│   │   └── middleware.py
│   ├── db/
│   │   ├── models.py           # SQLAlchemy models
│   │   ├── session.py          # Database session
│   │   └── migrations/         # Alembic migrations
│   ├── schemas/
│   │   ├── curriculum.py       # Pydantic schemas
│   │   ├── lesson.py
│   │   ├── user.py
│   │   └── progress.py
│   ├── services/
│   │   ├── curriculum_generator.py
│   │   ├── lesson_generator.py
│   │   ├── content_library.py
│   │   └── ai_client.py
│   └── tasks/
│       ├── lesson_generation.py  # Celery tasks
│       └── curriculum_adaptation.py
├── tests/
└── requirements.txt
```

### Key Services

#### 1. Curriculum Generation Service

```python
from anthropic import Anthropic
from app.schemas.curriculum import CurriculumRequest, Curriculum

class CurriculumGenerator:
    def __init__(self):
        self.client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    
    async def generate_curriculum(
        self, 
        request: CurriculumRequest
    ) -> Curriculum:
        """
        Generate personalized curriculum based on user profile.
        
        Args:
            request: User's learning profile (topic, skill level, goals, etc.)
            
        Returns:
            Curriculum: Full roadmap with phases, modules, lessons
        """
        
        # Build AI prompt
        prompt = self._build_curriculum_prompt(request)
        
        # Call Claude API
        response = await self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        # Parse AI response into structured curriculum
        curriculum_data = self._parse_curriculum_response(response.content[0].text)
        
        # Save to database
        curriculum = await self._save_curriculum(request.user_id, curriculum_data)
        
        return curriculum
    
    def _build_curriculum_prompt(self, request: CurriculumRequest) -> str:
        return f"""
        Generate a personalized learning curriculum for:
        
        Topic: {request.topic}
        Subtopics: {', '.join(request.subtopics)}
        Skill Level: {request.skill_level}
        Learning Style: {request.learning_style}
        Goal: {request.goal}
        Time Available: {request.hours_per_week} hours/week
        Duration: {request.duration_weeks} weeks
        
        Output a structured curriculum with:
        1. Phases (major learning sections, 2-4 weeks each)
        2. Modules (focused skill areas, 3-5 per phase)
        3. Lessons (individual learning units, 45-90 minutes each)
        
        For each lesson, include:
        - Lesson ID (e.g., P01-M01-L01)
        - Title
        - Estimated duration (minutes)
        - Learning objectives
        - Prerequisites
        
        Format as JSON.
        """
```

#### 2. Lesson Generation Service

```python
class LessonGenerator:
    def __init__(self):
        self.client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        self.content_library = ContentLibrary()
    
    async def generate_lesson(
        self,
        lesson_metadata: LessonMetadata,
        user_profile: UserProfile
    ) -> Lesson:
        """
        Generate individual lesson content.
        
        First checks content library for cached lesson.
        If not found, generates new lesson via Claude API.
        
        Args:
            lesson_metadata: Lesson structure from curriculum
            user_profile: User's learning preferences
            
        Returns:
            Lesson: Complete lesson with content, checkpoints, etc.
        """
        
        # Check content library for matching lesson
        cached_lesson = await self.content_library.find_match(
            topic=lesson_metadata.topic,
            skill_level=user_profile.skill_level,
            learning_style=user_profile.learning_style
        )
        
        if cached_lesson and cached_lesson.rating >= 4.0:
            # Personalize cached lesson (name, examples)
            return await self._personalize_lesson(cached_lesson, user_profile)
        
        # Generate new lesson
        lesson_content = await self._generate_new_lesson(
            lesson_metadata, 
            user_profile
        )
        
        # Save to content library
        await self.content_library.save(lesson_content)
        
        return lesson_content
    
    async def _generate_new_lesson(
        self,
        metadata: LessonMetadata,
        profile: UserProfile
    ) -> Lesson:
        """Generate lesson content via Claude API."""
        
        prompt = f"""
        Create a {metadata.duration_minutes}-minute lesson on: {metadata.title}
        
        Learning objectives:
        {chr(10).join(f'- {obj}' for obj in metadata.objectives)}
        
        Learner profile:
        - Skill level: {profile.skill_level}
        - Learning style: {profile.learning_style}
        - Goal: {profile.goal}
        
        Format the lesson as Markdown with:
        1. Introduction (motivation, why this matters)
        2. Core concepts (explanations, examples, visuals)
        3. Checkpoints (4-6 interactive questions throughout)
        4. Summary (key takeaways)
        5. Practice exercise (hands-on application)
        
        Use {profile.learning_style} learning techniques:
        - Visual: Include diagrams, charts, step-by-step screenshots
        - Auditory: Use analogies, narratives, conversational tone
        - Hands-on: Emphasize practical exercises, real-world projects
        - Reading: Provide detailed explanations, supplemental resources
        
        Output: Markdown format with embedded checkpoint markers.
        """
        
        response = await self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        markdown_content = response.content[0].text
        
        # Parse checkpoints from markdown
        checkpoints = self._extract_checkpoints(markdown_content)
        
        return Lesson(
            id=metadata.id,
            title=metadata.title,
            content=markdown_content,
            checkpoints=checkpoints,
            duration_minutes=metadata.duration_minutes,
            created_at=datetime.utcnow()
        )
```

#### 3. Content Library Service

```python
class ContentLibrary:
    """
    Manages cached lessons for reuse across users.
    Implements matching algorithm to find suitable cached lessons.
    """
    
    async def find_match(
        self,
        topic: str,
        skill_level: str,
        learning_style: str
    ) -> Optional[Lesson]:
        """
        Find cached lesson matching user profile.
        
        Matching algorithm:
        1. Exact match (topic + skill + style) → 100% match
        2. Partial match (topic + skill) → 80% match, adapt style
        3. No match → return None (generate new lesson)
        """
        
        # Try exact match
        exact_match = await db.lessons.find_one({
            "topic": topic,
            "skill_level": skill_level,
            "learning_style": learning_style,
            "rating": {"$gte": 4.0}
        })
        
        if exact_match:
            return exact_match
        
        # Try partial match (same topic + skill, different style)
        partial_match = await db.lessons.find_one({
            "topic": topic,
            "skill_level": skill_level,
            "rating": {"$gte": 4.0}
        })
        
        return partial_match  # Will be adapted for learning style
    
    async def save(self, lesson: Lesson) -> None:
        """Save lesson to library for future reuse."""
        await db.lessons.insert_one(lesson.dict())
    
    async def rate_lesson(
        self, 
        lesson_id: str, 
        rating: int,
        user_id: str
    ) -> None:
        """Update lesson rating based on user feedback."""
        
        # Calculate new average rating
        lesson = await db.lessons.find_one({"id": lesson_id})
        total_ratings = lesson.total_ratings + 1
        new_avg = ((lesson.rating * lesson.total_ratings) + rating) / total_ratings
        
        await db.lessons.update_one(
            {"id": lesson_id},
            {
                "$set": {
                    "rating": new_avg,
                    "total_ratings": total_ratings
                }
            }
        )
        
        # If rating drops below 3.0, flag for regeneration
        if new_avg < 3.0:
            await self._flag_for_regeneration(lesson_id)
```

---

## Database Schema

### PostgreSQL Tables

```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- User profiles (learning preferences)
CREATE TABLE user_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    skill_level VARCHAR(50),  -- novice, beginner, intermediate, advanced
    learning_style VARCHAR(50),  -- visual, auditory, hands-on, reading
    hours_per_week INT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Curricula
CREATE TABLE curricula (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    topic VARCHAR(255) NOT NULL,
    skill_level VARCHAR(50),
    goal TEXT,
    total_weeks INT,
    total_lessons INT,
    total_hours INT,
    status VARCHAR(50),  -- draft, active, completed, archived
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Phases
CREATE TABLE phases (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    curriculum_id UUID REFERENCES curricula(id) ON DELETE CASCADE,
    phase_number INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    weeks INT,
    hours INT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Modules
CREATE TABLE modules (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    phase_id UUID REFERENCES phases(id) ON DELETE CASCADE,
    module_number INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    skipped BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Lessons
CREATE TABLE lessons (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    module_id UUID REFERENCES modules(id) ON DELETE CASCADE,
    lesson_number INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,  -- Markdown content
    duration_minutes INT,
    checkpoints JSONB,  -- Array of checkpoint objects
    rating DECIMAL(3,2),  -- Average rating 0.00-5.00
    total_ratings INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Lesson completions (progress tracking)
CREATE TABLE lesson_completions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    lesson_id UUID REFERENCES lessons(id) ON DELETE CASCADE,
    confidence_rating INT,  -- 1-5 scale
    duration_minutes INT,  -- Actual time spent
    checkpoint_responses JSONB,  -- User's checkpoint answers
    completed_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(user_id, lesson_id)  -- One completion per user per lesson
);

-- Lesson ratings (user feedback)
CREATE TABLE lesson_ratings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    lesson_id UUID REFERENCES lessons(id) ON DELETE CASCADE,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    feedback TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(user_id, lesson_id)
);

-- Content library (cached lessons for reuse)
CREATE TABLE content_library (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    topic VARCHAR(255) NOT NULL,
    skill_level VARCHAR(50),
    learning_style VARCHAR(50),
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,  -- Markdown
    checkpoints JSONB,
    duration_minutes INT,
    rating DECIMAL(3,2),
    total_ratings INT DEFAULT 0,
    times_used INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    INDEX idx_topic_skill (topic, skill_level),
    INDEX idx_rating (rating DESC)
);
```

---

## API Endpoints

### Authentication

```
POST   /api/v1/auth/register        # Create new user
POST   /api/v1/auth/login           # Login (returns JWT)
POST   /api/v1/auth/refresh         # Refresh JWT token
POST   /api/v1/auth/logout          # Logout (invalidate token)
```

### Curriculum

```
POST   /api/v1/curriculum/generate  # Generate new curriculum
GET    /api/v1/curriculum/:id       # Get curriculum by ID
PUT    /api/v1/curriculum/:id       # Update curriculum (skip/add modules)
DELETE /api/v1/curriculum/:id       # Delete curriculum
GET    /api/v1/curriculum/user/:id  # Get all curricula for user
POST   /api/v1/curriculum/:id/regenerate  # Regenerate with new params
```

### Lessons

```
GET    /api/v1/lessons/:id          # Get lesson by ID
POST   /api/v1/lessons/:id/complete # Mark lesson complete
POST   /api/v1/lessons/:id/rate     # Rate lesson (1-5 stars)
GET    /api/v1/lessons/:id/export   # Export lesson (markdown/pdf/html)
```

### Progress

```
GET    /api/v1/progress/user/:id    # Get user's overall progress
GET    /api/v1/progress/curriculum/:id  # Get progress for specific curriculum
POST   /api/v1/progress/checkpoint  # Submit checkpoint answer
```

### User Profile

```
GET    /api/v1/users/me             # Get current user
PUT    /api/v1/users/me             # Update user profile
GET    /api/v1/users/me/stats       # Get learning statistics
```

---

## Deployment Architecture

### Infrastructure (AWS)

```
┌─────────────────────────────────────────────────┐
│              CloudFront (CDN)                   │
│  - Static assets (JS, CSS, images)              │
│  - Edge caching                                 │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│         Application Load Balancer               │
│  - HTTPS termination                            │
│  - Auto-scaling                                 │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│        ECS Fargate (Docker Containers)          │
│  - FastAPI backend (2+ containers)              │
│  - Celery workers (background tasks)            │
│  - Auto-scaling based on CPU/memory             │
└─────────────────────────────────────────────────┘
        ↓                        ↓
┌──────────────────┐    ┌──────────────────┐
│  RDS PostgreSQL  │    │  ElastiCache     │
│  (Primary DB)    │    │  (Redis)         │
│  - Multi-AZ      │    │  - Session cache │
│  - Automated     │    │  - Lesson cache  │
│    backups       │    │  - Task queue    │
└──────────────────┘    └──────────────────┘
```

### CI/CD Pipeline (GitHub Actions)

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: |
          pip install -r requirements.txt
          pytest
  
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Build Docker image
        run: docker build -t doqtra-backend .
      
      - name: Push to ECR
        run: |
          aws ecr get-login-password | docker login
          docker push doqtra-backend:latest
      
      - name: Deploy to ECS
        run: |
          aws ecs update-service \
            --cluster doqtra-prod \
            --service backend \
            --force-new-deployment
```

---

## Security Considerations

### Authentication & Authorization

- JWT tokens with 24-hour expiry
- Refresh tokens with 30-day expiry
- Password hashing with bcrypt (12 rounds)
- Rate limiting on auth endpoints (5 attempts/minute)

### Data Protection

- All API traffic over HTTPS (TLS 1.3)
- Database encryption at rest (AWS RDS)
- PII redaction in logs
- GDPR compliance (data export, deletion)

### API Security

- CORS configured for specific domains only
- Request size limits (10MB max)
- SQL injection prevention (parameterized queries)
- XSS prevention (HTML sanitization)

---

## Monitoring & Observability

### Metrics (Datadog)

- Request latency (p50, p95, p99)
- Error rates (4xx, 5xx)
- Database query performance
- Celery task queue length
- AI API costs per lesson

### Logging (CloudWatch)

- Structured JSON logs
- Error tracking with stack traces
- Audit logs (user actions)
- AI API request/response logs

### Alerts

- Error rate > 1% → PagerDuty
- Response time > 2s → Slack
- Database CPU > 80% → Email
- AI API cost spike → Slack

---

## Cost Estimates (MVP Scale)

**Monthly costs at 1,000 active users:**

- AWS ECS Fargate: $150 (2 containers)
- RDS PostgreSQL: $100 (db.t3.medium)
- ElastiCache Redis: $50 (cache.t3.micro)
- CloudFront + S3: $30 (static assets)
- Claude API: $500 (assuming 80% cache hit rate)
- **Total: ~$830/month**

**Revenue at 1,000 users (25% conversion to Pro):**
- 250 Pro users × $20/month = $5,000/month
- **Profit: $4,170/month**

---

## Performance Targets

### API Response Times

- GET requests: <100ms (cached)
- POST requests: <500ms (database writes)
- Curriculum generation: <10s (AI calls)
- Lesson generation: <30s (AI calls, cached after first use)

### Availability

- Uptime SLA: 99.5% (4 hours downtime/year)
- Database backup: Hourly snapshots, 7-day retention
- Disaster recovery: <1 hour RTO (recovery time objective)

---

**This architecture scales to 100K users before major refactoring needed.**
