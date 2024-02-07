num = int(input())
numbers = list(map(int, input().split()))

min_val = numbers[0]
cnt = 1
for number in numbers:
    if min_val > number:
        min_val = number
        cnt = 1

    elif min_val == number:
        cnt += 1

print(min_val, cnt)