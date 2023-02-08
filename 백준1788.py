x = int(input())
for i in range(x+1):
    if i == 0:
        num = 0
        feb.append(1)
    else:
        num = feb[-1] + feb[-2]
    feb.append(num)

print(feb[-1])
print(feb[-2])
