x = int(input())
ary = []

for i in range (x):
    a, b = map(int, input().split())
    ary.append([b, a])

ary.sort()

for i in range(x):
    print(ary[i][1], ary[i][0])
