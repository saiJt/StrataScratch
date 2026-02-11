# Import your libraries
import pandas as pd

customers_info = customers[['id','first_name']]

final_table = pd.merge(customers_info,orders,left_on = 'id',right_on = 'cust_id')

target_name = ['Jill','Eva']
final_table = final_table[final_table['first_name'].isin(target_name)]
                                                   .sort_values(by='cust_id')
                                                    [['first_name','order_date','order_details','total_order_cost']]
