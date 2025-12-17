"""
A/B Testing - Email Campaign Analysis
Simple and Easy to Understand!
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

print("="*60)
print("A/B TESTING - EMAIL CAMPAIGN")
print("="*60)

# ============================================================================
# 1. LOAD DATA
# ============================================================================

print("\n[Step 1] Loading data...")
df = pd.read_csv('ab_test_data.csv')

print(f"✓ Total users: {len(df)}")
print(f"✓ Group A: {len(df[df['Group']=='A'])} users")
print(f"✓ Group B: {len(df[df['Group']=='B'])} users")

# ============================================================================
# 2. DESCRIPTIVE STATISTICS
# ============================================================================

print("\n" + "="*60)
print("METRICS COMPARISON")
print("="*60)

# Separate groups
group_a = df[df['Group'] == 'A']
group_b = df[df['Group'] == 'B']

# Calculate metrics
metrics = {
    'Metric': [
        'Open Rate (%)',
        'Click Rate (%)',
        'Purchase Rate (%)',
        'Avg Revenue per User ($)'
    ],
    'Group A': [
        (group_a['EmailOpened'].sum() / len(group_a) * 100),
        (group_a['Clicked'].sum() / len(group_a) * 100),
        (group_a['Purchased'].sum() / len(group_a) * 100),
        group_a['AmountSpent'].mean()
    ],
    'Group B': [
        (group_b['EmailOpened'].sum() / len(group_b) * 100),
        (group_b['Clicked'].sum() / len(group_b) * 100),
        (group_b['Purchased'].sum() / len(group_b) * 100),
        group_b['AmountSpent'].mean()
    ]
}

results_df = pd.DataFrame(metrics)
results_df['Difference'] = results_df['Group B'] - results_df['Group A']
results_df['Lift (%)'] = (results_df['Difference'] / results_df['Group A'] * 100).round(1)

print("\n" + results_df.to_string(index=False))

# ============================================================================
# 3. STATISTICAL SIGNIFICANCE TEST
# ============================================================================

print("\n" + "="*60)
print("STATISTICAL TESTS")
print("="*60)

# Test 1: Open Rate (Chi-Square Test)
print("\n[Test 1] Open Rate Comparison:")
print(f"  Group A: {group_a['EmailOpened'].sum()}/{len(group_a)} opened")
print(f"  Group B: {group_b['EmailOpened'].sum()}/{len(group_b)} opened")

# Create contingency table
contingency_table = pd.crosstab(df['Group'], df['EmailOpened'])
chi2, p_value_open, dof, expected = stats.chi2_contingency(contingency_table)

print(f"\n  Chi-Square Statistic: {chi2:.4f}")
print(f"  P-value: {p_value_open:.4f}")

if p_value_open < 0.05:
    print(f"  ✓ Result: SIGNIFICANT difference (p < 0.05)")
    print(f"  → Group B is statistically better!")
else:
    print(f"  ✗ Result: NO significant difference (p >= 0.05)")
    print(f"  → No clear winner")

# Test 2: Purchase Rate (Chi-Square Test)
print("\n[Test 2] Purchase Rate Comparison:")
print(f"  Group A: {group_a['Purchased'].sum()}/{len(group_a)} purchased")
print(f"  Group B: {group_b['Purchased'].sum()}/{len(group_b)} purchased")

contingency_table_purchase = pd.crosstab(df['Group'], df['Purchased'])
chi2_purchase, p_value_purchase, dof, expected = stats.chi2_contingency(contingency_table_purchase)

print(f"\n  Chi-Square Statistic: {chi2_purchase:.4f}")
print(f"  P-value: {p_value_purchase:.4f}")

if p_value_purchase < 0.05:
    print(f"  ✓ Result: SIGNIFICANT difference (p < 0.05)")
    print(f"  → Group B converts better!")
else:
    print(f"  ✗ Result: NO significant difference (p >= 0.05)")
    print(f"  → Similar conversion rates")

# Test 3: Revenue (T-Test)
print("\n[Test 3] Revenue Comparison:")
print(f"  Group A Avg: ${group_a['AmountSpent'].mean():.2f}")
print(f"  Group B Avg: ${group_b['AmountSpent'].mean():.2f}")

t_stat, p_value_revenue = stats.ttest_ind(
    group_a['AmountSpent'], 
    group_b['AmountSpent']
)

print(f"\n  T-Statistic: {t_stat:.4f}")
print(f"  P-value: {p_value_revenue:.4f}")

if p_value_revenue < 0.05:
    print(f"  ✓ Result: SIGNIFICANT difference (p < 0.05)")
    print(f"  → Group B generates more revenue!")
else:
    print(f"  ✗ Result: NO significant difference (p >= 0.05)")
    print(f"  → Similar revenue performance")

# ============================================================================
# 4. CONFIDENCE INTERVALS
# ============================================================================

print("\n" + "="*60)
print("CONFIDENCE INTERVALS (95%)")
print("="*60)

# Open Rate CI
open_rate_a = group_a['EmailOpened'].mean()
open_rate_b = group_b['EmailOpened'].mean()

se_a = np.sqrt(open_rate_a * (1 - open_rate_a) / len(group_a))
se_b = np.sqrt(open_rate_b * (1 - open_rate_b) / len(group_b))

ci_a = (open_rate_a - 1.96*se_a, open_rate_a + 1.96*se_a)
ci_b = (open_rate_b - 1.96*se_b, open_rate_b + 1.96*se_b)

print(f"\nOpen Rate:")
print(f"  Group A: {open_rate_a*100:.1f}% (95% CI: {ci_a[0]*100:.1f}% - {ci_a[1]*100:.1f}%)")
print(f"  Group B: {open_rate_b*100:.1f}% (95% CI: {ci_b[0]*100:.1f}% - {ci_b[1]*100:.1f}%)")

# ============================================================================
# 5. BUSINESS RECOMMENDATIONS
# ============================================================================

print("\n" + "="*60)
print("RECOMMENDATIONS")
print("="*60)

# Determine winner
if p_value_open < 0.05 and results_df.loc[0, 'Group B'] > results_df.loc[0, 'Group A']:
    winner = "B"
    lift = results_df.loc[0, 'Lift (%)']
    print(f"\n✓ WINNER: Group B")
    print(f"\n  Group B performs {abs(lift):.1f}% better than Group A")
    print(f"\n  Subject line: 'Limited Time: Save 20% Today!'")
    print(f"\n  Recommendation:")
    print(f"  → Use Version B for future campaigns")
    print(f"  → Expected improvement: +{abs(lift):.1f}% in open rate")
    
    # Calculate business impact
    if len(df) >= 100:
        total_users = 10000  # Assume 10k users in next campaign
        improvement = (results_df.loc[0, 'Group B'] - results_df.loc[0, 'Group A']) / 100
        additional_opens = total_users * improvement
        print(f"  → For 10,000 users: ~{additional_opens:.0f} more email opens")

elif p_value_open < 0.05 and results_df.loc[0, 'Group A'] > results_df.loc[0, 'Group B']:
    print(f"\n✓ WINNER: Group A")
    print(f"\n  Subject line: 'Special Offer - 20% Off!'")
    print(f"\n  Recommendation: Use Version A")
else:
    print(f"\n⚠ NO CLEAR WINNER")
    print(f"\n  Both versions perform similarly")
    print(f"\n  Recommendations:")
    print(f"  → Consider other factors (brand consistency, etc.)")
    print(f"  → Run test with larger sample size")
    print(f"  → Test different variations")

# ============================================================================
# 6. KEY INSIGHTS
# ============================================================================

print("\n" + "="*60)
print("KEY INSIGHTS")
print("="*60)

insights = []

# Insight 1: Sample size
if len(df) < 100:
    insights.append("⚠ Small sample size - results may not be reliable")
else:
    insights.append(f"✓ Good sample size ({len(df)} users) for reliable results")

# Insight 2: Open rate
if abs(results_df.loc[0, 'Lift (%)']) > 10:
    insights.append(f"💡 Large difference in open rates ({abs(results_df.loc[0, 'Lift (%)']):.1f}%)")

# Insight 3: Conversion
if abs(results_df.loc[2, 'Lift (%)']) > 20:
    insights.append(f"💡 Significant difference in purchase rate ({abs(results_df.loc[2, 'Lift (%)']):.1f}%)")

# Insight 4: Revenue
revenue_diff = results_df.loc[3, 'Difference']
if abs(revenue_diff) > 5:
    insights.append(f"💡 Notable revenue difference (${abs(revenue_diff):.2f} per user)")

for i, insight in enumerate(insights, 1):
    print(f"\n{i}. {insight}")

# ============================================================================
# 7. SUMMARY
# ============================================================================

print("\n" + "="*60)
print("SUMMARY")
print("="*60)

print(f"""
Test Setup:
- Total Users: {len(df)}
- Group A: {len(group_a)} users (Control)
- Group B: {len(group_b)} users (Variant)

Primary Metric: Email Open Rate
- Group A: {results_df.loc[0, 'Group A']:.1f}%
- Group B: {results_df.loc[0, 'Group B']:.1f}%
- Difference: {results_df.loc[0, 'Difference']:.1f}%
- Statistical Significance: {'YES' if p_value_open < 0.05 else 'NO'} (p={p_value_open:.4f})

Secondary Metrics:
- Click Rate: A={results_df.loc[1, 'Group A']:.1f}%, B={results_df.loc[1, 'Group B']:.1f}%
- Purchase Rate: A={results_df.loc[2, 'Group A']:.1f}%, B={results_df.loc[2, 'Group B']:.1f}%
- Avg Revenue: A=${results_df.loc[3, 'Group A']:.2f}, B=${results_df.loc[3, 'Group B']:.2f}
""")

print("\n" + "="*60)
print("A/B TEST COMPLETE")
print("="*60)
