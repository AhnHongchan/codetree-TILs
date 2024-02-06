numbers = list(map(int, input().split()))
sum = 0
for i in range(len(numbers)):
    if numbers[i] == 0:
        sum = sum + numbers[i-1] + numbers[i-2] + numbers[i-3]
        break

print(sum)