#!/usr/bin/env python3
"""
Migration script to convert lesson files from flat structure to nested directory structure.

BEFORE:
curriculum/lessons/
├── P01-M01-L01.json
├── P01-M01-L01_lesson_doc.md
└── P01-M01-L01_response_and_eval.md

AFTER:
curriculum/lessons/
└── P01-M01-L01/
    ├── lesson.json
    ├── lesson.md
    └── completion.md
"""

import shutil
from pathlib import Path

def migrate_lesson(lesson_dir, lesson_id):
    """Migrate a single lesson to nested directory structure."""
    
    # Create nested directory
    nested_dir = lesson_dir / lesson_id
    nested_dir.mkdir(exist_ok=True)
    
    # Map old filenames to new filenames
    file_mappings = {
        f"{lesson_id}.json": "lesson.json",
        f"{lesson_id}_lesson_doc.md": "lesson.md",
        f"{lesson_id}_response_and_eval.md": "completion.md",
    }
    
    migrated_files = []
    
    for old_name, new_name in file_mappings.items():
        old_path = lesson_dir / old_name
        new_path = nested_dir / new_name
        
        if old_path.exists():
            shutil.move(str(old_path), str(new_path))
            migrated_files.append(f"{old_name} → {lesson_id}/{new_name}")
            print(f"✓ Moved {old_name} → {lesson_id}/{new_name}")
        else:
            print(f"⊘ Skipped {old_name} (not found)")
    
    return migrated_files

def main():
    """Run migration on all lessons in curriculum/lessons/."""
    repo_root = Path(__file__).parent.parent
    lesson_dir = repo_root / "curriculum" / "lessons"
    
    if not lesson_dir.exists():
        print("Error: curriculum/lessons/ directory not found")
        return
    
    # Find all lesson JSON files (flat structure)
    lesson_files = list(lesson_dir.glob("P*-M*-L*.json"))
    
    if not lesson_files:
        print("No lessons found to migrate (already migrated or no lessons exist)")
        return
    
    print(f"Found {len(lesson_files)} lesson(s) to migrate\n")
    
    for lesson_file in lesson_files:
        lesson_id = lesson_file.stem  # e.g., "P01-M01-L01"
        print(f"Migrating {lesson_id}...")
        migrate_lesson(lesson_dir, lesson_id)
        print()
    
    print("=" * 60)
    print("Migration complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Run validation: python tools/validate.py")
    print("2. Verify files manually in VS Code")
    print("3. Commit changes:")
    print('   git add curriculum/lessons/')
    print('   git commit -m "refactor(lessons): migrate to nested directory structure"')

if __name__ == "__main__":
    main()
