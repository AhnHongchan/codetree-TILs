n, k = map(int, input().split())
arr = [0] * 101
for _ in range(n):
    candy, idx = map(int, input().split())
    arr[idx] = candy

ans = 0
for i in range(101-2*k):
    val = sum(arr[i:i+2*k+1])
    ans = max(ans, val)
print(ans)