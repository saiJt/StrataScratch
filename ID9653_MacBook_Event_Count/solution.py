# Import your libraries
import pandas as pd

# Start writing code

final_table = playbook_events[playbook_events['device'].str.lower() =='macbook pro']
final_table = (
                final_table[['event_name','device']]
                  .groupby('event_name')
                  .size()
                  .reset_index(name = 'event_count')
                  .sort_values(by = 'event_count',ascending=False)
)


# Method_Chaining
final_table = (
                (playbook_events[playbook_events['device'].str.lower() =='macbook pro'])[['event_name','device']]
                  .groupby('event_name')
                  .size()
                  .reset_index(name = 'event_count')
                  .sort_values(by = 'event_count',ascending=False)
)
