'''
5. The Dictionary of Two Kingdoms
The “North” kingdom and the “South” kingdom both keep ledgers of gold reserves. 
Suddenly, there’s a war—when they merge, the South’s gold value should overwrite the North’s wherever 
the city names match! What do the ledgers look like after the kingdoms unite?
Input: north = {'Winterfell': 1000, 'The Eyrie': 800}, south = {'The Eyrie': 1200, "King's Landing": 2500}
Expected Output: {'Winterfell': 1000, 'The Eyrie': 1200, "King's Landing": 2500}
'''
import ast

inp=input("input1:")

north=ast.literal_eval(inp)

inp=input("input2:")

south=ast.literal_eval(inp)

north.update(south)

print(north)
