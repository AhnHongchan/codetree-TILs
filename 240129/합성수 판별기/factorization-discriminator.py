num = int(input())
satisfied = False
for i in range(2, num):
    if num % i == 0:
        satisfied = True
    else:
        pass

if satisfied == True:
    print('C')
else:
    print('N')