numbers = list(map(int, input().split()))

cnt = 0
sum = 0
for number in numbers:
    if number == 0:
        break
    if number % 2 == 0:
        cnt += 1
        sum += number

print(cnt, sum)