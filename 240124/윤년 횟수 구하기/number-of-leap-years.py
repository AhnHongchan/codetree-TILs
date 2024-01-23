num = int(input())
year = 0
for i in range(1, num+1):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        year += 1

print(year)