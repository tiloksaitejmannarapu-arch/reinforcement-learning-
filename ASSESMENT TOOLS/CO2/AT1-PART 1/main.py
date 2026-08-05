import subprocess
import os

# ----------------------------------------
# Function to Run Python Files
# ----------------------------------------

def run_script(script_name):
    print("\n" + "=" * 60)
    print(f"Running {script_name}...")
    print("=" * 60)

    result = subprocess.run(
        ["python", script_name],
        text=True
    )

    if result.returncode == 0:
        print(f"{script_name} completed successfully!")
    else:
        print(f"Error while running {script_name}")

# ----------------------------------------
# Create Required Folders
# ----------------------------------------

folders = [
    "dataset",
    "tables",
    "graphs",
    "output"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# ----------------------------------------
# Execute Project
# ----------------------------------------

scripts = [
    "dataset_generator.py",
    "dynamic_programming.py",
    "monte_carlo.py",
    "statistical_analysis.py",
    "visualization.py"
]

for script in scripts:
    run_script(script)

print("\n" + "=" * 60)
print("PROJECT EXECUTED SUCCESSFULLY")
print("=" * 60)

print("\nGenerated Files")

print("\nDataset")
print("   synthetic_dataset.csv")

print("\nTables")
print("   dp_results.csv")
print("   mc_results.csv")
print("   comparison_table.csv")
print("   statistics_table.csv")
print("   feature_summary.csv")

print("\nGraphs")
print("   feature_distribution.png")
print("   dp_rewards.png")
print("   mc_rewards.png")
print("   dp_vs_mc_rewards.png")
print("   feature_comparison.png")
print("   feature_dp_mc_comparison.png")
print("   statistical_comparison.png")
print("   reward_distribution.png")
print("   execution_time.png")

print("\nProject Finished Successfully!")