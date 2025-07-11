'''
Task: Write a Python program to multiply all the items in a list.
Sample input: [1, 2, 3, 4]
Output: 24
'''

num=list(map(int,input("enter list:").split()))

prod=1

for i in num:
    prod*=i

print("product:",prod)