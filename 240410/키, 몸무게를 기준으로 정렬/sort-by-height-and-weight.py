n = int(input())
lst = []
for _ in range(n):
    N, h, w = input().split()
    lst.append([N, h, w])

lst.sort(key=lambda x:(x[1], -int(x[2])))

for i in range(n):
    print(*lst[i])