def recur(x, y):
    gcd = 1
    for i in range(1, min(x, y)+1):
        if x % i == 0 and y % i == 0:
            gcd = i
    return x * y // gcd

n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)-1):
    arr[i+1] = recur(arr[i], arr[i+1])

print(arr[-1])