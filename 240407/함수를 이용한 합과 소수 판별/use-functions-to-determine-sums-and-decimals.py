def judge(n):
    cnt = 0
    for i in range(2, n+1):
        if n % i == 0:
            cnt += 1
    if cnt == 1:
        sum_v = 0
        while n >= 10:
            sum_v += n % 10
            n //= 10
        sum_v += n
        if sum_v % 2 == 0:
            return True
    return False
a, b = map(int, input().split())
value = 0
for i in range(a, b+1):
    if judge(i):
        value += 1
print(value)