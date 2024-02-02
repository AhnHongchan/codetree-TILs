num = int(input())
cnt = 1
for i in range(num):
    for j in range(num):
        if cnt == 5:
            print(2, end=" ")
            cnt = 2
        else:
            print(2 * cnt, end =" ")
            cnt += 1
    print()