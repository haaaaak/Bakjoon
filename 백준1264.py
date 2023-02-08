while True:
    n = input()
    cnt = 0
    if n == '#':
        break
    else:
        for i in n:
            if i in "aeiouAEIOU" :
                cnt += 1
        print(cnt)
