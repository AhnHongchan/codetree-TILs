def recur(n):
    if n == 0:
        return 0
    a = n % 10
    return recur(n//10) + a ** 2

n = int(input())
print(recur(n))