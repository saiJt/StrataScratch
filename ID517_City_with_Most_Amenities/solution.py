# Import your libraries
import pandas as pd

# Step 1: Calculate the number of amenities for each host.
df_amenities = airbnb_search_details
df_amenities['amenity_count'] = df_amenities['amenities'].str
                                                         .split(',')
                                                         .apply(len)
# Step 2: Aggregate the total amenity count by city
city_sums = df_amenities.groupby('city')['amenity_count'].sum()
                                                         .reset_index()

# Step 3: Identify the city (or cities) with the maximum total amenities
final_table = city_sums[city_sums['amenity_count'] == city_sums['amenity_count'].max()]['city']
