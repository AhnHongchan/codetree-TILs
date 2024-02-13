n, m = map(int, input().split())

lst = [[3*i+j+1 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(lst[i][j], end = ' ')
    print()