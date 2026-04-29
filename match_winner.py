# Task 10: Match Winner Approximation
import numpy as np
from data_loader import load_data
match_ids, batting_team, _, _, _, _, _, total_runs = load_data()
unique_matches = np.unique(match_ids)
print("Match Winners:")
for m_id in unique_matches[:10]:
    mask = (match_ids == m_id)
    teams = np.unique(batting_team[mask])
    scores = [np.sum(total_runs[mask & (batting_team == t)]) for t in teams]
    if len(scores) >= 2:
        winner = teams[np.argmax(scores)]
        print(f"Match {m_id}: {winner}")