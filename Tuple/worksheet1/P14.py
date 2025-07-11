'''
Description: Convert a tuple of characters to a string and then back to a tuple.
Useful for text manipulation and transitioning between data representations.
Input: t = ('P', 'y', 't', 'h', 'o', 'n')
Output: String: "Python"
Tuple: ('P', 'y', 't', 'h', 'o', 'n')
'''

import ast

inp=input("enter tuple:")

t=ast.literal_eval(inp)

s=''.join(t)

print("string:",s)

print("tuple:",tuple(s))