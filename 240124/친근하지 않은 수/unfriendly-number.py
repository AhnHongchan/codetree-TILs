num = int(input())
cnt = 0
for i in range(1, num+1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        pass
    else:
        cnt += 1

print(cnt)