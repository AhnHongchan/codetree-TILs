txt = input()
command = list(input())

for i in range(len(command)):
    if command[i] == 'L':
        txt = txt[1:] + txt[0]
    elif command[i] == 'R':
        txt = txt[-1] + txt[:-1]

print(txt)