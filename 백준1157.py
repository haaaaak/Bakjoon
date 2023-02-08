n = input().upper()

n_set = list(set(n))

cnt = []

for i in n_set:
    cnt.append(n.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')

else:
    print(n_set[cnt.index(max(cnt))])
