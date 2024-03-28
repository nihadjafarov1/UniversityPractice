a = float(input("Enter length: "))
b = float(input("Enter width: "))

n = float(input("Enter side of table: "))
k = 0

while n > a or n > b:
    if a < b:
        a *= 2
    else:
        b *= 2
    k += 1

print(k)
