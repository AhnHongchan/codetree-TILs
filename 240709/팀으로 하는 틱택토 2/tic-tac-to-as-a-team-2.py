from collections import Counter

teams = [input() for _ in range(3)]
ans = 0

# 1. 같은 행에 숫자 2개 있는 지 확인

for i in range(3):
    freq = {}
    digits = teams[i]
    for digit in digits:
        if digit in freq:
            freq[digit] += 1
        else:
            freq[digit] = 1
    for cnt in freq.values():
        if cnt == 2:
            ans += 1

# 2. 같은 열에 숫자 2개 있는 지 여부 확인하기

for j in range(3):
    case = []
    for i in range(3):
        a = teams[i][j]
        case.append(a)
    count = Counter(case)

    for cnt in count.values():
        if cnt == 2:
            ans += 1
    
# 3. 양쪽 대각선 재기

case2 = [teams[0][0], teams[1][1], teams[2][2]]
count2 = Counter(case2)
for cnt in count2.values():
    if cnt == 2:
        ans += 1

case3 = [teams[2][0], teams[1][1], teams[0][2]]
count3 = Counter(case3)
for cnt in count3.values():
    if cnt == 2:
        ans += 1

print(ans)