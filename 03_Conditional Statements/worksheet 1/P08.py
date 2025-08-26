#Given a digital input value (0–255), determine and print which of 4 quadrants it falls into:
#- 0–63, 64–127, 128–191, 192–255

n=int(input("input: (0-255):"))

if 0 <= n <= 63:
    print("1st Quadrant")
elif 64 <= n <= 127:
    print("2nd Quadrant")
elif 128 <= n <= 191:
    print("3rd Quadrant")
elif 192 <= n <= 255:
    print("4th Quadrant")
