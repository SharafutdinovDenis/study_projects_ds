import pandas as pd
from datetime import date

data = pd.read_csv('../datasets/glassdoor_jobs.csv', index_col=0)
data.info()

# Salary Parsing
def get_salary(sal):
    cl_sal = sal.split('(')[0]
    cl_sal = cl_sal.split(':')[-1]
    cl_sal = cl_sal.lower().replace('per hour', '')
    cl_sal = cl_sal.lower().replace('$', '').replace('k', '')
    return cl_sal

data['hourly'] = data['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
data['employer_provided'] = data['Salary Estimate'].apply(lambda x: 1 if 'employer provided' in x.lower() else 0)

data = data[data['Salary Estimate'] != '-1']

range_salary = data['Salary Estimate'].apply(get_salary)

data['min_salary'] = range_salary.apply(lambda x: int(x.split('-')[0]))
data['max_salary'] = range_salary.apply(lambda x: int(x.split('-')[-1]))
data['avg_salary'] = (data['max_salary'] - data['min_salary'] / 2)

# Remove from 'Company Name' number of rating
data['Company Name'] = data['Company Name'].apply(lambda x: x.split('\n')[0])
# state field
# Add column 'Age company'
current_year = date.today().year
data['age'] = data['Founded'].apply(lambda x: current_year - x if x>0 else x)
# parsing of job description
# fill nan
# print(data.isna().sum())