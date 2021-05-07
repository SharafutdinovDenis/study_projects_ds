import pandas as pd
import numpy as np

def deptime_to_minuts(t):
    while len(t) < 4:
        t = '0' + t
    t = int(t[:2])*60 + int(t[2:4])
    return t
    
df = pd.read_csv('../datasets/flight_delays_train.csv')
df.info()

# Data cleaning

# rename column
df.rename(columns={'DayofMonth': 'DayOfMonth'}, inplace=True)

# convert date columns to numeric
date_cols = ['Month', 'DayOfMonth', 'DayOfWeek']
for col in date_cols:
    df[col] = df[col].apply(lambda x: int(x.split('-')[-1]))

# refine Deptime when it's more than 2400
df['DepTime'] = df['DepTime'].apply(lambda x: str(x - 2400) if x >=2400 else str(x))

# transform hours and mins to seconds
df['DepTime'] = df['DepTime'].apply(deptime_to_minuts)

# transform dep_delayed_15min to int (1 or 0)
df['dep_delayed_15min'] = df['dep_delayed_15min'].apply(lambda x: 1 if x=='Y' else 0)

