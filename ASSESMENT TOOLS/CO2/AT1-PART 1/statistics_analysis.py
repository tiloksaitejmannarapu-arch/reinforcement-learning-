import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# -------------------------------------------------
# Load Results
# -------------------------------------------------

dp = pd.read_csv("tables/dp_results.csv")
mc = pd.read_csv("tables/mc_results.csv")

# -------------------------------------------------
# Extract Reward Values
# -------------------------------------------------

dp_rewards = dp["Optimal_Reward"]

# Use first 100 Monte Carlo simulations
mc_rewards = mc["Total_Reward"][:100]

# -------------------------------------------------
# Statistical Measures
# -------------------------------------------------

dp_mean = dp_rewards.mean()
mc_mean = mc_rewards.mean()

dp_std = dp_rewards.std()
mc_std = mc_rewards.std()

dp_var = dp_rewards.var()
mc_var = mc_rewards.var()

# -------------------------------------------------
# Independent t-test
# -------------------------------------------------

t_stat, p_value = ttest_ind(dp_rewards, mc_rewards)

# -------------------------------------------------
# Statistical Significance
# -------------------------------------------------

if p_value < 0.05:
    significance = "Significant Difference"
else:
    significance = "No Significant Difference"

# -------------------------------------------------
# Comparison Table
# -------------------------------------------------

comparison = pd.DataFrame({

    "Metric":[
        "Mean",
        "Standard Deviation",
        "Variance",
        "Maximum",
        "Minimum"
    ],

    "Dynamic Programming":[
        round(dp_mean,2),
        round(dp_std,2),
        round(dp_var,2),
        round(dp_rewards.max(),2),
        round(dp_rewards.min(),2)
    ],

    "Monte Carlo":[
        round(mc_mean,2),
        round(mc_std,2),
        round(mc_var,2),
        round(mc_rewards.max(),2),
        round(mc_rewards.min(),2)
    ]

})

# -------------------------------------------------
# Statistical Summary
# -------------------------------------------------

summary = pd.DataFrame({

    "Test":[
        "t-statistic",
        "p-value",
        "Result"
    ],

    "Value":[
        round(t_stat,4),
        round(p_value,6),
        significance
    ]

})

# -------------------------------------------------
# Save Tables
# -------------------------------------------------

comparison.to_csv(
    "tables/comparison_table.csv",
    index=False
)

summary.to_csv(
    "tables/statistics_table.csv",
    index=False
)

# -------------------------------------------------
# Print Results
# -------------------------------------------------

print("\n========== COMPARISON TABLE ==========\n")
print(comparison)

print("\n========== STATISTICAL TEST ==========\n")
print(summary)

# -------------------------------------------------
# Feature Summary Table
# -------------------------------------------------

dataset = pd.read_csv("dataset/synthetic_dataset.csv")

feature_summary = pd.DataFrame({
    "Feature": dataset.columns,
    "Mean": dataset.mean().round(2).values,
    "Standard Deviation": dataset.std().round(2).values,
    "Minimum": dataset.min().round(2).values,
    "Maximum": dataset.max().round(2).values
})

feature_summary.to_csv(
    "tables/feature_summary.csv",
    index=False
)

print("\nFeature summary saved successfully!")