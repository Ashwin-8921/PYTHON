'''
Description: Join two tuples together using the + operator and print the result.
Concatenation helps combine multiple tuples into a single sequence for further processing.
Input: t1 = (1, 2), t2 = (3, 4)
Output: (1, 2, 3, 4)

'''

import ast

inp=input("enter t1:")

t1=ast.literal_eval(inp)

inp=input("enter t2:")

t2=ast.literal_eval(inp)

print("output:",t1+t2)