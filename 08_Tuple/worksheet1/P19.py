'''
Description: Identify and print elements that occur more than once in a tuple.
Spotting duplicates in sequences is common in data cleaning and interviews.
Input: t = (2, 4, 6, 2, 8, 4, 6, 2)
Output: 2, 4, 6
'''

import ast
inp=input("enter tuple:")

t=ast.literal_eval(inp)

dup= tuple(set(x for x in t if t.count(x) > 1))

print(*dup, sep=", ")