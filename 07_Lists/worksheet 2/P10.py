'''
Task: Write a Python program to find the list of words that are longer than n from a given list of words.
Sample input: ['hello', 'world', 'python', 'is', 'great'], n = 4
Output: ['hello', 'world', 'python', 'great']
'''

import ast

inp=input("enter list:")

list1=ast.literal_eval(inp)

n=int(input("enter n:"))

long=[word for word in list1 if len(word) > n]

print("output:",long)