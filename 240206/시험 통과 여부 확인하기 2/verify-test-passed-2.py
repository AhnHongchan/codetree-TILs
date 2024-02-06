T = int(input())
pass_cnt = 0
for tc in range(1, T+1):
    score_list = list(map(int, input().split()))
    
    sum = 0
    cnt = 0

    for score in score_list:
        sum += score
        cnt += 1
    
    avg = sum / cnt

    if avg >= 60:
        print('pass')
        pass_cnt += 1
    else:
        print('fail')
    
print(pass_cnt)