import pandas as pd
import yfinance as yf
import numpy as np
import statsmodels.api as sm

# Define the portfolio and market tickers
portfolio_symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']  # Example portfolio
market_symbol = '^GSPC'  # S&P 500
risk_free_symbol = '^IRX'  # 3-month Treasury bill

# Define the time period
start_date = '2020-01-01'
end_date = '2021-01-01'

# Download data
portfolio_data = yf.download(portfolio_symbols, start=start_date, end=end_date)['Adj Close']
market_data = yf.download(market_symbol, start=start_date, end=end_date)['Adj Close']
risk_free_data = yf.download(risk_free_symbol, start=start_date, end=end_date)['Adj Close']

# Calculate portfolio returns
portfolio_returns = portfolio_data.pct_change().dropna()

# Calculate portfolio weighted returns
portfolio_weights = [0.2, 0.3, 0.25, 0.15, 0.1]
portfolio_returns['Portfolio'] = portfolio_returns.dot(portfolio_weights)

# Calculate market returns
market_returns = market_data.pct_change().dropna()

# Calculate risk-free returns (daily)
risk_free_returns = risk_free_data / 100 / 252
risk_free_returns = risk_free_returns.fillna(method='ffill').dropna()

# Align data by date
data = pd.concat([portfolio_returns['Portfolio'], market_returns, risk_free_returns], axis=1)
data.columns = ['Portfolio', 'Market', 'RiskFree']
data.dropna(inplace=True)

# Calculate excess returns
data['ExcessPortfolio'] = data['Portfolio'] - data['RiskFree']
data['ExcessMarket'] = data['Market'] - data['RiskFree']

# Define the dependent and independent variables
X = data['ExcessMarket']
y = data['ExcessPortfolio']

# Add a constant (intercept) to the independent variable
X = sm.add_constant(X)

# Run the OLS regression
model = sm.OLS(y, X).fit()

# Print the regression results
print(model.summary())