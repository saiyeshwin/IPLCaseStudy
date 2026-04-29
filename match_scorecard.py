# Task 11: Match Scorecard
import numpy as np
from data_loader import load_data
match_ids, batting_team, _, _, _, _, _, total_runs = load_data()
unique_matches = np.unique(match_ids)
print("--- IPL Scorecards (First 5) ---")
for m_id in unique_matches[:5]:
    mask = (match_ids == m_id)
    teams = np.unique(batting_team[mask])
    print(f"\nMatch {m_id}:")
    for t in teams:
        score = np.sum(total_runs[mask & (batting_team == t)])
        print(f"  {t}: {score} runs")