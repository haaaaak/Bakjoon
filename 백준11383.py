n, m = map(int, input().split())

A, B = "", ""

for _ in range(n):
    for i in input():
        A += i*2

for _ in range(n):
    B += input()

if A == B:
    print("Eyfa")
else:
    print("Not Eyfa")
