'''
Detect URLs Within a String
Explanation: Extract all URLs from the string.
Input: "Check this link: https://openai.com and http://github.com"
Expected Output: URLs found: ['https://openai.com', 'http://github.com']
'''



import re

s = "Check this link: https://openai.com and http://github.com"

urls = re.findall(r'https?://\S+', s)

print("URLs found:", urls)
