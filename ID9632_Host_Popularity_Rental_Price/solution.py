# Import your libraries
import pandas as pd

# Step 1: deduplicate based on ID
airbnb_host_searches = airbnb_host_searches[['id','price','number_of_reviews']].copy().drop_duplicates(subset='id')

# Step 2:Binning
bins = [-1,0,5,15,40, float('inf')]
group_name = ['New','Rising','Trending Up','Popular','Hot']

airbnb_host_searches['host_popularity'] = pd.cut(airbnb_host_searches['number_of_reviews'], bins=bins, labels=group_name)

# Step 3: Calculate summary statistics and sort by the lowest entry price.
result = airbnb_host_searches.groupby('host_popularity')['price'].agg(['min', 'mean', 'max']).sort_values(by = 'min').reset_index().rename(columns = {'min':'min_price','mean':'avg_price','max':'max_price'})







import pandas as pd

airbnb_host_searches = airbnb_host_searches[['id','price','number_of_reviews']].copy()
                                                                               .drop_duplicates(subset='id')

bins = [-1,0,5,15,40, float('inf')]
group_name = ['New','Rising','Trending Up','Popular','Hot']


airbnb_host_searches['host_popularity'] = pd.cut(airbnb_host_searches['number_of_reviews'], bins=bins, labels=group_name)

result = airbnb_host_searches.groupby('host_popularity')['price'].agg([
                                                                       min_price = 'min', 
                                                                       mean_price = 'mean', 
                                                                       max_price = 'max'])
                                                                 .reset_index()
final_table = result.sort_values(by='min_price')
