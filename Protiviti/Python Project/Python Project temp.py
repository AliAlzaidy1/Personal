# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""









## Find below my second approach



# import seaborn as sns
# import matplotlib.pyplot as plt
# import yfinance as yf
# import pandas as pd
# import plotly.graph_objects as go

# # Define the ticket symbol
# ticker_symbol = "SPOT"

# # Create a Ticker object
# ticker = yf.Ticker(ticker_symbol)

# # Fetch historical market data
# spot_data1y = ticker.history(period="1y") # data for the last year
# spot_data5y = ticker.history(period="5y")  # data for the last 5 years
# spot_data10y = ticker.history(period="10y")  # data for the last 10 years


# # Function to plot trading volume
# def plot_volume(data, period):
#     plt.figure(figsize=(14, 7))
#     plt.bar(data.index, data['Volume'], color='blue', alpha=0.6, label=f"Trading Volume ({period})")
#     plt.title(f"Spotify (SPOT) Trading Volume Over the Last {period}", fontsize=16)
#     plt.xlabel("Date", fontsize=12)
#     plt.ylabel("Volume", fontsize=12)
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# # Function to calculate and display trading volume summary
# def volume_summary(data, period):
#     total_volume = data['Volume'].sum()
#     average_volume = data['Volume'].mean()
#     print(f"\n--- Trading Volume Summary for the Last {period} ---")
#     print(f"Total Trading Volume: {total_volume}")
#     print(f"Average Daily Trading Volume: {average_volume:.2f}")
#     high_volume_threshold = data['Volume'].quantile(0.95)  # Top 5% of volumes
#     high_volume_days = data[data['Volume'] > high_volume_threshold]
#     print(f"High Volume Days (Top 5%):")
#     print(high_volume_days[['Volume']])

# # Function to plot Open, High, Low, Close prices
# def plot_prices(data, period, price_type):
#     price_types = {
#         'Open': 'Opening Price',
#         'High': 'High Price',
#         'Low': 'Low Price',
#         'Close': 'Closing Price'
#     }
    
#     if price_type not in price_types:
#         print(f"Invalid price type: {price_type}. Choose from {list(price_types.keys())}.")
#         return

#     plt.figure(figsize=(14, 7))
#     plt.plot(data.index, data[price_type], label=f"{price_types[price_type]}", linewidth=2)
#     plt.title(f"Spotify (SPOT) {price_types[price_type]} Over the Last {period}", fontsize=16)
#     plt.xlabel("Date", fontsize=12)
#     plt.ylabel(f"{price_types[price_type]} (USD)", fontsize=12)
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# # Process data for 1 year
# print("\n--- 1 Year Data ---")
# plot_volume(spot_data1y, "Year")
# volume_summary(spot_data1y, "Year")
# plot_prices(spot_data1y, "Year", "Open")
# plot_prices(spot_data1y, "Year", "High")
# plot_prices(spot_data1y, "Year", "Low")
# plot_prices(spot_data1y, "Year", "Close")

# # Process data for 5 years
# print("\n--- 5 Year Data ---")
# plot_volume(spot_data5y, "5 Years")
# volume_summary(spot_data5y, "5 Years")
# plot_prices(spot_data5y, "5 Years", "Open")
# plot_prices(spot_data5y, "5 Years", "High")
# plot_prices(spot_data5y, "5 Years", "Low")
# plot_prices(spot_data5y, "5 Years", "Close")

# # Process data for 10 years
# print("\n--- 10 Year Data ---")
# plot_volume(spot_data10y, "10 Years")
# volume_summary(spot_data10y, "10 Years")
# plot_prices(spot_data10y, "10 Years", "Open")
# plot_prices(spot_data10y, "10 Years", "High")
# plot_prices(spot_data10y, "10 Years", "Low")
# plot_prices(spot_data10y, "10 Years", "Close")








## Find below my first approach

# import seaborn as sns
# import matplotlib.pyplot as plt
# import yfinance as yf

# # Define the ticket symbol
# ticker_symbol = "SPOT"

# # Create a Ticker object
# ticker = yf.Ticker(ticker_symbol)

# # Fetch historical market data
# spot_data1y = ticker.history(period="1y")
# spot_data5y = ticker.history(period="5y")  # data for the last 5 years
# spot_data10y = ticker.history(period="10y")  # data for the last 10 years
# print("Historical Data:")
# print(spot_data5y)



# # Plot the opening price over time (1 year)
# plt.figure(figsize=(14, 7))  # Set figure size
# plt.plot(spot_data1y.index, spot_data1y['Open'], label="Opening Price", linewidth=2)
# plt.title(f"Spotify (SPOT) Opening Prices Over the Last Year", fontsize=16)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("Opening Price (USD)", fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.show()

# # Plot the high price over time (1 year)
# plt.figure(figsize=(14, 7))  # Set figure size
# plt.plot(spot_data1y.index, spot_data1y['High'], label="High Price", linewidth=2)
# plt.title(f"Spotify (SPOT) High Price Over the Last Year", fontsize=16)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("High Price (USD)", fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.show()

# # Plot the low price over time (1 year)
# plt.figure(figsize=(14, 7))  # Set figure size
# plt.plot(spot_data1y.index, spot_data1y['Low'], label="Low Price", linewidth=2)
# plt.title(f"Spotify (SPOT) Low Price Over the Last Year", fontsize=16)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("Low Price (USD)", fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.show()

# # Plot the closing price over time (1 year)
# plt.figure(figsize=(14, 7))  # Set figure size
# plt.plot(spot_data1y.index, spot_data1y['Close'], label="Closing Price", linewidth=2)
# plt.title(f"Spotify (SPOT) Closing Prices Over the Last Year", fontsize=16)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("Closing Price (USD)", fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.show()


# # Plot the opening price over time (5 year)
# plt.figure(figsize=(14, 7))  # Set figure size
# plt.plot(spot_data5y.index, spot_data5y['Open'], label="Opening Price", linewidth=2)
# plt.title(f"Spotify (SPOT) Opening Prices Over the Last 5 Years", fontsize=16)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("Opening Price (USD)", fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.show()


# # Plot the high price over time (5 year)
# plt.figure(figsize=(14, 7))  # Set figure size
# plt.plot(spot_data5y.index, spot_data5y['High'], label="High Price", linewidth=2)
# plt.title(f"Spotify (SPOT) High Price Over the Last 5 Years", fontsize=16)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("High Price (USD)", fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.show()

# # Plot the low price over time (5 year)
# plt.figure(figsize=(14, 7))  # Set figure size
# plt.plot(spot_data5y.index, spot_data5y['Low'], label="Low Price", linewidth=2)
# plt.title(f"Spotify (SPOT) Low Price Over the Last 5 Years", fontsize=16)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("Low Price (USD)", fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.show()


# # Plot the closing price over time (5 year)
# plt.figure(figsize=(14, 7))  # Set figure size
# plt.plot(spot_data5y.index, spot_data5y['Close'], label="Closing Price", linewidth=2)
# plt.title(f"Spotify (SPOT) Closing Prices Over the Last 5 Years", fontsize=16)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("Closing Price (USD)", fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.show()

# # Plot the opening price over time (10 Year)
# plt.figure(figsize=(14, 7))  # Set figure size
# plt.plot(spot_data10y.index, spot_data10y['Open'], label="Opening Price", linewidth=2)
# plt.title(f"Spotify (SPOT) Opening Prices Over the Last 10 Years", fontsize=16)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("Opening Price (USD)", fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.show()

# # Plot the high price over time (10 year)
# plt.figure(figsize=(14, 7))  # Set figure size
# plt.plot(spot_data10y.index, spot_data10y['High'], label="High Price", linewidth=2)
# plt.title(f"Spotify (SPOT) High Price Over the Last 10 Years", fontsize=16)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("High Price (USD)", fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.show()

# # Plot the low price over time (10 year)
# plt.figure(figsize=(14, 7))  # Set figure size
# plt.plot(spot_data10y.index, spot_data10y['Low'], label="Low Price", linewidth=2)
# plt.title(f"Spotify (SPOT) Low Price Over the Last 10 Years", fontsize=16)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("Low Price (USD)", fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.show()


# # Plot the closing price over time (10 year)
# plt.figure(figsize=(14, 7))  # Set figure size
# plt.plot(spot_data10y.index, spot_data10y['Close'], label="Closing Price", linewidth=2)
# plt.title(f"Spotify (SPOT) Closing Prices Over the Last 10 Years", fontsize=16)
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("Closing Price (USD)", fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.show()



