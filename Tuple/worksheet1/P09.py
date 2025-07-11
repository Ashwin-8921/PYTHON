'''
Description: Repeat a tuple’s elements multiple times using the * operator.
Tuple repetition is useful for generating predictable patterns or test data.
Input: t = (5, 6)
Output: (5, 6, 5, 6, 5, 6)
'''

import ast

inp=input("enter tuple:")

t=ast.literal_eval(inp)

print("output:",t*3)