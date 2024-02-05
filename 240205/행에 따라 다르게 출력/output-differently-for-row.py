num = int(input())

for i in range(num):
    for j in range(num):
        if i % 2 == 0:
            print(3 * num * (i//2) + j + 1, end =" ")
        if i % 2 == 1:
            print(2 * num - 1 + 2 * j, end = " ")
    print()