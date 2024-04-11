n = int(input())
ctr = 100
arr = [[0] * (2*ctr+1) for _ in range(2*ctr+1)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(ctr+x, ctr+x+8):
        for j in range(ctr+y, ctr+y+8):
            arr[i][j] = 1

cnt = 0
for x in range(2*ctr+1):
    for y in range(2*ctr+1):
        if arr[x][y] == 1:
            cnt += 1

print(cnt)