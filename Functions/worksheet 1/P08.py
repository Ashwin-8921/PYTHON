'''
Question: Write a function power(base, exponent=2) that returns base raised to exponent (default is square).
Sample data:
print(power(3))
print(power(2, 5))
output:
9
32
'''

def power(base,exp=2):
    return base**exp


base=int(input("enter base:"))
exp=int(input("enter exponent:"))
print(power(base))
print(power(base,exp))
