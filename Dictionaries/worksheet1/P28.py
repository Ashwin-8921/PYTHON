'''
Explain (with code) the difference between a shallow copy and a deep copy using a nested dictionary. 
Show the effect of changing an inner list.
'''



import copy

a = {'x': [1, 2], 'y': [3, 4]}
shallow = a.copy()
deep = copy.deepcopy(a)

shallow['x'].append(99)
deep['y'].append(100)

print("Original (a):", a)
print("Shallow Copy:", shallow)
print("Deep Copy   :", deep)
