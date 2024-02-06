num = list(map(int, input().split()))

sum = 0
cnt = 0
for i in num:
    if i == 0:
        break
    sum += i
    cnt += 1

avg = sum / cnt
print(sum, f'{avg:.1f}')