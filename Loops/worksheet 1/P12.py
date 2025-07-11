#For n rows, print a right-aligned triangle pattern
'''
    *
   **
  ***
 ****
*****
'''

n=int(input("n:"))

for i in range(1,n+1):
    for j in range(1,n+1):
        if j <= (n-i):
         print(" ",end='')
        else:
           print("*",end='')
    print()