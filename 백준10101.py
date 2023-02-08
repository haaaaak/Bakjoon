ary = []
for i in range(3):
    x = int(input())
    ary.append(x)

if (ary[0]+ary[1]+ary[2] == 180):
    if (ary[0]==ary[1]==ary[2]):
        print('Equilateral')
    elif (ary[0]==ary[1] or ary[0]==ary[2] or ary[1]==ary[2]):
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
