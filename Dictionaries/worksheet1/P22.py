'''
Loop and print all values in the same dictionary.

'''

import ast

inp=input("enter dict:")

d=ast.literal_eval(inp)

for value in d.values():
    print(value)