# Greedy
n, k = map(int, input().split())

cnt = 0
ary = []

for _ in range(n):
    cn = int(input())
    
    ary.append(cn)

ary.sort(reverse=True)

for i in ary:
    cnt += k // i
    k %= i

print(cnt)
