start, end = map(int, input().split())

case = 0
for i in range(start, end+1):
    cnt = 0
    for j in range(1, i):
        if i % j == 0:
            cnt += 1
    
    if cnt == 3:
        case += 1
        if cnt > 3:
            case -= 1
    
print(case)