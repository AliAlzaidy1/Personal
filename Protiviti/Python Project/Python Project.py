import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

# setting the default render environment
pio.renderers.default = "browser"



# Define the ticker symbol and ticker name of the stock
ticker_symbol = "SPOT"
ticker_name = "Spotify"

# Define the time periods of the historic stock data we'll be reviewing
timeframes = {
    "1y": "Last Year",
    "5y": "Last 5 Years",
    "10y": "Last 10 Years"
}

# Function to get the historical stock data
def get_data(symbol, timeframe):
    return yf.Ticker(symbol).history(period=timeframe)

# Function to clean and normalise the historical stock data
def clean_and_normalise(data):
    data = data.dropna()  # Drop rows with missing data
    
    # Detect anomalies (Comparing the Z-score to see if it's outside of the norm)
    z_scores = (data - data.mean()) / data.std()
    anomalies = (z_scores.abs() > 3).any(axis=1)  # Define anomalies (Z-Score of over 3 in either direction)
    non_anomalies = anomalies == False  # Keep rows where anomalies is False (Not an anomaly)
    data = data[non_anomalies]

    # Normalise the numeric columns
    cols_to_normalise = ['Open', 'High', 'Low', 'Close', 'Volume']
    for i in cols_to_normalise:
        col_min = data[i].min()
        col_max = data[i].max()
        data[i] = (data[i] - col_min) / (col_max - col_min)
    
    return data

# Function to plot trading volume
def plot_trading_volume(data, name, timeframe):
    plt.figure(figsize=(12, 6))
    plt.bar(data.index, data['Volume'], color='skyblue', alpha=0.7)
    plt.title(f"{name} Trading Volume ({timeframe})")
    plt.xlabel("Date")
    plt.ylabel("Volume (Normalised)")
    plt.tight_layout()
    plt.show()

# Function to plot stock prices
def plot_stock_prices(data, name, timeframe, collumn):
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data[collumn], label=f"{collumn} Price", color='darkblue')
    plt.title(f"{name} {collumn} Prices ({timeframe})")
    plt.xlabel("Date")
    plt.ylabel("Price (Normalised)")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Using the defined functions to get the data as well as plot the graphs we want
for i, j in timeframes.items(): # Iterate through the different time frames
    data = get_data(ticker_symbol, i) # Uses the get_data function to fetch historical stock data
    data = clean_and_normalise(data) # Uses the clean_and_normalise to clean and normalise the data

    plot_trading_volume(data, ticker_name, j) # The trading Volume data is plotted

    for collumn in ['Open', 'High', 'Low', 'Close']: # Iterate through the different columns in the spotify dataframe to get only the 4 that we're looking for
        plot_stock_prices(data, ticker_name, j, collumn) # The stock price data is plotted
        
fig = px.line(data, x=data.index, y = 'Open')
fig.show()
