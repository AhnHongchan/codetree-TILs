num = int(input())
satisfied = False
for i in range(2, num):
    if num % i == 0:
        satisfied = True
        if num == 2:
            satisfied = False
    else:
        pass

if satisfied == True:
    print('C')
else:
    print('N')