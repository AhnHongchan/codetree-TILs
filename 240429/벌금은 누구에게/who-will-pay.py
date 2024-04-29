N,M,K = map(int, input().split())
N = [0] * (N+1)
for i in range(M):
    num = int(input())
    N[num] += 1
    if N[num] == 3:
        print(num)
        break
else:
    print(-1)