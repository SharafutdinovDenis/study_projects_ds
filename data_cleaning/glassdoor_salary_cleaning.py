import pandas as pd

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

# COMPLETE README for main
# company name text only
# state field
# age company
# parsing of job description
# fill nan
# print(data.isna().sum())