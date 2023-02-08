ary = []

for _ in range(7):
    x = int(input())
    if (x%2 != 0):
        ary.append(x)
if ary:
    print(sum(ary))
    print(min(ary))

else:
    print(-1)
