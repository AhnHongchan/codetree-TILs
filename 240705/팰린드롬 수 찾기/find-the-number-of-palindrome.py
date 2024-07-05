x, y = map(int, input().split())

ans = 0
for i in range(x, y+1):
    i = str(i)
    if i[0] == i[-1]:
        ans += 1

print(ans)