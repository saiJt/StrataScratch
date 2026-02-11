# Import your libraries
import pandas as pd

events = fact_events[['client_id','time_id','user_id',]]

events['month'] = events['time_id'].dt.month

result= events.groupby(['client_id','month'])['user_id']
              .nunique()
              .reset_index()
              .rename(columns={'user_id':'users_num'})
