T = int(input())
for tc in range(1, T+1):
    num = int(input())
    cnt = 0
    while num > 1:
        if num % 2  == 1:
            num = 3 * num + 1
            cnt += 1
        else:
            num //= 2
            cnt += 1
    
    print(cnt)