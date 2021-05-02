# Data Cleaning
Here's I'm preparing datasets for analysis by removing or modifying data that is incorrect, incomplete, irrelevant, duplicated, or improperly formatted.
## Fifa 21 
- Remove new lines from 'Clubs'
- Add columns 'ContractStart', 'ContractEnd'
- Transform 'Loan Date End' and 'Joined' to datetime
- Transform 'Height' and 'Weight' to numeric
- Money fields ('Value', 'Wage' and 'Release Clause') to numeric and a single equivalent (Millions)
- Transform stars fields ('W/F', 'SM' and 'IR') to numeric
- Transform 'Hits' to numeric
- Fill NaN in 'Hits' on mean value with references to 'Best Position'
- Based on the 'Joined' column, check which players have been playing at a club for more than 10 years

## Glassdoor jobs
- Salary Parsing
- Remove from 'Company Name' number of rating
- Add columns 'job_state' and 'headquarters_state'
- Add column 'headquarters_abroad' if headquarters locate not in US
- Add columns 'same_location' if Location and Headquarters match 
- Add column 'age' for companies
- Parse 'Job Desctiption' to popular tools
- Add column 'simple_title' for classificating jobs
- Add column 'seniority'
- Add columns 'desc_length'
- Count competitors of each company
- Convert hourly salary to annual
