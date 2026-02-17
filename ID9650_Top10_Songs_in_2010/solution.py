# Import your libraries
import pandas as pd

rank = billboard_top_100_year_end[billboard_top_100_year_end['year'] == 2010].drop_duplicates(subset=['group_name','song_name'])
                                                                             .sort_values(by='year_rank')[['year_rank','group_name','song_name']]
                                                                             .head(10)
