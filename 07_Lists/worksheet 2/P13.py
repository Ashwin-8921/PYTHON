'''
Task: Write a Python program to create a list of squares from 1 to 10 using list comprehension.
Sample input: Range: 1 to 10
Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

i=int(input("enter range \nstart:"))

n=int(input("end:"))
list1=[]

for i in range(i,n+1):
    list1.append(i**2)

print("output:",list1)