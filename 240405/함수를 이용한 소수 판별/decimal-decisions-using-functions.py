def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a, b = map(int, input().split())

sum_v = 0

for i in range(a, b+1):
    if i >= 2:
        if is_prime(i):
            sum_v += i
print(sum_v)