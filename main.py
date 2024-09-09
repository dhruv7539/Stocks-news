import requests
from datetime import * 
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = 'AC78a91e03ef896e603763b4ede93c761c'
auth_token = '3998102bee6af72d82194a78d94bb511'

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

params_news={
    "q":COMPANY_NAME,
    "sortBy":"popularity",
    "apiKey":"42e8500fa41f41d386b0ea2651c7bceb"    
}

params_price={
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":"TSCO.LON",
    "apikey":"L0LNTHJXSKEF6JTA"
}

data=requests.get(STOCK_ENDPOINT,params=params_price)
dates=date.today()
yesterday=dates-timedelta(days=2)
day_before_yesterday=dates-timedelta(days=3)
price_yesterday=float(data.json()["Time Series (Daily)"][str(yesterday)]['4. close'])
price_before_yesterday=float(data.json()["Time Series (Daily)"][str(day_before_yesterday)]['4. close'])

price_difference=((price_before_yesterday-price_yesterday)/price_before_yesterday)*100
if price_difference>=0 or price_difference<=0:
    print("Get news")
    news_data=requests.get(NEWS_ENDPOINT,params=params_news)
    article_5=news_data.json()["articles"][:5]
    for article in article_5:
        title=article["title"]
        description=article['description']
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=f"Headlines:{title} \n Brief: {description}",from_='+12184191996',to="+919773118633")
        print(message.status)
    



## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

