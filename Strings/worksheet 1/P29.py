'''
Minimum Rotations to Get the Original String
Explanation: Count the rotations needed for a string to return to its original form.
Input: "abcde"
Expected Output: 5
'''

s=input("enter string:")
org=s
c=1

s=s[-1:] + s[:-1]

while org!=s :
     c=c+1
     s=s[-1:] + s[:-1]
   


print("output:",c)




    
