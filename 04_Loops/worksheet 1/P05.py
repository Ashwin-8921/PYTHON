#Take an integer input and print its digits in reverse order (don’t use slicing or strings).

a=int(input("n:"))
b=0
while a>0:
    b=(b*10)+(a%10)
    a=a//10
print(b)