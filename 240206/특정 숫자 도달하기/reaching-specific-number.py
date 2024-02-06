arr = list(map(int, input().split()))

sum = 0
cnt = 0
for i in range(10):
    sum += arr[i]
    cnt += 1
    if arr[i] >= 250:
        sum -= arr[i]
        cnt -= 1
        break

avg = sum / cnt

print(sum, avg)