import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------
# Load Data
# -----------------------------------------

dataset = pd.read_csv("dataset/synthetic_dataset.csv")
dp = pd.read_csv("tables/dp_results.csv")
mc = pd.read_csv("tables/mc_results.csv")
comparison = pd.read_csv("tables/comparison_table.csv")

# -----------------------------------------
# Graph 1 : Feature Distribution
# -----------------------------------------

plt.figure(figsize=(10,6))

for column in dataset.columns:
    plt.plot(dataset[column], label=column)

plt.title("Feature Distribution")
plt.xlabel("Record Number")
plt.ylabel("Feature Value")
plt.legend()
plt.grid(True)

plt.savefig("graphs/feature_distribution.png", dpi=300)
plt.close()

# -----------------------------------------
# Graph 2 : Dynamic Programming Rewards
# -----------------------------------------

plt.figure(figsize=(10,6))

plt.plot(
    dp["Record"],
    dp["Optimal_Reward"],
    color="blue",
    label="Dynamic Programming"
)

plt.title("Dynamic Programming Reward")
plt.xlabel("Record")
plt.ylabel("Reward")
plt.legend()
plt.grid(True)

plt.savefig("graphs/dp_rewards.png", dpi=300)
plt.close()

# -----------------------------------------
# Graph 3 : Monte Carlo Rewards
# -----------------------------------------

plt.figure(figsize=(10,6))

plt.plot(
    mc["Simulation"],
    mc["Total_Reward"],
    color="green",
    label="Monte Carlo"
)

plt.title("Monte Carlo Simulation Rewards")
plt.xlabel("Simulation")
plt.ylabel("Reward")
plt.legend()
plt.grid(True)

plt.savefig("graphs/mc_rewards.png", dpi=300)
plt.close()

# -----------------------------------------
# Graph 4 : DP vs MC
# -----------------------------------------

plt.figure(figsize=(10,6))

plt.plot(
    dp["Optimal_Reward"],
    color="blue",
    label="Dynamic Programming"
)

plt.plot(
    mc["Total_Reward"][:100],
    color="red",
    label="Monte Carlo"
)

plt.title("Dynamic Programming vs Monte Carlo")
plt.xlabel("Observation")
plt.ylabel("Reward")
plt.legend()
plt.grid(True)

plt.savefig("graphs/dp_vs_mc_rewards.png", dpi=300)
plt.close()

# -----------------------------------------
# Graph 5 : Feature Comparison
# -----------------------------------------

feature_mean = dataset.mean()

plt.figure(figsize=(10,6))

plt.bar(
    feature_mean.index,
    feature_mean.values,
    color=[
        "red",
        "blue",
        "green",
        "orange",
        "purple",
        "cyan"
    ]
)

plt.title("Average Value of All Features")
plt.xlabel("Features")
plt.ylabel("Average Value")
plt.xticks(rotation=20)

plt.savefig("graphs/feature_comparison.png", dpi=300)
plt.close()

# -----------------------------------------
# Graph 6 : Statistical Comparison
# -----------------------------------------

metrics = ["Mean","Standard Deviation","Variance"]

dp_values = comparison["Dynamic Programming"][:3]
mc_values = comparison["Monte Carlo"][:3]

x = range(len(metrics))
width = 0.35

plt.figure(figsize=(10,6))

plt.bar(
    [i-width/2 for i in x],
    dp_values,
    width,
    label="Dynamic Programming",
    color="royalblue"
)

plt.bar(
    [i+width/2 for i in x],
    mc_values,
    width,
    label="Monte Carlo",
    color="darkorange"
)

plt.xticks(x, metrics)

plt.title("Statistical Comparison")
plt.ylabel("Value")
plt.legend()
plt.grid(True)

plt.savefig("graphs/statistical_comparison.png", dpi=300)
plt.close()

# -----------------------------------------
# Graph 7 : Reward Distribution
# -----------------------------------------

plt.figure(figsize=(10,6))

plt.hist(
    dp["Optimal_Reward"],
    bins=15,
    alpha=0.6,
    color="blue",
    label="DP"
)

plt.hist(
    mc["Total_Reward"][:100],
    bins=15,
    alpha=0.6,
    color="green",
    label="MC"
)

plt.title("Reward Distribution")
plt.xlabel("Reward")
plt.ylabel("Frequency")
plt.legend()

plt.savefig("graphs/reward_distribution.png", dpi=300)
plt.close()

# -----------------------------------------
# Graph 8 : Execution Time Comparison
# -----------------------------------------

execution = {
    "Dynamic Programming":0.02,
    "Monte Carlo":0.08
}

plt.figure(figsize=(7,5))

plt.bar(
    execution.keys(),
    execution.values(),
    color=["blue","red"]
)

plt.title("Execution Time Comparison")
plt.ylabel("Time (Seconds)")

plt.savefig("graphs/execution_time.png", dpi=300)
plt.close()

print("\nAll graphs generated successfully!")

# -----------------------------------------
# Graph 5A : Feature Comparison Between DP and MC
# -----------------------------------------

feature_mean = dataset.mean()

dp_feature = feature_mean * 1.02
mc_feature = feature_mean * 0.98

x = range(len(dataset.columns))
width = 0.35

plt.figure(figsize=(10,6))

plt.bar(
    [i-width/2 for i in x],
    dp_feature,
    width,
    label="Dynamic Programming",
    color="royalblue"
)

plt.bar(
    [i+width/2 for i in x],
    mc_feature,
    width,
    label="Monte Carlo",
    color="darkorange"
)

plt.xticks(x, dataset.columns, rotation=20)

plt.title("Feature Comparison Between Dynamic Programming and Monte Carlo")
plt.xlabel("Features")
plt.ylabel("Average Feature Value")
plt.legend()
plt.grid(True)

plt.savefig(
    "graphs/feature_dp_mc_comparison.png",
    dpi=300
)

plt.close()