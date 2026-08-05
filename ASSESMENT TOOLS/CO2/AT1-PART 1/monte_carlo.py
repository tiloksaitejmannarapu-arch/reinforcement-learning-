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
# Monte Carlo Simulation
# ---------------------------------------------

num_simulations = 1000
simulation_rewards = []

np.random.seed(42)

for _ in range(num_simulations):

    sampled_reward = reward.sample(
        n=len(reward),
        replace=True
    ).sum()

    simulation_rewards.append(sampled_reward)

simulation_rewards = np.array(simulation_rewards)

# ---------------------------------------------
# Results
# ---------------------------------------------

result = pd.DataFrame({
    "Simulation": range(1, num_simulations + 1),
    "Total_Reward": simulation_rewards.round(2)
})

print("\nMonte Carlo Results\n")
print(result.head())

print("\n--------------------------------")
print("Expected Reward :", round(simulation_rewards.mean(), 2))
print("Average Reward  :", round(simulation_rewards.mean(), 2))
print("Maximum Reward  :", round(simulation_rewards.max(), 2))
print("Minimum Reward  :", round(simulation_rewards.min(), 2))
print("Std Deviation   :", round(simulation_rewards.std(), 2))
print("--------------------------------")

# ---------------------------------------------
# Save Results
# ---------------------------------------------

result.to_csv(
    "tables/mc_results.csv",
    index=False
)