#For n rows, print the following double triangle pattern
'''
*
**
***
**
*
'''

n=int(input("n:"))
mid=(n//2)+1

for i in range(1,mid+1):
    for j in range(i):
        print("*",end='')
    print()
for i in range(mid-1,0,-1):
    for j in range(i):
        print("*",end='')
    print()
