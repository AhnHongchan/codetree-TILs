n, k, t = input().split()
n = int(n)
k = int(k)
lst = []
for _ in range(n):
    a = input()
    if t == a[0:len(t)]:
        lst.append(a)

lst.sort()
print(lst[k-1])