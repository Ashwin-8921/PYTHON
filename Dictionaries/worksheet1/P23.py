'''
Loop and print each key and its value together.
'''
import ast

inp=input("enter dict:")

d=ast.literal_eval(inp)

for key,values in d.items():
    print(key,values)