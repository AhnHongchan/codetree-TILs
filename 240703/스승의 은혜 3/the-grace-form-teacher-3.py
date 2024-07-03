n, b = map(int, input().split())

payment = [tuple(map(int, input().split())) for _ in range(n)]

sorted_payment = sorted(payment, key=lambda x:((sum(x), x[0])))
sum_payment = [x+y for x,y in sorted_payment]
keep = []

ans = 0

for i in range(n):
    b -= sum_payment[i]
    keep = [sorted_payment[i][0]]
    if b > 0:
        ans += 1
    else:
        b += sum_payment[i]
        if b - (max(keep) // 2 + sorted_payment[i][1]) >= 0:
            ans += 1
            break

print(ans)