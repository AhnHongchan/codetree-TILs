numbers = list(map(int, input().split()))
for i in range(len(numbers)):
    if (i+1) % 3 == 0:
        print(numbers[i-1])
        break