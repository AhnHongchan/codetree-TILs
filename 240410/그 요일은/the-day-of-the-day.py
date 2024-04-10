m1, d1, m2, d2 = map(int, input().split())
day = input()
cnt = 0

week = ['Mon', 'Tue', 'Wed', 'Tue', 'Fri', 'Sat', 'Sun']

while True:
    if m1 == m2 and d1 == d2:
        break
    cnt += 1
    d1 += 1
    if m1 in [1, 3, 5, 7, 8, 10, 12] and d1 == 31:
        d1 = 0
        m1 += 1
    elif m1 in [4, 6, 9, 11] and d1 == 30:
        d1 = 0
        m1 += 1
    elif m1 == 2 and d1 == 29:
        d1 = 0
        m1 += 1

a = week.index(day)
b = cnt % 7
cnt //= 7

if a >= b:
    print(cnt+1)
else:
    print(cnt)