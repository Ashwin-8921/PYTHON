'''
Task: Write a Python program to get the smallest number from a list.
Sample input: [1, 2, 3, 4, 5]
Output: 1
'''

num=list(map(int,input("enter list:").split()))

s=min(num)

print("smallest:",s)