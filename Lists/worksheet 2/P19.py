'''
Task: Write a Python program to create a list of numbers from 1 to 20, where each number is squared if it is even, and cubed if it is odd.
Sample input: Range: 1 to 20
Output: [1, 4, 27, 16, 125, 36, 343, 64, 729, 100, 1331, 144, 2197, 196, 3375, 256, 4913, 324, 6859, 400]

'''

i=int(input("enter range \nstart:"))

n=int(input("end:"))
list1=[k**2 if k%2==0 else k**3 for k in range(i,n+1)]

print("output:",list1)