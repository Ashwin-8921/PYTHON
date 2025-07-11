'''
Generate a Random Binary String
Explanation: Log Session a string of a given length containing only random 0s and 1s.
Input: Length = 8
Expected Output: e.g., "10101001"
'''
import random

l=int(input("length:"))

bin=''.join(random.choice('01') for i in range(l) )

print("output:",bin)