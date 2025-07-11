'''
Merge two dictionaries: d1 = {'x': 1} and d2 = {'y': 2}.
Expected Output: {'x': 1, 'y': 2}
'''
import ast

inp=input("enter dict1:")

dict1=ast.literal_eval(inp)

inp=input("enter dict2:")

dict2=ast.literal_eval(inp)
dict1.update(dict2)
print(dict1)