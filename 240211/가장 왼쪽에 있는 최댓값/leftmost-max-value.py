N = int(input())
numbers = list(map(int, input().split()))

max_num = 0
cnt = 0
j = N
lst = []

while j >= 1:
    for i in range(j):
        if max_num < numbers[i]:
            max_num = numbers[i]
            cnt = i

    lst.append(cnt+1)
    j = cnt
    max_num = 0
    cnt = 0

print(*lst)