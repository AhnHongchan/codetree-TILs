num = int(input())
cnt = 9
for i in range(num):
    for j in range(num):
        if cnt == 0:
            print(9, end="")
            cnt = 8
        else:
            print(cnt, end="")
            cnt -= 1
    print()