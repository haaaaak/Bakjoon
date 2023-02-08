a = list(map(int,input().split()))
b = list(map(int,input().split()))
x = 0
y = 0

for i in range(4):
    x += a[i]
    y += b[i]

if x==b:
    print(x)
else:
    print(max(x,y))
