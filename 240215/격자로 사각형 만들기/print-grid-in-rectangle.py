n = int(input())
arr = [[1] * n for _ in range(n)]

for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = arr[i][j-1] + arr[i-1][j-1] + arr[i-1][j]

for lst in arr:
    for x in lst:
        print(x, end = ' ')
    print()