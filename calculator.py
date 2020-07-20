import definitions,requests,sys,statistics,math
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
    if type(data) == type("String"):
        print("You didn't have a valid stock")
        sys.exit()
    firstClose = data[0]["close"]
    lastClose = data[len(data)-1]["close"]
    return ((lastClose-firstClose) / firstClose) * 100

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

def getStockVolatility(ticker,startdate,enddate):
    api = "https://api.tiingo.com/tiingo/daily/{}/prices?token={}&startDate={}&endDate={}".format(ticker,key,startdate,enddate)
    data = requests.get(api).json()
    if type(data) == type("String"):
        print("You didn't input a valid stock")
        sys.exit()
    close_dates = []
    for i in data:
        close_dates.append(i["close"])
    pctDelta = []
    for i in range(0,len(close_dates)-1):
        pctDelta.append(((close_dates[i+1] - close_dates[i]) / close_dates[i])*100)
    stdDev = statistics.stdev(pctDelta) * math.sqrt(len(close_dates))
    print (f"The volatility of the stock during the given period was %{stdDev}")
    return

def compare_stocksUser():
    stock1 = input("What is one stock you wanna compare:\n").upper()
    stock2 = input("And another?:\n").upper()
    date1 = input("What is the beginning date you want to consider(format:mm-dd-yyyy):")
    date2 = input("What is the ending date you want to consider(format:mm-dd-yyyy):")
    print(compare_stocks(stock1,stock2,date1,date2))
    return

#MVP
# print(compare_stocks("AAPL","AMD","01-02-2019","01-02-2020"))
# print(percent_profit("AMD","01-02-2019","01-02-2020"))
# compare_stocksUser()
print(getStockVolatility("AMD","07-13-2020","07-15-2020"))