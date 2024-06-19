import pandas as pd
import yfinance as yf
import numpy as np

# Step 1: Download Historical Data
stock_symbol = 'AAPL'  # You can change this to any stock symbol you like
market_symbol = '^GSPC'  # S&P 500 as the market index
start_date = '2020-01-01'
end_date = '2021-01-01'

# Download data from Yahoo Finance
# Use the adjusted closing prices to calculate daily returns for both the stock and the market index.
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
market_data = yf.download(market_symbol, start=start_date, end=end_date)

# Step 2: Calculate Daily Returns
stock_data['Daily Return'] = stock_data['Adj Close'].pct_change()
market_data['Daily Return'] = market_data['Adj Close'].pct_change()

# Remove the first row with NaN values resulting from pct_change()
stock_data = stock_data.dropna()
market_data = market_data.dropna()

# Step 3: Calculate Beta
# Calculate the covariance matrix of the daily returns.
# Extract the covariance between the stock and the market and the variance of the market returns to calculate beta.
cov_matrix = np.cov(stock_data['Daily Return'], market_data['Daily Return'])
beta = cov_matrix[0, 1] / cov_matrix[1, 1]
print(f"The beta of {stock_symbol} is: {beta:.4f}")

# Optional: Plot the returns for visualization
# Plot the daily returns of the stock and the market for visualization.
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(stock_data.index, stock_data['Daily Return'], label=f'{stock_symbol} Daily Return')
plt.plot(market_data.index, market_data['Daily Return'], label='Market Daily Return', alpha=0.7)
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.title(f'{stock_symbol} vs Market Daily Returns')
plt.legend()
plt.grid(True)
plt.show()