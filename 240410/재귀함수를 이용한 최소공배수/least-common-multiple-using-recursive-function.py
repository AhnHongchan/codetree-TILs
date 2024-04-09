def recur(x, y):
    for i in range(max(x, y), x*y+1):
        if i % x == 0 and i % y == 0:
            return i

n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)-1):
    arr[i+1] = recur(arr[i], arr[i+1])

print(arr[-1])