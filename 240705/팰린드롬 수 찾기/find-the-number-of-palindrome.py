x, y = map(int, input().split())

ans = 0
for i in range(x, y+1):
    if str(i) == str(i)[::-1]:  # 숫자를 문자열로 변환한 뒤 뒤집어서 비교
        ans += 1
print(ans)