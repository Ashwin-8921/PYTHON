'''
Description: Check whether all elements in a tuple are unique using set comparison.
Ensures data integrity in scenarios where duplicate values are not allowed.
Input: t = (1, 2, 3, 4, 5)
Output: True
'''


import ast
inp=input("enter tuple:")

t=ast.literal_eval(inp)


is_unique = len(set(t)) == len(t)

print(is_unique)