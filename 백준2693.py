x = int(input())
for i in range(x):
    y = list(map(int, input().split()))
    y.sort(reverse=True)
    print(y[2])
