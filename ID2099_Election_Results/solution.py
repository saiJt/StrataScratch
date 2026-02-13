# Import your libraries
import pandas as pd

# Step 1: Remove null entries to focus on voters who did vote
voters = voting_results.dropna().sort_values('voter')

# Step 2: Assign a weight to each vote by dividing it by the number of candidates selected
voters['vote_value'] = 1/voters.groupby('voter')['candidate'].transform('size')

# Step 3: Calculate the total weighted votes received by each candidates got
most_candidate = voters.groupby('candidate')['vote_value'].sum().reset_index()

# Step 4: Identify the candidate with the highest votes total
final_table = most_candidate[most_candidate['vote_value'] == most_candidate['vote_value'].max()]['candidate']
