'''
Description: Find the index of a specified value in a tuple using the index() method.
Locating elements within tuples is crucial for data lookup and manipulation.
Input: t = ("cat", "dog", "rabbit"), Find: "dog"
Output: 1

'''


import ast

inp=input("enter tuple:")

t=ast.literal_eval(inp)

find=input("find:")
v=t.index(find)
print("output:",v)
