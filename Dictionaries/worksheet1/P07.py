'''
How can you safely access a value for key 'history' in a dictionary scores without causing an error?
Sample Input: scores = {'math': 80, 'science': 90}
Expected Output: If not present, print a custom message like 'Not found'.
'''
import ast

inp=input("enter dict:")

marks=ast.literal_eval(inp)

k=input("enter key:")

print(marks.get(k,"not found"))