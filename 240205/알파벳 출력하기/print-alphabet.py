n = int(input())
cnt = 0

for i in range(1, n+1):
    for j in range(i):
        print(chr(65+cnt), end='')
        cnt += 1
    print()