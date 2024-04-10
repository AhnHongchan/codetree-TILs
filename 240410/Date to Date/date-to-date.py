m1, d1, m2, d2 = map(int, input().split())

cnt = 1
while True:
    if m1 == m2 and d1 == d2:
        print(cnt)
        break
    
    cnt += 1
    d1 += 1
    if m1 == 2:
        if d1 == 28:
            m1 += 1
            d1 = 0
    elif m1 in [1,3,5,7,8,10,12]:
        if d1 == 31:
            m1 += 1
            d1 = 0
    else:
        if d1 == 30:
            m1 += 1
            d1 = 0