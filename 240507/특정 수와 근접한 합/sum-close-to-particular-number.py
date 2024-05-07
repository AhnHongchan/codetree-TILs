from itertools import combinations

n, s= map(int, input().split())
arr = list(map(int, input().split()))
val = sum(arr)

ans = 10000000
for comb in combinations(arr, 2):
    val2 = sum(comb)
    result = val-val2
    ans = min(ans, abs(result - s))
print(ans)