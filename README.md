
```markdown
# Sales Data Analysis

This Python script performs data analysis on synthetic retail sales data generated using the Faker library. The analysis covers various aspects of the data, including data generation, exploration, cleaning, and visualization.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/shan305/Sales_Data_Analysis.git
   cd sales-data-analysis
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv salesenv
   ```

3. Activate the virtual environment:

   - On macOS/Linux:

     ```bash
     source salesenv/bin/activate
     ```

   - On Windows:

     ```bash
     .\salesenv\Scripts\activate
     ```

4. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the script:

```bash
python sales_data_analysis.py
```

The script will generate synthetic sales data, perform data analysis, and save output images and text in the "output" folder.

## Output

- **Total Sales Distribution**: `output/total_sales_distribution.png`
- **Sales Trends Over Time**: `output/sales_trends_over_time.png`
- **Aggregated Sales Trends**: `output/aggregated_sales_trends.png`
- **Top Selling Products**: `output/top_selling_products.png`
- **Price Distribution**: `output/price_distribution.png`
- **Data Information**: `output/data_info.txt`
- **Duplicate Entries**: `output/duplicate_entries.txt`
- **Missing Values**: `output/missing_values.txt`
- **Top Selling Products Text**: `output/top_selling_products.txt`
- **Conclusion**: `output/conclusion.txt`

## Acknowledgments

- [Faker](https://github.com/joke2k/faker) - A library for generating fake data.

## Author

- Zeeshan Ali
```
