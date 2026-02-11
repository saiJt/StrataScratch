## [ID 9688] Churro Activity Date
### Objective
Find the inspection date and risk category (`pe_description`) of facilities named 'STREET CHURROS' that received a score below 95.

### Problem Link
[StrataScratch ID 9688](https://platform.stratascratch.com/coding/9688-churro-activity-date?code_type=2)

### Analysis Approach
- **Flexible String Matching**: Used `.str.contains('STREET CHURROS', case=False)` to ensure all relevant facilities are captured, regardless of potential case variations or additional suffixes in the naming.
- **Boolean Logic**: Combined the naming condition with a numeric threshold (`socre < 95`) using **AND**(`&`) operator.

### Key Functions
- `.str.contains('', case = False)`: To perform a case-insensitive search within a string column.
- `(cond1) & (cond2)`: To filter rows based on multiple logical criteria.
- `df[['col1', 'col2']]`: To select specific columns for the final output.
