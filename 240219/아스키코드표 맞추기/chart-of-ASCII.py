# 숫자 5개를 입력받습니다.
a = list(map(int, input().split()))

# 주어진 값에 해당하는 아스키코드의 문자를 출력합니다.
for elem in a:
	print(chr(elem), end=" ")