import os, sys, argparse
import pandas as pd 
import backtrader as bt
from crossoverstrategy import GCrossover

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)

spy_prices = pd.read_csv('EURUSD.csv', index_col = 'Date', parse_dates = True)

feed = bt.feeds.PandasData(dataname = spy_prices)
cerebro.adddata(feed)

cerebro.addstrategy(GCrossover)

cerebro.run()
cerebro.plot()