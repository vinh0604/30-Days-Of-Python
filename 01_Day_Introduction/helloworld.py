# Introduction
# Day 1 - 30DaysOfPython Challenge

from typing import Tuple
from math import sqrt

print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

def euclidian_distance(p1: Tuple[int, int], p2: Tuple[int, int]):
  root_distance = ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)
  return sqrt(root_distance)

print('Euclidian distance: ', euclidian_distance((2, 3), (10, 8)))