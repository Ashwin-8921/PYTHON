'''
Update the age of 'Anil' from 21 to 22 in this dictionary: ages = {'Anil': 21, 'Sunita': 20}.
'''
import ast

inp=input("enter dict:")

ages=ast.literal_eval(inp)

k=input("enter key:")

num=int(input("enter updated value:"))

#ages[k]=num

ages.update({k:num})

print(ages)