numbers = list(map(int, input().split()))
max_val = numbers[0]

for elem in numbers:
    if max_val <= elem:
        max_val = elem

print(max_val)