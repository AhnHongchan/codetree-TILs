a, b, c = map(int, input().split())
lst = [a, b, c]
for i in lst:
    max = lst[0]
    if i > max:
        max = i

print(max)