'''
Generate All Valid IP Addresses from a String
Explanation: Given a string of digits, form all possible valid IP addresses.
Input: "25525511135"
Expected Output: ['255.255.11.135', '255.255.111.35']
'''

def restore_ip_addresses(s):
    res = []

    def backtrack(start=0, path=[]):
        if len(path) == 4:
            if start == len(s):
                res.append(".".join(path))
            return

        for length in range(1, 4):
            if start + length > len(s):
                break
            segment = s[start:start + length]
            if (segment.startswith('0') and len(segment) > 1) or int(segment) > 255:
                continue
            backtrack(start + length, path + [segment])

    backtrack()
    return res

input_string = input("Enter a string of digits: ")
print(restore_ip_addresses(input_string))
