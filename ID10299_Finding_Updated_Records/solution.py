# Import your libraries
import pandas as pd


ms_employee_salary = ms_employee_salary.sort_values('salary',ascending=False)
                                       .drop_duplicates(subset=['first_name', 'last_name'], keep='first')
                                       .sort_values('id')
