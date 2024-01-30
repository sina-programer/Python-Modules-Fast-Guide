'''
download historical data for an individual stock.
available features: open, high, low, close, adj-close, volume
'''

import yfinance as yf

STOCK = 'AAPL'
df = yf.download(STOCK)
