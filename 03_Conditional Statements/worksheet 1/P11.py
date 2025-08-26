#Enter a 16-bit value and print if parity (number of 1s) is even or odd.
#Input: 0xAAAA
#Output: Parity: Even

a=int(input("enter hex:"),16)

c=bin(a).count('1')

if c%2 == 0:
    print("parity:Even")
else:
    print("parity:odd")