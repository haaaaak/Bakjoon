n = int(input())
stack = []
lst = []
cnt = 1

for i in range(1, n+1):
    m = int(input())
    while cnt <= m:
        stack.append(cnt)
        cnt +=1
        lst.append('+')

    if stack[-1] == m:
        stack.pop()
        lst.append('-')
    else:
        print('NO')
        exit()

print('\n'.join(lst))
