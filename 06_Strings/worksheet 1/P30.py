'''
Count Frequency of Words in String (Short Form)
Explanation: Show how many times each word appears.
Input: "apple apple orange"
Expected Output: {'apple': 2, 'orange': 1}
'''

'''s=input("input:")

words=s.split()

freq={}

for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1


print("output:",freq)'''


from collections import Counter

s = input("enter string:")
words = s.split()  
result = Counter(words)
print(dict(result))
