a, b, c = map(int, input().split())

def mul(a, b, c):
    return a*b*c

result = mul(a, b, c)

def sum_v(n):
    if n == 0:
        return 0
    else:
        return sum_v(n//10) + n%10
print(sum_v(result))