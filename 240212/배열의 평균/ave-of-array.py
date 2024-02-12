lst = [list(map(int, input().split())) for _ in range(2)]


for i in range(2):
    sum = 0
    cnt = 0
    for j in range(4):
        sum += lst[i][j]
        cnt += 1
    
    avg = sum / cnt
    print(f'{avg:.1f}', end = ' ')
print()


for j in range(4):
    sum = 0
    cnt = 0
    for i in range(2):
        sum += lst[i][j]
        cnt += 1
    
    avg = sum / cnt
    print(f'{avg:.1f}', end = ' ')
print()

sum = 0
cnt = 0
for i in range(2):
    for j in range(4):
        sum += lst[i][j]
        cnt += 1

avg = sum / cnt
print(f'{avg:.1f}', end= ' ')