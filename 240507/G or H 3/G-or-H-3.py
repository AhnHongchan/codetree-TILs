n, k = map(int, input().split())
arr = [''] * 10001  # 물건의 종류를 추적할 리스트

# 입력 받기
for _ in range(n):
    i, l = input().split()
    arr[int(i)] = l

ans = 0
for i in range(1, 10001):  # 1부터 10000까지의 위치에 대해 반복
    cnt = 0
    for j in range(i, min(i + k+1, 10001)):  # i부터 i+k까지 반복
        if arr[j] == 'G':
            cnt += 1
        elif arr[j] == 'H':
            cnt += 2
    ans = max(ans, cnt)

print(ans)