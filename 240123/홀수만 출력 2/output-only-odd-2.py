a, b = map(int, input().split())
for i in range(b, a+1, 2):
    print(a+b-i, end=" ")