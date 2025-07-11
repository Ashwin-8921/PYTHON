'''
Description: Find and print the maximum and minimum values in a tuple of numbers.
This is helpful for statistical analysis and summarizing numeric data in tuples.
Input: t = (11, 3, 55, 21)
Output: 55
3
'''

import ast

inp=input("enter tuple:")

t=ast.literal_eval(inp)

print("output:",max(t))

print(min(t))