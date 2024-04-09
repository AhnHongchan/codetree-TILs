n = int(input())
arr = list(map(int, input().split()))

def max_v(n):
    if n == 0:
        return arr[0]
    return max(max_v(n-1), arr[n])

print(max_v(n-1))