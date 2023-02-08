import sys

def push(x):
    ary.append(x)

def pop():
    if not ary:
        print(-1)
    else:
        print(ary.pop(0))

def size():
    print(len(ary))

def empty():
    if not ary:
        print(1)
    else:
        print(0)

def front():
    if ary:
        print(ary[0])
    else:
        print(-1)

def back():
    if ary:
        print(ary[len(ary)-1])
    else:
        print(-1)

n = int(sys.stdin.readline())

ary =[]

for i in range(n):
    x = list(map(str, sys.stdin.readline().split()))
    if x[0] == 'push':
        push(int(x[1]))
    elif x[0] == 'pop':
        pop()
    elif x[0] == 'size':
        size()
    elif x[0] == 'empty':
        empty()
    elif x[0] == 'front':
        front()
    elif x[0] == 'back':
        back()
