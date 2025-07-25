'''
Task: Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample input: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Output: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

list1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print("input:",list1)

sorted_list=sorted(list1,key=lambda x:x[-1])

print("output:",sorted_list)