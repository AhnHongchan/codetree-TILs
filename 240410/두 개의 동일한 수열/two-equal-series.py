n = int(input())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
arr_1.sort()
arr_2.sort()

# if arr_1[:] == arr_2[:]:
#     print('Yes')
# else:
#     print('No')

for i in range(n):
    if arr_1[i] != arr_2[i]:
        print('No')
        break
else:
    print('Yes')