import yfinance as yf
stock_info = yf.Ticker('INTU').info
market_cap = stock_info['marketCap']
market_price = stock_info['regularMarketPrice']
Gross_Profits = stock_info['grossProfits']
DE = stock_info['debtToEquity']
Cash_Flow = stock_info['freeCashflow']
shares_Outstanding = stock_info['sharesOutstanding']


print('Market Capitalization ', market_cap)
print('market price ', market_price)
print(' Gross Profits ', Gross_Profits)
print(' Debt/Equity Ratio ', DE)
print('Free Cash Flow', Cash_Flow)
print('Outstanding Shares', Cash_Flow)


'''
 region
 language
 quoteType
 quoteSourceName
 epsForward
 currency
 sharesOutstanding
 bidSize
 trailingPE
 priceToBook
 dividendDate
 regularMarketChangePercent
 market
 fiftyDayAverageChange
 forwardPE
 regularMarketPrice
 regularMarketTime
 regularMarketChange
 regularMarketOpen
 regularMarketDayHigh
 regularMarketDayLow
 regularMarketVolume
 bookValue
 ask
 regularMarketPreviousClose
 preMarketChangePercent
 regularMarketDayRange
 twoHundredDayAverageChange
 bid
 fiftyTwoWeekLowChange
 askSize
 financialCurrency
 twoHundredDayAverage
 gmtOffSetMilliseconds
 shortName
 longName
 preMarketChange
 twoHundredDayAverageChangePercent
 trailingAnnualDividendYield
 exchangeDataDelayedBy
 fiftyTwoWeekLow
 fiftyTwoWeekHigh
 averageDailyVolume3Month
 fiftyDayAverage
 exchangeTimezoneShortName
 esgPopulated
 marketState
  marketCap
 epsTrailingTwelveMonths
 fullExchangeName
 earningsTimestampStart
 earningsTimestampEnd
 trailingAnnualDividendRate
 earningsTimestamp
 fiftyTwoWeekLowChangePercent
 fiftyTwoWeekHighChangePercent
 averageDailyVolume10Day
 exchange
 priceHint
 exchangeTimezoneName
 preMarketTime
 fiftyDayAverageChangePercent
 fiftyTwoWeekRange
 tradeable
 fiftyTwoWeekHighChange
 preMarketPrice
 sourceInterval
 messageBoardId
 price
'''
