# API Cost Analysis Tools

Three Python tools to help you estimate, monitor, and optimize Claude API costs for your dev-curriculum product.

## Tools Overview

### 1. `api_cost_analyzer.py` - Cost Estimation

**Purpose:** Estimate API costs based on curriculum structure and typical usage patterns.

**Usage:**
```bash
python api_cost_analyzer.py
```

**Outputs:**
- System setup costs (one-time lesson generation)
- Per-learner costs (evaluation + advisory)
- Scaling analysis (1 to 1000 users)
- Break-even analysis
- Optimization strategies

**When to use:** During planning phase, before building the product.

---

### 2. `actual_usage_analyzer.py` - Actual Cost Analysis

**Purpose:** Analyze costs based on actual lesson files you've already generated.

**Usage:**
```bash
python actual_usage_analyzer.py
```

**Outputs:**
- Actual token usage from your lessons
- Refined cost estimates based on real data
- Business model viability analysis
- Optimization recommendations

**When to use:** After generating your first 10-20 lessons to refine estimates.

---

### 3. `api_usage_monitor.py` - Usage Tracking

**Purpose:** Log and analyze actual API operations during development and production.

**Usage:**
```bash
python api_usage_monitor.py
```

**Features:**
- Manual operation logging (since Anthropic doesn't have a public usage API yet)
- Usage log analysis and reporting
- Cost projections based on actual usage
- Per-learner cost calculations

**When to use:** During development and in production to track real costs.

---

## Quick Start

1. **Run the cost estimation:**
```bash
python api_cost_analyzer.py
```

2. **Analyze actual usage after generating lessons:**
```bash
python actual_usage_analyzer.py
```

3. **Start logging operations during development:**
```bash
python api_usage_monitor.py
# Select option 2 to log operations manually
# Select option 3 to analyze the log
```

---

## Key Findings Summary

Based on your current dev-curriculum structure (124 modules, ~496 lessons):

### Costs

**One-time setup (generate all lessons):**
- Lesson generation: ~$116
- Curriculum design: ~$30
- **Total: ~$150**

**Per-learner ongoing costs:**
- With Sonnet: ~$40/learner
- With Haiku: ~$3.50/learner
- Hybrid approach: ~$15/learner

### Recommendations

1. **Pre-generate all lessons** ✅ (you're already doing this)
   - Upfront cost: $150
   - Amortized to <$2/learner at 100+ users

2. **Use Haiku for routine operations**
   - 92% cost reduction
   - Perfect for checkpoints and progress tracking
   - Keep Sonnet for final evaluations

3. **Optimal pricing strategy:**
   - MVP (first 100 users): $49/learner
   - Scale (500+ users): $29/learner with Haiku
   - Premium tier: $99/learner with Sonnet

4. **Target margins:**
   - At $29 with Haiku: 87% profit margin
   - At $49 with Haiku: 92% profit margin
   - At $99 hybrid: 85% profit margin

---

## Detailed Analysis

See `API_COST_ANALYSIS.md` for comprehensive analysis including:
- Scaling economics
- Risk analysis
- Competitive positioning
- Enterprise pricing strategies
- 12-month revenue projections

---

## Updating Token Estimates

The cost analyzer uses these default token estimates:

| Operation | Input Tokens | Output Tokens |
|-----------|--------------|---------------|
| Lesson Generation | 8,000 | 6,000 |
| Curriculum Design | 5,000 | 3,000 |
| Evaluation | 3,000 | 1,500 |
| Advisory | 2,000 | 800 |

**To refine estimates with your actual data:**

1. Generate 10-20 lessons
2. Check Anthropic's dashboard for actual token usage
3. Update the `TokenEstimates` class in `api_cost_analyzer.py`:

```python
@dataclass
class TokenEstimates:
    lesson_generation_input: int = YOUR_ACTUAL_INPUT
    lesson_generation_output: int = YOUR_ACTUAL_OUTPUT
    # ... etc
```

4. Re-run the analyzer

---

## Tracking Real Usage

### Method 1: Anthropic Dashboard (Recommended)

1. Go to https://console.anthropic.com/settings/billing
2. Note your current token usage
3. Run your dev-curriculum operations
4. Note the new token usage
5. Calculate the difference
6. Log it using `api_usage_monitor.py`

### Method 2: Claude Desktop Usage Stats

If using Claude Desktop for development:
1. Check "Settings" → "Usage"
2. Track tokens per conversation
3. Map conversations to operations (lesson generation, evaluation, etc.)
4. Log using the monitor tool

### Method 3: API Response Headers

If building a web app with direct API access:
```python
import anthropic

client = anthropic.Anthropic(api_key="your-key")
response = client.messages.create(
    model="claude-sonnet-3.5-20250514",
    messages=[{"role": "user", "content": "Hello"}]
)

# Token usage is in the response
input_tokens = response.usage.input_tokens
output_tokens = response.usage.output_tokens
```

---

## Cost Optimization Checklist

- [ ] Pre-generate all lessons (amortizes setup cost)
- [ ] Use Haiku for checkpoints and progress tracking
- [ ] Keep Sonnet for final evaluations only
- [ ] Implement caching for common evaluation responses
- [ ] Batch-generate related lessons to share context
- [ ] Monitor actual usage with the tracking tool
- [ ] Refine token estimates based on real data
- [ ] A/B test Haiku vs Sonnet quality
- [ ] Set up cost alerts at $500, $1000, $5000

---

## Break-Even Analysis

At **$49/learner pricing** with **Haiku optimization** ($5/learner cost):

| Metric | Value |
|--------|-------|
| Revenue per learner | $49 |
| Cost per learner | $5 |
| Profit per learner | $44 |
| Setup cost | $150 |
| Break-even | 4 learners |

**You break even after just 4 paid users.** Every user after that is $44 in profit.

---

## Enterprise Scaling

For corporate training at scale:

**500-seat enterprise contract:**
- Annual contract value: $50,000
- API costs (Haiku): $2,500
- Gross margin: 95%

**Implementation:**
- Custom curriculum generation: $1,000 one-time
- Integration work: $10,000 one-time
- Support: $5,000/year

**Total costs:** $18,500 first year, $7,500 ongoing  
**Profit:** $31,500 first year, $42,500 ongoing

---

## Questions?

1. **What if Anthropic raises prices?**
   - Even if prices double, you're still profitable at $49 with Haiku
   - Build abstraction layer to switch to OpenAI/Gemini if needed

2. **Is Haiku good enough for evaluations?**
   - Run A/B test with 20 evaluations
   - Use hybrid approach (Haiku for checkpoints, Sonnet for finals)

3. **How do I reduce costs further?**
   - Caching: 30-50% savings on evaluation costs
   - Batch operations: 20-30% savings on lesson generation
   - Smart routing: Use cheapest model that meets quality threshold

4. **When should I switch from Sonnet to Haiku?**
   - After validating Haiku quality with 50+ evaluations
   - When scaling beyond 100 users
   - When profit margins are critical

---

## Support

For questions or issues with these tools:
1. Check the comprehensive analysis in `API_COST_ANALYSIS.md`
2. Review your actual usage data in Anthropic's dashboard
3. Run the tools with different parameters to model scenarios
4. Join the dev-curriculum community (when available)

---

## Next Steps

1. ✅ Run `api_cost_analyzer.py` to see baseline estimates
2. Generate 10-20 lessons and track actual token usage
3. Update estimates based on real data
4. Run `actual_usage_analyzer.py` for refined projections
5. Set up `api_usage_monitor.py` to track ongoing costs
6. Launch MVP with 10 beta users
7. Monitor real costs vs estimates
8. Optimize based on actual data
9. Scale to 100+ users
10. Celebrate profitability! 🎉
