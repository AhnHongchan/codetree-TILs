lst = []
for _ in range(5):
    n, h, w = input().split()
    lst.append([n, h, w])

print('name')
lst.sort(key=lambda x: x[0])

for i in range(5):
    print(*lst[i])
print()
print('height')
lst.sort(key=lambda x: -int(x[1]))

for i in range(5):
    print(*lst[i])