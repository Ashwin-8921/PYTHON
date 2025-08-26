'''
Question: Write a function factorial(n) that uses recursion to calculate the factorial of a number.
Sample data:
print(factorial(5))
output:
120
'''

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
        


n=int(input("enter num:"))

print(factorial(n))