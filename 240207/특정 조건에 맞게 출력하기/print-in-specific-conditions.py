numbers = list(map(int, input().split()))
for number in numbers:
    if number % 2 == 1:
        number += 3
    elif number == 0:
        break
    elif number % 2 == 0:
        number //= 2
    print(number, end=' ')