'''
Task: Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are the same from a given list of strings.
Sample input: ['abc', 'xyz', 'aba', '1221']
Output: 2
'''

list1=input("enter list:").split()
c=0
for word in list1:
    if len(word) >= 2 and word[0] == word[-1]:
          c+=1


print(c)