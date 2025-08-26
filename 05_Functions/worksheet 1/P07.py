'''
Question: Write a function sign(num) that returns 'Positive' if num > 0, 
'Negative' if num < 0, and 'Zero' if num == 0.
Sample data:
print(sign(10))
print(sign(-4))
print(sign(0))
output:
Positive
Negative
Zero

'''

def sign(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'
    

num=int(input("enter num:"))

print(sign(num))