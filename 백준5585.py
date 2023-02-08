n = 1000 - int(input())

mlist = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in mlist:
    cnt += n // i
    n %= i

print(cnt)
