# Import your libraries
import pandas as pd

# Step 1: Filter for flags approved by YT
flag_review = flag_review[flag_review['reviewed_outcome'] == 'APPROVED']
flag_info = [['flag_id','reviewed_by_yt','reviewed_outcome']]

# Step 2: Merge datasets on flag_id
approved = pd.merge(user_flags,flag_review)

# Step 3: Deduplicate flags for distinct videos per user
approved=approved.drop_duplicates(subset=['video_id', 'user_firstname', 'user_lastname'])
approved['username'] = approved['user_firstname'] +' ' + approved['user_lastname']

# Step 4: Group users by their name and get the number of flag_id
approved = approved.groupby('username')['flag_id'].size().reset_index()

# Step 5: Identify user with the maximum number of approved flags
final_table = approved[approved['flag_id'] == approved['flag_id'].max()]['username']
