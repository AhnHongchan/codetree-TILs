num = int(input())
i = 1
while i <= num:
    if i % 3 == 0:
        print(0, end = " ")
    elif i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print(0, end = " ")
    elif i // 10 == 3 or i// 10 == 6 or i // 10 == 9:
        print(0, end = " ")
    else:
        print(i, end = " ")
    i += 1