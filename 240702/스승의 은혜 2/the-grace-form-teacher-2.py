n, budget = map(int, input().split())
prices = [int(input()) for _ in range(n)]
prices.sort()
cnt = 0

for i in range(n):
    budget -= prices[i]
    if budget >= 0:
        cnt += 1
        pass
    else:
        budget += prices[i]
        sale = prices[i] // 2
        if budget - sale >= 0:
            cnt += 1
        break

print(cnt)