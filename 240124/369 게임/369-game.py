num = int(input())
i = 1
while i <= num:
    if i % 3 == 0:
        print(0, end = " ")
    else:
        print(i, end = " ")
    i += 1