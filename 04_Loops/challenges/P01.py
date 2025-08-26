#Print all 4-digit numbers where the product of the first two digits equals the product of the last two digits.
#Valid Example: 1441 → (1 × 4) == (4 × 1) → 4 == 4 (valid)
#Invalid Example: 2356 → (2 × 3) == (5 × 6) → 6 == 30 (not valid)


for i in range(1000,10000):
    a=i%10
    b=(i//10)%10
    c=(i//100)%10
    d=(i//1000)

    if a*b == c*d:
        print(i)
    