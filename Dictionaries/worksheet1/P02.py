'''
Suppose you write a dictionary with the same key twice. What value is stored?
Sample Input: d = {'x': 1, 'y': 2, 'x': 5}
Sample Output: {'x': 5, 'y': 2}
'''

import ast

inp=input("enter dict:")

student=ast.literal_eval(inp)

print(student)