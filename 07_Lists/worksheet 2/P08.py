'''
Task: Write a Python program to check if a list is empty or not.
Sample input: []
Output: List is empty

'''
import ast

inp=input("enter list:")

list1=ast.literal_eval(inp)

if not list1:
    print("list is empty")
else:
    print("list is not empty")