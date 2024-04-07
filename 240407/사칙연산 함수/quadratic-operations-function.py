def calculator(a, b, c):
    if b not in '+_/*':
        return False
    else:
        if b == '+':
            return a + c
        elif b == '-':
            return a - c
        elif b == '*':
            return a * c
        elif b == '/':
            return a / c

a, b, c = input().split()
result = calculator(int(a), b, int(c))
if not result:
    print(False)
else:
    print(a, b, c, '=', f'{result}')