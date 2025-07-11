#How do you convert between data types (e.g., string to int, int to float, list to tuple) in Python? Show a code example.


a = "100"
b = int(a)
c = float(b)
d = str(c)

lst = [1, 2, 3]
tpl = tuple(lst)
lst2 = list(tpl)

print(b, c, d, tpl, lst2)
