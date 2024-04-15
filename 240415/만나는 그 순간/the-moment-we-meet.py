N, M = map(int, input().split())
arr_a = [0]
arr_b = [0]
for _ in range(N):
    d, t = input().split()
    t = int(t)
    if d == 'R':
        for i in range(arr_a[-1]+1, arr_a[-1]+t+1):
            arr_a.append(i)
    else:
        for i in range(arr_a[-1]-1, arr_a[-1]-t-1, -1):
            arr_a.append(i)

for _ in range(M):
    d, t = input().split()
    t = int(t)
    if d == 'R':
        for i in range(arr_b[-1]+1, arr_b[-1]+t+1):
            arr_b.append(i)
    else:
        for i in range(arr_b[-1]-1, arr_b[-1]-t-1, -1):
            arr_b.append(i)

# print(arr_a)
# print(arr_b)

n = min(len(arr_a), len(arr_b))
for i in range(1, n+1):
    if arr_a[i] == arr_b[i]:
        print(i)
        break
else:
    print(-1)