numbers = list(map(int, input().split()))
count = [0] * 7
for number in numbers:
    count[number] += 1

for i in range(1, 7):
    print(f"{i} - {count[i]}")