#!/usr/bin/env python3
"""
Learner State Reset Script

⚠️  DANGER: This script will DELETE all learner progress data.
Use ONLY for troubleshooting and testing purposes.

This script resets:
1. learner-state/current.json to initial state (P01-M01-L01)
2. learner-state/skills.json to baseline novice levels
3. learner-state/metrics.json to zero progress
4. learner-state/completed/*.json files (removes all completion records)

Usage:
    python reset_learner_state.py [--confirm]

Without --confirm flag, script runs in dry-run mode and shows what would be deleted.
"""

import json
import os
import shutil
from datetime import datetime
from pathlib import Path
import argparse


# Repository root directory (parent of tools/)
REPO_ROOT = Path(__file__).parent.parent
LEARNER_STATE_DIR = REPO_ROOT / "learner-state"
COMPLETED_DIR = LEARNER_STATE_DIR / "completed"


def get_initial_current_state():
    """Return initial current.json structure."""
    return {
        "learner_id": "jeff",
        "current_phase_id": "P01",
        "current_module_id": "P01-M01",
        "current_lesson_id": "P01-M01-L01",
        "last_updated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    }


def get_initial_skills():
    """Return initial skills.json structure."""
    return {
        "skills": {
            "git_basics": {
                "level": "novice",
                "last_practiced": None,
                "confidence": 0,
                "modules_practiced": []
            },
            "terminal_comfort": {
                "level": "novice",
                "last_practiced": None,
                "confidence": 0,
                "modules_practiced": []
            },
            "html_css": {
                "level": "novice",
                "last_practiced": None,
                "confidence": 0,
                "modules_practiced": []
            },
            "javascript_basics": {
                "level": "novice",
                "last_practiced": None,
                "confidence": 0,
                "modules_practiced": []
            },
            "python_basics": {
                "level": "novice",
                "last_practiced": None,
                "confidence": 0,
                "modules_practiced": []
            },
            "react_fundamentals": {
                "level": "novice",
                "last_practiced": None,
                "confidence": 0,
                "modules_practiced": []
            },
            "backend_api_development": {
                "level": "novice",
                "last_practiced": None,
                "confidence": 0,
                "modules_practiced": []
            },
            "database_design": {
                "level": "novice",
                "last_practiced": None,
                "confidence": 0,
                "modules_practiced": []
            },
            "markdown_documentation": {
                "level": "novice",
                "last_practiced": None,
                "confidence": 0,
                "modules_practiced": []
            },
            "project_organization": {
                "level": "novice",
                "last_practiced": None,
                "confidence": 0,
                "modules_practiced": []
            }
        },
        "last_updated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    }


def get_initial_metrics():
    """Return initial metrics.json structure."""
    return {
        "total_time_minutes": 0,
        "lessons_completed": 0,
        "modules_completed": 0,
        "phases_completed": 0,
        "catchbook_features_shipped": 0,
        "reflections_written": 0,
        "average_confidence": 0,
        "consistency_score": 0,
        "last_updated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "lesson_history": []
    }


def get_completed_files():
    """Get list of all completion record files."""
    if not COMPLETED_DIR.exists():
        return []
    
    return [
        f for f in COMPLETED_DIR.iterdir() 
        if f.is_file() and f.suffix == '.json' and f.name != '.gitkeep'
    ]


def print_current_state():
    """Print current learner state summary."""
    print("\n" + "="*70)
    print("CURRENT LEARNER STATE")
    print("="*70)
    
    # Read current position
    if (LEARNER_STATE_DIR / "current.json").exists():
        with open(LEARNER_STATE_DIR / "current.json", 'r') as f:
            current = json.load(f)
        print(f"\n📍 Current Position:")
        print(f"   Phase:  {current.get('current_phase_id', 'N/A')}")
        print(f"   Module: {current.get('current_module_id', 'N/A')}")
        print(f"   Lesson: {current.get('current_lesson_id', 'N/A')}")
    
    # Read metrics
    if (LEARNER_STATE_DIR / "metrics.json").exists():
        with open(LEARNER_STATE_DIR / "metrics.json", 'r') as f:
            metrics = json.load(f)
        print(f"\n📊 Progress:")
        print(f"   Lessons completed: {metrics.get('lessons_completed', 0)}")
        print(f"   Modules completed: {metrics.get('modules_completed', 0)}")
        print(f"   Time invested:     {metrics.get('total_time_minutes', 0)} minutes")
        print(f"   Avg confidence:    {metrics.get('average_confidence', 0)}")
    
    # Count completed lessons
    completed_files = get_completed_files()
    print(f"\n📝 Completion Records:")
    print(f"   Files in completed/: {len(completed_files)}")
    if completed_files:
        for f in completed_files:
            print(f"      - {f.name}")
    
    print("\n" + "="*70)


def reset_learner_state(dry_run=True):
    """
    Reset all learner state files to initial values.
    
    Args:
        dry_run: If True, only shows what would be done without making changes
    """
    mode = "DRY RUN MODE (no changes will be made)" if dry_run else "LIVE MODE (changes will be applied)"
    print(f"\n{'='*70}")
    print(f"LEARNER STATE RESET - {mode}")
    print(f"{'='*70}\n")
    
    actions = []
    
    # 1. Reset current.json
    current_path = LEARNER_STATE_DIR / "current.json"
    if current_path.exists():
        actions.append(f"✏️  Reset current.json to P01-M01-L01")
        if not dry_run:
            with open(current_path, 'w') as f:
                json.dump(get_initial_current_state(), f, indent=2)
    else:
        actions.append(f"⚠️  current.json not found, will create")
        if not dry_run:
            with open(current_path, 'w') as f:
                json.dump(get_initial_current_state(), f, indent=2)
    
    # 2. Reset skills.json
    skills_path = LEARNER_STATE_DIR / "skills.json"
    if skills_path.exists():
        actions.append(f"✏️  Reset skills.json to baseline novice levels")
        if not dry_run:
            with open(skills_path, 'w') as f:
                json.dump(get_initial_skills(), f, indent=2)
    else:
        actions.append(f"⚠️  skills.json not found, will create")
        if not dry_run:
            with open(skills_path, 'w') as f:
                json.dump(get_initial_skills(), f, indent=2)
    
    # 3. Reset metrics.json
    metrics_path = LEARNER_STATE_DIR / "metrics.json"
    if metrics_path.exists():
        actions.append(f"✏️  Reset metrics.json to zero progress")
        if not dry_run:
            with open(metrics_path, 'w') as f:
                json.dump(get_initial_metrics(), f, indent=2)
    else:
        actions.append(f"⚠️  metrics.json not found, will create")
        if not dry_run:
            with open(metrics_path, 'w') as f:
                json.dump(get_initial_metrics(), f, indent=2)
    
    # 4. Delete completion records
    completed_files = get_completed_files()
    if completed_files:
        actions.append(f"\n🗑️  Delete {len(completed_files)} completion record(s):")
        for f in completed_files:
            actions.append(f"   - {f.name}")
            if not dry_run:
                f.unlink()
    else:
        actions.append(f"\n✅ No completion records to delete")
    
    # Print all actions
    print("Actions to perform:\n")
    for action in actions:
        print(action)
    
    if dry_run:
        print(f"\n{'='*70}")
        print("DRY RUN COMPLETE - No changes were made")
        print("Run with --confirm flag to apply changes")
        print(f"{'='*70}\n")
    else:
        print(f"\n{'='*70}")
        print("✅ RESET COMPLETE - All learner state has been reset")
        print(f"{'='*70}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Reset learner state to initial values (DESTRUCTIVE OPERATION)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Show what would be reset (dry run)
  python reset_learner_state.py
  
  # Actually reset all learner state (DESTRUCTIVE)
  python reset_learner_state.py --confirm
        """
    )
    parser.add_argument(
        '--confirm',
        action='store_true',
        help='Confirm reset operation (without this, script runs in dry-run mode)'
    )
    
    args = parser.parse_args()
    
    # Show current state before reset
    print_current_state()
    
    # Perform reset (dry run by default)
    reset_learner_state(dry_run=not args.confirm)
    
    # If changes were made, show new state
    if args.confirm:
        print("\nVerifying reset state...")
        print_current_state()


if __name__ == "__main__":
    main()
