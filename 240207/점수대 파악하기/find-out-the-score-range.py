scores = list(map(int, input().split()))
count = [0] * 11
for score in scores:
    if score == 0:
        break
    count[score // 10] += 1

for j in range(10,0,-1):
    print(f"{j * 10} - {count[j]}")