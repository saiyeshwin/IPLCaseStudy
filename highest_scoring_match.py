# Task 8: Highest Scoring Match
import numpy as np
from data_loader import load_data

match_ids, _, _, _, _, _, _, total_runs = load_data()

ids, inverse = np.unique(match_ids, return_inverse=True)
match_totals = np.bincount(inverse, weights=total_runs)

max_idx = np.argmax(match_totals)
print(f"Highest Scoring Match: {ids[max_idx]} with {match_totals[max_idx]} runs")