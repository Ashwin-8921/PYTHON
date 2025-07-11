'''
Question: Write a function string_stats(s) that returns the number of vowels, consonants, and digits in the string s.
Sample data:
print(string_stats("Hello123"))
output:
(2, 5, 3)
'''

def string_stats(s):
    vowels='aeiouAEIOU'
    v=d=c=0
    for ch in s:
        if ch.isdigit():
            d+=1
        elif ch.isalpha():    
            if ch in vowels:
                v+=1
            else:
                c+=1
    return v,c,d


s=input("enter string:")

print(string_stats(s))