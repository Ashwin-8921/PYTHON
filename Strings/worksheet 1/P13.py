'''
Find Uncommon Words Between Two Strings
Explanation: List words present in only one of the two strings.
Input: "red blue green", "blue yellow red"
Expected Output: Uncommon words: ['green', 'yellow']
'''

l1=input("string1:")
l2=input("string2:")

word1=set(l1.split())
word2=set(l2.split())

uncmn=list(word1^word2)

print("uncommin words:",uncmn)