N = int(input())
numbers = list(map(int, input().split()))

i = 0
while i <= N-2:
    if numbers[i] < numbers[i+1]:
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        i = 0
    else:
        i += 1

print(numbers[0], numbers[1])