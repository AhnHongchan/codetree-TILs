n, a = input().split()
n = int(n)

cnt = 0
for i in range(n):
    x = input()
    if x == a:
        cnt += 1

print(cnt)