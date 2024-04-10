MAXNUM = 100000
n = int(input())
start = MAXNUM
arr = [0] * (2 * MAXNUM + 1)
for _ in range(n):
    num, direction = input().split()
    num = int(num)
    if direction == 'R':
        for i in range(num):
            arr[start+i] = 'B'
        start += num - 1
    else:
        for i in range(num):
            arr[start-i] = 'W'
        start -= num - 1

cnt_w = 0
cnt_b = 0
for i in range(len(arr)):
    if arr[i] == 'W':
        cnt_w += 1
    elif arr[i] == 'B':
        cnt_b += 1

print(cnt_w, cnt_b)