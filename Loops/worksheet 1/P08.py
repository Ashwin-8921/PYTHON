#Print a hollow square pattern of size n (n ≥ 3).
#Example for n = 5:

'''
*****
*   *
*   *
*   *
*****
'''

n=int(input("n:"))

for i in range(0,n):
    for j in range(0,n):
        if i==0 or i==(n-1) or  j==0 or j==(n-1):
         print("*",end=' ')
        else:
            print(" ",end=' ')
    print()