arr = [[1] * 5 for _ in range(5)]
for i in range(1,5):
    for j in range(1,5):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

for lst in arr:
    for x in lst:
        print(x, end=' ')
    print()