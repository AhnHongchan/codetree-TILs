arr = input()
n = len(arr)
cnt = 0
for i in range(n-3):
    for j in range(i+2,n-1):
        if arr[i] == '(' and arr[i+1] == '(' and arr[j] == ')' and arr[j+1] == ')':
            cnt += 1

print(cnt)