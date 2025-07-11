'''
Description: Convert a tuple of string numbers to a tuple of integers using comprehension.
This is important for data cleaning and type conversion in real-world datasets.
Input: t = (("11", "22"), ("33", "44"))
Output: ((11, 22), (33, 44))

'''

import ast

inp=input("enter tuple:")

t=ast.literal_eval(inp)

converted = tuple(tuple(int(x) for x in inner) for inner in t)

print(converted)
