import yfinance as yf
import pandas as pd
import os
tesla = "TSLA"
tesla_y = yf.Ticker(tesla)
esg_data = pd.DataFrame.transpose(tesla_y.sustainability)
esg_data['company_ticker'] = str(tesla_y.ticker)
os.chdir("/Users/ronaldkim/Downloads")
esg_data.to_csv('tesla_sustainability_scores.csv', encoding='utf-8')
