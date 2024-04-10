n = int(input())
lst = []
for _ in range(n):
    name, height, age = input().split()
    lst.append([name, height, age])

lst.sort(key=lambda x:x[1])

for i in range(n):
    print(*lst[i])