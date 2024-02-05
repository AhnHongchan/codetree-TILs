num = int(input())
for i in range(1, num+1):
    for j in range(1, num +1):
        print(f"({i}, {j})", end=' ')
        if (i + j) % 4 == 0:
            print()