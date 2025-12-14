#!/usr/bin/env python3
"""
Migration script to convert curriculum files to hierarchical directory structure.

This script:
1. Renames phase files: P01.json → P01.phase.json
2. Moves modules to nested structure: P01-M01.json → P01/P01-M01.module.json
3. Moves lessons to nested structure: P01-M01-L01/ → P01/M01/L01/
4. Updates any file path references in learner-state files

Usage:
    python tools/migrate_to_hierarchical_structure.py           # Dry run
    python tools/migrate_to_hierarchical_structure.py --execute # Execute migration
"""

import os
import sys
import json
import shutil
from pathlib import Path
from typing import List, Tuple, Dict

# Repository root
REPO_ROOT = Path(__file__).parent.parent

# Directories
PHASES_DIR = REPO_ROOT / "curriculum" / "phases"
MODULES_DIR = REPO_ROOT / "curriculum" / "modules"
LESSONS_DIR = REPO_ROOT / "curriculum" / "lessons"
LEARNER_STATE_DIR = REPO_ROOT / "learner-state"


def log(message: str, level: str = "INFO"):
    """Print formatted log message."""
    print(f"[{level}] {message}")


def get_phase_files() -> List[Path]:
    """Get all phase files that need migration."""
    if not PHASES_DIR.exists():
        return []
    
    phase_files = []
    for file in PHASES_DIR.glob("P*.json"):
        # Only migrate if it doesn't already have .phase extension
        if not file.stem.endswith(".phase"):
            phase_files.append(file)
    
    return sorted(phase_files)


def get_module_files() -> List[Path]:
    """Get all module files that need migration."""
    if not MODULES_DIR.exists():
        return []
    
    module_files = []
    for file in MODULES_DIR.glob("P*-M*.json"):
        # Only migrate if it doesn't already have .module extension
        if not file.stem.endswith(".module"):
            module_files.append(file)
    
    return sorted(module_files)


def get_lesson_directories() -> List[Path]:
    """Get all lesson directories that need migration."""
    if not LESSONS_DIR.exists():
        return []
    
    lesson_dirs = []
    for item in LESSONS_DIR.iterdir():
        if item.is_dir() and item.name.startswith("P") and "-M" in item.name and "-L" in item.name:
            # Check if it's in flat structure (needs migration)
            # Flat: curriculum/lessons/P01-M01-L01/
            # Hierarchical: curriculum/lessons/P01/M01/L01/
            if item.parent == LESSONS_DIR:
                lesson_dirs.append(item)
    
    return sorted(lesson_dirs)


def migrate_phase_file(phase_file: Path, dry_run: bool = True) -> Tuple[bool, str]:
    """
    Migrate phase file to include .phase extension.
    
    Args:
        phase_file: Path to phase file (e.g., P01.json)
        dry_run: If True, only simulate the migration
    
    Returns:
        Tuple of (success, message)
    """
    # Extract phase ID (e.g., P01)
    phase_id = phase_file.stem
    
    # New filename with .phase extension
    new_filename = f"{phase_id}.phase.json"
    new_path = phase_file.parent / new_filename
    
    if new_path.exists():
        return False, f"Target already exists: {new_path}"
    
    if dry_run:
        log(f"Would rename: {phase_file} → {new_path}", "DRY-RUN")
        return True, "Simulated"
    
    try:
        shutil.move(str(phase_file), str(new_path))
        log(f"Renamed: {phase_file.name} → {new_filename}", "SUCCESS")
        return True, "Renamed"
    except Exception as e:
        log(f"Failed to rename {phase_file}: {e}", "ERROR")
        return False, str(e)


def migrate_module_file(module_file: Path, dry_run: bool = True) -> Tuple[bool, str]:
    """
    Migrate module file to hierarchical structure with .module extension.
    
    Args:
        module_file: Path to module file (e.g., P01-M01.json)
        dry_run: If True, only simulate the migration
    
    Returns:
        Tuple of (success, message)
    """
    # Extract phase ID from module filename (e.g., P01-M01.json → P01)
    module_id = module_file.stem
    phase_id = module_id.split("-")[0]  # P01
    
    # Create new directory structure
    phase_dir = MODULES_DIR / phase_id
    new_filename = f"{module_id}.module.json"
    new_path = phase_dir / new_filename
    
    if new_path.exists():
        return False, f"Target already exists: {new_path}"
    
    if dry_run:
        log(f"Would create: {phase_dir}/", "DRY-RUN")
        log(f"Would move: {module_file} → {new_path}", "DRY-RUN")
        return True, "Simulated"
    
    try:
        # Create phase directory if it doesn't exist
        phase_dir.mkdir(parents=True, exist_ok=True)
        
        # Move and rename file
        shutil.move(str(module_file), str(new_path))
        log(f"Moved: {module_file.name} → {phase_id}/{new_filename}", "SUCCESS")
        return True, "Moved"
    except Exception as e:
        log(f"Failed to migrate {module_file}: {e}", "ERROR")
        return False, str(e)


def migrate_lesson_directory(lesson_dir: Path, dry_run: bool = True) -> Tuple[bool, str]:
    """
    Migrate lesson directory to hierarchical structure.
    
    Args:
        lesson_dir: Path to lesson directory (e.g., P01-M01-L01/)
        dry_run: If True, only simulate the migration
    
    Returns:
        Tuple of (success, message)
    """
    # Extract phase, module, lesson IDs from directory name
    # e.g., P01-M01-L01 → P01, M01, L01
    lesson_id = lesson_dir.name
    parts = lesson_id.split("-")
    
    if len(parts) != 3:
        return False, f"Invalid lesson directory format: {lesson_id}"
    
    phase_id = parts[0]      # P01
    module_id = parts[1]     # M01
    lesson_num = parts[2]    # L01
    
    # Create new hierarchical path
    new_path = LESSONS_DIR / phase_id / module_id / lesson_num
    
    if new_path.exists():
        return False, f"Target already exists: {new_path}"
    
    if dry_run:
        log(f"Would create: {LESSONS_DIR}/{phase_id}/{module_id}/{lesson_num}/", "DRY-RUN")
        log(f"Would move: {lesson_dir} → {new_path}", "DRY-RUN")
        return True, "Simulated"
    
    try:
        # Create parent directories
        new_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Move entire directory
        shutil.move(str(lesson_dir), str(new_path))
        log(f"Moved: {lesson_id}/ → {phase_id}/{module_id}/{lesson_num}/", "SUCCESS")
        return True, "Moved"
    except Exception as e:
        log(f"Failed to migrate {lesson_dir}: {e}", "ERROR")
        return False, str(e)


def check_learner_state_references(dry_run: bool = True) -> Dict[str, List[str]]:
    """
    Check if learner-state files reference old file paths.
    
    Returns:
        Dictionary of issues found
    """
    issues = {
        "current.json": [],
        "completed": []
    }
    
    # Check current.json (shouldn't have file paths, just IDs)
    current_file = LEARNER_STATE_DIR / "current.json"
    if current_file.exists():
        try:
            with open(current_file, 'r') as f:
                data = json.load(f)
            
            # Check for any path-like strings (unlikely but good to check)
            data_str = json.dumps(data)
            if "curriculum/lessons/" in data_str or "curriculum/modules/" in data_str:
                issues["current.json"].append("Contains curriculum file paths (unexpected)")
        except Exception as e:
            issues["current.json"].append(f"Failed to read: {e}")
    
    # Check completed/*.json files
    completed_dir = LEARNER_STATE_DIR / "completed"
    if completed_dir.exists():
        for completed_file in completed_dir.glob("*.json"):
            try:
                with open(completed_file, 'r') as f:
                    data = json.load(f)
                
                # Check for any path-like strings
                data_str = json.dumps(data)
                if "curriculum/lessons/" in data_str or "curriculum/modules/" in data_str:
                    issues["completed"].append(f"{completed_file.name}: Contains curriculum file paths")
            except Exception as e:
                issues["completed"].append(f"{completed_file.name}: Failed to read - {e}")
    
    return issues


def main():
    """Main migration function."""
    # Check if --execute flag is provided
    dry_run = "--execute" not in sys.argv
    
    if dry_run:
        log("=" * 60)
        log("DRY RUN MODE - No changes will be made")
        log("Run with --execute flag to perform actual migration")
        log("=" * 60)
    else:
        log("=" * 60)
        log("EXECUTE MODE - Changes will be made to files")
        log("=" * 60)
    
    print()
    
    # Summary counters
    phase_count = 0
    module_count = 0
    lesson_count = 0
    phase_success = 0
    module_success = 0
    lesson_success = 0
    
    # 1. Migrate phase files
    log("Step 1: Migrating phase files", "STEP")
    phase_files = get_phase_files()
    
    if not phase_files:
        log("No phase files need migration", "INFO")
    else:
        for phase_file in phase_files:
            phase_count += 1
            success, message = migrate_phase_file(phase_file, dry_run)
            if success:
                phase_success += 1
    
    print()
    
    # 2. Migrate module files
    log("Step 2: Migrating module files to hierarchical structure", "STEP")
    module_files = get_module_files()
    
    if not module_files:
        log("No module files need migration", "INFO")
    else:
        for module_file in module_files:
            module_count += 1
            success, message = migrate_module_file(module_file, dry_run)
            if success:
                module_success += 1
    
    print()
    
    # 3. Migrate lesson directories
    log("Step 3: Migrating lesson directories to hierarchical structure", "STEP")
    lesson_dirs = get_lesson_directories()
    
    if not lesson_dirs:
        log("No lesson directories need migration", "INFO")
    else:
        for lesson_dir in lesson_dirs:
            lesson_count += 1
            success, message = migrate_lesson_directory(lesson_dir, dry_run)
            if success:
                lesson_success += 1
    
    print()
    
    # 4. Check learner-state files
    log("Step 4: Checking learner-state files for path references", "STEP")
    issues = check_learner_state_references(dry_run)
    
    has_issues = False
    for file_type, file_issues in issues.items():
        if file_issues:
            has_issues = True
            log(f"Issues found in {file_type}:", "WARNING")
            for issue in file_issues:
                log(f"  - {issue}", "WARNING")
    
    if not has_issues:
        log("No issues found in learner-state files", "INFO")
    
    print()
    
    # Summary
    log("=" * 60, "SUMMARY")
    log(f"Phase files: {phase_success}/{phase_count} migrated")
    log(f"Module files: {module_success}/{module_count} migrated")
    log(f"Lesson directories: {lesson_success}/{lesson_count} migrated")
    
    if has_issues:
        log("Learner-state files: Issues detected (manual review needed)", "WARNING")
    else:
        log("Learner-state files: No issues detected")
    
    log("=" * 60)
    
    if dry_run:
        print()
        log("This was a DRY RUN - no changes were made", "INFO")
        log("Run with --execute flag to perform actual migration:", "INFO")
        log("  python tools/migrate_to_hierarchical_structure.py --execute", "INFO")
    else:
        print()
        log("Migration complete!", "SUCCESS")
        log("Next steps:", "INFO")
        log("  1. Run: python tools/validate.py", "INFO")
        log("  2. Review changes with: git status", "INFO")
        log("  3. If satisfied, commit changes", "INFO")


if __name__ == "__main__":
    main()
