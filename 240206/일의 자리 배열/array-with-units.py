a, b = map(int, input().split())
arr = [a, b]
for i in range(2, 10):
    arr.append(arr[-1]+arr[-2])
    if arr[-1] >= 10:
        arr[-1] = arr[-1] % 10

print(*arr)