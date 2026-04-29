# Task 6: Boundary Analysis
import numpy as np
from data_loader import load_data
_, batting_team, _, _, _, _, batsman_runs, _ = load_data()
fours = np.sum(batsman_runs == 4)
sixes = np.sum(batsman_runs == 6)
print(f"Total 4s: {fours}")
print(f"Total 6s: {sixes}")