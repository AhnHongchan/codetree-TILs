small = [list(input().split()) for _ in range(5)]

for i in range(5):
    for j in range(3):
        print(chr(ord(small[i][j])-32), end=' ')
    print()