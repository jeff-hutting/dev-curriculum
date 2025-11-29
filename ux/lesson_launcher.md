# Lesson Launcher

This document defines the minimal structure for initiating a lesson within the AI-assisted curriculum system. Its purpose is to provide a consistent entry point for tools, automation, or future UX flows. It does not contain instructional material or lesson-specific content.

## Purpose

- Establish a standardized launch format for any lesson.
- Provide a neutral metadata block that other roles (Professor, Advisor, Evaluator) can read.
- Ensure the presence of a UX anchor referenced in `project_files_index.json`.

## Launch Parameters

- **Lesson ID:** {{lesson_id}}
- **Phase:** {{phase_id}}
- **Title:** {{lesson_title}}
- **Estimated Time:** {{estimated_time_minutes}} minutes
- **Lesson Type:** {{lesson_type}}

> Fields use double-curly template syntax to indicate they must be filled by the calling system, not by this template.

## Launch Flow

1. Validate that the lesson file exists and follows `lesson_schema.json`.
2. Load lesson metadata into the interface initiating the session.
3. Select role:
   - **Professor** to deliver lesson
   - **Advisor** to determine readiness
   - **Evaluator** if the learner is submitting work
4. Begin session after explicit learner confirmation.

## Notes

- This template intentionally avoids lesson content.
- This is a structural document, not a pedagogical one.
- No assumptions about curriculum sequencing are made here.
