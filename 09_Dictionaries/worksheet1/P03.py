'''
How can you check if the key 'fruit' exists in a dictionary called d?
Sample Input: d = {'fruit': 'apple', 'veg': 'carrot'}
Sample Output: True (when checked for 'fruit')
'''
import ast

inp=input("enter dict:")

fruits=ast.literal_eval(inp)

fruit=input("enter key:")

print(fruit in fruits)