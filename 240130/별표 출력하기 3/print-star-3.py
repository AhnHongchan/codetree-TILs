num = int(input())
for i in range(num):
    for j in range(2*i):
        print('', end=" ")

    for k in range(2 * (num-i)-1):
        print('*', end=" ")
    print()