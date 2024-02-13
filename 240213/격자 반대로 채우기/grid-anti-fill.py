n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

cnt = 1
for j in range(n-1,-1,-1):
    for i in range(n):
        if j % 2 == 1:
            arr[n-i-1][j] = cnt
            cnt += 1
        else:
            arr[i][j] = cnt
            cnt += 1

for lst in arr:
    for elem in lst:
        print(elem, end=' ')
    print()