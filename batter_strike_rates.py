# Task 3: Strike Rate of Batters
import numpy as np
from data_loader import load_data
_, _, _, _, batter, _, batsman_runs, _ = load_data()
names, inverse = np.unique(batter, return_inverse=True)
total_runs = np.bincount(inverse, weights=batsman_runs)
balls_faced = np.bincount(inverse)
sr = np.divide(total_runs * 100, balls_faced, out=np.zeros_like(total_runs, dtype=float), where=balls_faced!=0)
for i in range(5):
    print(f"{names[i]}: {sr[i]:.2f} SR")