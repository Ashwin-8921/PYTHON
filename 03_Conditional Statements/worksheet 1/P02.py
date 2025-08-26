#Take an 8-bit register value and print if the **MSB** (most significant bit) is set or not.
#Input: 0b10010010
#Output: MSB set

n=int(input("bin:"),2)

print("n:",n)

if n & 0b10000000:
    print("MSB set")
else:
    print("MSB not set")

