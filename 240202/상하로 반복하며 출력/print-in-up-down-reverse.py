num = int(input())
for i in range(num):
    for j in range(1, num+1):
        if j % 2 == 1:
            print(i+1, end="")
        else:
            print(4-i, end="")
    print()