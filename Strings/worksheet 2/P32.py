'''
Explanation: Given a list of strings, find the position of a specific character in the k-th word.
Input: List = ["hello", "world"], k = 2, char = "r"
Expected Output: Position: 2
'''

x=input("input:").split()
k=int(input("k:"))

word = x[k-1]

c=input("char:")
'''count=0
flag=1
for char in word:
    if c == char:
        flag=0
        break
    else:
        count+=1
if flag==0:
 print("position:",count)'''


for i, ch in enumerate(word):
    if ch == c:
        print("Position:", i)
        break
else:
    print("Character not found")



