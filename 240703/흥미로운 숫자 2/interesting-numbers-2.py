min_v, max_v = map(int, input().split())

ans = 0

for num in range(min_v, max_v + 1):
    str_num = str(num)
    digit_count = {}
    
    for digit in str_num:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

    for count in digit_count.values():
        if count == len(str_num) - 1:
            ans += 1
            break

print(ans)