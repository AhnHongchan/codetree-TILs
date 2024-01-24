num = int(input())
prod = 1
for i in range(1, num+1):
    prod *= i
    if prod >= num:
        print(i)
        break