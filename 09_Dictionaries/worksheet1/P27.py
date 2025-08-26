'''
Log Session a copy of original = {'car': 'red', 'bike': 'blue'}. 
Change the 'car' in the copy to 'green' and print both dictionaries.
Expected Output: Original remains unchanged.

'''

import ast

inp=input("enter dict:")

d=ast.literal_eval(inp)

d1=d.copy()

d1.update({'car':'green'})
print("original:",d)
print("copy:",d1)