a, b = map(int, input().split())
arr = [a, b]
cnt = 1

while True:
	cnt += 1
	arr.append(arr[cnt-1]+ arr[cnt-2] + arr[cnt-2])
	if cnt == 9:
		break

print(*arr, sep=' ')