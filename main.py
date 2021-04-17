import datetime as dt

import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

# Define time Frame

start = dt.datetime(2020, 1, 1)
end = dt.datetime(2020, 12, 31)

# Load Data

data = web.DataReader('AMZN', 'yahoo', start, end)

print(data.columns)

# Restructure data

data = data[['Open', 'High', 'Low', 'Close']]

print(data)

data.reset_index(inplace=True)
data['Date'] = data['Date'].map(mdates.date2num)
print(data.head())

# Visualization

ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title('AMZN Share Price', color='white')
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', color='white')
ax.tick_params(axis='y', color='white')
ax.xaxis_date()

candlestick_ohlc(ax, data.values, width=0.5, colorup='#00ff00')
plt.show()


