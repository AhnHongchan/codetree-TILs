def change(x, y):
    if x > y:
        x *= 2
        y += 10
    else:
        x += 10
        y *= 2
    return x, y

a, b = map(int, input().split())
a, b = change(a, b)
print(a, b)