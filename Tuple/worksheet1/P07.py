'''
Description: Iterate through all elements in a tuple and print each one on a separate line.
Looping over tuples is a fundamental skill for data processing and display.
Input: t = ("apple", "banana", "cherry")
Output: apple
banana
cherry
'''
import ast

inp=input("enter tuple:")

t=ast.literal_eval(inp)

print("output:")

for i in t:
    print(i)