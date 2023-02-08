ary = []
y = 0
for _ in range(3):
    x = int(input())
    ary.append(x)

y = ary[0]*1+ary[1]*2+ary[2]*3

if y>=10:
    print('happy')
else:
    print('sad')
