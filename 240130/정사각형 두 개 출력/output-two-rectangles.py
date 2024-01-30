num = int(input())
for i in range(2 * num + 1):
    if i != num:
        for j in range(num):
            print('*', end ='')

        print()
    else:
        print()