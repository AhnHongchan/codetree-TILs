n = int(input())
arr = [input() for _ in range(n)]
char = input()

cnt = 0
len_sum = 0
for x in arr:
    if x[0] == char:
        cnt += 1
        len_sum += len(x)

avg = len_sum / cnt
print(f'{cnt} {avg:.2f}')