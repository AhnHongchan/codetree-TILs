num = int(input())
cnt = 0
while num < 1000:
    if num % 2 == 0:
        num = 3 * num + 1
        cnt += 1
    else:
        num = 2 * num + 2
        cnt += 1

print(cnt)