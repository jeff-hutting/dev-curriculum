# Lesson Summary — {{lesson_id}} / {{lesson_title}}

## Learning Objectives

{{list each objective exactly as written in the lesson JSON}}

## Key Concepts Covered

{{bullet points summarizing the most important ideas from the lesson}}

## Hands‑On Exercises Completed

{{brief list of exercises and checks performed}}

## Evidence of Understanding

{{observable demonstrations, statements, or proof of comprehension}}

> Only include evidence explicitly demonstrated by the learner. Do not infer understanding or generate assumptions.

## Assessment Result

- Status: {{met | partial | not_met}}
- Criteria Reference: {{objective_id or rubric label}}
- Supporting Notes: {{notes used by Evaluator based on rubric}}

## Reflection Prompt

{{reflection prompt from lesson or professor}}

> If no reflection prompt exists in the lesson JSON, request clarification instead of inventing one.

---

### Proposed Learner State Update (Pending Confirmation)

```json
{
  "update": {
    "lesson_id": "{{lesson_id}}",
    "status": "{{completed | in_progress | repeat}}",
    "objective_updates": [
      {
        "objective_id": "{{objective_id}}",
        "result": "{{met | partial | not_met}}",
        "notes": "{{optional}}"
      }
    ]
  }
}
```

> This summary is generated based strictly on explicit lesson JSON and learner submission; no inferred or assumed information should be included.
