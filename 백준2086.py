x, y = map(int, input().split())
a, b = 0, 1

for i in 10:
    a, b = (a+b)%1000000000, a%1000000000

print(a, b)

print(x, y)
