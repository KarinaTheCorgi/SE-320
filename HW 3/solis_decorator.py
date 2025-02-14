"""
FileName:  solis_decorator.py
Author: Karina Solis
Date: 2/13/2025
Resources:
    - Wolf Paulus: Python Syntax - decorators
    - random module (Ln[15]):
        - https://www.w3schools.com/python/module_random.asp
    - time module (Ln[16]): 
        - https://www.geeksforgeeks.org/python-time-module/
    - getting function name (Ln[])
        - https://www.geeksforgeeks.org/python-how-to-get-function-name/
"""

from random import randint
from time import sleep, asctime

def backoff(initial_delay: float, back_off_factor: float, max_delay: float) -> callable:
    """
    adds customization to the backoff parameters
    
    args: 
        - initial_delay (float) -- delay after the first call that isn't true
        - back_off_factor (float) -- how much exponentially the delay should grow
        - max_delay (float) -- the maximum amount of delay 
    returns: 
        - backoff (callable) -- executes the initial/base decorator (no customization)
    """
    def backoff(func: callable) -> callable:
        """
        (initial) backoff decorator to add exponential backoff
        
        args: 
            - func (callable) -- function/callable to be decorated
        
        returns:
            - inner (callable) -- executes the inner funcion
        """
        delay = 0
    
        def inner(*args, **kwargs):
            """
            imposes the specified delay
            
            args:
                - *args -- non-keyworded list of unspecified arguments
                - **kwargs -- keyworded list of unspecified arguments
            
            returns:
                - result -- the return from calling func (in this case bool)
            """
            nonlocal delay, initial_delay, back_off_factor
            result = func(*args, **kwargs)
            
            # capping the delay
            if delay >= max_delay:
                delay = max_delay
                
            #Output: {Date/time} will be calling {func} after {delay} sec delay
            print(f"{asctime()}: will be calling {func.__name__} after {delay} sec delay")
            
            # sleep for the delay duration
            sleep(delay)
            
            # if func is true, delay resets, otherwise the delay increments exponentially
            if result:
                delay = 0
            else:
                if delay == 0:
                    delay += initial_delay
                else:
                    delay *= back_off_factor
            
            return result
        return inner
    return backoff

# using custom backoff decorator with added parameterizing implementation
@backoff(initial_delay=0.1, back_off_factor=1.5, max_delay=2.5)
def call_shaky_service() -> bool:
    """
    simulates a 1/6 chance of the call going through
    
    args: N/A
    
    returns:
        - true if a random int between 1 and 6 is 6, false otherwise
    """
    return 6 == randint(1, 6)

# testing the function (ctrl + c in terminal - to stop loop)
while True:
    print(call_shaky_service())
