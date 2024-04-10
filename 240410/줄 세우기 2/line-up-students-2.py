n = int(input())
lst = []
for i in range(n):
    h, w = map(int, input().split())
    lst.append([h, w, i+1])

lst.sort(key=lambda x: (x[0], -x[1]))

for i in range(n):
    print(*lst[i])