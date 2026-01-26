# Import your libraries
import pandas as pd

# Start writing code

employees_info = facebook_employees[['id','location']]
survey_info = facebook_hack_survey[['employee_id','popularity']]

final_table = employees_info.set_index('id').join(survey_info.rename(columns = {'employee_id':'id'}).set_index('id'))

final_table = final_table.groupby('location')['popularity'].mean().reset_index()



# Method_Chaining
final_table = (
               facebook_employees[['id','location']]
                .set_index('id')
                .join(
                  facebook_hack_survey[['employee_id','popularity']]
                  .rename(columns = {'employee_id':'id'})
                  .set_index('id')
                )
                .groupby('location')['popularity']
                .mean()
                .reset_index()
)
