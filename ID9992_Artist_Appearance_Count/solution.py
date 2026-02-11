# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking.head()

ranking = spotify_worldwide_daily_song_ranking.groupby('artist')
                                              .size()
                                              .reset_index(name = 'n_occurences')
                                              .sort_values(by='n_occurences', ascending = False)
