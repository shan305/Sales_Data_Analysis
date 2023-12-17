#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random
import datetime

# Create the 'output' folder if it doesn't exist
output_folder = 'output'
os.makedirs(output_folder, exist_ok=True)

def generate_sales_data(num_records=1000):
    """Generate dummy retail sales data."""
    fake = Faker()
    Faker.seed(42)  # Use class method to set seed
    
    data = []
    for _ in range(num_records):
        date = fake.date_between(start_date='-1y', end_date='today')
        product = fake.word()
        price = round(random.uniform(5, 100), 2)
        quantity = random.randint(1, 100)
        total_sales = round(price * quantity, 2)

        data.append([date, product, price, quantity, total_sales])

    columns = ['Date', 'Product', 'Price', 'Quantity', 'Total Sales']
    df = pd.DataFrame(data, columns=columns)
    return df


def save_text_to_file(text, filename):
    """Save text to a file in the 'output' folder."""
    filepath = os.path.join(output_folder, filename)
    with open(filepath, 'w') as file:
        file.write(text)

def display_data_info(sales_data):
    """Display basic information about the dataset."""
    info_text = str(sales_data.info())
    print(info_text)
    save_text_to_file(info_text, 'data_info.txt')

    head_text = str(sales_data.head())
    print(head_text)
    save_text_to_file(head_text, 'data_head.txt')

def check_duplicates_missing_values(sales_data):
    """Check for duplicate entries and missing values."""
    duplicates_text = f"Duplicate entries: {sales_data.duplicated().sum()}"
    missing_values_text = f"Missing values:\n{sales_data.isnull().sum()}"
    
    print(duplicates_text)
    print(missing_values_text)
    
    save_text_to_file(duplicates_text, 'duplicate_entries.txt')
    save_text_to_file(missing_values_text, 'missing_values.txt')

def visualize_total_sales_distribution(sales_data):
    """Visualize the distribution of total sales."""
    plt.figure(figsize=(10, 6))
    sns.histplot(sales_data['Total Sales'], bins=30, kde=True)
    plt.title('Distribution of Total Sales')
    plt.xlabel('Total Sales')
    
    # Save the plot
    plt.savefig(os.path.join(output_folder, 'total_sales_distribution.png'))
    
    plt.show()

def visualize_sales_trends_over_time(sales_data):
    """Visualize trends in sales over time (monthly, yearly)."""
    sales_data['Date'] = pd.to_datetime(sales_data['Date'])
    sales_data.set_index('Date', inplace=True)

    plt.figure(figsize=(12, 6))
    sales_data.resample('M')['Total Sales'].sum().plot(label='Monthly Sales')
    sales_data.resample('Y')['Total Sales'].sum().plot(label='Yearly Sales', linestyle='dashed')
    plt.title('Sales Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    
    # Save the plot
    plt.savefig(os.path.join(output_folder, 'sales_trends_over_time.png'))
    
    plt.show()

def feature_engineering(sales_data):
    """Extract month and year from the date for further analysis."""
    sales_data['Month'] = sales_data.index.month
    sales_data['Year'] = sales_data.index.year

def aggregate_data(sales_data):
    """Aggregate data for analysis by month and year."""
    monthly_sales = sales_data.groupby(['Year', 'Month'])['Total Sales'].sum()
    yearly_sales = sales_data.groupby('Year')['Total Sales'].sum()
    return monthly_sales, yearly_sales

def visualize_aggregated_data(monthly_sales, yearly_sales):
    """Visualize monthly and yearly sales trends."""
    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    monthly_sales.plot(kind='bar', color='skyblue')
    plt.title('Monthly Sales Trends')
    plt.xlabel('Year-Month')
    plt.ylabel('Total Sales')

    plt.subplot(1, 2, 2)
    yearly_sales.plot(kind='bar', color='salmon')
    plt.title('Yearly Sales Trends')
    plt.xlabel('Year')
    plt.ylabel('Total Sales')
    
    # Save the plot
    plt.savefig(os.path.join(output_folder, 'aggregated_sales_trends.png'))
    
    plt.tight_layout()
    plt.show()

def analyze_top_selling_products(sales_data):
    """Analyze and visualize top-selling products."""
    top_products = sales_data.groupby('Product')['Total Sales'].sum().nlargest(5)
    top_products_text = str(top_products)
    
    print("Top Selling Products:\n", top_products_text)
    save_text_to_file(top_products_text, 'top_selling_products.txt')

    plt.figure(figsize=(10, 6))
    top_products.plot(kind='bar', color='green')
    plt.title('Top Selling Products')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    
    # Save the plot
    plt.savefig(os.path.join(output_folder, 'top_selling_products.png'))
    
    plt.show()

def analyze_price_distribution(sales_data):
    """Analyze the distribution of product prices."""
    plt.figure(figsize=(10, 6))
    sns.histplot(sales_data['Price'], bins=20, kde=True, color='purple')
    plt.title('Distribution of Product Prices')
    plt.xlabel('Price')
    
    # Save the plot
    plt.savefig(os.path.join(output_folder, 'price_distribution.png'))
    
    plt.show()

def main():
    # Generate dummy data with 1000 records
    sales_data = generate_sales_data()

    # Display basic information about the dataset
    display_data_info(sales_data)

    # Check for duplicate entries and missing values
    check_duplicates_missing_values(sales_data)

    # Visualize the distribution of total sales
    visualize_total_sales_distribution(sales_data)

    # Visualize trends in sales over time (monthly, yearly)
    visualize_sales_trends_over_time(sales_data)

    # Extract month and year from the date for further analysis
    feature_engineering(sales_data)

    # Aggregate data for analysis by month and year
    monthly_sales, yearly_sales = aggregate_data(sales_data)

    # Visualize monthly and yearly sales trends
    visualize_aggregated_data(monthly_sales, yearly_sales)

    # Analyze and visualize top-selling products
    analyze_top_selling_products(sales_data)

    # Analyze the distribution of product prices
    analyze_price_distribution(sales_data)

    # Conclusion

if __name__ == "__main__":
    main()
