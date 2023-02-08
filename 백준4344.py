n = int(input())

for i in range(n):
    cnt = 0
    m = list(map(int, input().split()))
    avg = sum(m[1:])/m[0]
    for j in range(1, len(m)):
        if m[j] > avg:
            cnt += 1
        tavg = cnt / m[0] * 100
    print("{:.3f}%".format(tavg))
