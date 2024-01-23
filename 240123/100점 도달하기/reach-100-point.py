num = int(input())
while num <= 100:
    if num < 60:
        print('F', end = " ")
    elif num < 70:
        print('D', end = " ")
    elif num < 80:
        print('C', end = " ")
    elif num < 90:
        print('B', end = " ")
    elif num >= 90:
        print('A', end = " ")
    num += 1