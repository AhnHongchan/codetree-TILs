num = int(input())
div = num
for i in range(1, num+1):
    div /= i
    if div <= 1:
        print(i)
        break