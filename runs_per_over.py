# Task 5: Runs per Over
import numpy as np
from data_loader import load_data
_, _, _, over, _, _, _, total_runs = load_data()
unique_overs = np.unique(over)
avg_runs_list = []
for o in unique_overs:
    mask = (over == o)
    avg = np.mean(total_runs[mask]) * 6 
    avg_runs_list.append(np.sum(total_runs[mask]) / (np.sum(mask) / 6))
print("Average Runs per Over (1-20):")
print(np.round(avg_runs_list, 2))