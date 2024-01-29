num = int(input())
satisfied = True
for i in range(2, num):
    if num % i == 0:
        satisfied = False
    else:
        pass

if satisfied == True:
    print('P')
else:
    print('C')