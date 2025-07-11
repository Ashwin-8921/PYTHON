'''
7. Erase the Forbidden Spells
You have a dictionary of spells, but some spells are now forbidden.
Given a list of banned spell names, wipe them from your magic book!
Input: spells = {'fireball': 5, 'healing': 10, 'curse': 2}, banned = ['curse', 'fireball']
Expected Output: {'healing': 10}
'''
import ast
inp=input("input1:")

spells=ast.literal_eval(inp)

inp=input("input2:")

banned=ast.literal_eval(inp)

for spell in banned:
    if spell in spells:
        spells.pop(spell)

print(spells)