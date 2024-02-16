n = int(input())
arr = input().split()
str = ''
for i in range(len(arr)):
    str += arr[i]

cnt = 0
for x in str:
    cnt += 1
    print(x, end ='')
    if cnt % 5 == 0:
        print()