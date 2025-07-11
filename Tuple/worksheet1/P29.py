'''
Description: Convert a tuple of nested tuples into a single flat tuple.
Flattening data structures is often needed for uniform data processing and analysis.
Input: t = ((1, 2), (3, 4), (5, 6))
Output: (1, 2, 3, 4, 5, 6)
'''

import ast
inp=input("enter tuple:")

t=ast.literal_eval(inp)
flat = tuple(x for sub in t for x in sub)

print(flat)