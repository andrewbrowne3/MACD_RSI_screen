# The Portfolio Object
import yfinance as yf
import pandas as pd
import requests
from dotenv import load_dotenv
import os


load_dotenv()


my_tickers = ["APPL", "GOOG", "MFST", "SPY"]

class Portfolio:
    
    def __init__(self, ticker_list=None, period="max"):
        self.api_key = os.environ.get("FINANCE_API_KEY")
        self.period=period
        self.ticker_list=ticker_list
        self.tickers = {}
        for ticker in ticker_list:
            self.init_ticker(ticker)
        
    def init_ticker(self, ticker_symbol):
        try:
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker_symbol}&interval=5min&apikey={self.api_key}'
            r = requests.get(url)
            data = r.json()
            if data.get("Time Series (5min)"):
                flat_data = []
                for timestamp, price_data in data.get("Time Series (5min)").items():
                    new_data = {
                        "date" : timestamp,
                        "open" : price_data.get("1. open"),
                        "high" : price_data.get("2. high"),
                        "low" : price_data.get("3. low"),
                        "close" : price_data.get("4. low"),
                        "volume" : price_data.get("5. volume")
                    }
                    flat_data.append(new_data)
                self.tickers[ticker_symbol] = pd.DataFrame(flat_data)
        except Exception as e:
            print(e)
                

