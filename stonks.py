import matplotlib.pyplot as plt
import seaborn as sns  # statistical graphs
import yfinance as yf

form = input('Enter the Stock ID   ')
stock_info = yf.Ticker(form).info
print('You entered : ' + stock_info['longName'])

# Stock Info
market_cap = stock_info['marketCap']
market_price = stock_info['regularMarketPrice']
dividend_rate = stock_info['dividendRate']


print('Market Capitalization ', 'USD', market_cap)
print('Market price ', 'USD', market_price)
print('Dividend Yield Rate', dividend_rate)


# Graph
validtimeperiods = '1h, 1d, 5d, 1wk, 1mo, 3mo, 5mo, ytd, 1y, 3y, 5y, 10y, max'


input_timeperiod = input('Enter the desired time span . The valid time periods are : ' + validtimeperiods)


def market_end_prices(symbol, period=input_timeperiod):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period)
        return data["Close"]
    except Exception as e:
        print("Error", e)


ticker = form
period = input_timeperiod
prices_data = market_end_prices(ticker, period)

sns.lineplot(data=prices_data)
sns.set_theme()
plt.xticks(rotation=30)
plt.title(f"Historical stock data of " + stock_info['longName'] + 'of time period ' + input_timeperiod)
plt.show()
