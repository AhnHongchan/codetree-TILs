def calculator(a, b, c):
    if b not in '+_/*':
        return False
    else:
        if b == '+':
            return a + b
        elif b == '-':
            return a - b
        elif b == '*':
            return a * b
        elif b == '/':
            return a / b

a = list(input())
a[0] = int(a[0])
a[2] = int(a[2])
result = calculator(a[0], a[1], a[2])
print(result)