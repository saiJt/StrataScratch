# Import your libraries
import pandas as pd
import math 

# Step 1: Calculate the duration of each projects.
linkedin_projects['working_days'] = ((pd.to_datetime(linkedin_projects['end_date'])) - (pd.to_datetime(linkedin_projects['start_date']))).dt.days
link_project = linkedin_projects[['id','title','budget','working_days']]

# Step 2: Merge three datasets into one table.
salary_info = linkedin_employees[['id','salary']]
merged_dataset = pd.merge(link_project,
                          linkedin_emp_projects, 
                          left_on = 'id', 
                          right_on = 'project_id', 
                          how = 'outer')

final_dataset = pd.merge(merged_dataset,
                         salary_info, 
                         left_on = 'emp_id', 
                         right_on = 'id')

# Step 3: Calculate the prorated cost by using [End date - Start date]/365 * Annual Salary
final_dataset['prorated_cost'] = final_dataset['working_days'] / 365 * final_dataset['salary']

# Step 4: Aggregate prorated costs by project and apply ceiling..
final_dataset = final_dataset.groupby(['title','budget'])['prorated_cost'].sum()
                                                                          .apply(math.ceil)
                                                                          .reset_index(name = 'prorated_expense')

# Step 5: Filter projects that expense more than the budget.
result = final_dataset[final_dataset['budget'] <= final_dataset['prorated_expense']]

