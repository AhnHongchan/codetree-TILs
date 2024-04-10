binary = input()
n = len(binary)
ans = 0
for i in range(n):
    ans += int(binary[n-1-i]) * (2 ** i)

print(ans)