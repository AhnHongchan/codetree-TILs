n, m = map(int, input().split())

lst = [[m*i+j+1 for j in range(m)] for i in range(n)]

for x in lst:
    for y in x:
        print(y, end=' ')
    print()