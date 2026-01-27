## [ID 2056] Number of Shipments Per Month
### Objective
Calculate the total number of unique shipments for each month. A unique shipment is defined by the combinations of `shipment_id` and `sub_id`. 
The final output should display the month in `YYYY-MM` format along with the corresponding shipment cout.

### Problem Link
[StrataScratch ID 2056](https://platform.stratascratch.com/coding/2056-number-of-shipments-per-month?code_type=2)

### Analysis Approach
- **Time Transformation**: Converted the `shipment_date` column to a datetime object using `pd.to_datetime()`
- **Feature Engineering**: Formatted the date into a `YYYY-MM` string using `.dt.strftime('%Y-%m')` to facilitate montly aggregation.
- **Data Deduplication**: Used `drop_duplicates()` to ensure that each unique combination of `shipment_id` and `sub_id` is counted only once per month, maintaining data integrity.
- **Aggregation**: Grouped the data by the formatted `shipment_date` and calculated the total number of shipments using `.size()`.


### Key Functions
- `pd.to_datetime()`: For converting string dates to datetime objects.
- `.dt.strftime()`: For reformatting date objects into specific string patterns.
- `drop_duplicates()`: To remove redundant records based on the composite key.
- `groupby().size()`: For counting the number of occurrences within each monthly group.
