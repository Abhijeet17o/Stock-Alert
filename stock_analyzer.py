import requests

STOCK = "NAME OF STOCK"
API_KEY = "YOUR API KEY FOR THE ENDPOINT"
ENDPOINT = "https://www.alphavantage.co/query"

STOCK_PARAMETERS = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":API_KEY,
}

NEWS_PARAMETERS = {
    "function":"NEWS_SENTIMENT",
    "tickers":STOCK,
    "limit":3,
    "apikey":API_KEY,
    "sort": "Relevance"
}

#===============FUNCTIONALITY=================#
def main():
    output_res = output(STOCK)
    with open("final.txt", mode="w", encoding="utf-8") as file:
        file.write(output_res)
    
def output(stock:str):
    res = str()
    percent_change = get_stock()
    news_list = get_news()
    
    up = "🔺"
    down = "🔻"
    
    if percent_change < 0:
        indication = down
    else:
        indication = up
        
    res += f"{stock}: {indication}{percent_change}%"
    for i, news in enumerate(news_list):
        res += f"\n\nHEADLINE {i+1}: {news[0]}\n"
        res += f"BRIEF: {news[1]}"
        
    return res

def get_stock() -> int:
    RESPONSE = requests.get(url=ENDPOINT, params=STOCK_PARAMETERS)
    STOCK_DATA = RESPONSE.json()

    PREVIOUS_DATE = (list(STOCK_DATA["Time Series (Daily)"].keys()))[0]

    OPEN = float(STOCK_DATA["Time Series (Daily)"][PREVIOUS_DATE]["1. open"])
    CLOSE = float(STOCK_DATA["Time Series (Daily)"][PREVIOUS_DATE]["4. close"])
    diff_percent =round(((OPEN-CLOSE)/OPEN*100)*-1, 3)
    
    return diff_percent

def get_news() -> list:
    news_list = list()
    NEWS_RESPONSE = requests.get(url=ENDPOINT, params=NEWS_PARAMETERS)
    NEWS_DATA = NEWS_RESPONSE.json()["feed"]
    for i in range(3):
        news_title = NEWS_DATA[i]["title"]
        news_summary = NEWS_DATA[i]["summary"]
        news_list.append((news_title, news_summary))
    return news_list


#================RUN=================#
if __name__=="__main__":
    main()
