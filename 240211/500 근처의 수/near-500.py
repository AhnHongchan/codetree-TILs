numbers = list(map(int, input().split()))

min_lst = []
max_lst= []

for number in numbers:
    if number < 500:
        min_lst.append(number)
    else:
        max_lst.append(number)
    
max = max_lst[0]
min = min_lst[0]

for i in range(len(min_lst)):
    if min < min_lst[i]:
        min = min_lst[i]

for j in range(len(max_lst)):
    if max > max_lst[j]:
        max = max_lst[j]

print(min, max)