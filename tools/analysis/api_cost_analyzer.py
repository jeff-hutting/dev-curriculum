#!/usr/bin/env python3
"""
API Cost Analyzer for dev-curriculum Project
==============================================

Estimates Claude API costs based on curriculum structure and lesson generation patterns.
Uses current Anthropic pricing as of December 2024.

Pricing Reference (as of Dec 2024):
- Claude Sonnet 4: $3 per MTok input, $15 per MTok output
- Claude Sonnet 3.5: $3 per MTok input, $15 per MTok output  
- Claude Haiku 3: $0.25 per MTok input, $1.25 per MTok output
"""

import json
import csv
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, field

# Anthropic Pricing (December 2024)
PRICING = {
    "sonnet-4": {"input": 3.00, "output": 15.00},      # per MTok
    "sonnet-3.5": {"input": 3.00, "output": 15.00},    # per MTok
    "haiku-3": {"input": 0.25, "output": 1.25},        # per MTok
}

@dataclass
class TokenEstimates:
    """Token usage estimates for different operation types"""
    
    # Lesson generation (Professor role)
    lesson_generation_input: int = 8000      # System prompt + lesson JSON + examples
    lesson_generation_output: int = 6000     # Full lesson markdown document
    
    # Curriculum design (Designer role)
    curriculum_design_input: int = 5000      # Specs + schemas + examples
    curriculum_design_output: int = 3000     # Lesson JSON file
    
    # Evaluation (Evaluator role)
    evaluation_input: int = 3000             # Rubric + learner work
    evaluation_output: int = 1500            # Feedback + scoring
    
    # Advisory (Advisor role)
    advisory_input: int = 2000               # Learner state + curriculum
    advisory_output: int = 800               # Recommendations
    
    # Architecture validation (Architect role)
    architecture_input: int = 4000           # Schemas + files to validate
    architecture_output: int = 2000          # Validation report


@dataclass
class CostBreakdown:
    """Detailed cost breakdown for different operations"""
    lesson_generation_cost: float = 0.0
    curriculum_design_cost: float = 0.0
    evaluation_cost: float = 0.0
    advisory_cost: float = 0.0
    architecture_cost: float = 0.0
    total_cost: float = 0.0
    
    def add(self, other: 'CostBreakdown') -> 'CostBreakdown':
        """Add two cost breakdowns together"""
        return CostBreakdown(
            lesson_generation_cost=self.lesson_generation_cost + other.lesson_generation_cost,
            curriculum_design_cost=self.curriculum_design_cost + other.curriculum_design_cost,
            evaluation_cost=self.evaluation_cost + other.evaluation_cost,
            advisory_cost=self.advisory_cost + other.advisory_cost,
            architecture_cost=self.architecture_cost + other.architecture_cost,
            total_cost=self.total_cost + other.total_cost
        )


class CostAnalyzer:
    """Analyzes API costs for the dev-curriculum system"""
    
    def __init__(self, 
                 curriculum_csv: Path,
                 model: str = "sonnet-3.5",
                 estimates: Optional[TokenEstimates] = None):
        self.curriculum_csv = curriculum_csv
        self.model = model
        self.pricing = PRICING[model]
        self.estimates = estimates or TokenEstimates()
        self.curriculum_data = self._load_curriculum()
        
    def _load_curriculum(self) -> List[Dict]:
        """Load curriculum from CSV"""
        with open(self.curriculum_csv, 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    def _calculate_operation_cost(self, input_tokens: int, output_tokens: int) -> float:
        """Calculate cost for a single API operation"""
        input_cost = (input_tokens / 1_000_000) * self.pricing["input"]
        output_cost = (output_tokens / 1_000_000) * self.pricing["output"]
        return input_cost + output_cost
    
    def estimate_lesson_generation_cost(self) -> CostBreakdown:
        """
        Estimate cost to generate all lesson documents.
        
        Assumes:
        - Each module has 3-5 lessons (avg 4)
        - Each lesson requires 1 generation call
        """
        total_modules = len(self.curriculum_data)
        avg_lessons_per_module = 4
        total_lessons = total_modules * avg_lessons_per_module
        
        cost_per_lesson = self._calculate_operation_cost(
            self.estimates.lesson_generation_input,
            self.estimates.lesson_generation_output
        )
        
        total_cost = cost_per_lesson * total_lessons
        
        return CostBreakdown(
            lesson_generation_cost=total_cost,
            total_cost=total_cost
        )
    
    def estimate_curriculum_design_cost(self) -> CostBreakdown:
        """
        Estimate cost to generate all lesson JSON files.
        
        Assumes:
        - Each module has 3-5 lessons (avg 4)
        - Each lesson JSON requires 1 design call
        """
        total_modules = len(self.curriculum_data)
        avg_lessons_per_module = 4
        total_lessons = total_modules * avg_lessons_per_module
        
        cost_per_design = self._calculate_operation_cost(
            self.estimates.curriculum_design_input,
            self.estimates.curriculum_design_output
        )
        
        total_cost = cost_per_design * total_lessons
        
        return CostBreakdown(
            curriculum_design_cost=total_cost,
            total_cost=total_cost
        )
    
    def estimate_evaluation_cost(self, evaluations_per_lesson: int = 2) -> CostBreakdown:
        """
        Estimate cost for evaluating learner work.
        
        Args:
            evaluations_per_lesson: Number of evaluation calls per lesson
                (checkpoint + final assessment)
        """
        total_modules = len(self.curriculum_data)
        avg_lessons_per_module = 4
        total_lessons = total_modules * avg_lessons_per_module
        
        cost_per_eval = self._calculate_operation_cost(
            self.estimates.evaluation_input,
            self.estimates.evaluation_output
        )
        
        total_cost = cost_per_eval * total_lessons * evaluations_per_lesson
        
        return CostBreakdown(
            evaluation_cost=total_cost,
            total_cost=total_cost
        )
    
    def estimate_advisory_cost(self, advisor_calls_per_lesson: int = 1) -> CostBreakdown:
        """
        Estimate cost for progress recommendations.
        
        Args:
            advisor_calls_per_lesson: Advisory checks per lesson
        """
        total_modules = len(self.curriculum_data)
        avg_lessons_per_module = 4
        total_lessons = total_modules * avg_lessons_per_module
        
        cost_per_advisory = self._calculate_operation_cost(
            self.estimates.advisory_input,
            self.estimates.advisory_output
        )
        
        total_cost = cost_per_advisory * total_lessons * advisor_calls_per_lesson
        
        return CostBreakdown(
            advisory_cost=total_cost,
            total_cost=total_cost
        )
    
    def estimate_architecture_cost(self, validations: int = 10) -> CostBreakdown:
        """
        Estimate cost for architecture validation.
        
        Args:
            validations: Number of major validation passes during development
        """
        cost_per_validation = self._calculate_operation_cost(
            self.estimates.architecture_input,
            self.estimates.architecture_output
        )
        
        total_cost = cost_per_validation * validations
        
        return CostBreakdown(
            architecture_cost=total_cost,
            total_cost=total_cost
        )
    
    def estimate_per_learner_cost(self) -> CostBreakdown:
        """
        Estimate total cost per learner completing the curriculum.
        
        Includes:
        - Lesson generation (one-time, but amortized per learner)
        - Evaluation (per learner)
        - Advisory (per learner)
        """
        # One-time costs (amortized over first 100 learners)
        lesson_gen = self.estimate_lesson_generation_cost()
        curriculum_design = self.estimate_curriculum_design_cost()
        architecture = self.estimate_architecture_cost()
        
        one_time_costs = lesson_gen.add(curriculum_design).add(architecture)
        one_time_per_learner = CostBreakdown(
            lesson_generation_cost=one_time_costs.lesson_generation_cost / 100,
            curriculum_design_cost=one_time_costs.curriculum_design_cost / 100,
            architecture_cost=one_time_costs.architecture_cost / 100,
            total_cost=one_time_costs.total_cost / 100
        )
        
        # Per-learner costs
        evaluation = self.estimate_evaluation_cost()
        advisory = self.estimate_advisory_cost()
        
        return one_time_per_learner.add(evaluation).add(advisory)
    
    def estimate_system_setup_cost(self) -> CostBreakdown:
        """
        Estimate one-time cost to set up the entire system.
        
        Includes:
        - All lesson generation
        - All curriculum design
        - Initial architecture validation
        """
        lesson_gen = self.estimate_lesson_generation_cost()
        curriculum_design = self.estimate_curriculum_design_cost()
        architecture = self.estimate_architecture_cost()
        
        return lesson_gen.add(curriculum_design).add(architecture)
    
    def print_detailed_report(self):
        """Generate a comprehensive cost analysis report"""
        
        print("=" * 80)
        print("DEV-CURRICULUM API COST ANALYSIS")
        print("=" * 80)
        print(f"\nModel: Claude {self.model}")
        print(f"Pricing: ${self.pricing['input']}/MTok input, ${self.pricing['output']}/MTok output")
        print(f"\nCurriculum Size:")
        print(f"  - Modules: {len(self.curriculum_data)}")
        print(f"  - Est. Lessons: {len(self.curriculum_data) * 4} (avg 4 per module)")
        
        print("\n" + "=" * 80)
        print("SYSTEM SETUP COSTS (One-time)")
        print("=" * 80)
        setup = self.estimate_system_setup_cost()
        print(f"\nLesson Generation:      ${setup.lesson_generation_cost:,.2f}")
        print(f"Curriculum Design:      ${setup.curriculum_design_cost:,.2f}")
        print(f"Architecture Validation: ${setup.architecture_cost:,.2f}")
        print(f"\nTotal Setup Cost:       ${setup.total_cost:,.2f}")
        
        print("\n" + "=" * 80)
        print("PER-LEARNER COSTS (Ongoing)")
        print("=" * 80)
        per_learner = self.estimate_per_learner_cost()
        print(f"\nLesson Access (amortized): ${per_learner.lesson_generation_cost:,.2f}")
        print(f"Evaluation:                ${per_learner.evaluation_cost:,.2f}")
        print(f"Advisory:                  ${per_learner.advisory_cost:,.2f}")
        print(f"\nTotal Per Learner:         ${per_learner.total_cost:,.2f}")
        
        print("\n" + "=" * 80)
        print("SCALING ANALYSIS")
        print("=" * 80)
        
        learner_counts = [1, 10, 50, 100, 500, 1000]
        print(f"\n{'Learners':<12} {'Setup Cost':<15} {'Ongoing Cost':<15} {'Total Cost':<15} {'Cost/Learner':<15}")
        print("-" * 80)
        
        for count in learner_counts:
            ongoing_cost = per_learner.total_cost * count
            total = setup.total_cost + ongoing_cost
            cost_per = total / count
            print(f"{count:<12} ${setup.total_cost:<14,.2f} ${ongoing_cost:<14,.2f} ${total:<14,.2f} ${cost_per:<14,.2f}")
        
        print("\n" + "=" * 80)
        print("OPTIMIZATION STRATEGIES")
        print("=" * 80)
        print("\n1. Use Haiku for simple operations:")
        haiku_analyzer = CostAnalyzer(self.curriculum_csv, model="haiku-3")
        haiku_per_learner = haiku_analyzer.estimate_per_learner_cost()
        savings = per_learner.total_cost - haiku_per_learner.total_cost
        print(f"   Haiku per learner: ${haiku_per_learner.total_cost:,.2f}")
        print(f"   Savings: ${savings:,.2f} ({(savings/per_learner.total_cost)*100:.1f}%)")
        
        print("\n2. Cache generated lessons:")
        print(f"   Setup cost amortized over 100 learners: ${setup.total_cost/100:,.2f}/learner")
        print(f"   Setup cost amortized over 1000 learners: ${setup.total_cost/1000:,.2f}/learner")
        
        print("\n3. Reduce evaluation frequency:")
        reduced_eval = self.estimate_evaluation_cost(evaluations_per_lesson=1)
        eval_savings = per_learner.evaluation_cost - reduced_eval.total_cost
        print(f"   1 eval/lesson instead of 2: ${eval_savings:,.2f} savings/learner")
        
        print("\n" + "=" * 80)
        print("BREAK-EVEN ANALYSIS (at $49/learner price point)")
        print("=" * 80)
        revenue_per_learner = 49.00
        profit_per_learner = revenue_per_learner - per_learner.total_cost
        break_even_learners = setup.total_cost / profit_per_learner if profit_per_learner > 0 else float('inf')
        
        print(f"\nRevenue per learner:    ${revenue_per_learner:,.2f}")
        print(f"Cost per learner:       ${per_learner.total_cost:,.2f}")
        print(f"Profit per learner:     ${profit_per_learner:,.2f}")
        print(f"\nBreak-even point:       {break_even_learners:,.0f} learners")
        
        if break_even_learners < float('inf'):
            print(f"Revenue at break-even:  ${break_even_learners * revenue_per_learner:,.2f}")
            print(f"\nAt 100 learners:        ${(revenue_per_learner * 100) - (setup.total_cost + per_learner.total_cost * 100):,.2f} profit")
            print(f"At 500 learners:        ${(revenue_per_learner * 500) - (setup.total_cost + per_learner.total_cost * 500):,.2f} profit")
            print(f"At 1000 learners:       ${(revenue_per_learner * 1000) - (setup.total_cost + per_learner.total_cost * 1000):,.2f} profit")


def main():
    """Run the cost analysis"""
    curriculum_csv = Path("/mnt/user-data/uploads/catchbook-curriculum-v1.csv")
    
    if not curriculum_csv.exists():
        print(f"Error: Curriculum file not found at {curriculum_csv}")
        return
    
    # Analyze with Sonnet 3.5 (current default)
    analyzer = CostAnalyzer(curriculum_csv, model="sonnet-3.5")
    analyzer.print_detailed_report()
    
    print("\n\n" + "=" * 80)
    print("TOKEN ASSUMPTIONS")
    print("=" * 80)
    estimates = analyzer.estimates
    print(f"\nLesson Generation: {estimates.lesson_generation_input:,} input + {estimates.lesson_generation_output:,} output tokens")
    print(f"Curriculum Design: {estimates.curriculum_design_input:,} input + {estimates.curriculum_design_output:,} output tokens")
    print(f"Evaluation: {estimates.evaluation_input:,} input + {estimates.evaluation_output:,} output tokens")
    print(f"Advisory: {estimates.advisory_input:,} input + {estimates.advisory_output:,} output tokens")
    print(f"Architecture: {estimates.architecture_input:,} input + {estimates.architecture_output:,} output tokens")
    print("\nNote: These are estimates. Actual usage may vary based on:")
    print("  - Lesson complexity and length")
    print("  - Number of iterations during lesson generation")
    print("  - Learner interaction patterns")
    print("  - System prompt engineering efficiency")


if __name__ == "__main__":
    main()
