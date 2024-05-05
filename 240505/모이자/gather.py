n = int(input())
arr = list(map(int, input().split()))

min_v = 1000000

for i in range(n):
    sum_v = 0
    for j in range(n):
        sum_v += arr[j] * abs(i-j)
    if min_v > sum_v:
        min_v = sum_v

print(min_v)