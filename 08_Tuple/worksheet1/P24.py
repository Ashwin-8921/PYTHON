'''
Description: Remove all empty tuples from a list of tuples and print the cleaned list.
This is useful for sanitizing input data before processing.
Input: lst = [(), (), ('a', 'b'), ('c',)]
Output: [('a', 'b'), ('c',)]
'''
import ast
inp=input("enter list:")

lst=ast.literal_eval(inp)

cleaned_list = [t for t in lst if t]

print(cleaned_list)
