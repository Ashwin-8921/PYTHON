#Count the Number of 1 Bits in an Integer (No Loops)
#Write an expression (using built-in functions) to count how many 1s are in the binary representation of a number.
#Sample Input: n = 29

n=int(input("n:"))

print(bin(n).count("1"))