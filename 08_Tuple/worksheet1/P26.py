'''
Description: From a list of tuples, keep only those where all numbers are positive.
Filtering based on condition is commonly used for cleaning or selecting data.
Input: lst = [(1, 2), (-3, 4), (5, 6)]
Output: [(1, 2), (5, 6)]
'''
import ast
inp=input("enter list:")

lst=ast.literal_eval(inp)

pos = [tup for tup in lst if all(x > 0 for x in tup)]

print(pos)