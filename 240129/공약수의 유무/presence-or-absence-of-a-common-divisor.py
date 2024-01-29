a, b = map(int, input().split())
satisfied = False
for i in range(2, b):
    if (a % i == 0) and (b % i == 0):
        satisfied = True
    else:
        pass

if satisfied == True:
    print(1)
else:
    print(0)