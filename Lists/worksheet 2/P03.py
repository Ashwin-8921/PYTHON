'''
Task: Write a Python program to get the largest number from a list.
Sample input: [1, 2, 3, 4, 5]
Output: 5

'''
num=list(map(int,input("enter list:").split()))

l=max(num)

print("largest:",l)
