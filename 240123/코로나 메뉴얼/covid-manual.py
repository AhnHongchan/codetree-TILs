symp0, temp0 = input().split()
symp1, temp1 = input().split()
symp2, temp2 = input().split()
if symp0 == 'Y' and int(temp0) >= 37:
    if symp1 == 'Y' and int(temp1) >= 37:
        print('E')
    else:
        if symp2 == 'Y' and int(temp2) >= 37:
            print('E')
        else:
            print('N')
else:
    if (symp1 == 'Y' and int(temp1)) and (symp2 == 'Y' and int(temp2)):
        print('E')
    else:
        print('N')