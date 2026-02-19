# Import your libraries
import pandas as pd

grouped = facebook_complaints.groupby('type')['processed'].mean()
                                                          .round(2)
                                                          .reset_index()
                                                          .rename(columns= {'processed':'processed_rate'})
