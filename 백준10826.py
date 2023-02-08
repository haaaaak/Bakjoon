x = int(input())
a, b = 0, 1

for i in range(x):
    a, b = (a+b)%1000000007, a%1000000007

print(a)
