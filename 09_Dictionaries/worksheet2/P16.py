'''
16. Log Session Nested Dictionary from List
Given a list, build a nested dictionary where each item is a deeper level (like a Russian doll).
Input: lst = ['a', 'b', 'c', 'd']
Expected Output: {'a': {'b': {'c': {'d': {}}}}}
'''
import ast

lst = ast.literal_eval(input("Input list: "))

nested = {}
for key in reversed(lst):
    nested = {key: nested}

print(nested)