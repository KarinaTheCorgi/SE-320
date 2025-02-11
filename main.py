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
        
        # getting the closing data
        hist_dict = response.json().get("data", {}).get("tradesTable", {}).get("rows", [])
        # reformatting the data
        close_dict = {
            entry["date"]: entry["close"].replace("$", "")
            for entry in hist_dict
        }
        return close_dict
    except Exception as e:
        print(e) 

print(get_data("AAPL"))