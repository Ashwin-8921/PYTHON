#Enter a signal frequency (Hz). Print "Low Band" (<1000), "Mid Band" (1000–9999), "High Band" (10000–99999), or "Out of Range".
#Input: 8000
#Output: Mid Band

a=int(input("Freq:"))

if a < 1000:
    print("Low Band")
elif 1000 <= a <= 9999:
    print("Mid Band")
elif 10000 <= a <= 99999:
    print("High Band")
else:
    print("Out of Range")