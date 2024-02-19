a, b = map(int, input().split())
c = str(a + b)

cnt = 0
for x in c:
    if x == '1':
        cnt += 1

print(cnt)