def absolute(lst):
    for i in range(len(lst)):
        if lst[i] <0:
            lst[i] = abs(lst[i])
        

N = int(input())
arr = list(map(int, input().split()))
absolute(arr)

for elem in arr:
    print(elem, end=" ")