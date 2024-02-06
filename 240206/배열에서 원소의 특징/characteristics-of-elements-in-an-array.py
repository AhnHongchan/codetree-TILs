numbers = list(map(int, input().split()))

num3 = 0

for num in numbers:
    if num % 3 == 0:
        break
    num3 = num

print(num3)