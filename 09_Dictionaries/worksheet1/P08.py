'''
Print all subjects and marks from this dictionary: 
student = {'math': 90, 'english': 88, 'science': 92}.
Sample Output:
math 90
english 88
science 92
'''
import ast

inp=input("enter dict:")

marks=ast.literal_eval(inp)

for key,value in marks.items():
    print(key,value)