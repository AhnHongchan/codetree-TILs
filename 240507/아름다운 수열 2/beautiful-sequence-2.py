n, m = map(int, input().split())
nlst = list(map(int, input().split()))
mlst = list(map(int, input().split()))

# mlst에 있는 숫자 갯수
lst = [0] * 101
for x in mlst:
    lst[x] += 1

cnt = 0
for i in range(n - m + 1):
    lst2 = lst[:]  # lst를 복사하여 lst2 초기화
    newlst = nlst[i:i + m]
    for y in newlst:
        lst2[y] -= 1

    if all(val == 0 for val in lst2):
        cnt += 1

print(cnt)