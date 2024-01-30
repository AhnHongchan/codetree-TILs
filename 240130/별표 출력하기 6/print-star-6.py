num = int(input())
for i in range(num):
    for j in range(i):
        print(' ', end = " ")

    for j in range(2 * (num - i) - 1):
        print('*', end= " ")
   
    for j in range(num-i-2):
        print(' ', end = " ")
    print()

for i in range(num-1):
    for j in range(num-2-i):
        print(' ', end = " ")

    for j in range(2 * i + 3):
        print('*', end= " ")
   
    for j in range(num-i-2):
        print(' ', end = " ")
    print()