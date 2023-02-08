n = [i for i in range(1, 31)]

for j in range(28):
    n.remove(int(input()))

print(min(n))
print(max(n))

