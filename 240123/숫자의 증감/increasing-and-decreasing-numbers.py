a, b = input().split()
b = int(b)
i = 1
if a  == 'A':
    while i <= b:
        print(i, end=" ")
        i += 1
elif a == 'D':
    while i <= b:
        print(b+1-i, end = " ")