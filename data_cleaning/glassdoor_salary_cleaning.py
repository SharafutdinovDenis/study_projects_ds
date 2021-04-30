import pandas as pd

data = pd.read_csv('../../datasets/glassdoor_jobs.csv', na_values='-1', index_col=0)
data.info()
# salary parsing
# company name text only
# state field
# age company
# parsing of job description
# fill nan
# print(data.isna().sum())