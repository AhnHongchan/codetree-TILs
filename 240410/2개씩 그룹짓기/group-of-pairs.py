n = int(input())
arr = list(map(int, input().split()))
arr.sort()
max_v = 0
for i in range(len(arr)//2):
    v = arr[i] + arr[len(arr)-1-i]
    if max_v < v:
        max_v = v

print(max_v)