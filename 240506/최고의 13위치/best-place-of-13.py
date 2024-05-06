n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_v = 0
for i in range(n):
    for j in range(n-2):
        sum_v = arr[i][j]+arr[i][j+1]+arr[i][j+2]
        if max_v < sum_v:
            max_v = sum_v
    if max_v == n:
        break
print(max_v)