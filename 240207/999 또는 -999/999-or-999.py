numbers = list(map(int, input().split()))
min_val = numbers[0]
max_val = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] == 999 or numbers[i] == -999:
        break
    if min_val > numbers[i]:
        min_val = numbers[i]
    if max_val < numbers[i]:
        max_val = numbers[i]

print(max_val, min_val)