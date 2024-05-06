a = list(map(int, input()))

n = len(a)
for i in range(n):
    if a[i] != 1:
        a[i] = 1
        break

sum_v = 0

for j in range(n):
    sum_v += a[j] * (2 ** (n-j-1))

print(sum_v)