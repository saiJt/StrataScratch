# Import your libraries
import pandas as pd

# Start writing code
orders.head()

customer_info = customers[['id','first_name','last_name','city',]]
orders_info = orders[['cust_id','order_details']]

final_table = pd.merge(customer_info,orders_info, left_on = 'id',right_on = 'cust_id',how='left')
              [['first_name','last_name','city','order_details']]
              .sort_values(by='first_name')
