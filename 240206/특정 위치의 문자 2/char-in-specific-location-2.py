letters = input().split()
for i in range(len(letters)):
    if i % 3 == 1:
        print(letters[i], end=' ')