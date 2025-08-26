'''
Description: Print the first and last elements of a tuple using positive and negative indexing.
Learn how to access tuple elements using both forward and backward indexes, which is essential for tuple manipulation.
Input: my_tuple = (10, 20, 30, 40, 50)
Output: 10
50
'''

import ast

inp=input("enter tuple:")

my_tuple=ast.literal_eval(inp)

print("output:",my_tuple[0])
print(my_tuple[-1])