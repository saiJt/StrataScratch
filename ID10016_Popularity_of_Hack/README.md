## [ID 10061] Popularity of Hack
### Objective
Find the average popularity of the 'Hack' programming language per office location.

### Problem Link
[StrataScratch ID 10061](https://platform.stratascratch.com/coding/10061-popularity-of-hack?code_type=2)

### Analysis Approach
- **Data Merging**: Joining `facebook_employees` (location data) and `facebook_hack_survey` (popularity data) using `user_id` as the index key.
- **Index Management**: Aligned both datasets by setting **the id column** as the index before joining to ensure data.
- **Aggregation**: Grouped the merged dataset by `location` and calculated the mean `popularity` score.
- **Data Formatting**: Reverted the index to a column format using `reset_index()` for a clean output.


### Key Functions
- `set_index()`, `join()`, `groupby()`, `mean()`, `reset_index()`


