n = int(input())
arr = list(map(int, input().split()))
max_v = 0
for i in range(n//2):
    v = arr[i] + arr[n-1-i]
    if max_v < v:
        max_v = v

print(max_v)