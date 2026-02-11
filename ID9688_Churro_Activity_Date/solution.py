# Import your libraries
import pandas as pd

# Start writing code
los_angeles_restaurant_health_inspections.head()
dataSet = los_angeles_restaurant_health_inspections

below_stand = dataSet[(dataSet['facility_name'].str.contains('STREET CHURROS', case = False))&(dataSet['score'] < 95)][['activity_date','pe_description']]
