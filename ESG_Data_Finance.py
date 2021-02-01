import yfinance as yf
import pandas as pd
import os

# any stock ticker
tesla = "TSLA"
tesla_y = yf.Ticker(tesla)
esg_data = pd.DataFrame.transpose(tesla_y.sustainability)
esg_data['company_ticker'] = str(tesla_y.ticker)

# location to export the spreadsheet
os.chdir("/Users/ ")
esg_data.to_csv('tesla_sustainability_scores.csv', encoding='utf-8')
