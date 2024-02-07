A = 0
B = 0
C = 0
D = 0

for tc in range(3):
    symp, temp = input().split()
    temp = int(temp)



    if temp >= 37:
        if symp == 'Y':
            A += 1
        else:
            B += 1
    else:
        if symp == 'Y':
            C += 1
        else:
            D += 1


print(A, B, C, D, end =' ')
if A >= 2:
    print('E')