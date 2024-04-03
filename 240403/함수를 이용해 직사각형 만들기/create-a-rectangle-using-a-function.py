def square(x, y):
    for _ in range(x):
        print('1'*y)

n, m = map(int, input().split())
square(n, m)