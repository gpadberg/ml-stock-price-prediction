import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Step 1: Download Historical Data
stock_symbol = 'AAPL'  # You can change this to any stock symbol you like
start_date = '2020-01-01'
end_date = '2021-01-01'

# Download data from Yahoo Finance
data = yf.download(stock_symbol, start=start_date, end=end_date)
#Download Historical Data:
#Define the stock symbol, start date, and end date.
#Use yfinance to download the data.

# Step 2: Calculate Daily Returns
data['Daily Return'] = data['Adj Close'].pct_change()
#Calculate Daily Returns:
#Use the adjusted closing prices to calculate daily returns.

# Step 3: Plot the Returns
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Daily Return'], label='Daily Return')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.title(f'{stock_symbol} Daily Returns')
plt.legend()
plt.grid(True)
plt.show()
#Plot the Returns:
#Create a plot using matplotlib.