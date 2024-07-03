n, k = map(int, input().split())

bombs = [int(input()) for _ in range(n)]
fire = []

for i in range(n-3):
    bomb = bombs[i]
    for j in range(i+1, i+4):
        if bomb == bombs[j]:
            fire.append(bomb)

print(max(fire))