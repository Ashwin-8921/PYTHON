'''
Convert Snake Case to Pascal Case
Explanation: Change a snake_case string (words separated by underscores) into PascalCase (words start with uppercase, no underscores).
Input: "my_variable_name"
Expected Output: "MyVariableName"
'''


s=input("enter string:")

x=s.split('_')

pascal=""

for word in x:
    pascal += word.capitalize()


print("output:",pascal)