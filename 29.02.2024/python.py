# n = int(input("Enter n: "))
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# print(sum)

# sum2 = int((n * (n + 1))/2)
# print(sum2)

# y = int(input("Enter y: "))
# p = 1
# for x in range(1, 51, 7):
#     p *= (x - y**2)
# print(p)

n = int(input("Enter n: "))
x = int(input("Enter x: "))
s = 0
f = 1
for i in range(1, n + 1, 1):
    f *= i
    s += (x ** i)/f
print(s)