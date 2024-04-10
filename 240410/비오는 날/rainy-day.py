n = int(input())
q = []
for _ in range(n):
    a, b, c = input().split()
    if c == 'Rain':
        q.append([a, b, c])

q.sort(key=lambda x:x[0], reverse=True)
print(*q.pop())