num = int(input())
for i in range(num):
    for j in range(1, 2 * (i + 1)):
        print('*', end = "")
    print()