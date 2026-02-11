# Import your libraries
import pandas as pd

# Start writing code
airbnb_search_details.head()

furniture_avg = airbnb_search_details[['city','property_type','bathrooms','bedrooms']]

bathroom_avg = furniture_avg.groupby(['city','property_type'])[['bathrooms','bedrooms']]
                            .mean()
                            .reset_index()
                            .rename(columns = {'bathrooms':'n_bathrooms_avg','bedrooms':'n_bedrooms_avg'})
