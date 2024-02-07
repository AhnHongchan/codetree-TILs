n1, n2 = map(int, input().split())
n1_set = list(map(int, input().split()))
n2_set = list(map(int, input().split()))

if n2_set in n1_set:
    print('Yes')
else:
    print('No')