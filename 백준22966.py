n = int(input())
ary = []

for i in range(n):
    a, b = map(str, input().split())
    ary.append([int(b), a])

ary.sort()
print(ary[0][1])
