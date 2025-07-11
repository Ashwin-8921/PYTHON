'''
Question: Write a recursive function sum_list(lst) to return the sum of all elements in a list.
Sample data:print(sum_list([1, 2, 3, 4]))
output:
10
'''

def sum_list(x):
   if len(x) == 0:
      return 0
   else:
      return x[0] + sum_list(x[1:])

print("output:",sum_list([1,2,3,4]))