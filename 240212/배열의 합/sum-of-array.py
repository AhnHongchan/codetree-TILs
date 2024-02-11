lst = [list(map(int, input().split())) for _ in range(4)]
new_lst = []

for i in range(4):
    sum = 0
    for j in range(4):
        sum += lst[i][j]
    new_lst.append(sum)

print(*new_lst, sep='\n')