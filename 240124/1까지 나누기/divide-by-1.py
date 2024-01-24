num = int(input())
div = num
cnt = 0
for i in range(1, num+1):
    div /= i
    cnt += 1
    if div <= 1:
        print(cnt)
        break