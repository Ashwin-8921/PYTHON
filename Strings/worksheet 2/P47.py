'''
Remove Redundant Substrings from a List
Explanation: From a list of strings, remove repeated substring patterns.
Input: ["hellohello", "world", "testtesttest"]
Expected Output: ["hello", "world", "test"]
'''

def remove_redundant_substrings(strings):
    result = []
    for word in strings:
        n = len(word)
        for i in range(1, n // 2 + 1):
            pattern = word[:i]
            if pattern * (n // i) == word:
                result.append(pattern)
                break
        else:
            result.append(word)
    return result

strings = input("string:").split()
output = remove_redundant_substrings(strings)
print(output)
