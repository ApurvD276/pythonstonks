import matplotlib.pyplot as plt
import seaborn as sns  # statistical graphs
import yfinance as yf

form = input('Enter the Stock ID   ')
stock_info = yf.Ticker(form).info
print('You entered : ' + stock_info['longName'])

# Stock Info
market_cap = stock_info['marketCap']
market_price = stock_info['regularMarketPrice']
annual_dividend = stock_info['trailingAnnualDividendYield']


print('Market Capitalization ', 'USD', market_cap)
print('Market price ', 'USD', market_price)
print('Annual Dividend Yield', annual_dividend)


# Graph

def market_end_prices(symbol, period="1mo"):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period)
        return data["Close"]
    except Exception as e:
        print("Error , can't get data", e)

timeperiod = input('Enter the desired time span  ')

ticker = form
period = timeperiod = input('Enter the the span  ')
prices_data = market_end_prices(ticker, period)

sns.lineplot(data=prices_data)
sns.set_theme()
plt.xticks(rotation=30)
plt.title(f"Historical stock data of " + stock_info['longName'])
plt.show()



