# import pandas as pd
# import matplotlib.dates as mdates
# import matplotlib.pyplot as plt
# import datetime as dt


# stock_data = pd.read_csv('./NFLX.csv', index_col = 'Date')
# stock_data.head()

# plt.figure(figsize = (15, 10))
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval = 60))
# x_dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in stock_data.index.values]

# plt.ion()
# plt.plot(x_dates, stock_data['High'], label = 'High')
# plt.plot(x_dates, stock_data['Low'], label = 'Low')
# plt.xlabel('Time Scale')
# plt.ylabel('Scaled USD')
# plt.legend()
# plt.gcf().autofmt_xdate()
# plt.show()


import pandas as pd
from matplotlib.dates import DateFormatter, DayLocator
import matplotlib.pyplot as plt
import datetime as dt

# Load the stock data
stock_data = pd.read_csv('./NFLX.csv', index_col='Date')

# Display the first few rows of the dataframe to ensure it's loaded correctly
print(stock_data.head())

# Create a figure and axis
plt.figure(figsize=(15, 10))

# Configure the x-axis with date format and locator
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(DayLocator(interval=60))

# Convert string dates to datetime objects
x_dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in stock_data.index.values]

# Plot the high and low stock prices
plt.plot(x_dates, stock_data['High'], label='High')
plt.plot(x_dates, stock_data['Low'], label='Low')

# Label the axes and add a legend
plt.xlabel('Time Scale')
plt.ylabel('Scaled USD')
plt.legend()

# Rotate and format the x-axis dates
plt.gcf().autofmt_xdate()

# Display the plot
plt.show()
