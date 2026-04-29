# Task 7: Death Overs Analysis
import numpy as np
from data_loader import load_data

_, batting_team, _, over, _, _, _, total_runs = load_data()
is_death = (over >= 15)
death_runs = total_runs[is_death]
death_teams = batting_team[is_death]

print(f"Total runs in death overs: {np.sum(death_runs)}")

teams, inverse = np.unique(death_teams, return_inverse=True)
runs_by_team = np.bincount(inverse, weights=death_runs)
print(f"Team with most death runs: {teams[np.argmax(runs_by_team)]}")