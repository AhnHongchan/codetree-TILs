a, b, c = map(int, input().split())
satisfied = True
for i in range(a, b+1):
    if i % c == 0:
        pass
    else:
        satisfied = False

if satisfied == True:
    print('NO')
else:
    print('YES')