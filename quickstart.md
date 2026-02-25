# Helm Curriculum — Quick Start

**Goal:** Complete your first lesson and make your first Helm commit in 60 minutes.

## What You're Building

**Helm** is an AI-powered fishing journal app. Over 28 phases, you'll build it from scratch: mobile UI, backend API, database, AI species identification, and more.

This curriculum isn't about throwaway exercises—you're shipping real features that compound into a production app.

---

## Step 1: Bootstrap the System

Open Claude Desktop and type:

```text
/bootstrap
```

Claude will load your curriculum and show your current position within the 28-phase Helm roadmap.

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

- **Why this matters for Helm** (context)
- **Concepts to learn** (theory)
- **Hands-on exercise** (practice with Helm repo)
- **Checkpoint questions** (verify understanding)

Read through it at your own pace.

---

## Step 4: Answer Checkpoint Questions

When you reach a checkpoint, answer the question in the chat.

**Example checkpoint:**
> **Checkpoint 1:** In your own words, why is version control important for the Helm project?

Type your answer. Claude will adapt the next section based on your response.

---

## Step 5: Complete the Hands-On Exercise

Follow the instructions to:

1. Create a Helm repository
2. Write a README describing the project
3. Make your first Git commit

This is your first **real Helm deliverable**—not a toy example.

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

- Your progress in the Helm curriculum
- Skills you've mastered
- Which Helm features are ready to build next

---

## The Big Picture

**28 Phases. 139 Modules. ~850 Hours. One Real Product.**

You're not just learning full-stack development—you're building **Helm** from day 1 to production launch.

Every lesson ships a feature. Every module completes a major component. Every phase advances Helm toward launch.

---

**Ready?** Start with `/bootstrap` in Claude Desktop.

For advanced features, see `instructions.md`.