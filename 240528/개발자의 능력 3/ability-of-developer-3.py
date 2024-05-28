numbers = list(map(int, input().split()))
n = len(numbers)

def get_diff(i, j, k):
    sum1 = numbers[i] + numbers[j] + numbers[k]
    sum2 = sum(numbers) - sum1
    return abs(sum1 - sum2)

min_diff = 6000000
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            min_diff = min(min_diff, get_diff(i, j, k))

print(min_diff)