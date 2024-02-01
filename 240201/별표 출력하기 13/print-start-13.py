n = int(input())
for i  in range(1, 2*n+1):
    if i % 2 == 1:
        for j in range(int(n+1-(i+1)/2)):
            print('*', end = " ")
    else:
        for k in range(int((i+1)/2)):
            print('*', end = " ")
    print()