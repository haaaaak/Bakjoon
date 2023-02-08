lst = []

for i in range(10):
    x = int(input())
    x = x % 42
    lst.append(x)

lst = set(lst)
print(len(lst))
