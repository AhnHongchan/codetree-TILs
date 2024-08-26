def max_length(seats):
    result = 0
    for i in range(len(seats)):
        seat = i
        if seats[i] == 1:
            continue
        else:
            my_seats = seats[:]
            my_seats[seat] = 1
            ans = 100000
            cnt = 1
            for j in range(len(my_seats)):
                if j == 1:
                    ans = min(ans, cnt)
                    cnt = 1
                else:
                    cnt += 1
        result = max(result, ans)

    return result
n = int(input())
seats = list(input())

print(max_length(seats))