e = 1000000007
n = int(input())
fibonacci = n-2
f1 = f2 = 1

for i in range(3, n+1):
    f2, f1 = (f1+f2) % e, f2

print(f2, fibonacci)
