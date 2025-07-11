'''
Description: Sort a list of tuples by the total number of digits across all elements in each tuple.
This requires counting the digits and sorting accordingly, which strengthens comprehension of tuple processing.
Input: lst = [(1, 2), (10, 11), (3, 44)]
Output: [(1, 2), (3, 44), (10, 11)]
'''


def count_digits(tup):
    return sum(len(str(x)) for x in tup)

import ast
inp=input("enter tuple:")

t=ast.literal_eval(inp)

sorted_list = sorted(t, key=count_digits)

print(sorted_list)