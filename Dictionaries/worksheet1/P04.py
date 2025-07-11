'''
Count the frequency of each letter in the string "apple", store results in a dictionary, and print it.
Sample Input: "apple"
Sample Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
'''

s=input("enter string:")

freq={}

for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq)