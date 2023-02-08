x = int(input())
n = int(input())

ary = []
for i in range(n):
    a, b = map(int, input().split())

    ary.append(a*b)

if x == sum(ary):
    print("Yes")
else:
    print("No")
