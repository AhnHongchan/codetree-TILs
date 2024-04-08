def swap(x, y):
    x, y = y, x
    print(x, y)
a, b = map(int, input().split())
swap(a, b)