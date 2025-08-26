'''
Description: Count the number of tuples where every element is divisible by a given integer K.
This builds filtering skills and strengthens logic construction for data validation.
Input: lst = [(3, 6), (9, 12, 15), (4, 8)], K = 3
Output: 2
'''

import ast
inp=input("enter list:")

lst=ast.literal_eval(inp)

k=int(input("input:"))

count = sum(all(x % k == 0 for x in tup) for tup in lst)

print(count)