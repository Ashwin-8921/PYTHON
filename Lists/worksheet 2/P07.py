'''
Task: Write a Python program to remove duplicates from a list.
Sample input: [1, 2, 3, 2, 4, 3, 5]
Output: [1, 2, 3, 4, 5]
'''

import ast

inp=input("enter list:")

list1=ast.literal_eval(inp)
converted=list(set(list1))

print(converted)
