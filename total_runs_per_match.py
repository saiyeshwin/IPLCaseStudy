# Task 1: Total Runs per Match
import numpy as np
from data_loader import load_data

match_ids, _, _, _, _, _, _, total_runs = load_data()

unique_ids, inverse = np.unique(match_ids, return_inverse=True)

runs_per_match = np.bincount(inverse, weights=total_runs)

for i in range(len(unique_ids)):
    print(f"Match {unique_ids[i]}: {runs_per_match[i]} runs")