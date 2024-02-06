numbers = list(map(int, input().split()))
sum2 = 0
cnt = 0
sum3 = 0
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        sum2 += numbers[i]
    elif numbers[i] % 3 == 0:
        sum3 += numbers[i]
        cnt += 1

avg = sum3 / cnt

print(sum2, f'{avg:.1f}')