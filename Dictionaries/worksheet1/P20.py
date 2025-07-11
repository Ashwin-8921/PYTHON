'''
Write a program to remove key 'z' from d = {'x': 1, 'y': 2} only if it exists.
Expected Output: If not found, print 'Key not found'.
'''

import ast

inp=input("enter dict:")

d=ast.literal_eval(inp)

key=input("key:")

if key in d:
    d.pop(key)
else:
    print("key not found")

print(d)
