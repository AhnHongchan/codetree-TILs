num = int(input())

for i in range(1, num+1):
	for j in range(i-1, -1, -1):
		print(num - j, end =" ")

	print()