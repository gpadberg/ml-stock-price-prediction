import yfinance as yf
import pandas as pd
import statsmodels.api as sm
import numpy as np
import requests
from io import BytesIO
from zipfile import ZipFile

# Download stock data
tickers = ["AAPL"]
stock_data = yf.download(tickers, start="2020-01-01", end="2024-01-01")['Adj Close']

# Calculate daily returns
stock_returns = stock_data.pct_change().dropna()

# Download Fama-French 3 factors using requests and handle SSL verification
ff3_url = 'https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip'
response = requests.get(ff3_url, verify=False)

if response.status_code == 200:
    with ZipFile(BytesIO(response.content)) as z:
        # Extract the CSV file from the zip file
        with z.open('F-F_Research_Data_Factors_daily.CSV') as f:
            ff3_factors = pd.read_csv(f, skiprows=3)
else:
    raise Exception("Failed to download Fama-French data")

# Clean Fama-French data
ff3_factors.columns = ['Date', 'Mkt-RF', 'SMB', 'HML', 'RF']
ff3_factors = ff3_factors[ff3_factors['Date'] < '20240101']
ff3_factors['Date'] = pd.to_datetime(ff3_factors['Date'], format='%Y%m%d')
ff3_factors.set_index('Date', inplace=True)

# Merge stock returns with Fama-French factors
data = pd.merge(stock_returns, ff3_factors, left_index=True, right_index=True)
data['Excess_Return'] = data['Adj Close'] - data['RF']

# Define the regression model
X = data[['Mkt-RF', 'SMB', 'HML']]
y = data['Excess_Return']
X = sm.add_constant(X)  # Adds a constant term to the predictor

# Fit the model
model = sm.OLS(y, X).fit()

# Display the summary of the regression
print(model.summary())
