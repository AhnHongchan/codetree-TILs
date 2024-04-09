n = int(input())
sum_v = 0

def sum_add(n):
    global sum_v
    if n == 0:
        return
    sum_v += n
    sum_add(n-1)
sum_add(n)
print(sum_v)