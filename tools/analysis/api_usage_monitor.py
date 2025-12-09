#!/usr/bin/env python3
"""
API Usage Monitor
=================

Track actual Anthropic API usage and costs for the dev-curriculum system.
Integrates with Anthropic's usage API to provide real-time cost tracking.

Setup:
1. Set ANTHROPIC_API_KEY environment variable
2. Run this script to fetch usage data
3. Compare actual vs estimated costs
"""

import os
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import anthropic

def get_usage_data(days: int = 30) -> Dict:
    """
    Fetch actual usage data from Anthropic API.
    
    Note: As of Dec 2024, Anthropic doesn't have a public usage API endpoint.
    Check your dashboard at: https://console.anthropic.com/settings/billing
    
    For now, this is a template. When the API becomes available, update this function.
    """
    
    # Placeholder - replace with actual API call when available
    print("⚠️  Anthropic doesn't currently provide a public usage API.")
    print("   Check your usage at: https://console.anthropic.com/settings/billing")
    print()
    print("   To track usage manually:")
    print("   1. Note your current token usage")
    print("   2. Run your dev-curriculum operations")
    print("   3. Note the new token usage")
    print("   4. Calculate the difference")
    print()
    
    return {
        "error": "No public usage API available",
        "manual_tracking_required": True,
        "dashboard_url": "https://console.anthropic.com/settings/billing"
    }


def calculate_cost_from_usage(input_tokens: int, output_tokens: int, model: str) -> float:
    """Calculate cost from token counts"""
    
    PRICING = {
        "claude-sonnet-4": {"input": 3.00, "output": 15.00},
        "claude-sonnet-3.5": {"input": 3.00, "output": 15.00},
        "claude-haiku-3": {"input": 0.25, "output": 1.25},
    }
    
    if model not in PRICING:
        print(f"Unknown model: {model}")
        return 0.0
    
    pricing = PRICING[model]
    input_cost = (input_tokens / 1_000_000) * pricing["input"]
    output_cost = (output_tokens / 1_000_000) * pricing["output"]
    
    return input_cost + output_cost


def log_operation(
    operation_type: str,
    input_tokens: int,
    output_tokens: int,
    model: str,
    lesson_id: Optional[str] = None,
    notes: Optional[str] = None
):
    """
    Log an API operation for tracking.
    
    Creates a JSON log file that you can analyze later.
    """
    
    log_file = "api_usage_log.jsonl"
    
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "operation_type": operation_type,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "model": model,
        "cost": calculate_cost_from_usage(input_tokens, output_tokens, model),
        "lesson_id": lesson_id,
        "notes": notes
    }
    
    with open(log_file, 'a') as f:
        f.write(json.dumps(log_entry) + '\n')
    
    print(f"✅ Logged operation: {operation_type}")
    print(f"   Tokens: {input_tokens:,} in / {output_tokens:,} out")
    print(f"   Cost: ${log_entry['cost']:.4f}")


def analyze_usage_log(log_file: str = "api_usage_log.jsonl"):
    """Analyze the usage log and generate a report"""
    
    if not os.path.exists(log_file):
        print(f"No usage log found at {log_file}")
        return
    
    operations = []
    with open(log_file, 'r') as f:
        for line in f:
            operations.append(json.loads(line))
    
    if not operations:
        print("No operations logged yet")
        return
    
    # Aggregate by operation type
    by_type = {}
    for op in operations:
        op_type = op['operation_type']
        if op_type not in by_type:
            by_type[op_type] = {
                'count': 0,
                'total_input': 0,
                'total_output': 0,
                'total_cost': 0.0
            }
        
        by_type[op_type]['count'] += 1
        by_type[op_type]['total_input'] += op['input_tokens']
        by_type[op_type]['total_output'] += op['output_tokens']
        by_type[op_type]['total_cost'] += op['cost']
    
    # Print report
    print("=" * 80)
    print("API USAGE REPORT")
    print("=" * 80)
    print(f"\nTotal operations: {len(operations)}")
    print(f"Date range: {operations[0]['timestamp']} to {operations[-1]['timestamp']}")
    
    print("\n" + "=" * 80)
    print("BY OPERATION TYPE")
    print("=" * 80)
    
    total_cost = 0.0
    print(f"\n{'Operation':<25} {'Count':<8} {'Avg Input':<12} {'Avg Output':<12} {'Total Cost':<12}")
    print("-" * 80)
    
    for op_type, stats in sorted(by_type.items()):
        avg_input = stats['total_input'] / stats['count']
        avg_output = stats['total_output'] / stats['count']
        print(f"{op_type:<25} {stats['count']:<8} {avg_input:<12,.0f} {avg_output:<12,.0f} ${stats['total_cost']:<11,.2f}")
        total_cost += stats['total_cost']
    
    print("-" * 80)
    print(f"{'TOTAL':<25} {len(operations):<8} {'':<12} {'':<12} ${total_cost:<11,.2f}")
    
    print("\n" + "=" * 80)
    print("COST PROJECTIONS")
    print("=" * 80)
    
    # Estimate cost per learner based on actual usage
    eval_cost = by_type.get('evaluation', {}).get('total_cost', 0) / max(by_type.get('evaluation', {}).get('count', 1), 1)
    advisory_cost = by_type.get('advisory', {}).get('total_cost', 0) / max(by_type.get('advisory', {}).get('count', 1), 1)
    
    lessons_completed = len(set(op['lesson_id'] for op in operations if op.get('lesson_id')))
    total_lessons = 496  # from curriculum
    
    if lessons_completed > 0:
        cost_per_lesson = (eval_cost + advisory_cost)
        estimated_cost_per_learner = cost_per_lesson * total_lessons
        
        print(f"\nBased on {lessons_completed} completed lessons:")
        print(f"  Avg cost per lesson: ${cost_per_lesson:.2f}")
        print(f"  Estimated cost per learner: ${estimated_cost_per_learner:.2f}")
        
        print(f"\nProjected costs at scale:")
        for users in [100, 500, 1000]:
            total = estimated_cost_per_learner * users
            print(f"  {users:4} users: ${total:,.2f}")


def main():
    """Main entry point"""
    
    print("=" * 80)
    print("DEV-CURRICULUM API USAGE MONITOR")
    print("=" * 80)
    
    print("\nThis tool helps you track actual API costs for your dev-curriculum system.")
    print()
    
    print("Available commands:")
    print("  1. Fetch usage data (from Anthropic dashboard)")
    print("  2. Log an operation manually")
    print("  3. Analyze usage log")
    print("  4. Exit")
    
    while True:
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == "1":
            usage = get_usage_data()
            print(json.dumps(usage, indent=2))
        
        elif choice == "2":
            print("\nManual operation logging:")
            op_type = input("  Operation type (lesson_generation, evaluation, advisory): ")
            input_tokens = int(input("  Input tokens: "))
            output_tokens = int(input("  Output tokens: "))
            model = input("  Model (claude-sonnet-3.5, claude-haiku-3): ")
            lesson_id = input("  Lesson ID (optional): ") or None
            notes = input("  Notes (optional): ") or None
            
            log_operation(op_type, input_tokens, output_tokens, model, lesson_id, notes)
        
        elif choice == "3":
            analyze_usage_log()
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
