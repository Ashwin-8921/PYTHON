'''
Increase every salary in salaries = {'A': 20000, 'B': 30000} by 10%.
Sample Output: {'A': 22000.0, 'B': 33000.0}
'''
import ast

inp=input("enter dict:")

salaries=ast.literal_eval(inp)

for key in salaries:
    salaries[key]*=1.10

print(salaries)