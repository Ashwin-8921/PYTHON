'''
21. Remove High-Value Keys
Remove all keys whose value is greater than a given number. Ignore non-numeric values.
Input: d = {'a': 5, 'b': 10, 'c': 15, 'd': 'big'}, limit = 10
Expected Output: {'a': 5, 'b': 10, 'd': 'big'}
'''

import ast

d = ast.literal_eval(input("dict: "))
limit = ast.literal_eval(input("limit: "))

filtered = {k: v for k, v in d.items() if not isinstance(v, int) or v <= limit}

print(filtered)