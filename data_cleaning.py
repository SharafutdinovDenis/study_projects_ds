import pandas as pd
from datetime import date
import numpy as np

data = pd.read_csv('datasets/fifa21.csv', index_col='ID')
data.info()

# Remove new line from 'Clubs'
data['Club'] = data['Club'].apply(lambda x: x.replace('\n', ''))

# Add columns "ContractStart", "ContractEnd"
data['ContractStart'] = data['Contract'].apply(lambda x: int(x.split('~')[0]) if not any(w in x for w in ['Loan', 'Free']) else 0)
data['ContractEnd'] = data['Contract'].apply(lambda x: int(x.split('~')[-1]) if not any(w in x for w in ['Loan', 'Free']) else 0)

# 'Loan Date End' and 'Joined' to datetime
data['Loan Date End'] = pd.to_datetime(data['Loan Date End'])
data['Joined'] = pd.to_datetime(data['Joined'])

# 'Height' and 'Weight' to numeric
# There're 2 types of 'Height': 'cm' and 'feet with inches'
# And also there're 2 types of 'Weight': 'kg' and 'lbs'
def height_to_cm(h):
    if 'cm' in h:
        cm = int(h[:-2])
    else:   
        f, i = h.split("\'")
        const_f, const_i = (30.48, 2.54)
        cm = const_f*float(f) + const_i*float(i.replace('"', ''))
        
    return round(cm)

const_lbs = 0.4536

data['Height'] = data['Height'].apply(height_to_cm)
data['Weight'] = data['Weight'].apply(lambda x: int(x[:-2]) if 'kg' in x else round(int(x[:-3])*const_lbs))

# 'Value', 'Wage' and 'Release Clause' to numeric 
# There're 3 types of 'Value': M, k and 0
# All columns transform to M(millions)
def money_to_numeric(m):
    res = 0
    
    if m[-1] == 'M':
        res = float(m[1:-1])
    elif m[-1] == 'K':
        res = float(m[1:-1])*(10**-3)
        
    return res

money_cols = ['Value', 'Wage', 'Release Clause']

for col in money_cols:
    data[col] = data[col].apply(money_to_numeric)

# 'W/F', 'SM' and 'IR' to numeric
stars_cols = ['W/F', 'SM', 'IR']

for col in stars_cols:
    data[col] = data[col].apply(lambda x: int(x[0]))
    
# 'Hits' to numeric
# Initially, transform 'str' and 'float' to 'int'
data['Hits'] = data[data['Hits'].notnull()]['Hits'].apply(lambda x: int(float(x[:-1])*1000) if 'K' in str(x) else int(x))

# Find mean value for each position
position_hits = data.groupby(['Best Position'])['Hits'].mean().apply(lambda x: round(x))

# Fill NaN in 'Hits' on mean value with references to 'Best Position'
data['Hits'] = data['Hits'].fillna(data['Best Position'].map(position_hits))

# Based on the 'Joined' column, check which players have been playing at a club for more than 10 years
loyalty = data['Joined'].apply(lambda x: date.today() - x.date()) // np.timedelta64(1, 'Y')
# Check a player's loan
data['Loyalty'] = ((loyalty >= 10) & data['Loan Date End'].isnull()).apply(lambda x: 1 if x else 0)

# Drop redundant columns(in my opinion) and write df to csv
data_cleaned = data.drop(columns=['Name', 'photoUrl', 'playerUrl', 'Contract'])
data_cleaned.to_csv('datasets/fifa21_cleaned.csv')