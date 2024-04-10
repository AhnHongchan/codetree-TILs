m1, d1, m2, d2 = map(int, input().split())
lst = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

cnt = 0
if 100 * m1 + d1 <= 100 * m2 + d2:
    while True:
        if m1 == m2 and d1 == d2:
            break
        cnt += 1
        d1 += 1
        if m1 in [1, 3, 5, 7, 8, 10, 12] and d1 == 31:
            d1 = 0
            m1 += 1
        elif m1 == 2 and d1 == 28:
            d1 = 0
            m1 += 1
        elif m1 in [4, 6, 9, 11] and d1 == 30:
            d1 = 0
            m1 += 1

else:
    while True:
        if m1 == m2 and d1 == d2:
            break
        cnt -= 1
        d1 -= 1
        if m1 in [5, 7, 10, 12] and d1 == 0:
            d1 = 30
            m1 -= 1
        elif m1 == 3 and d1 == 0:
            d1 = 28
            m1 += 1
        elif m1 in [1, 2, 4, 6, 8, 9, 11] and d1 == 0:
            d1 = 31
            m1 -= 1

cnt %= 7
print(lst[cnt])