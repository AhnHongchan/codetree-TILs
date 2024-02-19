str = input()
lst = list(str)

for _ in range(len(lst)-1):
    c = int(input())
    if c >= len(lst)-1:
        lst.pop()
        print(''.join(lst), sep='')
    else:
        lst.pop(c)
        print(''.join(lst), sep='')