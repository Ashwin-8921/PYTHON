'''
Given marks = {'math': 75, 'science': 80}, access and print the marks for 'science'.
'''

import ast

inp=input("enter dict:")

marks=ast.literal_eval(inp)

k=input("enter key:")

print(marks.get(k))

