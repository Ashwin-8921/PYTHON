'''
Description: Add an item to a tuple by converting it to a list and back to a tuple.
This demonstrates tuple immutability and how to work around it for adding elements.
Input: t = (1, 2, 3), Add: 4
Output: (1, 2, 3, 4)
'''

import ast

inp=input("enter tuple:")

t=ast.literal_eval(inp)

num=int(input("add:"))

temp=list(t)

temp.append(num)

t=tuple(temp)

print("output:",t)