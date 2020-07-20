import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web
from scipy import stats
import seaborn as sns

def getBeta(tickers,wts):
    tickers = ['BND', 'VB', 'VEA', 'VOO', 'VWO']
    wts = [0.1,0.2,0.25,0.25,0.2]
    # use API to get data
    price_data = web.get_data_yahoo(tickers,
                               start = '2013-01-01',
                               end = '2018-03-01')
    price_data = price_data['Adj Close']
    ret_data = price_data.pct_change()[1:]
    port_ret = (ret_data * wts).sum(axis = 1)
    benchmark_price = web.get_data_yahoo('SPY',
                               start = '2013-01-01',
                               end = '2018-03-01')
                               
    benchmark_ret = benchmark_price["Adj Close"].pct_change()[1:]



