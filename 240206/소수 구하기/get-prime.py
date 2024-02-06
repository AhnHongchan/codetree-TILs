num = int(input())

for i in range(1, num +1):
    sum = 0
    for j in range(1,i+1):
        if i % j == 0:
            sum += j
    
    if sum == i + 1:
        print(i, end=' ')