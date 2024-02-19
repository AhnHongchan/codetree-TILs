txt = input()
for elem in txt:
    if 'a' <= elem <= 'z':
        print(elem.upper(), end='')
    if 'A' <= elem <= 'Z':
        print(elem.lower(), end='')