## [ID 9653] MacBookPro User Event Count
### Objective
Count the number of user events performed by 'MacBook Pro' users and output the results sorted by event count in descending order.

### Problem Link
[StrataScratch ID 9653](https://platform.stratascratch.com/coding/9653-count-the-number-of-user-events-performed-by-macbookpro-users?code_type=2)

### Analysis Approach
- **Case-Insensitive Filtering**: Applied `.str.lower()` to the `device` column to normalize the data, ensuring all 'MacBook Pro' events are captured regardless of original casing.
- **Data Selection**: Narrowed down the dataset to only essential variables (`event_name`, `device`) before grouping and focus on the target metric.
- **Aggregation**: Groupd by the data by `event_name` and utilized `.size()` to calculate the frequency of each event type.
- **Data Formatting**: Used `.reset_index(name='event_count') to convert the aggregated series into a structured DataFrame and assign a descriptive header to the count column.
- **Sorting**: Ordered the final result by `event_count` in descending order from the most frequent user events.


### Key Functions
- `.str.lower()`: To standardize string data for accurate filtering and prevent case-sensitive misses.
- `groupby().size()`: To group data by a specific variable and count the number of rows in each group.
- `.reset_index(name='...')`: To transform the index back into a column and name the newly created aggregation column.
- `.sort_values(ascending=False)`: To arrange data from highest to lowest values.
