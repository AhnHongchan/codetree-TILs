num = int(input())
cnt = 1
for i in range(num):
    for j in range(num):
        if cnt == 10:
            print((cnt+1) % 10, end="")
            cnt = 2
        else:
            print(cnt, end="")
            cnt += 1
    print()