T, a, b = map(int, input().split())
S_idx = []
N_idx = []


for i in range(T):
    alp, idx = input().split()
    if alp == 'S':
        S_idx.append(int(idx))
    else:
        N_idx.append(int(idx))

ans = 0

for j in range(a, b+1):
    s_val = 1000
    n_val = 1000
    
    for k in S_idx:
        s_can = abs(j-k)
        s_val = min(s_val, s_can)
    
    for l in N_idx:
        n_can = abs(l-j)
        n_val = min(n_val, n_can)
    
    if s_val <= n_val:
        ans += 1

print(ans)