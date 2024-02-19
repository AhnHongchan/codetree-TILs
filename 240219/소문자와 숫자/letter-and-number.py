# 문자열을 입력받습니다.
string = input()

# 문자를 하나하나 확인하여 알파벳일 경우 모두 소문자로, 숫자일 경우 그대로 출력합니다.
for elem in string:
	if(elem >= 'A' and elem <= 'Z') or (elem >= 'a' and elem <= 'z'):
		print(elem.lower(), end="")
	
	if(elem >= '0' and elem <= '9'):
		print(elem, end="")