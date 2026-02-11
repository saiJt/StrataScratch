# Import your libraries
import pandas as pd

department = employee[['id','department','first_name','salary']]

department['salary_avg'] = department.groupby('department')['salary']
                                     .transform('mean')

department = department[['department','first_name','salary','salary_avg']].sort_values(by='department')
