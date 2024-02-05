num = int(input())
cnt = 0

for i in range(num):
    for j in range(num):
        print(chr(65+cnt), end='')
        cnt += 1
    print()