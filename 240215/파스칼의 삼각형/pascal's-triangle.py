n = int(input())

arr = [[1 for j in range(1, i+1)] for i in range(1, n+1)]

i = 2
while i <= n-1:
    for j in range(1, i):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    i += 1

for lst in arr:
    for x in lst:
        print(x, end = ' ')
    print()