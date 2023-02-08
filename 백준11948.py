lst1 = []
lst2 = []
for i in range(4):
    x = int(input())
    lst1.append(x)
lst1.sort(reverse=True)
for j in range(2):
    y = int(input())
    lst2.append(y)

print(lst1[0]+lst1[1]+lst1[2]+max(lst2))
