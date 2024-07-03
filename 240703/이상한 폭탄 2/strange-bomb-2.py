n, k = map(int, input().split())

bombs = [int(input()) for _ in range(n)]
fire = []

for i in range(n):
    bomb = bombs[i]
    for j in range(i+1, i+k+1):
        if j < n and bomb == bombs[j]:
            fire.append(bomb)


if len(fire) == 0:
    print(-1)
else:
    print(max(fire))