n, m = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if numbers[i] == m:
        cnt += 1

print(cnt)