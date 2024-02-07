word = ['L', 'E', 'B', 'R', 'O', 'S']
alphabet = input()
for i in range(len(word)):
    if word[i] == alphabet:
        print(i)
        break
    else:
        print(None)