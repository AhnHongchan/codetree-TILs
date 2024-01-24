square = 0
while True:
    a, b, char = input().split()
    num_1 = int(a)
    num_2 = int(b)
    square = num_1 * num_2
    print(square)
    if char == 'C':
        break