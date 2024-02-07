num = int(input())
numbers = list(map(int, input().split()))

min_val = numbers[0]
cnt = 1
for i in range(1, num):
    if min_val > numbers[i]:
        min_val = numbers[i]
        cnt = 1

    elif min_val == numbers[i]:
        cnt += 1

print(min_val, cnt)