#!/usr/bin/env python3
"""
Fix lesson.json file naming to use full lesson ID format.

Renames: lesson.json → P01-M01-L01.lesson.json
"""

import os
import sys
from pathlib import Path

# Repository root
REPO_ROOT = Path(__file__).parent.parent
LESSONS_DIR = REPO_ROOT / "curriculum" / "lessons"


def fix_lesson_filenames(dry_run=True):
    """Rename lesson.json files to {lesson_id}.lesson.json format."""
    
    if dry_run:
        print("=" * 60)
        print("DRY RUN MODE - No changes will be made")
        print("=" * 60)
        print()
    else:
        print("=" * 60)
        print("EXECUTE MODE - Renaming files")
        print("=" * 60)
        print()
    
    renamed_count = 0
    already_correct = 0
    
    # Walk through hierarchical lesson directories
    for phase_dir in sorted(LESSONS_DIR.glob("P*")):
        if not phase_dir.is_dir():
            continue
            
        for module_dir in sorted(phase_dir.glob("M*")):
            if not module_dir.is_dir():
                continue
                
            for lesson_dir in sorted(module_dir.glob("L*")):
                if not lesson_dir.is_dir():
                    continue
                
                # Extract lesson ID from directory path
                # e.g., P01/M01/L01 → P01-M01-L01
                phase_id = phase_dir.name
                module_num = module_dir.name
                lesson_num = lesson_dir.name
                lesson_id = f"{phase_id}-{module_num}-{lesson_num}"
                
                # Check for old naming (lesson.json)
                old_path = lesson_dir / "lesson.json"
                new_path = lesson_dir / f"{lesson_id}.lesson.json"
                
                if old_path.exists():
                    if new_path.exists():
                        print(f"[SKIP] {lesson_id}: Both files exist")
                        continue
                    
                    if dry_run:
                        print(f"[DRY-RUN] Would rename: {old_path.relative_to(REPO_ROOT)} → {new_path.name}")
                    else:
                        old_path.rename(new_path)
                        print(f"[RENAMED] {lesson_id}: lesson.json → {lesson_id}.lesson.json")
                    
                    renamed_count += 1
                    
                elif new_path.exists():
                    already_correct += 1
                    print(f"[OK] {lesson_id}: Already using correct naming")
    
    print()
    print("=" * 60)
    print(f"Files to rename: {renamed_count}")
    print(f"Already correct: {already_correct}")
    print("=" * 60)
    
    if dry_run and renamed_count > 0:
        print()
        print("Run with --execute to perform renaming:")
        print("  python tools/fix_lesson_naming.py --execute")


def main():
    dry_run = "--execute" not in sys.argv
    fix_lesson_filenames(dry_run)


if __name__ == "__main__":
    main()
