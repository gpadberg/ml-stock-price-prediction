import pandas as pd
import numpy as np
import yfinance as yf
import statsmodels.api as sm
from scipy.stats import shapiro, normaltest, jarque_bera
from statsmodels.tsa.stattools import adfuller
from arch.unitroot import VarianceRatio

# Step 1: Obtain Historical Stock and Market Returns
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]  # Example tickers
market_index = "^GSPC"  # S&P 500 as the market index

# Download data
data = yf.download(tickers + [market_index], start="2020-01-01", end="2024-01-01")['Adj Close']

# Step 2: Preprocess Data
# Calculate daily returns
daily_returns = data.pct_change().dropna()

# Separate market returns
market_returns = daily_returns[market_index]
stock_returns = daily_returns.drop(columns=[market_index])

# Step 3: Run Statistical Tests
def run_stat_tests(returns, ticker):
    print(f"\nResults for {ticker}:")

    # Durbin-Watson Test for autocorrelation
    dw_stat = sm.stats.durbin_watson(returns)
    print(f"Durbin-Watson Statistic: {dw_stat}")

    # Runs Test for randomness
    runs_test_stat, runs_test_p = sm.stats.runstest_1samp(returns)
    print(f"Runs Test p-value: {runs_test_p}")

    # Variance Ratio Test for predictability
    vr_stat = VarianceRatio(returns, lags=2)
    print(f"Variance Ratio Test p-value: {vr_stat.pvalue}")

    # Shapiro-Wilk Test for normality
    shapiro_stat, shapiro_p = shapiro(returns)
    print(f"Shapiro-Wilk Test p-value: {shapiro_p}")

    # Additional Normality Tests
    k2, p_normaltest = normaltest(returns)
    print(f"D'Agostino's K^2 Test p-value: {p_normaltest}")

    jb_stat, jb_p = jarque_bera(returns)
    print(f"Jarque-Bera Test p-value: {jb_p}")

    # Augmented Dickey-Fuller Test for stationarity
    adf_stat, adf_p, _, _, _, _ = adfuller(returns)
    print(f"Augmented Dickey-Fuller Test p-value: {adf_p}")

# Apply tests to each stock
for ticker in stock_returns.columns:
    run_stat_tests(stock_returns[ticker], ticker)

# Apply tests to market returns
run_stat_tests(market_returns, market_index)

# Step 5: Interpret Results
def interpret_results(dw_stat, runs_test_p, vr_stat, shapiro_p, p_normaltest, jb_p, adf_p):
    print("\nInterpretation of results:")
    
    if dw_stat < 1.5:
        print("Low Durbin-Watson statistic suggests potential positive autocorrelation.")
    elif dw_stat > 2.5:
        print("High Durbin-Watson statistic suggests potential negative autocorrelation.")
    else:
        print("Durbin-Watson statistic indicates no significant autocorrelation.")

    if runs_test_p > 0.05:
        print("Runs Test p-value indicates no significant runs, supporting randomness.")
    else:
        print("Runs Test rejects the null hypothesis of randomness in runs.")

    if vr_stat > 0.05:
        print("Variance Ratio Test p-value supports randomness.")
    else:
        print("Variance Ratio Test suggests potential predictability in returns.")

    if shapiro_p > 0.05:
        print("Shapiro-Wilk Test p-value suggests normality.")
    else:
        print("Shapiro-Wilk Test rejects the null hypothesis of normality in returns.")
    
    if p_normaltest > 0.05:
        print("D'Agostino's K^2 Test p-value suggests normality.")
    else:
        print("D'Agostino's K^2 Test rejects the null hypothesis of normality in returns.")
    
    if jb_p > 0.05:
        print("Jarque-Bera Test p-value suggests normality.")
    else:
        print("Jarque-Bera Test rejects the null hypothesis of normality in returns.")

    if adf_p < 0.05:
        print("Augmented Dickey-Fuller Test p-value suggests stationarity.")
    else:
        print("Augmented Dickey-Fuller Test p-value suggests non-stationarity.")

# Example interpretation for a single stock (AAPL)
run_stat_tests(stock_returns['AAPL'], 'AAPL')
interpret_results(1.89, 0.12, 0.18, 0.34, 0.45, 0.29, 0.02)  # Example test statistics for AAPL
