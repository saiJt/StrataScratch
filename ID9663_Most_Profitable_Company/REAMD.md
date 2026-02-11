## [ID 9663] Most Profitable Financial Company
### Objective
Find the most profitable company from **the financial sector** and output the company name along with its continent.

### Problem Link
[StrataScratch ID 9663](https://platform.stratascratch.com/coding/9663-find-the-most-profitable-company-in-the-financial-sector-of-the-entire-world-along-with-its-continent?code_type=2)

### Analysis Approach
- **Data Filtering**: Filter the dataset to include only companies where the `sector` is 'Financials'.
- **Sorting for Ranking**: Sort the filtered data by the `profits` column in descending order (`ascending=False`) to place the most profitable company at the top.
- **Column Selection (Projection)**: Select only the required columns, `company` and `continent`, to meet the output requirements.
- **Top Result**: Use `.head(1)` to extract the single most profitable company after sorting.

### Key Functions
- `df[df['column'] == 'value']`: **Boolean Indexing** used to filter rows based on a specific condition.
- `.sort_values(by='', ascending=False)`: To arrange the data based on a numeric column from highest to lowest.
- `df[['col1','col2']]`: **DataFrame Indexing** with a list of strings to select multiple columns and maintain the DataFrame structure.
- `.head(1)`: To retrieve only the first row of the resulting DataFrame.
