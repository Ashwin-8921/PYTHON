#Take an error code (integer). Print "Critical" if code ≥1000, "Warning" if 100–999, and "Info" if <100.
#Input: 230
#Output: Warning

a=int(input("code:"))

if 100 <= a <= 999:
    print("Warning")
elif a >= 1000:
    print("Critical")
else:
    print("Info")