import sys

def push():
    global cnt
    ary.append(int(x[1]))

def pop():
    global cnt
    if len(ary) - cnt == 0:
        print(-1)
    else:
        print(ary[cnt])
        cnt += 1
        
def size():
    global cnt
    print(len(ary) - cnt)
    
def empty():
    global cnt
    if len(ary) - cnt == 0:
        print(1)
    else:
        print(0)
        
def front():
    global cnt
    if len(ary) - cnt == 0:
        print(-1)
    else:
        print(ary[cnt])
    
def back():
    global cnt
    if len(ary) - cnt == 0:
        print(-1)
    else:
        print(ary[-1])

ary = []

cnt = 0
n = int(sys.stdin.readline())

for _ in range(n):
    x = list(map(str, sys.stdin.readline().split()))

    if x[0] == 'push':
        push()
    elif x[0] == 'pop':
        pop()
    elif x[0] == 'size':
        size()
    elif x[0] == 'empty':
        empty()
    elif x[0] == 'front':
        front()
    else:
        back()
