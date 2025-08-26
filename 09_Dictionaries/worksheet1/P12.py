'''
Assign a value to a key that doesn't exist (e.g., add 'C': 25000 to salaries). What happens?
'''
import ast

inp=input("enter dict:")

salaries=ast.literal_eval(inp)

#salaries.update({'C':25000})
salaries['C'] = 25000

print(salaries)