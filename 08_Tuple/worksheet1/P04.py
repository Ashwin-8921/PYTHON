'''
Description: Check if a specified value exists in a tuple and print the result.
Use the "in" keyword to efficiently search for elements inside a tuple.
Input: my_tuple = ('a', 'b', 'c'), Check: 'b'
Output: True
'''

import ast

inp=input("enter tuple:")

t=ast.literal_eval(inp)

c=input("check:")
print(c in t)