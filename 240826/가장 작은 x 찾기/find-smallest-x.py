n = int(input())
range_list = []
for i in range(n):
    a, b = map(int, input().split())
    range_list.append((a, b))

x = 1
while True:
    y = x
    for j in range(n):
        y *= 2
        if range_list[j][0] < y < range_list[j][1]:
            pass
        else:
            x += 1
            break
    if y == x * 16:
        break

print(x)