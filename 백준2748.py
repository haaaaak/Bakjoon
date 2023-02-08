n = int(input())

feb = []
num = 0

for i in range(n+1):
    if i == 0:
        num = 0
    elif i == 1 or i == 2:
        num = 1
    else:
        num = feb[-1] + feb[-2]
    feb.append(num)

print(feb[-1])
