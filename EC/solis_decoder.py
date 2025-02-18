"""
FileName:  solis_decoder.py
Author: Karina Solis
Date: 2/17/2025

Resources:
    - Wolf Paulus -- General Python Syntax
    - Sorted Function for Custom Objects:
        - https://software.land/python-custom-sorting
    - Parsing Google Doc Data:
        - https://stackoverflow.com/questions/78832288/how-can-i-parse-the-data-from-a-table-on-a-google-docs-using-python
    - Requests Module:
        - https://www.w3schools.com/python/module_requests.asp
    - BeautifulSoup:
        - https://pypi.org/project/beautifulsoup4/
        - https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup
        - https://pytutorial.com/understand-how-to-work-with-table-in-beautifulsoup/
    - Reverse List:
        - https://www.w3schools.com/python/ref_func_reversed.asp
"""

# External Libraries
from requests import get
from bs4 import BeautifulSoup

"""
pip install requests
pip install bs4
"""


class Point:
    """
    the Point class
    """
    def __init__(self, x:int=0, y:int=0, character:str='') -> None:
        """
        creates a Point given an x, y, and character
        """
        self.x = x
        self.y = y
        self.char = character
        
    def __lt__(self, b) -> bool:
        """
        used for the sorted function, compares y values of 2 points then the x values
        returns true if:
            the 1st y value is less than the 2nd
            if both y values are equal, the 1st x value is less than the 2nd
        """
        if self.y == b.y:
            return self.x < b.x
        return self.y < b.y
        
    def __repr__(self) -> str:
        """
        turns the Point object into a string (just the character), was used for testing sorting
        """
        return f"{self.char}"


class Grid:
    """
    the Grid Class, holds a 2D list of points
    """
    def __init__(self, url:str):
        """
        creates a grid given a url (to google doc)
        """
        self.points = []
        titles = BeautifulSoup(get(url).text, 'html.parser').find_all('table')
        rows = BeautifulSoup(str(titles), 'html.parser').find_all('tr')[1:]  # skips title row
        
        for row in rows:
            columns = row.find_all('td')
            
            x = int(columns[0].get_text(strip=True))
            character = columns[1].get_text(strip=True)
            y = int(columns[2].get_text(strip=True))
            
            self.points.append(Point(x, y, character))
        
    def sep_lists(self) -> list[list[Point]]:
        """
        sorts grid's points by y value then x value
        seperates each y value into its own list of points
        then makes sure that each row has the same number of points
        adding ' ' when no existing point in the grid
        """
        pts = sorted(self.points)
        sep_list = []
        row = []
        curr_y = None
        
        for pt in pts:
            if pt.y != curr_y:
                if row:
                    sep_list.append(row)
                row = [pt]
                curr_y = pt.y
            else:
                row.append(pt)

        sep_list.append(row)
        
        max_x = max(pt.x for pt in pts)

        for row in sep_list:
            existing_x = {pt.x for pt in row}

            for x in range(max_x):
                if x not in existing_x:
                    row.append(Point(x, row[0].y, ' ')) 

            row.sort()

        return sep_list
        
    def __repr__(self):
        """
        prints the structured grid, printing the higher y values first
        """
        sep_list = self.sep_lists()
        result = ""

        for row in reversed(sep_list):
            row_str = ""
            for point in row:
                row_str = row_str + (f"{point}")
            result = result + row_str + '\n'
            
        return result 


def decode(url:str)->None:
    """
    decodes the google doc url by calling the Grid class
    
    args:
        - url (str): the link to the google doc
    
    returns:
        - none, but prints the decoded message to the terminal
    """
    print(Grid(url))


# Google Doc Tests
url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
decode(url)

url2 = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
decode(url2)