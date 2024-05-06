n = int(input())
code = []
for i in range(n):
    code.append(int(input()))

ans = -1
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(n):
            carry = False
            a, b, c = code[i], code[j], code[k]
            while a > 0 or b > 0 or c > 0:
                if a % 10 + b % 10 + c % 10 < 10:
                        a //= 10
                        b //= 10
                        c //= 10
                else:
                    carry = True
                    break
            if not carry:
                cnt = code[i] + code[j] + code[k]
                ans = max(ans, cnt)
print(ans)