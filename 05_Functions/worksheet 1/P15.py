'''
Question: Write a recursive function fibonacci(n) that returns the nth Fibonacci number.
Sample data:print(fibonacci(6))
output:8
'''

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
     return fibonacci(n-1) + fibonacci(n-2)





n=int(input("entr n:"))

print("output:",fibonacci(n))