n = int(input())
numbers = list(map(int, input().split()))

min_gap = 101
max_number = numbers[0]

for i in range(n-1):
    for j in range(i+1, n):
        gap = abs(numbers[i]-numbers[j])
        if min_gap > gap:
            min_gap = gap

print(min_gap)