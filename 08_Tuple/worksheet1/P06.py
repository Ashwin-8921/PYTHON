'''
Description: Print the number of elements in a tuple using the len() function.
Knowing the length of tuples is crucial when iterating or validating data.
Input: t = (10, 20, 30, 40)
Output: 4
'''

import ast

inp=input("enter tuple:")

t=ast.literal_eval(inp)

print("length:",len(t))