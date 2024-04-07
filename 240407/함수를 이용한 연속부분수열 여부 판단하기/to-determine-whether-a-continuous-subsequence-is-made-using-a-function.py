n1, n2 = map(int, input().split())
lst_n1 = list(map(int, input().split()))
lst_n2 = list(map(int, input().split()))

result = 'No'
for i in range(n1-n2+1):
    if lst_n1[i:i+n2] == lst_n2:
        result = 'Yes'
        break
print(result)