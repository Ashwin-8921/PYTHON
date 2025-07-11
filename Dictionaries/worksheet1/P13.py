'''
Add 'Bangalore': 12000000 to cities = {'Delhi': 18000000, 'Mumbai': 20000000}.

'''
import ast

inp=input("enter dict:")

cities=ast.literal_eval(inp)

inp=input("add:")
add=ast.literal_eval(inp)

cities.update(add)

print(cities)