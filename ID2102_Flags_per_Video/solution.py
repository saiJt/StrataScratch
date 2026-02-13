# Import your libraries
import pandas as pd

# Start writing code
user_flags.head()

user_flags = user_flags[user_flags['flag_id'].notnull()]
user_flags=user_flags.drop_duplicates(subset=['video_id', 'user_firstname', 'user_lastname'])
user_flags['full_name'] = user_flags['user_firstname'] + ' ' + user_flags['user_lastname']
final_table = user_flags.groupby('video_id')['full_name'].size().reset_index(name = 'number_unique_users')
