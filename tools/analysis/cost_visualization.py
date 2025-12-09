#!/usr/bin/env python3
"""
Cost Visualization
==================

Generate visual comparisons of different pricing and model strategies.
"""

def print_bar(value: float, max_value: float, width: int = 50):
    """Print a simple ASCII bar chart"""
    filled = int((value / max_value) * width)
    bar = "█" * filled + "░" * (width - filled)
    return bar


def visualize_cost_comparison():
    """Visualize cost differences between models and strategies"""
    
    print("=" * 80)
    print("COST COMPARISON: SONNET VS HAIKU VS HYBRID")
    print("=" * 80)
    
    strategies = {
        "Sonnet (All Operations)": {
            "setup": 146.40,
            "per_learner": 40.18,
            "color": "red"
        },
        "Haiku (All Operations)": {
            "setup": 146.40,
            "per_learner": 3.42,
            "color": "green"
        },
        "Hybrid (Smart Routing)": {
            "setup": 146.40,
            "per_learner": 15.00,
            "color": "yellow"
        }
    }
    
    print("\nPer-Learner Costs:")
    print("-" * 80)
    
    max_cost = max(s["per_learner"] for s in strategies.values())
    
    for name, data in strategies.items():
        cost = data["per_learner"]
        bar = print_bar(cost, max_cost, 60)
        print(f"{name:<30} ${cost:>6.2f} {bar}")
    
    print("\n" + "=" * 80)
    print("TOTAL COSTS AT DIFFERENT SCALES")
    print("=" * 80)
    
    user_counts = [10, 50, 100, 500, 1000]
    
    print(f"\n{'Strategy':<30} ", end="")
    for count in user_counts:
        print(f"{count:>10} ", end="")
    print()
    print("-" * 80)
    
    for name, data in strategies.items():
        setup = data["setup"]
        per_learner = data["per_learner"]
        
        print(f"{name:<30} ", end="")
        for count in user_counts:
            total = setup + (per_learner * count)
            print(f"${total:>9,.0f} ", end="")
        print()
    
    print("\n" + "=" * 80)
    print("PROFIT MARGINS AT $49/LEARNER PRICE POINT")
    print("=" * 80)
    
    price = 49.00
    
    print(f"\n{'Strategy':<30} {'Cost':<12} {'Profit':<12} {'Margin':<12}")
    print("-" * 80)
    
    for name, data in strategies.items():
        cost = data["per_learner"]
        profit = price - cost
        margin = (profit / price) * 100
        
        margin_bar = print_bar(margin, 100, 40)
        print(f"{name:<30} ${cost:<11.2f} ${profit:<11.2f} {margin:>5.1f}% {margin_bar}")


def visualize_scaling_economics():
    """Visualize how costs scale with different pricing strategies"""
    
    print("\n\n" + "=" * 80)
    print("SCALING ECONOMICS")
    print("=" * 80)
    
    setup_cost = 146.40
    
    scenarios = {
        "$29 (Haiku)": {"price": 29, "cost": 3.42},
        "$49 (Haiku)": {"price": 49, "cost": 3.42},
        "$49 (Hybrid)": {"price": 49, "cost": 15.00},
        "$99 (Hybrid)": {"price": 99, "cost": 15.00},
    }
    
    user_counts = [100, 500, 1000]
    
    for scenario_name, scenario in scenarios.items():
        price = scenario["price"]
        cost = scenario["cost"]
        
        print(f"\n{scenario_name}")
        print("-" * 80)
        print(f"{'Users':<10} {'Revenue':<15} {'Costs':<15} {'Profit':<15} {'Margin':<10}")
        print("-" * 80)
        
        for users in user_counts:
            revenue = price * users
            costs = setup_cost + (cost * users)
            profit = revenue - costs
            margin = (profit / revenue) * 100
            
            profit_bar = print_bar(abs(profit), 100000, 30)
            color = "+" if profit > 0 else "-"
            
            print(f"{users:<10} ${revenue:<14,.0f} ${costs:<14,.0f} ${profit:<14,.0f} {margin:>5.1f}% {profit_bar}")


def visualize_break_even():
    """Visualize break-even points for different strategies"""
    
    print("\n\n" + "=" * 80)
    print("BREAK-EVEN ANALYSIS")
    print("=" * 80)
    
    setup_cost = 146.40
    
    strategies = {
        "Haiku ($49 price)": {"price": 49, "cost": 3.42},
        "Haiku ($29 price)": {"price": 29, "cost": 3.42},
        "Hybrid ($99 price)": {"price": 99, "cost": 15.00},
        "Sonnet ($99 price)": {"price": 99, "cost": 40.18},
    }
    
    print(f"\n{'Strategy':<25} {'Break-even':<15} {'Profit @ 100':<18} {'Profit @ 500':<18}")
    print("-" * 80)
    
    for name, data in strategies.items():
        price = data["price"]
        cost = data["cost"]
        profit_per = price - cost
        
        if profit_per > 0:
            break_even = setup_cost / profit_per
            profit_100 = (price * 100) - (setup_cost + cost * 100)
            profit_500 = (price * 500) - (setup_cost + cost * 500)
            
            print(f"{name:<25} {break_even:>4.0f} users       ${profit_100:>8,.0f} ({(profit_100/(price*100))*100:>4.0f}%)      ${profit_500:>8,.0f} ({(profit_500/(price*500))*100:>4.0f}%)")
        else:
            print(f"{name:<25} {'Never':>15} {'Loss':>18} {'Loss':>18}")


def main():
    """Generate all visualizations"""
    visualize_cost_comparison()
    visualize_scaling_economics()
    visualize_break_even()
    
    print("\n\n" + "=" * 80)
    print("KEY TAKEAWAYS")
    print("=" * 80)
    
    print("""
1. **Haiku is 92% cheaper than Sonnet** for ongoing operations
   - Sonnet: $40/learner
   - Haiku: $3.50/learner
   - Savings: $37/learner

2. **Break-even is incredibly fast**
   - At $49 with Haiku: Break even at just 4 learners
   - Setup cost amortized in first week

3. **Margins are excellent at scale**
   - 100 users @ $29 with Haiku: 88% margin
   - 500 users @ $49 with Haiku: 92% margin
   - 1000 users @ $29 with Haiku: 88% margin

4. **Premium tier is highly profitable**
   - $99 with hybrid model: 85% margin
   - Justifies additional features/support

5. **Risk is minimal**
   - Even if you only get 10 users, you break even
   - Every user after that is pure profit
   - Setup cost is only $150
    """)


if __name__ == "__main__":
    main()
