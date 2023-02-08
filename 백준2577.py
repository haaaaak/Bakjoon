import sys

y = 1
for i in range(3):
    n = int(sys.stdin.readline())
    y *= n
    
y = list(str(y))

for i in range(10):
    print(y.count(str(i)))
