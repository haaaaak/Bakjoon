##n, k = map(int, input().split())
##
##lst = [0] * (n+1)
##
##for i in range(1, n+1):
##    if n % i == 0:
##        lst[i] = i
##    else:
##        lst[i] = 0
##
##print(lst[k])

n, k = map(int, input().split())

lst = []

for i in range(1, n+1):
    if n % i == 0:
        lst.append(i)

if len(lst) < k:
    print(0)

else:
    print(lst[k-1])
