'''
Question: Write a function calculate(a, b) that returns both the sum and difference of a and b.
Sample data:
s, d = calculate(10, 3)
print("Sum:", s)
print("Difference:", d)

output:
Sum: 13
Difference: 7

'''

def calc(a,b):
    return a+b,a-b

a=int(input("enter a:"))
b=int(input("enter b:"))

s,d=calc(a,b)

print("sum:",s)
print("diff:",d)