'''
Task: Write a Python program to combine two lists into a dictionary.
Sample input: ['a', 'b', 'c'], [1, 2, 3]
Output: {'a': 1, 'b': 2, 'c': 3}
'''

import ast

inp=input("enter key list:")
keys=ast.literal_eval(inp)

inp=input("enter value list:")
values=ast.literal_eval(inp)

comb_dict = dict(zip(keys, values))

print("output:",comb_dict)