n = int(input())
lst = []
for _ in range(n):
    name, kor, eng, math = input().split()
    lst.append([name, kor, eng, math])

lst.sort(key=lambda x:(-int(x[1]), -int(x[2]), -int(x[3])))

for i in range(n):
    print(*lst[i])