n = int(input())
lst = [0] * (100 + 1)
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        lst[i] += 1

print(max(lst))