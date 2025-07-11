'''
Loop and print all keys in d = {'a': 10, 'b': 20, 'c': 30}.
'''

import ast

inp=input("enter dict:")

d=ast.literal_eval(inp)

for key in d:
    print(key)