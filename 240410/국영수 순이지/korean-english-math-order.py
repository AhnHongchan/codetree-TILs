n = int(input())
lst = []
for _ in range(n):
    name, kor, eng, math = input().split()
    lst.append([name, kor, eng, math])

lst.sort(key=lambda x:(x[1], x[2], x[3]))

for i in range(n):
    print(*lst[n-1-i])