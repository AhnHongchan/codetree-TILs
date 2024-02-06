numbers = list(map(int, input().split()))

odd = 0
even = 0

for i in range(len(numbers)):
    if (i+1) % 2 == 0:
        even += numbers[i]
    else:
        odd += numbers[i]

if even >= odd:
    print(even - odd)
else:
    print(odd - even)