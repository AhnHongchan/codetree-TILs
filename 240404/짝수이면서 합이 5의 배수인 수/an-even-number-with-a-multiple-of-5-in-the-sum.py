def bool(n):
    if n % 2 != 0:
        return 'No'

    else:
        sum_v = 0
        while n > 0:
            if n < 10:
                sum_v += n
                break
            a = n // 10
            sum_v += a
            n %= 10
        if sum_v % 5 == 0:
            return 'Yes'
        else:
            return 'No'

N = int(input())
result = bool(N)
print(result)