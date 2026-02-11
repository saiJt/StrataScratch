# Import your libraries
import pandas as pd

# Start writing code
forbes_global_2010_2014.head()

company = forbes_global_2010_2014[forbes_global_2010_2014['sector'] == 'Financials']
          .sort_values(by='profits',ascending=False)
          [['company','continent']]
          .head(1)
