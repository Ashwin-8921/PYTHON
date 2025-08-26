'''
11. Empty Desk Detective
You check a colleague's desk (dictionary) for items. If it's empty, 
print a clear message so you don't miss anything!
Input: desk = {}
Expected Output: Dictionary is empty!
'''

import ast
inp=input("input1:")

dict1=ast.literal_eval(inp)

if not dict1:
    print("Dictionary is empty!")
else:
      print("Dictionary is not empty!")