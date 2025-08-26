'''
Question: Write a function find_duplicates(lst) that returns a list of all elements 
that appear more than once in the input list. The result should contain no duplicates
 and preserve the order of their first appearance.
Sample data:find_duplicates([4, 2, 4, 5, 2, 3, 4])
output: [4, 2]
'''

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    result = []

    for item in lst:
        if item in seen:
            if item not in duplicates:
                result.append(item)
                duplicates.add(item)
        else:
            seen.add(item)
    return result

input_list = [4, 2, 4, 5, 2, 3, 4]
print(find_duplicates(input_list))
