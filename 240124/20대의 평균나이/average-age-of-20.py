sum = 0
cnt = 0
while True:
    age = int(input())
    if age >= 30 or age <= 19:
        break
    else:
        sum += age
        cnt += 1

avg = f'{sum/cnt:.2f}'
print(avg)