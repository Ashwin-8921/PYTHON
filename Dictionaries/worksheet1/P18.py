'''
Use .pop() to remove 'name' from
 info = {'name': 'Amit', 'city': 'Pune'} and print the value removed.
'''

import ast

inp=input("enter dict:")

info=ast.literal_eval(inp)

d=input("remove:")



print(info.pop(d))