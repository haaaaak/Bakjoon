n, m = map(int, input().split())
x = list(map(int, input().split()))
lst = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if x[i]+x[j]+x[k] > m:
                continue
            else:
                lst.append(x[i]+x[j]+x[k])

print(max(lst))
