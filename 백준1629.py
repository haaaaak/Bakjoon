import sys

def dac(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (dac(a,b//2,c)**2)%c
    else:
        return ((dac(a,b//2,c)**2)*a)%c

x = list(map(int, sys.stdin.readline().split()))

print(dac(x[0], x[1], x[2]))
