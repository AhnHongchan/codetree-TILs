n = int(input())
arr = list(map(int, input().split()))

for i in range(0, n, 2):
    a = arr[:i+1]
    a.sort()
    print(a[i//2], end=" ")