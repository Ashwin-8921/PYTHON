'''
Sort a List of Strings Alphabetically
Explanation: Arrange the list of strings in lexicographical order.
Input: ["pear", "apple", "banana"]
Expected Output: ['apple', 'banana', 'pear']
'''

s = input("enter strings: ")
list1 = s.split(',')
list1 = [s.strip() for s in list1]
sorted_list = sorted(list1)
print("Sorted list:", sorted_list)
