n = int(input())

lst = [[i+n*j+1 for j in range(n)] for i in range(n)]

for x in lst:
    for elem in x:
        print(elem, end= ' ')
    print()