n , m = map(int, input().split())
lst = list(map(int, input().split()))

sum_v = 0

while m > 0:
    sum_v += lst[m-1]
    if m % 2 == 0:
        m //= 2
    else:
        m -= 1

print(sum_v)