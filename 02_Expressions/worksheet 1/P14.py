#Toggle a Specific Bit in an Integer
#Given a number and a bit position, write an expression to toggle (flip) that bit.
#Sample Input: n = 12, bit_position = 2

n=int(input("n:"))
pos=int(input("bit pos:"))
print(bin(n))

n = n ^ (1<<pos)
print(bin(n))
print(n)