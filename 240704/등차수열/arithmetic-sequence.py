n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

max_count = 0

for i in range(n):
    for j in range(i + 1, n):
        # Calculate potential k
        k = (numbers[i] + numbers[j]) / 2
        if k.is_integer():
            k = int(k)
            # Check how many times this k forms arithmetic sequences
            count = 0
            for x in range(n):
                for y in range(x + 1, n):
                    if (numbers[x] + numbers[y]) == 2 * k:
                        count += 1
            max_count = max(max_count, count)

print(max_count)