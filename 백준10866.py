import sys

def push_front(x):
    deque.insert(0, x)

def push_back(x):
    deque.insert(len(deque), x)

def pop_front():
    if not deque :
        print(-1)
    else:
        print(deque.pop(0))

def pop_back():
    if not deque :
        print(-1)
    else:
        print(deque.pop(len(deque)-1))

def size():
    print(len(deque))

def empty():
    if not deque:
        print(1)
    else:
        print(0)

def front():
    if not deque:
        print(-1)
    else:
        print(deque[0])

def back():
    if not deque:
        print(-1)
    else:
        print(deque[-1])
    

n = int(sys.stdin.readline())

deque = []

for i in range(n):
    x = list(map(str, sys.stdin.readline().split()))

    if x[0] == 'push_front':
        push_front(x[1])
    elif x[0] == 'push_back':
        push_back(x[1])
    elif x[0] == 'pop_front':
        pop_front()
    elif x[0] == 'pop_back':
        pop_back()
    elif x[0] == 'size':
        size()
    elif x[0] == 'empty':
        empty()
    elif x[0] == 'front':
        front()
    elif x[0] == 'back':
        back()
    else:
        pass
