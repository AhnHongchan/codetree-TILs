lst1 = [list(map(int, input().split())) for _ in range(3)]
space = input()
lst2 = [list(map(int, input().split())) for _ in range(3)]

lst4 = []

for x in range(3):
    lst3 = []
    for y in range(3):
        mul = lst1[x][y] * lst2[x][y]
        lst3.append(mul)
    lst4.append(lst3)

for x in lst4:
    for y in x:
        print(y, end=' ')
    print()