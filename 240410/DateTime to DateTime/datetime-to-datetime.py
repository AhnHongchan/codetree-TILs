a, b, c = map(int, input().split())
cnt = 0

if (a == 11 and b == 11 and c <= 11) or (a == 11 and b <= 10):
    while True:
        if a == 11 and b == 11 and c == 11:
            print(cnt)
            break
        c += 1
        cnt += 1
        if c == 60:
            c = 0
            b += 1


else:
    while True:
        if a == 11 and b == 11 and c == 11:
            print(cnt)
            break
        c -= 1
        cnt += 1
        if c == 0:
            c = 60
            b -= 1
            if b == -1:
                b = 23
                a -= 1