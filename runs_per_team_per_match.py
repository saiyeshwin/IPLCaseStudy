# Task 9: Runs per Team per Match
import numpy as np
from data_loader import load_data
match_ids, batting_team, _, _, _, _, _, total_runs = load_data()
keys = np.char.add(match_ids.astype(str), "_")
keys = np.char.add(keys, batting_team)
unique_keys, inverse = np.unique(keys, return_inverse=True)
team_match_totals = np.bincount(inverse, weights=total_runs)

print("Runs per team per match:")
for i in range(min(10, len(unique_keys))):
    print(f"{unique_keys[i]}: {team_match_totals[i]} runs")