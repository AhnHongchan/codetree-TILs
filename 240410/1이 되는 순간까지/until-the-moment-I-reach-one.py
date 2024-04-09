n = int(input())

def div(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return div(n//2) + 1
    else:
        return div(n//3) + 1

print(div(n))