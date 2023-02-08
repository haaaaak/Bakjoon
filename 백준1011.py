t = int(input())

for i in range(t):
    x, y = map(int,input().split())
    r = y - x
    cnt = 0
    a = 1
    b = 0
    while b < r :
        cnt += 1
        b += a
        if cnt % 2 == 0 :
            a += 1  
    print(cnt)
