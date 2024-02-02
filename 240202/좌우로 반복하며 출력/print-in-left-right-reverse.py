num = int(input())
for i in range(num):
    for j in range(num):
        if i % 2 == 0:
            print(j+1, end="")
        else:
            print(num-j, end="")
    print()