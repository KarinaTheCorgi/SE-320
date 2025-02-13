"""
FileName: stocks.py
Author: Karina Solis
Date: 2/10/2025
Resources:
    - Wolf Paulus: Python Syntax, api url to use, stock explanation (ln[34-38])
    - requests module: HTTP requests (Ln[16])
    - stack overflow: User-Agent Header (i wasn't getting any data after just using the url, 
                                         but once i saw the user-agent header (not the question 
                                         being asked in this post), it worked. Ln[40])
        - https://stackoverflow.com/questions/70629619/cannot-get-data-from-nasdaq-site
    - sys module: Command line arguments  (Ln[121])
        - https://docs.python.org/3/library/sys.html
"""
# Non-Python Modules
from requests import get
# Python Modules
from datetime import date
import sys 
import json

def get_data(ticker:str)->dict:
    """
    gets stock data from nasdaq api using http request and returns a dictionary
    
    Args:
        ticker (str): The stock ticker (signifies what kind of stock)
        
    Yields:
        close_dict (dict): The dictionary with the price data of a certain stock over 5 years
    
    """
    try:
        ticker = ticker.upper()
        today = date.today()
        start = str(today.replace(year=today.year - 5))
        base_url = "https://api.nasdaq.com"
        path = f"/api/quote/{ticker}/historical?assetclass=stocks&fromdate={start}&limit=9999"
        
        headers = {"User-Agent": "Mozilla/5.0"}
        
        response = get(base_url+path, headers = headers)
        
        if response.status_code != 200:
            print(f"Couldn't get data for: {ticker}. Status Code: {response.status_code}")
            return {}
        
        try:
            # getting the closing data (formatting seen just by using browser to view data)
            hist_dict = response.json().get("data", {}).get("tradesTable", {}).get("rows", [])
        except Exception as e:
            print(f"Couldn't parse data for: {ticker}. Error: {e}")
            return {}
        
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
        print(f"Couldn't get data for: {ticker}. Error: {e}") 

def process_data(data:dict)->dict:
    """
    processes data from get_data dictionary to create new dictionary with min/max/mean/median data
    
    Args:
        data (dict): dictionary with price info from a certain ticker
        
    Yields:
        processed_data (dict): The dictionary with the price data of a certain stock over 5 years
    
    """
    try: 
        if "prices" not in data or not data["prices"]:
            print(f"No prices data for {data["ticker"]}")
            return {}
        
        prices = [float(price) for price in data["prices"].values()]
        length = len(prices)
        
        if length == 0:
            print(f"No prices data for {data["ticker"]}")
        
        prices.sort()
        min = prices[0]
        max = prices[-1]
        mean = sum(prices)/length
        
        if length % 2:
            median = prices[int(length / 2)]
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
    except Exception as e:
        print(f"Couldn't process data. Error: {e}")
        return {}

def main()->None:
    """
    handles user input and creates a .json file with the ouput from the given input
    
    args: 
        none
        
    yields:
        none
    """
    tickers = sys.argv[1:]
    dict_results = {}
    
    if not tickers:
        print("No tickers. Use: python stocks.py ticker1 ticker2 ...")
    
    for ticker in tickers:
        processed_data = process_data(get_data(ticker))
        dict_results[ticker] = processed_data
        
    with open("stocks.json", "w") as json_file:
        json.dump(dict_results, json_file)
 
#for command line        
if __name__ == "__main__":
    main()
        
