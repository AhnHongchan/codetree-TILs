def judge(n):
    if n % 4 != 0:
        return 'false'
    elif n % 100 == 0 and n % 400 != 0:
        return 'false'
    return 'true'


N = int(input())
print(judge(N))