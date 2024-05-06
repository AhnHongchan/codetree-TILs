n = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    for j in range(i+2, n):
        cnt = arr[i] + arr[j]
        ans = max(ans, cnt)
print(ans)