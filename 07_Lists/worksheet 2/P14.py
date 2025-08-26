'''
Task: Write a Python program to create a list of even numbers from a given list using list comprehension.
Sample input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [2, 4, 6, 8, 10]
'''

import ast

inp=input("enter list:")

list1=ast.literal_eval(inp)

list2=[]

'''for i in list1:
    if i%2==0:
        list2.append(i)'''

list2 = [i for i in list1 if i % 2 == 0]

print("output:",list2)