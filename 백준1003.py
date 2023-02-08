n = int(input())
for i in range(n):
    x = int(input())
    feb = []
    num = 0

    for i in range(x+1):
        if i == 0:
            num = 0
            feb.append(1)
        elif i == 1 or i == 2:
            num = 1
        else:
            num = feb[-1] + feb[-2]
        feb.append(num)

    print('{} {}'.format(feb[-2], feb[-1]))
