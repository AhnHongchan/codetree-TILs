def TSN(n):
    while n > 0:
        a = n % 10
        if a == 3 or a == 6 or a == 9:
            return True
        n = n // 10
    return False
a, b = map(int, input().split())

cnt = 0
for i in range(a, b+1):
    if TSN(i) or (i % 3 == 0):
        cnt += 1

print(cnt)