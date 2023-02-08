x = int(input())

for i in range(x):
    a, b = input().split()

    for j in b:
        print(j*int(a), end='')
    print()
