n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

min_v = 1000000
for i in range(n):
    start = i
    sum_v = 0
    for j in range(1, n):
        start = (i+j) % 5
        sum_v += a[start] * j
    min_v = min(min_v, sum_v)

print(min_v)