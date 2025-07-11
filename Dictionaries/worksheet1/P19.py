'''
Remove all items from the dictionary: d = {'x': 1, 'y': 2}.

'''

import ast

inp=input("enter dict:")

d=ast.literal_eval(inp)

d.clear()

print(d)
