while True:
    try:
        a, b = map(int,input().split())
        if (a <= 0 and b >= 10):
            break
        else:
            print(a+b)
    except:
        break
