n = int(input())
lst=[]
for i in range(n):
    x, y = map(int, input().split())
    lst.append([x, y, i+1])

lst.sort(key=lambda x:(abs(x[0]-0)+abs(x[1]-0), x[2]))
for i in range(n):
    print(lst[i][2])