x, y = map(int, input().split())

ans = 0
for i in range(x, y+1):
    i = str(i)
    n = len(i)
    for j in range(n//2):
        if i[j] == i[n-j-1]:
            ans += 1
print(ans)