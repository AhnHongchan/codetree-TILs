def square(n):
    i = 0
    cnt = 0
    while i < n:
        for _ in range(n):
            cnt += 1
            if cnt == 10:
                cnt = 1
            print(cnt, end=" ")
        print()
        i += 1
n = int(input())
square(n)