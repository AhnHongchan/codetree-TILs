numbers = list(map(int, input().split()))
sum2 = 0
cnt = 0
sum3 = 0
for number in numbers:
    if number % 2 == 0:
        sum2 += number
    elif number % 3 == 0:
        sum3 += number
        cnt += 1

avg = sum3 / cnt

print(sum2, f'{avg:.1f}')