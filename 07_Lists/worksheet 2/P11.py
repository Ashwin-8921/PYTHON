'''
Task: Write a Python program to find the common elements between two lists.
Sample input: [1, 2, 3, 4], [3, 4, 5, 6]
Output: [3, 4]
'''

import ast

inp=input("enter list 1:")
list1=ast.literal_eval(inp)

inp=input("enter list 2:")
list2=ast.literal_eval(inp)

com=list(set(list1) & set(list2))

print("output:",com)