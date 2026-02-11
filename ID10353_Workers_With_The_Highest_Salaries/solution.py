# Import your libraries
import pandas as pd

work_info = worker[['worker_id','salary']]
title_info = title[['worker_ref_id','worker_title']]

final_table = pd.merge(work_info,title_info, left_on = 'worker_id', right_on = 'worker_ref_id', how = 'right')

max_salary = final_table['salary'].max()

final_table = final_table[final_table['salary'] == max_salary].sort_values(by='salary',ascending=False)[['worker_title']]
