"""
FileName: stocks.py
Author: Karina Solis
Date: 2/10/2025
Resources:
    - Wolf Paulus: Python Syntax
    - requests module: (Ln[])
    - stack overflow: User-Agent Header (i wasn't getting any data after just using the url, 
                                         but once i saw the user-agent header (not the question 
                                         being asked in this post), it worked. Ln[25])
        - https://stackoverflow.com/questions/70629619/cannot-get-data-from-nasdaq-site
"""

from requests import get
from datetime import date

def get_data(ticker:str)->dict:
    try:
        ticker = ticker.upper()
        today = date.today()
        start = str(today.replace(year=today.year - 5))
        base_url = "https://api.nasdaq.com"
        path = f"/api/quote/{ticker}/historical?assetclass=stocks&fromdate={start}&limit=9999"
        
        headers = {"User-Agent": "Mozilla/5.0"}
        
        response = get(base_url+path, headers = headers)
        
        # getting the closing data (formatting seen just by using browser to view data)
        hist_dict = response.json().get("data", {}).get("tradesTable", {}).get("rows", [])
        # reformatting the data
        close_dict = {
            "ticker": ticker,
            "prices": {
                entry["date"]: entry["close"].replace("$", "") # getting rid of $ for float conversion
                for entry in hist_dict
            }
        }
        return close_dict
    except Exception as e:
        print(e) 

def process_data(data:dict)->dict:
    prices = [float(price) for price in data["prices"].values()]
    prices.sort()
    min = prices[0]
    max = prices[-1]
    length = len(prices)
    mean = sum(prices)/length
    
    if length % 2:
        median = prices[length / 2]
    else:
        median = prices[int(length / 2)] + prices[int((length / 2) - 1)] /2
    
    processed_data = {
        "ticker": data["ticker"],
        "min": min,
        "max": max,
        "avg": mean,
        "median": median
    }
    
    return processed_data

print(process_data(get_data("AAPL")))