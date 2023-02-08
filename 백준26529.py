x = [0] * 46

x[0], x[1], x[2] = 1, 1, 2

for i in range(3, 46):
    x[i] = x[i-1]+x[i-2]

n = int(input())

for i in range(n):
    fib = int(input())
    if fib == 0 or fib == 1:
        print(x[0])
    else:
        print(x[fib])
