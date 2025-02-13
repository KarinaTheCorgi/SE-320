"""
FileName: infinite_generators.py
Author: Karina Solis
Date: 1/15/2025
Resources:
    - Wolf Paulus: Python Syntax (ex. I didn't know that you could declare variables simultaneously [ln 33])
    - PEP 484: Python Style Guide (ex. Type Hints)
        https://peps.python.org/pep-0484/
    - typing module: Generator Class (ex. Type Hints - Generator [ln 15])
        https://docs.python.org/3/library/typing.html#annotating-generators-and-coroutines
"""
from typing import Generator
from time import time

# Fibonacci Sequence Definition
def fibonacci(n:int = None)->Generator[int]:
    """
    Generates the fibonacci sequence.

    Args:
        (optional) n (int): The amount of numbers in the sequence to be generated.

    Yields:
        n1 (int): The nth number in the sequence.
    """
    n1 = 0 # 1st num in seq, later used to hold the (n - 2)th number to determine the nth number in the sequence
    n2 = 1 # 2nd num in seq, later used to hold the (n - 1)st number to determine the nth number in the sequence
    count = 0 # loop var (inc)
    while True:
        if n != None and count >= n:
            break
        yield n1
        n1, n2 = n2, n1 + n2
        count += 1
        

# Custom Sequence Definition
def custom_seq(n:int = None)->Generator[int]:
    """
    Generates a custom sequence, where the difference between each subsequent number in the sequence increases by one.

    Args:
        (optional) n (int): The amount of numbers in the sequence to be generated.

    Yields:
        n1 (int): The nth number in the sequence.
    """
    n1 = 1 # 1st num in the seq, diff is added to determine the next num in sequence
    diff = 1 # difference var (inc)
    count = 0 # loop var (inc)
    while True: 
        if n != None and count >= n:
                break
        yield n1  
        n1 += diff
        diff += 1
        count += 1


# Testing out the generators
print("Testing infinite fibonacci generator:")
count = 0
stop = 10 # used to test without generator parameter
for i in fibonacci():
    if count >= stop:
        break
    print(i)
    count += 1

print("Testing infinite custom generator:")
count = 0
# used same stop variable to test both custom and fibonacci generator
for i in custom_seq():
    if count >= stop:
        break
    print(i)
    count += 1
    

assert list(fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
assert list(fibonacci(-1)) == []
assert list(fibonacci(0)) == []
assert list(fibonacci(1)) == [0]
assert list(fibonacci(2)) == [0, 1]

# Calculation of First 10 Terms: 1, 1+1=2, 2+2=4, 4+3=7, 7+4=11, 11+5=16, 16+6=22, 22+7=29, 29+8=37, 37+9=46
assert list(custom_seq(10)) == [1, 2, 4, 7, 11, 16, 22, 29, 37, 46]
assert list(custom_seq(-1)) == []
assert list(custom_seq(0)) == []
assert list(custom_seq(1)) == [1]
assert list(custom_seq(2)) == [1, 2]


print("Millionth Test")

print("Millionth frib: ")
start = time()
for i in fibonacci(10000):  # Exhaust the generator
    prime = i 
end = time()
print(prime)
print(f"Time to find: {end-start} s")