n = int(input())

def scale(n):
    if n == 0:
        return
    scale(n-1)
    print(n, end = " ")

def reverse_scale(n):
    if n == 0:
        return
    print(n, end = " ")
    reverse_scale(n-1)

scale(n)
print()
reverse_scale(n)