import pandas as pd
import yfinance as yf
import numpy as np
import os
import pytz
from datetime import datetime
import matplotlib.pyplot as plt

# Step 1: Define the portfolio
portfolio_symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']  # Updated from 'FB' to 'META'
portfolio_weights = [0.2, 0.3, 0.25, 0.15, 0.1]

# Step 2: Set the time zone explicitly if not set
if not os.getenv('TZ'):
    os.environ['TZ'] = 'UTC'
    pytz.timezone('UTC')

# Step 3: Download historical data
start_date = '2020-01-01'
end_date = '2021-01-01'

# Ensure time zone awareness
start_date = pd.Timestamp(start_date).tz_localize('UTC')
end_date = pd.Timestamp(end_date).tz_localize('UTC')

# Download data from Yahoo Finance
data = yf.download(portfolio_symbols, start=start_date, end=end_date)['Adj Close']

# Check for missing data
if data.isnull().values.any():
    print("Warning: Missing data detected. Filling missing values.")
    data = data.fillna(method='ffill').fillna(method='bfill')

# Step 4: Calculate daily returns for each stock
returns = data.pct_change(fill_method=None).dropna()

# Step 5: Calculate portfolio return and risk
# Calculate the weighted average return
portfolio_return = np.dot(returns.mean(), portfolio_weights) * 252  # Annualize the return

# Calculate the covariance matrix
cov_matrix = returns.cov() * 252  # Annualize the covariance matrix

# Calculate the portfolio risk (standard deviation)
portfolio_variance = np.dot(portfolio_weights, np.dot(cov_matrix, portfolio_weights))
portfolio_risk = np.sqrt(portfolio_variance)

print(f"Annualized Portfolio Return: {portfolio_return:.2f}")
print(f"Annualized Portfolio Risk (Standard Deviation): {portfolio_risk:.2f}")

# Optional: Plot the portfolio's cumulative returns
cumulative_returns = (1 + returns).cumprod()
portfolio_cumulative_returns = cumulative_returns.dot(portfolio_weights)

plt.figure(figsize=(10, 5))
plt.plot(cumulative_returns.index, portfolio_cumulative_returns, label='Portfolio Cumulative Return')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.title('Portfolio Cumulative Returns Over Time')
plt.legend()
plt.grid(True)
plt.show()