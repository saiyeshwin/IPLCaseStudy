# Task 4: Economy Rate of Bowlers
import numpy as np
from data_loader import load_data
_, _, _, _, _, bowler, _, total_runs = load_data()
names, inverse = np.unique(bowler, return_inverse=True)
runs_conceded = np.bincount(inverse, weights=total_runs)
balls_bowled = np.bincount(inverse)
overs_bowled = balls_bowled / 6
economy = np.divide(runs_conceded, overs_bowled, out=np.zeros_like(runs_conceded, dtype=float), where=overs_bowled!=0)
valid = overs_bowled > 10
sorted_idx = np.argsort(economy[valid])
print("Top 5 Economical Bowlers:")
for i in sorted_idx[:5]:
    print(f"{names[valid][i]}: {economy[valid][i]:.2f} Economy")