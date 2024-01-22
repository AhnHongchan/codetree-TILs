a, b, c = map(int, input().split())
min_ = a
for i in a, b, c:
    if i < min_:
        min_ = i

print(min_)