'''
Change multiple values at once in the dictionary: 
info = {'a': 10, 'b': 20} so that both 'a' and 'b' become 100.
'''

import ast

inp=input("enter dict:")

info=ast.literal_eval(inp)

num=int(input("n:"))

info.update({'a':num,'b':num})

print(info)

