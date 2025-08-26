'''
Description: Check if a specified value is present in any of the inner tuples in a tuple of tuples.
This teaches how to search through nested tuples, which is useful in multi-dimensional data handling.
Input: t = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime')), Check: 'White'
Output: True
'''
import ast
inp=input("enter t:")

t=ast.literal_eval(inp)

check=input("check:")

found = any(check in inner for inner in t)

print(found)