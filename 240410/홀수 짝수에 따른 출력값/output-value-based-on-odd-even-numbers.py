n = int(input())

def recur(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n % 2 == 0:
        return recur(n-2)+n
    else:
        return recur(n-2)+n

print(recur(n))