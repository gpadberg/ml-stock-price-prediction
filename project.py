import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime as dt


stock_data = pd.read_csv('./NFLX.csv', index_col = 'Date')
stock_data.head()

plt.figure(figsize = (15, 10))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval = 60))
x_dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in stock_data.index.values]

plt.ion()
plt.plot(x_dates, stock_data['High'], label = 'High')
plt.plot(x_dates, stock_data['Low'], label = 'Low')
plt.xlabel('Time Scale')
plt.ylabel('Scaled USD')
plt.legend()
plt.gcf().autofmt_xdate()
plt.show()

# Save the plot to a file
plt.savefig('stock_plot.png')
print("Plot saved as 'stock_plot.png'. Open this file to view the plot.")