def counting(x, y):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if size[x+i][y+j] == 1:
                cnt += 1
    return cnt

N = int(input())
size = [list(map(int, input().split())) for _ in range(N)]

max_v = 0
for i in range(N-2):
    for j in range(N-2):
        result = counting(i, j)
        if max_v < result:
            max_v = result

print(max_v)