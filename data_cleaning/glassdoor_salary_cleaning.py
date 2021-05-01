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

# Add columns 'job_state' and 'headquarters_state'
data['jobs_state'] = data['Location'].apply(lambda x: x.split(',')[-1].strip())
print(data['jobs_state'].unique())

data['headquarters_state'] = data['Headquarters'].apply(lambda x: x.split(',')[-1].strip())
print(data['headquarters_state'].value_counts())

# Add column 'headquarters_abroad' if headquarters locate not in US
data['headquarters_abroad'] = data['headquarters_state'].apply(lambda x: 1 if len(x) > 2 else 0)
print(data['headquarters_abroad'].value_counts())

# Add columns 'same_location' if Location and Headquarters match 
data['same_location'] = data.apply(lambda x: 1 if x['Location'] == x['Headquarters'] else 0, axis = 1)

# Add column 'age' for companies
current_year = date.today().year
data['age'] = data['Founded'].apply(lambda x: current_year - x if x>0 else x)

# Parse 'Job Desctiption' to popular tools

#python
data['python'] = data['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
print(data['python'].value_counts())
 
#r studio 
data['R'] = data['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
print(data['R'].value_counts())

#spark 
data['spark'] = data['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
print(data['spark'].value_counts())

#tableau 
data['tableau'] = data['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
print(data['tableau'].value_counts())

#excel
data['excel'] = data['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
print(data['excel'].value_counts())
# fill nan
# print(data.isna().sum())