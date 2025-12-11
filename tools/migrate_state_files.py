#!/usr/bin/env python3
"""
Migration script to fix validation errors in learner state files.

Fixes:
1. Completed lesson files: Add missing confidence_rating field
2. skills.json: Convert confidence from 0-100 to 1-5 scale
3. metrics.json: Convert consistency_score from 0-100 to 0.0-1.0
4. current.json: Already valid with updated schema (accepts "completed")

Usage:
    python3 tools/migrate_state_files.py
    python3 tools/validate.py  # Verify fixes
"""

import json
from pathlib import Path
from datetime import datetime


def convert_confidence_level_to_rating(level_str):
    """Convert qualitative confidence level to 1-5 numeric rating."""
    mapping = {
        "low": 1,
        "medium-low": 2,
        "medium": 3,
        "medium-high": 4,
        "high": 5
    }
    return mapping.get(level_str, 3)


def convert_percentage_to_five_point(value):
    """Convert 0-100 percentage to 1-5 scale."""
    if value == 0:
        return 0  # Special case for uninitialized skills
    elif value <= 20:
        return 1
    elif value <= 40:
        return 2
    elif value <= 60:
        return 3
    elif value <= 80:
        return 4
    else:
        return 5


def fix_completed_lesson_files():
    """Add missing confidence_rating field to completed lesson files."""
    repo_root = Path(__file__).parent.parent
    completed_dir = repo_root / "learner-state" / "completed"
    
    if not completed_dir.exists():
        print("No completed lessons directory found")
        return
    
    fixed_count = 0
    for lesson_file in completed_dir.glob("P*-M*-L*.json"):
        with open(lesson_file, 'r') as f:
            data = json.load(f)
        
        # Check if confidence_rating is missing
        if "confidence_rating" not in data:
            # Convert confidence_level string to numeric rating
            level_str = data.get("confidence_level", "medium")
            data["confidence_rating"] = convert_confidence_level_to_rating(level_str)
            
            # Write back
            with open(lesson_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f"✓ Fixed {lesson_file.name}: Added confidence_rating={data['confidence_rating']}")
            fixed_count += 1
        else:
            print(f"○ {lesson_file.name}: Already has confidence_rating")
    
    print(f"\nFixed {fixed_count} completed lesson file(s)")


def fix_skills_json():
    """Convert confidence values from 0-100 to 1-5 scale."""
    repo_root = Path(__file__).parent.parent
    skills_file = repo_root / "learner-state" / "skills.json"
    
    if not skills_file.exists():
        print("No skills.json found")
        return
    
    with open(skills_file, 'r') as f:
        data = json.load(f)
    
    fixed_count = 0
    for skill_name, skill_data in data.get("skills", {}).items():
        confidence = skill_data.get("confidence", 0)
        
        # Check if confidence is out of range (likely 0-100 scale)
        if confidence > 5:
            old_value = confidence
            new_value = convert_percentage_to_five_point(confidence)
            skill_data["confidence"] = new_value
            print(f"✓ Fixed {skill_name}: confidence {old_value} → {new_value}")
            fixed_count += 1
    
    if fixed_count > 0:
        with open(skills_file, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"\nFixed {fixed_count} skill(s) in skills.json")
    else:
        print("○ skills.json: All confidence values already in 1-5 range")


def fix_metrics_json():
    """Convert consistency_score and average_confidence to correct scales."""
    repo_root = Path(__file__).parent.parent
    metrics_file = repo_root / "learner-state" / "metrics.json"
    
    if not metrics_file.exists():
        print("No metrics.json found")
        return
    
    with open(metrics_file, 'r') as f:
        data = json.load(f)
    
    fixed = False
    
    # Fix consistency_score (0-100 → 0.0-1.0)
    consistency = data.get("consistency_score", 0)
    if consistency > 1:
        old_value = consistency
        new_value = consistency / 100.0
        data["consistency_score"] = new_value
        print(f"✓ Fixed consistency_score: {old_value} → {new_value}")
        fixed = True
    
    # Fix average_confidence (0-100 → 0-5)
    avg_conf = data.get("average_confidence", 0)
    if avg_conf > 5:
        old_value = avg_conf
        new_value = convert_percentage_to_five_point(avg_conf)
        data["average_confidence"] = new_value
        print(f"✓ Fixed average_confidence: {old_value} → {new_value}")
        fixed = True
    
    if fixed:
        with open(metrics_file, 'w') as f:
            json.dump(data, f, indent=2)
        print("\nFixed metrics.json")
    else:
        print("○ metrics.json: All values already in correct range")


def main():
    """Run all migration fixes."""
    print("="*60)
    print("State File Migration Script")
    print("="*60)
    print()
    
    print("Step 1: Fixing completed lesson files...")
    print("-"*60)
    fix_completed_lesson_files()
    print()
    
    print("Step 2: Fixing skills.json...")
    print("-"*60)
    fix_skills_json()
    print()
    
    print("Step 3: Fixing metrics.json...")
    print("-"*60)
    fix_metrics_json()
    print()
    
    print("="*60)
    print("Migration complete!")
    print("Run 'python3 tools/validate.py' to verify all files pass validation")
    print("="*60)


if __name__ == "__main__":
    main()
