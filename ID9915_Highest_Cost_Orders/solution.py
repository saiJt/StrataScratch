# Import your libraries
import pandas as pd

# Start writing code
customers.head()

orders = orders[orders['order_date'].between('2019-02-01','2019-05-01')]
cust_info = customers[['id','first_name']]
order_info = orders [['cust_id','order_date','order_details','total_order_cost']]

merged_dataset = pd.merge(cust_info,order_info,left_on = 'id',right_on = 'cust_id')

final_table = merged_dataset.groupby(['id','first_name','order_date'])['total_order_cost'].sum().reset_index()


final_table['max_at_date'] = final_table.groupby('order_date')['total_order_cost'].transform('max')

result = final_table[final_table['total_order_cost'] == final_table['max_at_date']].sort_values(by= 'id')[['first_name','order_date','max_at_date']]
                                                                                   .rename(columns = {'max_at_date':'max_cost'})
