import sys

x = int(sys.stdin.readline())
ary = []

for i in range(x):
    y = int(sys.stdin.readline())
    ary.append(y)

ary.sort(reverse=True)

for i in range(x):
    print(ary[i])
