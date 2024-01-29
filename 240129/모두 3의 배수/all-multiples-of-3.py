p = True
for i in range(5):
    num = int(input())

    if num % 3 == 0:
        continue
    else:
        p = False
        break

if p == True:
    print(1)
else:
    print(0)