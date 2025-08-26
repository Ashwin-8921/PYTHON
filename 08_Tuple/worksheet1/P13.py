'''
Description: Remove a specific element from a tuple by converting it to a list and back.
Removing elements from tuples is a common interview question testing immutability handling.
Input: t = (1, 2, 3, 4), Remove: 2
Output: (1, 3, 4)
'''

import ast

inp=input("enter tuple:")

t=ast.literal_eval(inp)

num=int(input("remove:"))

temp=list(t)

temp.remove(num)

t=tuple(temp)

print("output:",t)