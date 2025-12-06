#!/usr/bin/env python3
"""
Schema validation script for CatchBook curriculum system.
Validates all JSON files against their corresponding schemas.
Updated to support nested lesson directory structure.
"""

import json
import sys
from pathlib import Path
from jsonschema import validate, ValidationError

def load_json(filepath):
    """Load JSON file and return parsed object."""
    with open(filepath, 'r') as f:
        return json.load(f)

def validate_file(data_file, schema_file):
    """Validate a data file against a schema."""
    try:
        data = load_json(data_file)
        schema = load_json(schema_file)
        validate(instance=data, schema=schema)
        return True, None
    except ValidationError as e:
        return False, str(e)
    except Exception as e:
        return False, f"Error loading files: {str(e)}"

def main():
    """Run validation on all curriculum and state files."""
    repo_root = Path(__file__).parent.parent
    
    validations = [
        (repo_root / "curriculum/curriculum.json", repo_root / "schemas/curriculum.schema.json"),
        (repo_root / "learner-state/current.json", repo_root / "schemas/state-current.schema.json"),
        (repo_root / "learner-state/skills.json", repo_root / "schemas/state-skills.schema.json"),
        (repo_root / "learner-state/metrics.json", repo_root / "schemas/state-metrics.schema.json"),
    ]
    
    # Validate phase files
    phase_dir = repo_root / "curriculum/phases"
    if phase_dir.exists():
        for phase_file in phase_dir.glob("P*.json"):
            validations.append((phase_file, repo_root / "schemas/phase.schema.json"))
    
    # Validate module files
    module_dir = repo_root / "curriculum/modules"
    if module_dir.exists():
        for module_file in module_dir.glob("P*-M*.json"):
            validations.append((module_file, repo_root / "schemas/module.schema.json"))
    
    # Validate lesson files (UPDATED: nested directory structure)
    lesson_dir = repo_root / "curriculum/lessons"
    if lesson_dir.exists():
        # Check for nested directories (e.g., P01-M01-L01/)
        for lesson_folder in lesson_dir.glob("P*-M*-L*"):
            if lesson_folder.is_dir():
                lesson_json = lesson_folder / "lesson.json"
                if lesson_json.exists():
                    validations.append((lesson_json, repo_root / "schemas/lesson.schema.json"))
        
        # Also check for legacy flat structure (P01-M01-L01.json)
        for lesson_file in lesson_dir.glob("P*-M*-L*.json"):
            validations.append((lesson_file, repo_root / "schemas/lesson.schema.json"))
    
    # Validate completed state files
    completed_dir = repo_root / "learner-state/completed"
    if completed_dir.exists():
        for completed_file in completed_dir.glob("P*-M*-L*.json"):
            validations.append((completed_file, repo_root / "schemas/state-completed.schema.json"))
    
    errors = []
    for data_file, schema_file in validations:
        if not data_file.exists():
            continue  # Skip missing files
        
        valid, error_msg = validate_file(data_file, schema_file)
        if valid:
            print(f"✓ {data_file.relative_to(repo_root)} — VALID")
        else:
            print(f"✗ {data_file.relative_to(repo_root)} — INVALID")
            print(f"  {error_msg}")
            errors.append(data_file)
    
    if errors:
        print(f"\n{len(errors)} file(s) failed validation.")
        sys.exit(1)
    else:
        print("\nAll files valid.")
        sys.exit(0)

if __name__ == "__main__":
    main()
    