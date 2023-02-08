ary = []
for i in range(5):
    x = int(input())
    ary.append(x)
x = min(ary[0], ary[1], ary[2])
y = min(ary[3], ary[4])

print(x+y-50)
