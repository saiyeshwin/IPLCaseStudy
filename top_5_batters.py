# Task 2: Top 5 Batters
import numpy as np
from data_loader import load_data
_, _, _, _, batter, _, batsman_runs, _ = load_data()
names, inverse = np.unique(batter, return_inverse=True)
runs_per_batter = np.bincount(inverse, weights=batsman_runs)
top_indices = np.argsort(runs_per_batter)[-5:][::-1]
print("Top 5 Batters:")
for i in top_indices:
    print(f"{names[i]}: {runs_per_batter[i]} runs")