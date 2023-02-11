# The Portfolio Object
import yfinance as yf
import pandas as pd

my_tickers = ["APPL", "GOOG", "MFST", "SPY"]
Portfolio(ticker_list=my_tickers)

class Portfolio:
    
    def __init__(self, ticker_list=None, period="max"):
        self.period=period
        self.ticker_list=ticker_list
        self.tickers = []
        for ticker in ticker_list:
            self.init_ticker(ticker)
        
    def init_ticker(ticker_symbol):
        Ticker = yf.Ticker(ticker_symbol)
        Ticker.history(period=self.period)
        #Logic based on ticker type
        
        self.tickers.append(Ticker)
    

