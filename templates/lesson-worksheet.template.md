# Lesson Worksheet Template — Complete Formatting Specification

> **Purpose:** This template defines the structure for lesson worksheets that learners use to answer checkpoint questions during lesson delivery.
> 
> **File Location:** `curriculum/lessons/{lesson_id}/{lesson_id}.worksheet.md`
> 
> **Last Updated:** 2025-12-08

---

## Document Purpose

The worksheet is a **per-lesson artifact** that:
- Lists all checkpoint questions from the lesson
- Provides structured space for learner answers
- Makes copying answers to chat easy and organized
- Includes space for notes and questions during lesson

---

## Generation Timing

**When to Generate:**
- AFTER lesson.md is created
- BEFORE user starts reading lesson
- As part of initial lesson delivery artifacts

**Generation Order:**
1. Professor generates `{lesson_id}.lesson.md`
2. Professor generates `{lesson_id}.worksheet.md` (this file)
3. User copies both to VS Code, saves to lesson directory
4. User reads lesson.md and fills in worksheet.md as they progress
5. User copies completed answers from worksheet and pastes into chat
6. After final checkpoint, Professor generates `{lesson_id}.feedback.md`

---

## Document Structure

Every worksheet follows this exact structure:

1. **Document Header** — `# {lesson_id} Worksheet`
2. **Metadata Block** — Indented blockquote with worksheet metadata
3. **Checkpoint Sections** — One section per checkpoint with questions and answer spaces
4. **Notes Section** — Unstructured space for additional thoughts

---

## Complete Worksheet Template

```markdown
# {lesson_id} Worksheet

---

> **Lesson:** {lesson_id} - {title}  
> **Date:** {YYYY-MM-DD}

---

## Checkpoint 1 ({minutes} minutes)

**Questions:**

1. {Question 1 text copied exactly from lesson.md}
2. {Question 2 text copied exactly from lesson.md}
3. {Question 3 text copied exactly from lesson.md}

**Answers:**

1. 

2. 

3. 

---

## Checkpoint 2 ({minutes} minutes)

**Questions:**

1. {Question 1 text copied exactly from lesson.md}
2. {Question 2 text copied exactly from lesson.md}

**Answers:**

1. 

2. 

---

## Checkpoint 3 ({minutes} minutes)

**Questions:**

1. {Question 1 text copied exactly from lesson.md}

**Answers:**

1. 

---

## Notes

{Space for additional notes, questions, or observations during the lesson}

---
```

---

## Component Specifications

### 1. Document Header

**Format:** `# {lesson_id} Worksheet`

**Rules:**
- Use lesson ID (e.g., `P01-M01-L01`)
- Add " Worksheet" suffix
- Single `#` (H1 heading)

**Example:**
```markdown
# P01-M01-L01 Worksheet
```

### 2. Metadata Block

**Location:** Immediately after document header  
**Format:** Indented blockquote with horizontal rules before and after

**Structure:**
```markdown
---

> **Lesson:** {lesson_id} - {title}  
> **Date:** {YYYY-MM-DD}

---
```

**Field Specifications:**
- **Lesson:** Combine lesson_id and title from lesson.json (e.g., `P01-M01-L01 - Version Control Concepts`)
- **Date:** Current date when worksheet is generated in ISO format (e.g., `2025-12-08`)

### 3. Checkpoint Sections

**Purpose:** One section per checkpoint in the lesson

**Heading Format:**
```markdown
## Checkpoint {N} ({cumulative_minutes} minutes)
```

**Section Structure:**
```markdown
## Checkpoint {N} ({cumulative_minutes} minutes)

**Questions:**

1. {Question 1 text copied exactly from lesson.md}
2. {Question 2 text copied exactly from lesson.md}
3. {Question 3 text copied exactly from lesson.md}

**Answers:**

1. 

2. 

3. 

---
```

**Rules:**

*Questions:*
- Copy question text EXACTLY from lesson.md checkpoint sections
- Preserve question numbering (1, 2, 3)
- Include all questions from that checkpoint
- Do NOT include any hints, examples, or guidance (just the questions)

*Answers:*
- Numbered list matching question count
- Leave blank (just number and blank space)
- User fills these in as they read lesson
- Blank lines between numbers for readability

*Horizontal Rules:*
- Add `---` after each checkpoint section (except after Notes section)

### 4. Notes Section

**Purpose:** Unstructured space for learner's thoughts during lesson

**Location:** Final section (after all checkpoints)

**Structure:**
```markdown
## Notes

{Space for additional notes, questions, or observations during the lesson}

---
```

**Rules:**
- Always include this section (even if learner doesn't use it)
- No specific formatting requirements within this section
- Learner can use however they want (bullet points, paragraphs, code snippets, etc.)
- Placeholder text guides usage
- End with horizontal rule

---

## Formatting Guidelines

### Horizontal Rules

**Placement:**
- Before metadata block (after document header)
- After metadata block (before first checkpoint)
- After EVERY checkpoint section (before next checkpoint or notes)
- After notes section (end of document)

### Number of Checkpoints

**Determine from lesson.json:**
- For 30-min lessons: 1 checkpoint at ~15 minutes. For 45-min lessons: 2 checkpoints at ~20 and ~40 minutes.
- 30-minute lesson = 1 checkpoint (15 minutes)
- 45-minute lesson = 2 checkpoints (20, 40 minutes)

**Include all checkpoints** in worksheet, even if last checkpoint is not exactly at 20-minute interval

### Blank Answer Spaces

**Formatting:**
```markdown
**Answers:**

1. 

2. 

3. 
```

**Rules:**
- Number matches question count
- Single blank line after each number
- No placeholder text (keep it clean for copy/paste)
- Extra blank line between answer numbers for visual space

---

## Complete Annotated Example

```markdown
# P01-M01-L01 Worksheet

---

> **Lesson:** P01-M01-L01 - Version Control Concepts and Why Git Matters  
> **Date:** 2025-12-08

---

## Checkpoint 1 (~20 minutes)

**Questions:**

1. In your own words, explain why version control is important for the Helm project.
2. What problems might you encounter if you tried to build Helm without version control?
3. How does version control enable experimentation during development?

**Answers:**

1. 

2. 

3. 

---

## Checkpoint 2 (40 minutes)

**Questions:**

1. What is the key difference between centralized and distributed version control systems?
2. Why is Git's distributed architecture particularly valuable for Helm development?
3. If you had to explain Git to someone who has never used version control, what would you say?

**Answers:**

1. 

2. 

3. 

---

## Checkpoint 3 (60 minutes)

**Questions:**

1. How does Git's snapshot model differ from the delta-based approach of older systems?
2. What does it mean that every developer has a "full copy" of the repository?
3. How will branching help you develop Helm features safely?

**Answers:**

1. 

2. 

3. 

---

## Notes

{Space for additional notes, questions, or observations during the lesson}

---
```

---

## Usage Notes for Professor Role

1. **Generate immediately after lesson.md** — Part of initial lesson delivery
2. **Copy questions exactly** — No modifications to question text
3. **Match checkpoint count** — Use same checkpoint structure as lesson.md
4. **Leave answers blank** — User fills these in during reading
5. **Include Notes section** — Always include, even if user might not use it
6. **One artifact per lesson** — Each lesson gets its own unique worksheet
7. **Simplify copy/paste workflow** — Learner can select entire "Answers:" section and paste into chat
8. **File placement:** `curriculum/lessons/{lesson_id}/{lesson_id}.worksheet.md`

---

## Learner Workflow

1. Professor generates lesson.md and worksheet.md as artifacts
2. Learner copies both files to VS Code
3. Learner saves both to `curriculum/lessons/{lesson_id}/` directory
4. Learner opens lesson.md in one pane, worksheet.md in another
5. As learner reads lesson.md and reaches checkpoints, they fill in worksheet.md answers
6. When ready to submit checkpoint, learner copies entire "Answers:" section from worksheet
7. Learner pastes answers into chat for Professor feedback
8. Professor provides conversational feedback
9. Learner continues reading lesson.md and filling in next checkpoint
10. After final checkpoint, Professor generates feedback.md with all Q&A preserved

---

## End of Template
