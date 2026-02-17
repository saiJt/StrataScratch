# Import your libraries
import pandas as pd
import math 
# Start writing code
linkedin_projects['working_days'] = ((pd.to_datetime(linkedin_projects['end_date'])) - (pd.to_datetime(linkedin_projects['start_date']))).dt.days
link_project = linkedin_projects[['id','title','budget','working_days']]

salary_info = linkedin_employees[['id','salary']]
merged_dataset = pd.merge(link_project,linkedin_emp_projects, left_on = 'id', right_on = 'project_id', how = 'outer')

final_dataset = pd.merge(merged_dataset,salary_info, left_on = 'emp_id', right_on = 'id')

final_dataset['prorated_cost'] = final_dataset['working_days']/365 * final_dataset['salary']

final_dataset = final_dataset.groupby(['title','budget'])['prorated_cost'].sum().apply(math.ceil).reset_index(name = 'prorated_expense')

result = final_dataset[final_dataset['budget'] <= final_dataset['prorated_expense']]
