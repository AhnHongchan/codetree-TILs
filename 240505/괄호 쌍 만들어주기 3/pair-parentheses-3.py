order = input()
n = len(order)

cnt = 0
for i in range(n-1):
    if order[i] == '(':
        for j in range(i+1, n):
            if order[j] == ')':
                cnt += 1

print(cnt)