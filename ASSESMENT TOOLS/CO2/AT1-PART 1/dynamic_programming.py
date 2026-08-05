import pandas as pd
import numpy as np

# ---------------------------------------------
# Load Dataset
# ---------------------------------------------

df = pd.read_csv("dataset/synthetic_dataset.csv")

# ---------------------------------------------
# Calculate Reward
# ---------------------------------------------

reward = (
    df["Stability"] * 0.20 +
    df["Model"] * 0.15 +
    df["Efficiency"] * 0.25 +
    df["Accuracy"] * 0.20 -
    df["Energy_Consumption"] * 0.10 -
    df["Maintenance_Cost"] * 0.10
)

# ---------------------------------------------
# Dynamic Programming
# ---------------------------------------------

n = len(reward)

dp = np.zeros(n)

dp[0] = reward.iloc[0]

for i in range(1, n):
    dp[i] = max(dp[i-1], dp[i-1] + reward.iloc[i])

# ---------------------------------------------
# Results
# ---------------------------------------------

result = pd.DataFrame({
    "Record": range(1, n + 1),
    "Reward": reward.round(2),
    "Optimal_Reward": dp.round(2)
})

print("\nDynamic Programming Results\n")
print(result.head())

print("\n--------------------------------")
print("Total Optimal Reward :", round(dp[-1], 2))
print("Average Reward       :", round(np.mean(dp), 2))
print("Maximum Reward       :", round(np.max(dp), 2))
print("Minimum Reward       :", round(np.min(dp), 2))
print("--------------------------------")

# Save results
result.to_csv("tables/dp_results.csv", index=False)