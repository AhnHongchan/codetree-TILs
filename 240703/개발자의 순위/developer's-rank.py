k, n = map(int, input().split())
numbers = [str(i) for i in range(1, n+1)]
leaderboard = [input().split() for _ in range(k)]

ans = 0

for x in numbers:
    for y in numbers:
        cnt = 0 
        if x == y:
            continue
        for i in range(k):
            if x in leaderboard[i] and y in leaderboard[i]:
                if leaderboard[i].index(x) < leaderboard[i].index(y):
                    cnt += 1

        if cnt == 3:
            ans += 1

print(ans)