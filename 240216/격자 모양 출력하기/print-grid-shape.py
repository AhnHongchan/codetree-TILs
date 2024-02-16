n, m = map(int, input().split())

arr = [[0] * n for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = a * b

for lst in arr:
    for x in lst:
        print(x, end=' ')
    print()