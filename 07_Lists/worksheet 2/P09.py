'''
Task: Write a Python program to clone or copy a list.
Sample input: [1, 2, 3, 4]
Output: [1, 2, 3, 4]
'''

import ast

inp=input("enter list:")

list1=ast.literal_eval(inp)

list2=list1.copy()

print("output:",list2)