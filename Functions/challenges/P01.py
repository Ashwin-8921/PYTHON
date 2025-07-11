'''
Question: Write a function deep_sum(lst) that takes a nested list of integers (arbitrary levels of nesting) and returns the total sum of all integers.
Sample data:deep_sum([1, [2, [3, 4], 5], 6])
output:21
'''



def deep_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += deep_sum(item)
        else:
            total += item
    return total

nested_list = [1, [2, [3, 4], 5], 6]
print(deep_sum(nested_list))
