from collections import Counter

n = int(input())
lst = list(input())

for k in range(1, len(lst)+1):
    combi_letters = [''.join(lst[i:i+k]) for i in range(len(lst) - k + 1)]
    count = Counter(combi_letters)
    twice = False
    for cnt in count.values():
        if cnt >= 2:
            twice = True
            break
    
    if not twice:
        ans = k
        break

print(ans)