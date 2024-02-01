n = int(input())

for i in range(2*n+1):
    if i % 2 == 0:
        for j in range(7):
            print('*', end = ' ')

    if i % 2 == 1:
        for j in range(4):
            print('*  ', end = ' ')
    
    print()