'''
13. Substring Key Find
Given a search term, find out which keys in your dictionary contain it. 
Useful for partial name search!
Input: d = {'hello': 1, 'world': 2, 'hell': 3}, substring = 'hell'
Expected Output: Keys containing 'hell': ['hello', 'hell']
'''

import ast

d = ast.literal_eval(input("dict:"))
substring = input("substring:")

match = [key for key in d if substring in key]

print(f"Keys containing '{substring}': {match}")

