#Using only loops, print all prime numbers between 2 and n (n is user input).

n=int(input("n:"))

for i in range(2,n):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i)