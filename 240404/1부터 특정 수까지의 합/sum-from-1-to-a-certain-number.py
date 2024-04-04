def sum_10(n):
    sum_v = 0
    for i in range(1, n+1):
        sum_v += i
    return sum_v // 10

N = int(input())
result = sum_10(N)
print(result)