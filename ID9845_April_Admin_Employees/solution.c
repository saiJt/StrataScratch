# Import your libraries
import pandas as pd

# Start writing code
worker.head()

department = worker[(worker['department'] == 'Admin') & (pd.to_datetime(worker['joining_date']).dt.month >= 4)].shape[0]

result = pd.DataFrame({'n_admins': [department]})
