import yfinance as yf
import pandas as pd

# Step 1: Define the list of stock symbols
stock_symbols = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'TSLA', 'BRK-B', 'JNJ', 'V', 'WMT',
    'JPM', 'PG', 'MA', 'NVDA', 'DIS', 'HD', 'PYPL', 'BAC', 'VZ', 'ADBE',
    'NFLX', 'INTC', 'CMCSA', 'PFE', 'KO', 'MRK', 'CSCO', 'PEP', 'XOM', 'T',
    'ABT', 'ABBV', 'COST', 'CRM', 'AVGO', 'NKE', 'MCD', 'ACN', 'MDT', 'TMO',
    'NEE', 'TXN', 'UNH', 'BMY', 'LLY', 'HON', 'IBM', 'QCOM', 'LIN', 'UNP'
]

# Step 2: Download historical data for each stock
data = yf.download(stock_symbols, start='2020-01-01', end='2021-01-01')

# Step 3: Save the data to a CSV file
data.to_csv('stocks_data.csv')

print("Data extraction complete and saved to stocks_data.csv")
