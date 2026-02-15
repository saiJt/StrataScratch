# Import your libraries
import pandas as pd

sat_scores = sat_scores[['student_id','sat_writing']]

final_table = sat_scores[sat_scores['sat_writing'] == sat_scores['sat_writing'].median()]['student_id']
