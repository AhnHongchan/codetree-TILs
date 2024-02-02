num = int(input())
cnt = 1
for i in range(num):
    for j in range(num):
        print(cnt, end=" ")
        cnt += 1
    print()