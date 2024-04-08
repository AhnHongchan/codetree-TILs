def divide(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] //= 2
    return arr

N = int(input())
arr = list(map(int, input().split()))
arr = divide(arr)

for elem in arr:
    print(elem, end= " ")