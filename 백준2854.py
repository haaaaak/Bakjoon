h, m = map(int, input().split())

if m >= 45 and m < 60:
    print(h, m-45)
elif m < 45:
    if h == 0:
        print(23, m+15)
    elif h > 0 and h < 24:
        print(h-1, m+15)
