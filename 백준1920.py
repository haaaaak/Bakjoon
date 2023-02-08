n = int(input())
x = set(map(int, input().split()))

m = int(input())
y = list(map(int, input().split()))

for k in y:
    print(1) if k in x else print(0)
