N,M = map(int, input().split())

arr = [0]*1000001
arr2 = [0] * 1000001

cnt = 1
for i in range(N):
    v,t = map(int, input().split())
    for j in range(t):
        arr[cnt] = arr[cnt-1]+v
        cnt += 1

cnt2 = 1
for i in range(M):
    v,t = map(int, input().split())
    for j in range(t):
        arr2[cnt2] = arr2[cnt2-1]+v
        cnt2 += 1

leader, ans = 0, 0
for i in range(1, cnt+1):
    if arr[i] > arr2[i]:
        if leader == 2:
            ans += 1
        leader = 1
    
    elif arr[i] < arr2[i]:
        if leader == 1:
            ans += 1
        leader = 2

print(ans)