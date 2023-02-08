import sys
n = int(sys.stdin.readline())
stack = []

def push(x):
    stack.append(x)

def pop():
    if not stack:
        return -1
    else:
        return stack.pop()
    
def size():
    return len(stack)

def empty():
    if not stack:
        return 1
    else:
        return 0

def top():
    if not stack:
        return -1
    else:
        return stack[-1]

for i in range(n):
    value = sys.stdin.readline().split()
    cmd = value[0]

    if cmd == 'push':
        push(value[1])
    elif cmd == 'pop':
        print(pop())
    elif cmd == 'size':
        print(size())
    elif cmd == 'empty':
        print(empty())
    elif cmd == 'top':
        print(top())
