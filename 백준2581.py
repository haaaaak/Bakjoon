import sys
import math

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

sum_lst = []

for i in range(m, n+1):
    cnt = 0
    print(i)
    if i > 1:
        for k in range(2, int(math.sqrt(i))+1):
            if i % k == 0:
                cnt += 1
                break
        if cnt == 0:
            sum_lst.append(i)

if sum_lst:
    print(sum(sum_lst), min(sum_lst), sep='\n')
else:
    print(-1)
