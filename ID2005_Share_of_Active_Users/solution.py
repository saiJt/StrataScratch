# Import your libraries
import pandas as pd

# Step 1: Get the total number of users in the dataset
total = len(fb_active_users)

# Step 2: Filter users who are from 'the USA' and have an 'open' status
open_user = fb_active_users[(fb_active_users['status'] == 'open') & (fb_active_users['country'] == 'USA')]

# Step 3: Count the number of users who meet both criteria
user = len(open_user)

# Step 4: Calculate the percentage of Active US users and store it in a DataFrame
final_table = pd.DataFrame({'us_active_share':[user/total*100]})
