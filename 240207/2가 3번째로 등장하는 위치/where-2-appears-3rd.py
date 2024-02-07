n = int(input())
numbers = list(map(int, input().split()))

cnt = 0
for i in range(len(numbers)):
    if numbers[i] == 2:
        cnt += 1
    if cnt == 3:
        print(i+1)
        break