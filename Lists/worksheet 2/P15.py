'''
Task: Write a Python program to remove all occurrences of a specific element from a list.
Sample input: [1, 2, 3, 2, 4, 2, 5], element to remove: 2
Output: [1, 3, 4, 5]
'''

import ast

inp=input("enter list:")

list1=ast.literal_eval(inp)

n=int(input("element to remove:"))

new=[i for i in list1 if i != n]

print("output:",new)

