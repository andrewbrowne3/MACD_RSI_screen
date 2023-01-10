import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# List of stocks to analyze
stocks = ["BIIB", "AMRN",'GME']

# Create a dictionary to store the distances
distances = {}

# Loop through the list of stocks
for stock in stocks:
    # Retrieve the stock data
    df = pdr.get_data_yahoo(stock, start="2020-01-01", end="2022-12-31")

    # Compute the MACD and RSI indicators
    df["macd"] = df.Close.ewm(12).mean() - df.Close.ewm(26).mean()
    df["rsi"] = (df.Close - df.Close.shift(1)).ewm(12).mean() / df.Close.ewm(12).std()

    # Check for a bullish crossover and RSI > 30
    if (df.macd > 0).any() and (df.macd.shift(1) < 0).any() and (df.rsi > 20).any():
        # Store the distance between the current stock price and the 200-day moving average
        distance = df.Close - df.Close.rolling(200).mean()
        distances[stock] = distance[-1]
        print(f"Bullish crossover and RSI > 30 detected in {stock}!")
    
    # Check for a bearish crossover
    if (df.macd < 0).any() and (df.macd.shift(1) > 0).any():
        distance = df.Close - df.Close.rolling(200).mean()
        distances[stock] = distance[-1]
        print(f"Bearish crossover in {stock}!")

# Print the list of distances sorted from greatest to least
for stock, distance in sorted(distances.items(), key=lambda item: item[1], reverse=True):
    print(f"{stock}: {distance}")

        
    


# Print the dataframe

#This code will retrieve the daily closing price data for Apple Inc. (AAPL) from January 1, 2020 to December 31, 2020 
#and compute the MACD indicator. It will then check if a bullish crossover (when the MACD crosses above zero) or a bearish crossover 
#(when the MACD crosses below zero) occurred during the period. If either of these events is detected, a message will be printed.
