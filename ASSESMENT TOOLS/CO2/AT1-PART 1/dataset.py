import numpy as np
import pandas as pd
from sklearn.mixture import GaussianMixture

# Make output reproducible
np.random.seed(42)

# --------------------------------------------------
# Step 1: Create Initial Dataset
# --------------------------------------------------

initial_data = np.random.rand(100, 6)

# Scale values between 50 and 100
initial_data = initial_data * 50 + 50

# Feature Names
columns = [
    "Stability",
    "Model",
    "Efficiency",
    "Accuracy",
    "Energy_Consumption",
    "Maintenance_Cost"
]

df = pd.DataFrame(initial_data, columns=columns)

# --------------------------------------------------
# Step 2: Train Gaussian Mixture Model
# --------------------------------------------------

gmm = GaussianMixture(
    n_components=3,
    random_state=42
)

gmm.fit(df)

# --------------------------------------------------
# Step 3: Generate Synthetic Dataset
# --------------------------------------------------

synthetic_data, _ = gmm.sample(100)

synthetic_df = pd.DataFrame(
    synthetic_data,
    columns=columns
)

# Round values
synthetic_df = synthetic_df.round(2)

# --------------------------------------------------
# Step 4: Save Dataset
# --------------------------------------------------

synthetic_df.to_csv(
    "dataset/synthetic_dataset.csv",
    index=False
)

# --------------------------------------------------
# Step 5: Display Dataset
# --------------------------------------------------

print("\nSynthetic Dataset Generated Successfully!\n")

print(synthetic_df.head())

print("\nDataset Shape:", synthetic_df.shape)