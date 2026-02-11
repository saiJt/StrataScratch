# Import your libraries
import pandas as pd

# 1. Filter for workers who joined on or after April 1, 2014
# 2. Group by department and count the occurrences
# 3. Sort by count, reset index, and name the resulting column

final_table = worker[pd.to_datetime(worker['joining_date']).dt.strftime('%Y%m%d').astype(int) >= 20140401]
                                                           .groupby('department')
                                                           .size()
                                                           .sort_values(ascending=False)
                                                           .reset_index(name='num_workers')

