'''
Task: Write a Python program to insert an element at a specified position in a list.
Sample input: [1, 2, 3, 4], element: 5, position: 2
Output: [1, 2, 5, 3, 4]
'''
import ast

inp=input("enter list:")

list1=ast.literal_eval(inp)

ele=int(input("element:"))

pos=int(input("position:"))

list1.insert(pos,ele)

print("output:",list1)

