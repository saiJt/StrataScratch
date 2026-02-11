# Import your libraries
import pandas as pd

max_cool = yelp_reviews['cool'].max()

coolest = yelp_reviews[yelp_reviews['cool']== max_cool].sort_values(by='cool',ascending=False)[['business_name','review_text']]


# or
coolest = yelp_reviews[yelp_reviews['cool']== yelp_reviews['cool'].max()].sort_values(by='cool',ascending=False)[['business_name','review_text']]
