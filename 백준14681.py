ary = []
for i in range(2):
    x = int(input())
    ary.append(x)
if (ary[0] > 0 and ary[1] > 0):
    print(1)
elif (ary[0] < 0 and ary[1] > 0):
    print(2)
elif (ary[0] < 0 and ary[1] < 0):
    print(3)
else:
    print(4)
