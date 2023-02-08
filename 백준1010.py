# nCr 함수 구현
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        num = 1
        for i in range(1, n+1):
            num *= i
        return num

import sys

x = int(sys.stdin.readline())

for i in range(x):
    n, m = map(int, input().split())
    print(factorial(m) // (factorial(m-n) * factorial(n)))

