n, m = map(int, input().split())
lst = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0

for j in range(m):
    for i in range(n):
        if j % 2 == 0:
            lst[i][j] = cnt
            cnt += 1
        else:
            lst[n-1-i][j] = cnt
            cnt += 1

for x in lst:
    for elem in x:
        print(elem, end=' ')
    print()