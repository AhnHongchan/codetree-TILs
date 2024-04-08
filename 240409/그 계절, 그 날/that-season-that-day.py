def Year(N):
    if N % 4 != 0:
        return False
    if N % 4 == 0 and N % 100 == 0 and N % 400 != 0:
        return False
    return True
    
def semester(M):
    if 3 <= M <= 5:
        return 'Spring'
    elif 6 <= M <= 8:
        return 'Summer'
    elif 9 <= M <= 11:
        return 'Fall'
    else:
        return 'Winter'

Y, M, D = map(int, input().split())
long = [1, 3, 5, 7, 8, 10, 12]
short = [4, 6, 9, 11]

result1 = Year(Y)

if result1:
    if M in long:
        if D <= 31:
            print(semester(M))
    elif M in short:
        if D <= 30:
            print(semester(M))
        else:
            print(-1)
    else:
        if D <= 29:
            print('Winter')
        else:
            print(-1)

if not result1:
    if M in long:
        if D <= 31:
            print(semester(M))
    elif M in short:
        if D <= 30:
            print(semester(M))
        else:
            print(-1)
    else:
        if D <= 28:
            print('Winter')
        else:
            print(-1)