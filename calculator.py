import definitions
# The line above will let you separate your concerns by defining functions your calculator might use in a separate file.
key = "66aa1fbcd15f0d1adf3e21ae25382d198deaeea3"
print("Welcome to the Stock Boss Calculator\n\nYou can check out a stock's performance, examine the Beta value of a stock versus SPY, or examine the volatility of a particular stock")

def net_profit(ticker,startdate,enddate,investment):
    api = "https://api.tiingo.com/tiingo/daily/{}/prices?token={}&startDate={}&endDate={}".format(ticker,key,startdate,enddate)
    data = requests.get(api).json()
    start = investment / float(data[0]['close'])
    end = start * float(data[len(data) - 1]['close'])
    return end - start

def percent_profit(ticker,startdate,enddate):
    api = "https://api.tiingo.com/tiingo/daily/{}/prices?token={}&startDate={}&endDate={}".format(ticker,key,startdate,enddate)
    data = requests.get(api).json()
    firstClose = data[0]["close"]
    lastClose = data[len(data)-1]["close"]
    return (lastClose-firstClose) / firstClose

def compare_stocks(ticker1,ticker2,startdate,enddate):
    investment1 = net_profit(ticker1,startdate,enddate,100.00)
    investment2 = net_profit(ticker2,startdate,enddate,100.00)
    if investment1 > investment2:
        percent = percent_profit(ticker1,startdate,enddate)
        return ("{} was the better choice to invest in between {} and {} as it changed by {}%").format(ticker1,startdate,enddate,percent)
    elif investment1 < investment2: 
        percent = percent_profit(ticker2,startdate,enddate)
        return ("{} was the better choice to invest in between {} and {} as it changed by {}%").format(ticker2,startdate,enddate,percent)
    else:
        return ("Both stocks performed equally over the given period of time")
    