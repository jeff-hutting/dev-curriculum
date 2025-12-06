# Curriculum Tools

Utility scripts for managing the dev-curriculum system.

## Scripts

### reset_learner_state.py

**⚠️ DESTRUCTIVE OPERATION - Use with caution**

Resets all learner progress to initial state. Use for troubleshooting and testing only.

**What it resets:**
- `learner-state/current.json` → P01-M01-L01
- `learner-state/skills.json` → All skills to novice/0 confidence
- `learner-state/metrics.json` → All progress counters to 0
- `learner-state/completed/*.json` → Deletes all completion records

**Usage:**

```bash
# Dry run (shows what would be reset, makes no changes)
python tools/reset_learner_state.py

# Actually reset (DESTRUCTIVE)
python tools/reset_learner_state.py --confirm
```

**Example output:**
```
======================================================================
CURRENT LEARNER STATE
======================================================================

📍 Current Position:
   Phase:  P01
   Module: P01-M01
   Lesson: P01-M01-L02

📊 Progress:
   Lessons completed: 1
   Modules completed: 0
   Time invested:     90 minutes
   Avg confidence:    4.5

📝 Completion Records:
   Files in completed/: 1
      - P01-M01-L01.json

======================================================================
LEARNER STATE RESET - DRY RUN MODE (no changes will be made)
======================================================================

Actions to perform:

✏️  Reset current.json to P01-M01-L01
✏️  Reset skills.json to baseline novice levels
✏️  Reset metrics.json to zero progress

🗑️  Delete 1 completion record(s):
   - P01-M01-L01.json

======================================================================
DRY RUN COMPLETE - No changes were made
Run with --confirm flag to apply changes
======================================================================
```

### validate.py

Schema validation script (existing).

### migrate_lessons.py

Lesson file migration utility (existing).

## Safety Features

All destructive scripts include:
- Dry-run mode by default
- Explicit `--confirm` flag required for changes
- Before/after state display
- Clear action descriptions

## Adding New Tools

When adding utility scripts:
1. Include docstring explaining purpose and usage
2. Add dry-run mode for destructive operations
3. Require explicit confirmation flag
4. Update this README
5. Test in safe environment first
