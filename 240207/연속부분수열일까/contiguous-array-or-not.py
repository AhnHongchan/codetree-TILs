n1, n2 = map(int, input().split())
n1_set = list(map(int, input().split()))
n2_set = list(map(int, input().split()))

for i in range(n1-n2+1):
    if n1_set[i:i+n2] == n2_set[:]:
        print('Yes')
        break
else:
    print('No')