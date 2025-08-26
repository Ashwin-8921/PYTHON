'''
Remove key 'math' from marks = {'math': 80, 'science': 85} using del
'''
import ast

inp=input("enter dict:")

marks=ast.literal_eval(inp)

d=input("delete:")

del marks[d]

print(marks)