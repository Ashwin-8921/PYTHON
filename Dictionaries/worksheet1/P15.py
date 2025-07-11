'''
Given a list ['dog', 'cat', 'rabbit'], create a dictionary with words as keys 
and their lengths as values.
Expected Output: {'dog': 3, 'cat': 3, 'rabbit': 6}
'''

import ast

inp=input("enter list:")

list1=ast.literal_eval(inp)

dict={}

for word in list1:
    dict[word]=len(word)

print(dict)