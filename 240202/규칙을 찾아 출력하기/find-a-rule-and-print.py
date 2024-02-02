n = int(input())

for i in range(n):
    if i == 0 or i == n-1:
        print("* " * n)
    else:
        for j in range(n):
            if i > j:
                print("*", end = " ") 
            elif i < j:
                print(" ", end = " ")
        if j == n-1:
            print("*", end = " ")
        print()