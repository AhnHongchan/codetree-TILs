n = int(input())
lst=[]
for i in range(n):
    x, y = map(int, input().split())
    lst.append([x, y, i+1])

lst.sort(key=lambda x:((x[0]**2+x[1]**2), x[2]))
for i in range(n):
    print(lst[i][2])