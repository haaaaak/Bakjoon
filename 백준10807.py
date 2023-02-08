n = int(input())
x = list(map(int, input().split()))
m = int(input())
cnt = 0
for i in range(n):
    if x[i] == m:
        cnt += 1

print(cnt)
