# Import your libraries
import pandas as pd

# Start writing code

num_shipments = amazon_shipment[['shipment_id','sub_id','shipment_date']].copy()

num_shipments['shipment_date'] = pd.to_datetime(num_shipments['shipment_date']).dt.strftime('%Y-%m')

num_cleaned = num_shipments.drop_duplicates().groupby('shipment_date').size().reset_index()
