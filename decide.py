import yfinance as yf
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

def should_buy(stock_symbol, plotGraph = False):
    # Define the ticker symbol
    tickerSymbol = stock_symbol

    # Define the start and end dates for the data
    start_date = dt.datetime.now() - dt.timedelta(days=365)
    end_date = dt.datetime.now()

    # Get the data from Yahoo Finance
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

    # Compute the 9-day and 20-day EMAs
    ema1 = tickerDf['Close'].ewm(span=5, adjust=False).mean()
    ema2 = tickerDf['Close'].ewm(span=15, adjust=False).mean()

    # Plot the closing prices and EMAs on a graph
    if plotGraph:
        plot_graph(tickerDf, ema1, ema2)

    # Check if the 9-ema > 20-ema
    last_ema1 = ema1.tail(1).iloc[0]
    last_ema2 = ema2.tail(1).iloc[0]

    if last_ema1 > last_ema2:
        return (last_ema1, last_ema2, "BUY")
    else:
        return (last_ema1, last_ema2, "SELL")

def plot_graph(tickerDf, ema9, ema20):
    plt.plot(tickerDf.index, tickerDf['Close'], label='Closing Price')
    plt.plot(ema9.index, ema9, label='9-day EMA')
    plt.plot(ema20.index, ema20, label='20-day EMA')
    plt.legend(loc='upper left')
    plt.show()

stocks = {
    'RELIANCE.NS' : 'Reliance Industries',
    'INFY.NS' : 'Infosys',
    'PARAS.NS' : 'Paras defence and space technology Ltd',
    'LATENTVIEW.NS' : 'Latent View Analytics Limited',
    'TATAMOTORS.NS' : 'Tata Motors Limited',
    'IRCTC.NS' : 'Indian Railway Catering & Tourism Corporation Limited',
    'PERSISTENT.NS' : 'Persistent Systems Limited',
    'ADANIGREEN.NS' : 'Adani Green Energy Limited',
    'BHARTIARTL.NS' : 'Bharti Airtel Limited',
    'NAZARA.NS' : 'Nazara Technologies Limited',
    'TCS.NS' : 'Tata consultancy services',
    'TATACOFFEE.NS' : 'Tata Coffee Limited',
    'ADANIPORTS.NS' : 'Adani Ports and Special Economic Zone Limited',
    'ZOMATO.NS' : 'Zomato Limited',
    'ADANIPOWER.NS' : 'Adani Power Limited',
    'MTARTECH.NS' : 'MTAR Technologies Limited',
    'ADANITRANS.NS' : 'Adani Transmission Limited',
    'PAYTM.NS' : 'One97 Communications Limited',
    'GLENMARK.NS': 'Glenmark Pharmaceuticals Limited',
    'SBIN.NS' : 'State Bank of India',
    'IOC.NS' : 'Indian Oil Corporation Limited',
    'TITAN.NS' : 'Titan Company Limited',
    'HAL.NS' : 'Hindustan Aeronautics Limited',
    'RELAXO.NS' : 'Relaxo Footwears Limited',
    'ESCORTS.NS' : 'Escorts Kubota Limited',
    'DEEPAKNTR.NS' : 'DEEPAKNTR.NS',
    'JSWENERGY.NS' : 'JSW Energy Limited',
    'VBL.NS' : 'Varun Beverages Ltd',
    'JINDALSTEL.NS' : 'Jindal Steel & Power Limited',
    'ABBOTINDIA.NS' : 'ABBOTINDIA.NS',
    'TATAELXSI.NS' : 'Tata Elxsi Ltd',
    'HONAUT.NS' : 'Honeywell Automation India Limited',
    'MSFT' : 'Microsoft Corporation',
    'HDFCBANK.NS' : 'HDFC Bank Limited',
    'HINDUNILVR.NS' : 'Hindustan Unilever Limited',
    'ICICIBANK.NS' : 'ICICI Bank Limited',
    'HDFC.NS' : 'Housing Development Finance Corporation Limited',
    'ITC.NS' : 'ITC Limited',
    'BAJFINANCE.NS' : 'Bajaj Finance Limited',
    'HCLTECH.NS' : 'HCL Technologies Limited',
    'LT.NS' : 'Larsen & Toubro Limited',
    'SUNPHARMA.NS' : 'Sun Pharmaceutical Industries Limited',
    'BAJAJFINSV.NS' : 'Bajaj Finserv Ltd.',
    'ONGC.NS' : 'Oil and Natural Gas Corporation Limited',
    'JSWSTEEL.NS' : 'JSW Steel Limited',
    'MON100.NS' : 'Motilal Oswal NASDAQ 100 ETF'
}

print("========= Generating report for : {} ==========".format(dt.datetime.now()))
print()

decisionList = []
for symbol in stocks:
    ema1, ema2, decision = should_buy(symbol)
    decisionList.append((ema1, ema2, stocks[symbol], decision))

sortedList = sorted(decisionList, key=lambda x : (x[3], x[2]))

for item in sortedList:
    ema1, ema2, stock, decision = item
    print("{},{},{},{}".format(decision, stock, ema1, ema2))
