lst1 = [list(map(int, input().split())) for _ in range(3)]
space = input()
lst2 = [list(map(int, input().split())) for _ in range(3)]

lst3 = [
    [0 for _ in range(3)]
    for _ in range(3)
]

# 두 배열의 곱을 새로운 배열에 담습니다.
for i in range(3):
	for j in range(3):
		lst3[i][j] = lst1[i][j] * lst2[i][j]
	
# 새로운 배열을 출력합니다.
for row in lst3:
	for elem in row:
		print(elem, end=" ")
	print()