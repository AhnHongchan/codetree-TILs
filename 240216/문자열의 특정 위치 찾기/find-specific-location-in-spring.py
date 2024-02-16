txt, char = input().split()

for i in range(len(txt)):
    if char in txt[i]:
        print(i)
        break
else:
    print('No')