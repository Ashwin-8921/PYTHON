'''
Task: Write a Python program to sum all the items in a list.
Sample input: [1, 2, 3, 4, 5]
Output: 15
'''

num=list(map(int,input("enter list:").split()))

sum=0

for i in num:
 sum+=i

print("sum:",sum)