n = int(input())
order = list(map(int, input().split()))
exs = []

ans = n ** 3

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            case = [i, j, k]
            exs.append(case)


for ex in exs:
    cnt = 0
    for m in range(3):
        judge = abs(ex[m]-order[m])
        if judge > 2:
            cnt += 1
    if cnt == 3:
        ans -= 1

print(ans)