n, m = map(int, input().split())

lst = []

for i in range(m):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    lst.append((a, b))

count_dict = {}

for j in range(m):
    if lst[j] in count_dict:
        count_dict[lst[j]] += 1
    else:
        count_dict[lst[j]] = 1

print(max(count_dict.values()))