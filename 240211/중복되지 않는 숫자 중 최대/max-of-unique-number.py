N = int(input())
numbers = list(map(int, input().split()))
max_num = -1

for number in numbers:
    if max_num < number:
        count = 0
        for elem in numbers:
            if elem == number:
                count += 1
        
        if count == 1:
            max_num = number

print(max_num)