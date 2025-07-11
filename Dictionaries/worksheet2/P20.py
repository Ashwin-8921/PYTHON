'''
20. Key Present in List and Dictionary
Given a list and a dictionary, extract values for all keys that appear in both.
Input: d = {'a': 100, 'b': 200, 'c': 300}, lst = ['b', 'c', 'd']
Expected Output: {'b': 200, 'c': 300}
'''
import ast

d = ast.literal_eval(input("dict: "))
lst = ast.literal_eval(input("list: "))

result = {key: d[key] for key in lst if key in d}

print(result)

