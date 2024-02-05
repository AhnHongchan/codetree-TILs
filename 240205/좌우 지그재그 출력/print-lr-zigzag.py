num = int(input())
for i in range(num):
    for j in range(num):
        if i % 2 == 0:
            print((i * num) + j + 1, end =" ")
        if i % 2 == 1:
            print((i * num) + num - j, end =" ")
    print()