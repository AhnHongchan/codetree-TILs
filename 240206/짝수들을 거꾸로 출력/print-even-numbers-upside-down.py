T = int(input())
numbers = list(map(int, input().split()))
num_list = []
for number in numbers:
    if number % 2 == 0:
        num_list.append(number)
    else:
        pass

print(*num_list[::-1])