'''
Convert Numeric Words to Actual Numbers
Explanation: Replace words like 'one', 'two' with their numeric equivalents.
Input: "I have one apple and two oranges."
Expected Output: "I have 1 apple and 2 oranges."

'''



import re

def words_to_numbers(text):
    word_to_num = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
        'ten': '10'
    }

    pattern = re.compile(r'\b(' + '|'.join(word_to_num.keys()) + r')\b', re.IGNORECASE)

    def replace(match):
        word = match.group(0).lower()
        return word_to_num.get(word, word)

    return pattern.sub(replace, text)

input_text = input("Enter a sentence: ")
print(words_to_numbers(input_text))

