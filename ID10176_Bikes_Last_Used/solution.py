# Import your libraries
import pandas as pd

# Method 1: The Aggregation Way
# Group by bike and find the maximum (latest) end_time
bike_used = dc_bikeshare_q1_2012.groupby('bike_number')['end_time']
                                .max()
                                .sort_values(ascending=False)
                                .reset_index()
                                .rename(columns = {'end_time':'last_used'})


# Method 2: The Sorting & Filtering Way
# 1. Create a numeric sort key for precise ordering
dc_bikeshare_q1_2012['sort_key'] = pd.to_datetime(dc_bikeshare_q1_2012['end_time']).dt.strftime("%Y%m%d%H%M%S").astype(int)


# 2. Sort by the key and keep the first occurrence of each bike
bike_use = dc_bikeshare_q1_2012.sort_values(by = 'sort_key',ascending=False)

bike_use = bike_use.drop_duplicates(subset='bike_number', keep='first')[['bike_number','end_time']]
                   .rename(columns = {'end_time':'last_used'})
