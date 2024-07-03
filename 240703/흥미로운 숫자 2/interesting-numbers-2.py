from collections import Counter

min_v, max_v = map(int, input().split())

ans = 0
for num in range(min_v, max_v+1):
    cnt = []
    while num:
        a = num % 10
        cnt.append(a)
        num //= 10
    element_counts = Counter(cnt)
    for element, count in element_counts.items():
        if count == len(cnt)-1:
            ans += 1

print(ans)