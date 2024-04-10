n = int(input())
start = 0
dic = {}
for _ in range(n):
    num, dir = input().split()
    if dir == 'R':
        for i in range(int(num)):
            if start + i in dic:
                dic[start + i] += 1
            else:
                dic[start + i] = 1
        start += int(num)
    
    else:
        for i in range(int(num)):
            if start - i - 1 in dic:
                dic[start - i - 1] += 1
            else:
                dic[start - i - 1] = 1
        start -= int(num)

cnt = 0
for value in dic.values():
    if value >= 2:
        cnt += 1
print(cnt)