num = int(input())
numbers = list(map(int, input().split()))
count = [0] * 10
for number in numbers:
    count[number] += 1

print(*count[1:], sep='\n')