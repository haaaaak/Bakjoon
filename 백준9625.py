a = [0] * 46
b = [0] * 46

a[2], a[3] = 1, 2  # [0, 0, 1, 2, 3, 5, ...]
b[1], b[2] = 1, 2  # [0, 1, 2, 3, 5, 8, ...]

for i in range(3, 46):
    a[i] = a[i-1]+a[i-2]

for i in range(2, 46):
    b[i] = b[i-1]+b[i-2]

k = int(input())

print(a[k], b[k])

##K=int(input())
##a,b=0,1
##for i in range(1,K):
##    a,b = b,a+b
##print(a,b)
