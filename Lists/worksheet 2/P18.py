'''
Task: Write a Python program to unzip a list of tuples into individual lists.
Sample input: [(1, 'a'), (2, 'b'), (3, 'c')]
Output: [1, 2, 3], ['a', 'b', 'c']
'''

import ast

inp=input("enter list:")

tuple_list=ast.literal_eval(inp)


list1, list2 = zip(*tuple_list)
list1 = list(list1)
list2 = list(list2)
print("output:")
print(list1)
print(list2)
