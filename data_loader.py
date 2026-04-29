import numpy as np
def load_data():
    raw = np.genfromtxt(
        'data/deliveries.csv',
        delimiter=',',
        dtype=str,
        skip_header=1,
        filling_values=''
    )
    match_ids    = raw[:, 0].astype(int)
    batting_team = raw[:, 2]
    bowling_team = raw[:, 3]
    over         = raw[:, 4].astype(int)
    batter       = raw[:, 6]
    bowler       = raw[:, 7]
    batsman_runs = raw[:, 9].astype(int)
    total_runs   = raw[:, 11].astype(int)
    return match_ids, batting_team, bowling_team, over, batter, bowler, batsman_runs, total_runs