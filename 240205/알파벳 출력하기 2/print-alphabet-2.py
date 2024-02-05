num = int(input())
cnt = 0
for i in range(num):
    for j in range(i):
        print(' ', end=' ')
    for j in range(num-i, 0, -1):
        print(chr(65+cnt), end=' ')
        cnt += 1

        if cnt > 25:
            cnt = 0
    print()