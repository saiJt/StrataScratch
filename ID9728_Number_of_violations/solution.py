# Import your libraries
import pandas as pd

# Start writing code
sf_restaurant_health_violations.head()
short = sf_restaurant_health_violations

short['inspection_date'] = pd.to_datetime(short['inspection_date'])
                             .dt.strftime('%Y')
                             .astype(int)


Rox_vio = short[short['business_name'].str.contains('Roxanne Cafe', case = False)]
                                      .groupby('inspection_date')
                                      .size()
                                      .reset_index(name = 'n_violations')
                                      .rename(columns = {'inspection_date' : 'inspection_year'})
