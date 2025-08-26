'''
What happens if you try to access a key that doesn’t exist in a dictionary? 
Try to print the value for key 'english' in marks = {'math': 75}.
Expected Output: A KeyError.
'''
import ast

inp=input("enter dict:")

marks=ast.literal_eval(inp)

k=input("enter key:")

print(marks[k])