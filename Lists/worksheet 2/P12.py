'''
Task: Write a Python program to flatten a shallow list.
Sample input: [[1, 2], [3, 4], [5, 6]]
Output: [1, 2, 3, 4, 5, 6]
'''

import ast

inp=input("enter list:")

list1=ast.literal_eval(inp)

flat=[]
for sublist in list1:
    for item in sublist:
        flat.append(item)


#flat = [item for sublist in list1 for item in sublist]

print("output:",flat)