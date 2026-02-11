# Import your libraries
import pandas as pd

ranking = spotify_worldwide_daily_song_ranking[spotify_worldwide_daily_song_ranking['position'] == 1].groupby('trackname')
                                                                                                     .size()
                                                                                                     .reset_index(name='times_top1')

ranking = ranking.sort_values('times_top1',ascending=False)
