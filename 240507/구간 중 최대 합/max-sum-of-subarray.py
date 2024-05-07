from itertools import combinations
n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(n-k+1):
    sum_v = sum(arr[i:i+k])
    ans = max(ans, sum_v)

print(ans)