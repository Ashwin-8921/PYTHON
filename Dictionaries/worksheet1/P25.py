'''
Make a shallow copy of d = {'p': 2, 'q': 3} and print the copy.
'''
import ast

inp=input("enter dict:")

d=ast.literal_eval(inp)

d1=d.copy()

d['p']=1000
print(d)
print(d1)