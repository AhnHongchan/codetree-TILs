num = int(input())
for i in range(1, num+1):
    if i % 2 == 1:
        print('*', end="")

    else:
        for j in range(i):
            print('*', end = " ")
    print()