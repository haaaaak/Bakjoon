n = int(input())

for i in range(n):
    x = list(input())
    cnt = 0
    total = 0
    for j in x:
        if j == 'O':
            cnt += 1
            total += cnt

        else:
            cnt = 0
            total += cnt

    print(total)
