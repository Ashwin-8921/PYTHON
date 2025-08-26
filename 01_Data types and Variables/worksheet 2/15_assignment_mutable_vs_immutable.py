#How does variable assignment differ between mutable and immutable objects? Illustrate with an example.


a = [1, 2, 3]
b = a
a[0] = 99
print(b)

x = 10
y = x
x = 20
print(y)

