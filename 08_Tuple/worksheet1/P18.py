'''
Description: Reverse the order of items in a tuple and print the result.
This practice is helpful in problems requiring reverse traversal or reordering.
Input: t = (10, 20, 30, 40)
Output: (40, 30, 20, 10)
'''

import ast
inp=input("enter tuple:")

t=ast.literal_eval(inp)

rev=t[::-1]

print("output:",rev)